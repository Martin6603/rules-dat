# MRS 构建与核对

`.mrs` 是 Mihomo 的二进制规则集。这些文件由 MetaCubeX 官方工具实际转换生成，使用 `behavior: domain`；文本和 YAML 内容也使用同一批匹配表达式（精确主机与 `+.根域`）。

## 官方依据

- [Mihomo rule-providers 文档](https://wiki.metacubex.one/config/rule-providers/)说明 `format: mrs` 及转换命令。
- [v1.19.32 官方转换源码](https://github.com/MetaCubeX/mihomo/blob/v1.19.32/rules/provider/mrs_converter.go)支持 MRS 输入并导出文本，可用于逐项反向核对。
- [v1.19.32 官方发布](https://github.com/MetaCubeX/mihomo/releases/tag/v1.19.32)提供构建工具；[发布 API](https://api.github.com/repos/MetaCubeX/mihomo/releases/tags/v1.19.32)包含资产 SHA256。

## 固定工具版本

本次生成使用 **Mihomo Meta v1.19.32**。工具仅用于离线规则转换，不启动代理、不改系统或用户设置；可执行文件不提交到此仓库。

| 平台 | 官方下载 | 压缩包 SHA256 |
| --- | --- | --- |
| Windows amd64 compatible | [ZIP](https://github.com/MetaCubeX/mihomo/releases/download/v1.19.32/mihomo-windows-amd64-compatible-v1.19.32.zip) | `974a4d7ad69aed27aa2e8f91d61113573c14dadb14562c63e58effabf59816f0` |
| Linux amd64 v1 | [GZIP](https://github.com/MetaCubeX/mihomo/releases/download/v1.19.32/mihomo-linux-amd64-v1-v1.19.32.gz) | `306f81e723e60ce6b828899a6fe83e1d00e9ecefb2dc8d4d849312a5bc00efdc` |

请下载后先与上表及官方发布 API 的 `digest` 核对，再解压使用。此次 Windows 压缩包核对一致；解压后可执行文件 SHA256 为 `04f8d7fc2b314771e1ecbf15951d59f0e1cb7914503c88cfb6972ff6a824e314`。

## 生成全部格式

在仓库根目录运行，`/path/to/mihomo` 替换为实际工具路径：

```sh
python scripts/build.py --mihomo /path/to/mihomo
python scripts/build.py --check --mihomo /path/to/mihomo
```

单独生成或检查 MRS：

```sh
python scripts/convert_mrs.py --mihomo /path/to/mihomo
python scripts/convert_mrs.py --mihomo /path/to/mihomo --check
```

官方单文件转换和反向核对命令：

```sh
mihomo convert-ruleset domain text rules/m-team/m-team.list m-team.mrs
mihomo convert-ruleset domain mrs m-team.mrs restored.list
```

反向导出的顺序可能与源文件不同，因此比较域名集合。脚本将三个集合先在临时目录生成，逐项反向核对，并确认有效二进制压缩格式；全部通过后才更新输出。`--check` 还要求重新生成的字节与仓库中的文件一致，且不会写入规则输出。固定版本可避免工具升级造成压缩字节变化；升级工具时须重新构建、检查并更新此说明中的版本。

## 2026-10-05 首次构建校验记录

| 文件 | 精确域名数 | 字节数 | SHA256 |
| --- | ---: | ---: | --- |
| `core.mrs` | 24 | 206 | `65f075bd3078cf7cf1645c645f82a1977ff202c4525fd8a44a69f43aa504b8d1` |
| `dependencies.mrs` | 36 | 481 | `548625779e5580f819dcf0da7b011e1f863916231fe844d5be1776893cdad2d3` |
| `m-team.mrs` | 60 | 601 | `ff8c9b1d60ce0967229c08adf428c340e2143bcd74c23e182cbb61c7d050a454` |

三组均已使用官方工具反向导出文本，与相应 `.list` 域名集合一致，并通过相同工具的重新生成字节一致检查。上表记录首次构建结果；以后域名更新会改变文件校验值。

## 2026-10-06 合并后构建校验记录

| 文件 | 规则数 | 字节数 | SHA256 |
| --- | ---: | ---: | --- |
| `core.mrs` | 6 | 135 | `0538e31ded7c2755c376efcf83943b30c4b27f1a283da35d71b8db69a61d049c` |
| `dependencies.mrs` | 38 | 501 | `af5d2ec3f10c88d36eaf93b7ed05fbbecb638f2a58fd0225a54c7675818980a7` |
| `m-team.mrs` | 44 | 560 | `2f7798978f26277ca2398c3058fbcc8f68e1f3300ca85997148064aba004d9f6` |

本轮含 `+.m-team.cc`、`+.m-team.io`、`+.gateway996.com` 后缀表达式。来源保留 64 个已纳入精确主机，生成 44 条匹配规则；三组已通过官方转换、反转集合一致与固定版本重建字节一致检查。
