#!/usr/bin/env python3
"""Build and verify domain MRS files with the official Mihomo executable."""

from __future__ import annotations

import argparse
import hashlib
import ipaddress
from pathlib import Path
import re
import shutil
import subprocess
import sys
import tempfile


SETS = ("core", "dependencies", "m-team")
LABEL = re.compile(r"[a-z0-9](?:[a-z0-9-]{0,61}[a-z0-9])?\Z")


def run_tool(executable: str, *args: str) -> str:
    result = subprocess.run(
        [executable, *args], capture_output=True, text=True,
        encoding="utf-8", errors="replace", timeout=60, check=False,
    )
    if result.returncode:
        raise ValueError(
            f"Mihomo exited {result.returncode}: "
            f"{result.stderr.strip() or result.stdout.strip()}"
        )
    return result.stdout.strip()


def normalize_domain_rule(entry: str) -> str:
    rule = entry.strip().lower()
    is_suffix = rule.startswith("+.")
    hostname = rule[2:] if is_suffix else rule
    if hostname.endswith("."):
        hostname = hostname[:-1]
    if (
        len(hostname) > 253
        or "." not in hostname
        or not all(LABEL.fullmatch(label) for label in hostname.split("."))
    ):
        raise ValueError(f"Expected an exact hostname or '+.' domain suffix: {entry!r}")
    try:
        ipaddress.ip_address(hostname)
    except ValueError:
        return ("+." if is_suffix else "") + hostname
    raise ValueError(f"Expected a domain rule, not an IP address: {entry!r}")


def read_domains(path: Path) -> set[str]:
    entries = [
        line.strip() for line in path.read_text(encoding="utf-8").splitlines()
        if line.strip() and not line.lstrip().startswith("#")
    ]
    if not entries:
        raise ValueError(f"Empty domain set: {path}")
    try:
        normalized = [normalize_domain_rule(entry) for entry in entries]
    except ValueError as exc:
        raise ValueError(f"Invalid domain rule in {path}: {exc}") from exc
    if len(normalized) != len(set(normalized)):
        raise ValueError(f"Duplicate domain rules after normalization: {path}")
    return set(normalized)


def convert(executable: str, rules_dir: Path, check: bool) -> None:
    version = run_tool(executable, "-v")
    if "Mihomo" not in version:
        raise ValueError("The executable did not identify itself as Mihomo")
    print(version.splitlines()[0])
    prepared: list[tuple[Path, bytes, int]] = []
    with tempfile.TemporaryDirectory(prefix="rules-dat-mrs-") as temporary:
        temporary_dir = Path(temporary)
        for name in SETS:
            source = rules_dir / f"{name}.list"
            expected_domains = read_domains(source)
            target = rules_dir / f"{name}.mrs"
            generated = temporary_dir / f"{name}.mrs"
            restored = temporary_dir / f"{name}.list"
            run_tool(executable, "convert-ruleset", "domain", "text",
                     str(source), str(generated))
            # The official converter supports MRS input and exports text.
            run_tool(executable, "convert-ruleset", "domain", "mrs",
                     str(generated), str(restored))
            if read_domains(restored) != expected_domains:
                raise ValueError(f"MRS round-trip changed the domain set: {name}")
            content = generated.read_bytes()
            if not content.startswith(bytes.fromhex("28b52ffd")):
                raise ValueError(f"MRS does not have the expected Zstandard frame: {name}")
            if check and (not target.is_file() or target.read_bytes() != content):
                raise ValueError(
                    f"MRS is missing or differs from this Mihomo build: {target}. "
                    "Use the documented pinned version for reproducible bytes."
                )
            prepared.append((target, content, len(expected_domains)))
    # All three sets have passed the round-trip before any output is replaced.
    for target, content, count in prepared:
        if not check:
            target.write_bytes(content)
        digest = hashlib.sha256(content).hexdigest()
        print(f"{'Verified' if check else 'Built'} {target.name}: "
              f"{count} domain rules, {len(content)} bytes, sha256={digest}")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--mihomo", required=True,
                        help="Path to an official Mihomo executable, or command on PATH")
    parser.add_argument("--rules-dir", type=Path,
                        default=Path(__file__).resolve().parent.parent / "rules" / "m-team")
    parser.add_argument("--check", action="store_true",
                        help="Rebuild in temporary storage and require identical published bytes")
    args = parser.parse_args()
    supplied = Path(args.mihomo).expanduser()
    executable = str(supplied.resolve()) if supplied.is_file() else shutil.which(args.mihomo)
    if executable is None:
        parser.error("Mihomo executable was not found")
    try:
        convert(executable, args.rules_dir.resolve(), args.check)
    except (OSError, ValueError, subprocess.SubprocessError) as error:
        print(f"MRS error: {error}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
