# rules-dat

可维护的域名规则集，格式参照 MetaCubeX。M-Team 源记录包含 **83 个主机名**：25 个核心服务、39 个图片等关联依赖、19 个不进入订阅的外链或示例。64 个纳入主机经同根域合并后生成 **44 条规则**。

首次采集：2026-10-05；最近核对及用户确认：**2026-10-06（Asia/Shanghai）**。

## 订阅地址

| 集合 | 来源主机数 | 生成规则数 | `.list` / Text | `.mrs` / MRS | `.yaml` / YAML |
| --- | ---: | ---: | --- | --- | --- |
| 核心服务 | 25 | 6 | [core.list](https://raw.githubusercontent.com/Martin6603/rules-dat/main/rules/m-team/core.list) | [core.mrs](https://raw.githubusercontent.com/Martin6603/rules-dat/main/rules/m-team/core.mrs) | [core.yaml](https://raw.githubusercontent.com/Martin6603/rules-dat/main/rules/m-team/core.yaml) |
| 图片等关联依赖 | 39 | 38 | [dependencies.list](https://raw.githubusercontent.com/Martin6603/rules-dat/main/rules/m-team/dependencies.list) | [dependencies.mrs](https://raw.githubusercontent.com/Martin6603/rules-dat/main/rules/m-team/dependencies.mrs) | [dependencies.yaml](https://raw.githubusercontent.com/Martin6603/rules-dat/main/rules/m-team/dependencies.yaml) |
| 合并集 | 64 | 44 | [m-team.list](https://raw.githubusercontent.com/Martin6603/rules-dat/main/rules/m-team/m-team.list) | [m-team.mrs](https://raw.githubusercontent.com/Martin6603/rules-dat/main/rules/m-team/m-team.mrs) | [m-team.yaml](https://raw.githubusercontent.com/Martin6603/rules-dat/main/rules/m-team/m-team.yaml) |

三种格式表示同一组匹配规则，均为 `behavior: domain`，不指定直连或代理策略。

| 扩展名 | provider 的 `format` | 内容 |
| --- | --- | --- |
| `.list` | `text` | 每行一个精确主机或 `+.根域` 表达式。 |
| `.mrs` | `mrs` | 官方 Mihomo 转换生成的二进制规则集。 |
| `.yaml` | `yaml` | 带引号的 `payload` 数组。 |

## 同根域合并

| 表达式 | 覆盖范围 |
| --- | --- |
| `+.m-team.cc` | 根域及其所有层级子域，包括 `api`、`api2`、`kp`、`img`、`tp` 等。 |
| `+.m-team.io` | 根域及其所有层级子域，包括 API、备用入口、Tracker、RSS 和工单。 |
| `+.gateway996.com` | 根域及其所有层级子域，合并已记录的 `api.gateway996.com` 与 `ai.gateway996.com`。 |

以上三个根域按用户要求合并；四个独立下载／Tracker 服务、其他图床和共享 CDN 保持精确主机匹配。合并依据是域名后缀，源记录仍保留每个主机的证据；相同 IP 不能作为跨域名合并的依据。根域规则也会覆盖尚未逐个记录的子域。格式依据：[MetaCubeX 域名通配符](https://wiki.metacubex.one/handbook/syntax/#域名通配符)、[规则集合内容](https://wiki.metacubex.one/config/rule-providers/content/)。

关联依赖包括图片、字体、网关及 5 个网关 `uri` 上游参考。上游参考和 CSS 引用不等于已观察到浏览器直接请求。独立共享图床／CDN 的精确主机也可能服务其他网站；需要较窄范围可使用核心集合。

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

在已有 `rules` 中加入 `RULE-SET,m-team,你的策略组`，替换成实际策略名称。选择 `.list` 时用 `format: text`，选择 `.yaml` 时用 `format: yaml`，同时替换 URL 和 path 的扩展名。

## Fake-IP 过滤

`blacklist` 模式可参考生成的 [DNS 合并示例](examples/m-team-fake-ip-filter.yaml)，它包含同样的 44 个匹配表达式。只合并过滤条目，保留已有配置。

现有 DNS 为 `fake-ip-filter-mode: rule` 时，应使用该模式的规则语法，把以下项放在兜底 `MATCH,fake-ip` 前；provider 名须与配置一致：

```yaml
dns:
  fake-ip-filter-mode: rule
  fake-ip-filter:
    - DOMAIN-SUFFIX,gateway996.com,real-ip
    - RULE-SET,m-team,real-ip
    # 保留原有其他规则
    - MATCH,fake-ip
```

第一条在远程规则暂未加载时覆盖 `api`、`ai` 和其他网关子域。过滤不改变业务分流策略，也不能单独保证所有图片成功。依据：[Mihomo Fake-IP 过滤](https://wiki.metacubex.one/config/dns/#fake-ip-filter-mode)。

## 来源和维护

- [采集说明](sources/m-team/README.md)：范围、证据等级与图片问题。
- [逐项明细](sources/m-team/DOMAINS.md)：83 个精确来源主机、生成规则及证据。
- [维护源数据](sources/m-team/domains.json)：每个 `hostname` 的脱敏证据和可选 `rule`。
- [2026-10-06 核对与合并记录](sources/m-team/REVIEW-20261006.md)。
- [生成文件](rules/m-team/)：三组 `.list`、`.mrs`、`.yaml`。
- [构建脚本](scripts/build.py)与 [MRS 校验说明](scripts/MRS.md)。

修改源数据后，使用 Python 和 [官方 Mihomo](https://github.com/MetaCubeX/mihomo/releases) 重新生成、检查并一起提交：

```text
python scripts/build.py --mihomo /path/to/mihomo
python scripts/build.py --check --mihomo /path/to/mihomo
```

`hostname` 必须为精确主机；省略 `rule` 时按该主机生成。需要后缀合并时显式设置 `rule: +.根域`，且必须覆盖该来源主机。脚本去重、校验组内／组间规则重叠，再用官方工具转换及反转 MRS。`--check` 在临时目录核对，固定版本应产生相同字节。可读格式可用 `--text-only`，发布仍须检查三种格式。

规则原先位于 `Martin6603/iptv`，现由此独立仓库维护。
