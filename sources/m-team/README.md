# M-Team 采集来源

首次采集为 2026-10-05，2026-10-06 重新浏览 Chrome 页面并结合用户确认修订。记录 **83 个精确来源主机**：25 个核心、39 个图片等关联依赖、19 个外链／示例。64 个纳入主机合并为 **6 条核心 + 38 条依赖 = 44 条规则**。

订阅及格式见[仓库首页](../../README.md)，所有来源和对应表达式见 [DOMAINS.md](DOMAINS.md)，维护数据见 [domains.json](domains.json)。

## 规则与来源主机

`hostname` 保留精确主机及证据，`rule` 保存显式合并的表达式。M-Team 命名空间归入 `+.m-team.cc`、`+.m-team.io`，两个网关主机归入 `+.gateway996.com`；其他条目缺省使用精确主机。来源表中的多条主机可对应同一生成规则，订阅不会重复输出。

控制台明确提供的四个独立服务保持精确匹配：`bt1.manfuz.co`、`fr1.halomt.com`、`hs1.holysalt.org`、`tra99.manfuz.co`。没有按共享 IP 合并不相关域名，也没有扩大其他第三方根域。

## 本轮增补

| 主机 | 证据 |
| --- | --- |
| `tp.m-team.cc` | 小组页新文档的图片资源记录；未取得该主机对应 DOM 图片状态。 |
| `img.digitalcore.club` | 分类分页的图片资源记录；独立刷新未重现，用户随后明确确认已检查。 |
| `fonts.gstatic.com` | 已观察手机版 Google Fonts CSS 内 Inter 字体 `src` 引用；条件依赖，未观察实际字体请求。 |
| `ai.gateway996.com` | 用户提供地址、确认遗漏并批准与 api 网关合并；不标成工具浏览证据。 |

`api.gateway996.com` 已收录，本轮两个电影详情有内联／计算样式与资源记录，游戏页有一个图像不可用状态。已收录并不等于 DNS／浏览器图片故障已经修复。

## 网关上游参考

以下 5 个主机仅观察到 `nested_uri`：`img1.doubanio.com`、`img2.doubanio.com`、`img3.doubanio.com`、`img9.doubanio.com`、`m.media-amazon.com`。没有直接客户端请求证据。按关联域名全集保留在依赖订阅并单列说明，未因本轮不直接出现删除；未来如定位为实际客户端连接集合，需结合重定向／请求证据再审核范围。

资料外链和文档示例仅保留来源，不进入规则。`tracker.abcdef.com` 是配置示例，不是实际 Tracker。

## 覆盖范围与证据

两轮分别有 40 与 29 条采样，包含首页、电影、电视、音乐、综合分类、软件、游戏、电子书、分类分页、详情、小组、展示、上传、卡片、论坛、片单、求种、候选、字幕、控制台、手机版、导航、工单及官方 Wiki。重复页面状态保留在 `pages_checked`，日期分开记录，不能把采样数当成不同页面数。

证据类型：`page` 为页面地址；`link`／`image`／`inline_style` 等为 DOM 引用；`visible_domain` 为控制台选项；`observed_*` 为资源记录；`nested_uri` 为上游参数；`nested_imdb`／`nested_douban` 为资料目标；`stylesheet_reference` 为已观察 CSS 的条件引用；`user_reported`／`user_confirmed` 为用户补充。每条证据保留日期和脱敏页面路径。

资源记录可能包含 SPA 较早请求，新文档资源也不提供 HTTP 状态、是否缓存或最终 IP。引用不独立证明加载成功；当前未重现不证明旧主机错误。本轮没有按未出现删除旧项，也没有穷尽历史种子、帖子、用户图床或未来子域。备用网址证据：[官方 Wiki 入口](https://wiki.m-team.cc/zh-tw/siteurl)。

只保存主机、匹配表达式与脱敏路径；查询、签名、passkey、账号信息、Cookie 和详情编号均不保留。控制台仅展开选项，没有保存设置，未探测 Tracker 或下载种子。

## 图片加载与 Fake-IP

用户此前控制台错误指向 `api.gateway996.com`，提示 `local` 地址空间访问被拒绝。本轮一个网关图片不可用状态没有对应错误码或当前 DNS 结果，不能据此认定其仍是同一原因。

网关后缀可用于现有 Fake-IP 过滤。`rule` 模式使用 `DOMAIN-SUFFIX,gateway996.com,real-ip` 与 `RULE-SET,你的provider名,real-ip`，放在 `MATCH,fake-ip` 前；`blacklist` 模式参考 [生成示例](../../examples/m-team-fake-ip-filter.yaml)。必须按现有模式合并，不能用 blacklist 片段替换 rule 配置。过滤不指定直连／代理业务策略。依据：[Mihomo DNS 过滤](https://wiki.metacubex.one/config/dns/#fake-ip-filter-mode)。

## 更新步骤

1. 确认来源主机、用途与证据，区分请求、条件引用、上游参数和外链。
2. 更新 `domains.json` 的日期、证据、纳入标记及必要的 `rule`。两组互斥；后缀须覆盖 hostname。
3. 执行 `python scripts/build.py --mihomo /path/to/mihomo` 和对应 `--check`。
4. 一并提交来源、说明、三种生成格式及最新构建校验记录。
