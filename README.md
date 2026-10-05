# rules-dat

可维护的域名规则集，格式参照 MetaCubeX。当前收录 M-Team：源数据包含 79 个已观察主机名，订阅规则包含 24 个核心服务和 36 个图片等依赖，合并后为 60 个精确主机名。另有 19 个资料外链或文档示例，仅记录来源，不进入规则。

首次采集日期：**2026-10-05（Asia/Shanghai）**。这是实际浏览范围内的初版清单，后续可继续补充。

## 订阅地址

| 集合 | 主机数 | `.list` / Text | `.mrs` / MRS | `.yaml` / YAML |
| --- | ---: | --- | --- | --- |
| 核心服务 | 24 | [core.list](https://raw.githubusercontent.com/Martin6603/rules-dat/main/rules/m-team/core.list) | [core.mrs](https://raw.githubusercontent.com/Martin6603/rules-dat/main/rules/m-team/core.mrs) | [core.yaml](https://raw.githubusercontent.com/Martin6603/rules-dat/main/rules/m-team/core.yaml) |
| 图片等依赖 | 36 | [dependencies.list](https://raw.githubusercontent.com/Martin6603/rules-dat/main/rules/m-team/dependencies.list) | [dependencies.mrs](https://raw.githubusercontent.com/Martin6603/rules-dat/main/rules/m-team/dependencies.mrs) | [dependencies.yaml](https://raw.githubusercontent.com/Martin6603/rules-dat/main/rules/m-team/dependencies.yaml) |
| 合并集 | 60 | [m-team.list](https://raw.githubusercontent.com/Martin6603/rules-dat/main/rules/m-team/m-team.list) | [m-team.mrs](https://raw.githubusercontent.com/Martin6603/rules-dat/main/rules/m-team/m-team.mrs) | [m-team.yaml](https://raw.githubusercontent.com/Martin6603/rules-dat/main/rules/m-team/m-team.yaml) |

三种格式表示同一组域名，均为 `behavior: domain`，不指定直连或代理策略。

| 扩展名 | provider 的 `format` | 文件内容 |
| --- | --- | --- |
| `.list` | `text` | 每行一个精确主机名，便于阅读和核对。 |
| `.mrs` | `mrs` | 由官方 Mihomo 转换生成的二进制规则集，适用于支持 MRS 的 Mihomo。 |
| `.yaml` | `yaml` | `payload` 数组，便于阅读和手动编辑配置。 |

全部条目采用精确主机名，不扩展第三方根域。例如 `api.gateway996.com` 只匹配该主机。依赖集合包含共享图床和封面 CDN，因此同一主机服务的其他网站也会匹配；需要较窄范围时使用核心集合。格式依据：[MetaCubeX 规则集合内容说明](https://wiki.metacubex.one/config/rule-providers/content/)。

## 使用示例

将 provider 合并到已有 Mihomo 配置中：

```yaml
rule-providers:
  m-team:
    type: http
    behavior: domain
    format: mrs
    url: https://raw.githubusercontent.com/Martin6603/rules-dat/main/rules/m-team/m-team.mrs
    path: ./ruleset/m-team.mrs
    interval: 86400
```

随后在已有 `rules` 中加入 `RULE-SET,m-team,你的策略组`，并替换成实际策略名称。选择 `.list` 时，将 `format` 改为 `text`；选择 `.yaml` 时改为 `yaml`，同时替换 `url` 和 `path` 为对应扩展名。

## 来源和维护

- [sources/m-team/README.md](sources/m-team/README.md)：采集范围、来源、证据类型和图片加载问题说明。
- [sources/m-team/DOMAINS.md](sources/m-team/DOMAINS.md)：全部 79 个主机名的用途及来源。
- [sources/m-team/domains.json](sources/m-team/domains.json)：可维护源数据，保留脱敏证据和纳入规则的标记。
- [rules/m-team/](rules/m-team/)：三组集合的 `.list`、`.mrs`、`.yaml` 生成文件。
- [scripts/build.py](scripts/build.py)：从源数据生成和检查订阅文件。
- [scripts/MRS.md](scripts/MRS.md)：官方转换工具版本、下载校验和 MRS 构建验证说明。

修改源数据后，使用 Python 和 [官方 Mihomo](https://github.com/MetaCubeX/mihomo/releases) 重新生成、检查并一起提交：

```text
python scripts/build.py --mihomo /path/to/mihomo
python scripts/build.py --check --mihomo /path/to/mihomo
```

Windows 可传入 `mihomo.exe` 的路径。生成器校验域名、证据和集合标记，再调用官方转换工具生成 MRS；`--check` 在临时目录重新转换并核对已提交文件，不修改仓库文件。只检查或生成可读格式时可使用 `--text-only`，发布更新时仍须完成三种格式的检查。

规则原先位于 `Martin6603/iptv`，现迁移至本独立仓库；新增订阅请使用上表地址。
