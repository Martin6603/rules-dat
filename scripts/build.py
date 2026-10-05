#!/usr/bin/env python3
"""Build exact-hostname M-Team rule files from the reviewed source inventory."""

import argparse
import datetime as dt
import ipaddress
import json
from pathlib import Path
import re
import subprocess
import sys


PROJECT = Path(__file__).resolve().parent.parent
ROLES = {"first_party", "service_dependency", "external_link", "alias_candidate"}
LABEL = re.compile(r"[a-z0-9](?:[a-z0-9-]{0,61}[a-z0-9])?\Z")


def require_text(value, location):
    if not isinstance(value, str) or not value.strip():
        raise ValueError(f"{location}: expected a nonempty string")
    return value


def normalize_hostname(value):
    hostname = require_text(value, "hostname").strip().lower()
    if hostname.endswith("."):
        hostname = hostname[:-1]
    try:
        hostname.encode("ascii")
    except UnicodeEncodeError as exc:
        raise ValueError("hostname: use an ASCII hostname (IDN in punycode)") from exc
    if len(hostname) > 253 or "." not in hostname:
        raise ValueError(f"invalid hostname: {value!r}")
    if not all(LABEL.fullmatch(label) for label in hostname.split(".")):
        raise ValueError(f"invalid hostname: {value!r}")
    try:
        ipaddress.ip_address(hostname)
    except ValueError:
        return hostname
    raise ValueError(f"expected a hostname, not an IP address: {value!r}")


def read_inventory(path):
    data = json.loads(path.read_text(encoding="utf-8-sig"))
    if not isinstance(data, dict):
        raise ValueError("inventory: expected a JSON object")
    for key in ("collected_at", "date", "time_zone", "scope"):
        require_text(data.get(key), key)
    try:
        date = dt.date.fromisoformat(data["date"])
        timestamp = dt.datetime.fromisoformat(data["collected_at"].replace("Z", "+00:00"))
    except ValueError as exc:
        raise ValueError("date / collected_at: expected ISO 8601 values") from exc
    if timestamp.tzinfo is None or timestamp.utcoffset() is None:
        raise ValueError("collected_at: include a timezone offset")
    if timestamp.date() != date:
        raise ValueError("date: must match the local date in collected_at")
    if not isinstance(data.get("pages_checked"), list):
        raise ValueError("pages_checked: expected an array")
    if not isinstance(data.get("limitations"), list) or not all(
        isinstance(item, str) for item in data["limitations"]
    ):
        raise ValueError("limitations: expected an array of strings")
    if not isinstance(data.get("domains"), list):
        raise ValueError("domains: expected an array")

    seen = set()
    entries = []
    for index, item in enumerate(data["domains"]):
        location = f"domains[{index}]"
        if not isinstance(item, dict):
            raise ValueError(f"{location}: expected an object")
        hostname = normalize_hostname(item.get("hostname"))
        if hostname in seen:
            raise ValueError(f"duplicate hostname after normalization: {hostname}")
        seen.add(hostname)
        if item.get("role") not in ROLES:
            raise ValueError(f"{location}.role: unsupported role")
        require_text(item.get("purpose"), f"{location}.purpose")
        for flag in ("include_in_core", "include_in_dependencies"):
            if type(item.get(flag)) is not bool:
                raise ValueError(f"{location}.{flag}: expected a boolean")
        if item["include_in_core"] and item["include_in_dependencies"]:
            raise ValueError(f"{location}: core and dependency sets must be disjoint")
        if item["role"] in {"external_link", "alias_candidate"} and (
            item["include_in_core"] or item["include_in_dependencies"]
        ):
            raise ValueError(f"{location}: unverified / external domains cannot enter rule sets")
        evidence = item.get("evidence")
        if not isinstance(evidence, list) or not evidence:
            raise ValueError(f"{location}.evidence: expected a nonempty array")
        for evidence_index, observation in enumerate(evidence):
            if not isinstance(observation, dict):
                raise ValueError(f"{location}.evidence[{evidence_index}]: expected an object")
            for field in ("page_path", "kind", "note"):
                require_text(observation.get(field), f"{location}.evidence[{evidence_index}].{field}")
        entries.append({**item, "hostname": hostname})
    return data, entries


def render_rule_files(data, entries):
    files = {}
    sets = {
        "core": sorted(item["hostname"] for item in entries if item["include_in_core"]),
        "dependencies": sorted(
            item["hostname"] for item in entries if item["include_in_dependencies"]
        ),
    }
    union = sorted(set(sets["core"]) | set(sets["dependencies"]))
    for name, hostnames in {**sets, "m-team": union}.items():
        domain_list = "".join(hostname + "\n" for hostname in hostnames)
        files[f"{name}.list"] = domain_list
        files[f"{name}.yaml"] = (
            f"# Generated from sources/m-team/domains.json; collected {data['date']}.\n"
            "# Mihomo rule-provider: behavior: domain; format: yaml. Exact hosts only.\n"
            + ("payload:\n" + "".join(f"  - '{hostname}'\n" for hostname in hostnames)
               if hostnames else "payload: []\n")
        )
    return {name: content.encode("utf-8") for name, content in files.items()}, sets


def render_fake_ip_example(sets):
    union = sorted(set(sets["core"]) | set(sets["dependencies"]))
    return (
        "# Example only: merge entries into your existing blacklist-mode DNS configuration.\n"
        "# This fragment does not select a traffic-routing policy. Exact hosts only.\n"
        "dns:\n"
        "  fake-ip-filter-mode: blacklist\n"
        + ("  fake-ip-filter:\n" + "".join(f"    - '{hostname}'\n" for hostname in union)
           if union else "  fake-ip-filter: []\n")
    ).encode("utf-8")


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--source", type=Path, default=PROJECT / "sources" / "m-team" / "domains.json")
    parser.add_argument("--output-dir", type=Path, default=PROJECT / "rules" / "m-team")
    parser.add_argument("--example", type=Path, default=PROJECT / "examples" / "m-team-fake-ip-filter.yaml")
    parser.add_argument("--check", action="store_true", help="check consistency without writing")
    mode = parser.add_mutually_exclusive_group(required=True)
    mode.add_argument("--mihomo", type=Path, help="official Mihomo executable; also build/check MRS files")
    mode.add_argument("--text-only", action="store_true", help="build/check only LIST, YAML and DNS example")
    args = parser.parse_args(argv)
    try:
        data, entries = read_inventory(args.source)
        files, sets = render_rule_files(data, entries)
        expected = {args.output_dir / name: content for name, content in files.items()}
        expected[args.example] = render_fake_ip_example(sets)
        mismatches = [path for path, content in expected.items() if not (
            path.is_file()
            and path.read_bytes() == content
        )]
        if args.check:
            if mismatches:
                print("Out of date or missing: " + ", ".join(str(path) for path in mismatches), file=sys.stderr)
                return 1
        else:
            for path in mismatches:
                path.parent.mkdir(parents=True, exist_ok=True)
                path.write_bytes(expected[path])
        print(f"{'Checked' if args.check else 'Built'} {len(expected)} text files: "
              f"{len(sets['core'])} core hosts, {len(sets['dependencies'])} dependency hosts")
        if args.mihomo:
            command = [sys.executable, str(PROJECT / "scripts" / "convert_mrs.py"),
                       "--mihomo", str(args.mihomo.resolve()),
                       "--rules-dir", str(args.output_dir.resolve())]
            if args.check:
                command.append("--check")
            subprocess.run(command, check=True)
        return 0
    except (OSError, ValueError, TypeError, subprocess.CalledProcessError) as exc:
        print(f"Error: {exc}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    sys.exit(main())
