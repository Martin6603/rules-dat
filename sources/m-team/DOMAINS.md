# M-Team 来源主机及生成规则

首次采集：2026-10-05；最近核对：2026-10-06（Asia/Shanghai）。共 83 条来源，64 个纳入主机映射到 44 条规则。`+.根域` 包含根域和任意层级子域；用途与完整证据见 [domains.json](domains.json)。

## 核心服务（25 来源／6 规则）

| 来源主机 | 生成规则 | 用途 | 证据类型／来源 |
| --- | --- | --- | --- |
| `api.m-team.cc` | `+.m-team.cc` | 站点 API 接口 | image, image_current, observed_image, observed_other；`https://kp.m-team.cc/browse/music` |
| `api.m-team.io` | `+.m-team.io` | 站点 API 接口（io 域名） | observed_other；`https://kp.m-team.cc/browse/music` |
| `api2.m-team.cc` | `+.m-team.cc` | 补充 API／图片资源接口 | image, observed_image, observed_other；`https://kp.m-team.cc/browse/music` |
| `bt1.manfuz.co` | `bt1.manfuz.co` | 控制台提供的种子下载服务地址；域名归属未独立核实 | observed_other, visible_domain, visible_text；`https://kp.m-team.cc/usercp` |
| `fr1.halomt.com` | `fr1.halomt.com` | 控制台提供的种子下载服务地址；域名归属未独立核实 | observed_other, visible_domain, visible_text；`https://kp.m-team.cc/usercp` |
| `h5.m-team.cc` | `+.m-team.cc` | 移动版入口及移动版资源 | dom_attribute, image, image_current, link, observed_image, observed_other, observed_script, observed_stylesheet, page, script, stylesheet_or_link；`https://kp.m-team.cc/browse/music` |
| `h5.m-team.io` | `+.m-team.io` | 页面提供的移动版入口（仅观察链接） | link；`https://zp.m-team.io/login` |
| `hs1.holysalt.org` | `hs1.holysalt.org` | 控制台提供的种子下载服务地址；域名归属未独立核实 | observed_other, visible_domain, visible_text；`https://kp.m-team.cc/usercp` |
| `img.m-team.cc` | `+.m-team.cc` | 站内图片服务 | image, image_current, observed_image；`https://kp.m-team.cc/browse/music` |
| `kp.m-team.cc` | `+.m-team.cc` | 当前桌面版主站入口 | image, image_current, link, observed_font, observed_image, page, visible_text；`https://kp.m-team.cc/browse/music` |
| `m-team.cc` | `+.m-team.cc` | 公开站点导航入口 | link, observed_image, page, visible_domain, visible_text；`https://wiki.m-team.cc/zh-tw/home` |
| `ob.m-team.cc` | `+.m-team.cc` | 官方 Wiki 列出的入口，已查看登录页 | image, link, observed_image, observed_other, observed_script, observed_stylesheet, page, script, stylesheet_or_link, visible_text；`https://wiki.m-team.cc/zh-tw/siteurl` |
| `rss.m-team.cc` | `+.m-team.cc` | 控制台提供的 RSS 服务地址 | observed_other, visible_domain, visible_text；`https://kp.m-team.cc/usercp` |
| `rss.m-team.io` | `+.m-team.io` | 控制台提供的 RSS 服务地址（io 域名） | observed_other, visible_domain, visible_text；`https://kp.m-team.cc/usercp` |
| `static.m-team.cc` | `+.m-team.cc` | 站点静态脚本、样式和图片资源 | dom_attribute, image, image_current, observed_image, observed_other, observed_script, observed_stylesheet, script, stylesheet_or_link；`https://kp.m-team.cc/browse/music` |
| `ticket.m-team.io` | `+.m-team.io` | 工单支持入口 | image, image_current, link, observed_font, observed_image, observed_other, observed_script, observed_stylesheet, page, script, stylesheet_or_link, visible_text；`https://kp.m-team.cc/browse/music` |
| `tp.m-team.cc` | `+.m-team.cc` | 小组页面观察到的站内图片资源主机（新文档资源记录；未取得对应 DOM 加载状态） | observed_image；`https://kp.m-team.cc/team` |
| `tra1.m-team.cc` | `+.m-team.cc` | 控制台提供的 Tracker 地址 | observed_other, visible_domain；`https://kp.m-team.cc/usercp` |
| `tra1.m-team.io` | `+.m-team.io` | 控制台提供的 Tracker 地址（io 域名） | observed_other, visible_domain；`https://kp.m-team.cc/usercp` |
| `tra99.manfuz.co` | `tra99.manfuz.co` | 控制台提供的 Tracker 地址；域名归属未独立核实 | observed_other, visible_domain；`https://kp.m-team.cc/usercp` |
| `tracker.m-team.cc` | `+.m-team.cc` | 控制台提供的 Tracker 地址 | observed_other, visible_domain；`https://kp.m-team.cc/usercp` |
| `tracker.m-team.io` | `+.m-team.io` | 控制台提供的 Tracker 地址（io 域名） | observed_other, visible_domain；`https://kp.m-team.cc/usercp` |
| `wiki.m-team.cc` | `+.m-team.cc` | 官方 Wiki 和站点使用说明 | image, inline_style, link, observed_font, observed_image, observed_other, observed_script, observed_stylesheet, page, script, stylesheet_or_link；`https://kp.m-team.cc/browse/music` |
| `www.m-team.cc` | `+.m-team.cc` | 公开导航页页脚链接（仅观察链接） | link；`https://m-team.cc/` |
| `zp.m-team.io` | `+.m-team.io` | 官方 Wiki 列出的备用入口，已查看登录页 | link, observed_font, page, visible_text；`https://wiki.m-team.cc/zh-tw/siteurl` |

## 图片等关联依赖（39 来源／38 规则）

| 来源主机 | 生成规则 | 用途 | 证据类型／来源 |
| --- | --- | --- | --- |
| `82.imagebam.com` | `82.imagebam.com` | 页面嵌入或浏览器资源清单中出现的第三方图片来源（共享主机） | image, image_current, observed_image；`https://kp.m-team.cc/browse/adult` |
| `ai.gateway996.com` | `+.gateway996.com` | 用户确认遗漏的网关主机；与 api.gateway996.com 合并为 gateway996.com 后缀规则 | user_reported；`https://ai.gateway996.com/` |
| `api.gateway996.com` | `+.gateway996.com` | 图片重定向网关；本次 Chrome 图片加载错误涉及的主机 | image, image_current, inline_style, observed_image；`https://kp.m-team.cc/browse/music` |
| `avatars.githubusercontent.com` | `avatars.githubusercontent.com` | 页面嵌入或浏览器资源清单中出现的第三方图片来源（共享主机） | image, image_current, observed_image；`https://kp.m-team.cc/browse` |
| `awsimgsrc.dmm.co.jp` | `awsimgsrc.dmm.co.jp` | 页面嵌入或浏览器资源清单中出现的第三方图片来源（共享主机） | image, image_current, observed_image；`https://kp.m-team.cc/browse/adult` |
| `et8.org` | `et8.org` | 页面嵌入或浏览器资源清单中出现的第三方图片来源（共享主机） | image, image_current, observed_image；`https://kp.m-team.cc/browse` |
| `fonts.googleapis.com` | `fonts.googleapis.com` | 移动版页面引用的 Google Fonts 样式资源（仅观察样式请求） | observed_stylesheet；`https://h5.m-team.cc/` |
| `fonts.gstatic.com` | `fonts.gstatic.com` | 手机版 Inter 字体 CSS 引用的字体文件主机（条件依赖，未观察实际字体请求） | stylesheet_reference；`https://h5.m-team.cc/` |
| `i.endpot.com` | `i.endpot.com` | 页面嵌入或浏览器资源清单中出现的第三方图片来源（共享主机） | image, observed_image；`https://kp.m-team.cc/browse` |
| `i.postimg.cc` | `i.postimg.cc` | 页面嵌入或浏览器资源清单中出现的第三方图片来源（共享主机） | image；`https://kp.m-team.cc/browse` |
| `i.slow.pics` | `i.slow.pics` | 页面嵌入或浏览器资源清单中出现的第三方图片来源（共享主机） | image, observed_image；`https://kp.m-team.cc/browse/music` |
| `image.bingfong.com` | `image.bingfong.com` | 页面嵌入或浏览器资源清单中出现的第三方图片来源（共享主机） | observed_image；`https://kp.m-team.cc/browse` |
| `image.tmdb.org` | `image.tmdb.org` | 封面／海报图片来源 | observed_image；`https://kp.m-team.cc/browse/music` |
| `images2.imgbox.com` | `images2.imgbox.com` | 页面嵌入或浏览器资源清单中出现的第三方图片来源（共享主机） | observed_image；`https://kp.m-team.cc/browse/tvshow` |
| `img.digitalcore.club` | `img.digitalcore.club` | M-Team 分类分页中观察到的第三方图片资源；用户确认已检查，独立刷新未稳定重现 | observed_image, user_confirmed；`https://kp.m-team.cc/browse/adult` |
| `img1.doubanio.com` | `img1.doubanio.com` | 图片网关 uri 参数中的豆瓣海报上游主机 | nested_uri；`https://kp.m-team.cc/browse/movie` |
| `img10.pixhost.to` | `img10.pixhost.to` | 页面嵌入或浏览器资源清单中出现的第三方图片来源（共享主机） | image, image_current, observed_image；`https://kp.m-team.cc/browse/adult` |
| `img2.doubanio.com` | `img2.doubanio.com` | 图片网关 uri 参数中的豆瓣海报上游主机 | nested_uri；`https://kp.m-team.cc/browse/tvshow` |
| `img3.doubanio.com` | `img3.doubanio.com` | 图片网关 uri 参数中的豆瓣海报上游主机 | nested_uri；`https://kp.m-team.cc/browse/movie` |
| `img9.doubanio.com` | `img9.doubanio.com` | 图片网关 uri 参数中的豆瓣海报上游主机 | nested_uri；`https://kp.m-team.cc/browse/music` |
| `imge.kugou.com` | `imge.kugou.com` | 音乐封面图片来源 | image, observed_image；`https://kp.m-team.cc/browse/music` |
| `imgs.aventertainments.com` | `imgs.aventertainments.com` | 页面嵌入或浏览器资源清单中出现的第三方图片来源（共享主机） | observed_image；`https://kp.m-team.cc/browse/adult` |
| `m.media-amazon.com` | `m.media-amazon.com` | 图片网关 uri 参数中的海报上游主机 | nested_uri；`https://kp.m-team.cc/browse/tvshow` |
| `open.cd` | `open.cd` | 页面嵌入或浏览器资源清单中出现的第三方图片来源（共享主机） | image, observed_image；`https://kp.m-team.cc/browse/music` |
| `origin.picgo.net` | `origin.picgo.net` | 页面嵌入或浏览器资源清单中出现的第三方图片来源（共享主机） | observed_image；`https://kp.m-team.cc/browse/music` |
| `phoenix.xboxunity.net` | `phoenix.xboxunity.net` | 游戏图片来源 | image, image_current, observed_image；`https://kp.m-team.cc/browse` |
| `pics.dmm.co.jp` | `pics.dmm.co.jp` | 页面嵌入或浏览器资源清单中出现的第三方图片来源（共享主机） | image, image_current, observed_image；`https://kp.m-team.cc/browse/adult` |
| `ptpimg.me` | `ptpimg.me` | 页面嵌入或浏览器资源清单中出现的第三方图片来源（共享主机） | image, observed_image；`https://kp.m-team.cc/browse/music` |
| `s2.loli.net` | `s2.loli.net` | 页面嵌入或浏览器资源清单中出现的第三方图片来源（共享主机） | image, observed_image；`https://kp.m-team.cc/browse` |
| `s3.bmp.ovh` | `s3.bmp.ovh` | 页面嵌入或浏览器资源清单中出现的第三方图片来源（共享主机） | image, image_current, observed_image；`https://kp.m-team.cc/browse` |
| `shared.akamai.steamstatic.com` | `shared.akamai.steamstatic.com` | 游戏封面图片来源 | image, image_current, observed_image；`https://kp.m-team.cc/browse` |
| `shared.fastly.steamstatic.com` | `shared.fastly.steamstatic.com` | 游戏封面图片来源 | observed_image；`https://kp.m-team.cc/browse` |
| `static.qobuz.com` | `static.qobuz.com` | 音乐封面图片来源 | image, observed_image；`https://kp.m-team.cc/browse/music` |
| `static2.fnnas.com` | `static2.fnnas.com` | 页面嵌入或浏览器资源清单中出现的第三方图片来源（共享主机） | image, observed_image；`https://kp.m-team.cc/browse` |
| `steamcdn-a.akamaihd.net` | `steamcdn-a.akamaihd.net` | 游戏封面图片来源 | image, image_current, observed_image；`https://kp.m-team.cc/browse` |
| `upload.wikimedia.org` | `upload.wikimedia.org` | 页面嵌入或浏览器资源清单中出现的第三方图片来源（共享主机） | image, observed_image；`https://kp.m-team.cc/browse` |
| `www.anduinos.com` | `www.anduinos.com` | 页面嵌入或浏览器资源清单中出现的第三方图片来源（共享主机） | image, observed_image；`https://kp.m-team.cc/browse` |
| `www.drive-image.com` | `www.drive-image.com` | 页面嵌入或浏览器资源清单中出现的第三方图片来源（共享主机） | image, image_current, observed_image；`https://kp.m-team.cc/browse` |
| `y.gtimg.cn` | `y.gtimg.cn` | 音乐封面图片来源 | image, observed_image；`https://kp.m-team.cc/browse/music` |

## 不纳入规则（19）

| 来源主机 | 生成规则 | 用途 | 证据类型／来源 |
| --- | --- | --- | --- |
| `bangumi.tv` | `不纳入` | 条目资料外链 | link；`https://kp.m-team.cc/browse` |
| `book.douban.com` | `不纳入` | 图书资料目标链接 | nested_douban；`https://kp.m-team.cc/browse` |
| `docs.qnap.com` | `不纳入` | Wiki 引用的 QNAP 文档链接 | link；`https://wiki.m-team.cc/zh-tw/cf-choose-better-ip` |
| `download.fastgit.org` | `不纳入` | Wiki 历史下载链接，未验证可用性 | link；`https://wiki.m-team.cc/zh-tw/cf-choose-better-ip` |
| `github.com` | `不纳入` | Wiki 引用的项目和工具链接 | link, visible_text；`https://wiki.m-team.cc/zh-tw/cf-choose-better-ip` |
| `ip.flares.cloud` | `不纳入` | Wiki 引用的 IP 查询链接 | link；`https://wiki.m-team.cc/zh-tw/cf-choose-better-ip` |
| `kb.synology.cn` | `不纳入` | Wiki 引用的 Synology 文档链接 | link；`https://wiki.m-team.cc/zh-tw/cf-choose-better-ip` |
| `movie.douban.com` | `不纳入` | 电影资料外链／目标链接 | link, nested_douban；`https://kp.m-team.cc/browse/music` |
| `music.douban.com` | `不纳入` | 音乐资料目标链接 | nested_douban；`https://kp.m-team.cc/browse/music` |
| `registry.hub.docker.com` | `不纳入` | Wiki 引用的容器镜像链接 | link；`https://wiki.m-team.cc/zh-tw/cf-choose-better-ip` |
| `stock.hostmonit.com` | `不纳入` | Wiki 引用的 IP 查询链接 | link；`https://wiki.m-team.cc/zh-tw/cf-choose-better-ip` |
| `t.me` | `不纳入` | 官方 Wiki 中的 Telegram 外链 | link, visible_text；`https://wiki.m-team.cc/zh-tw/home` |
| `tracker.abcdef.com` | `不纳入` | Wiki 配置示例中的占位域名，非实际 M-Team Tracker | link；`https://wiki.m-team.cc/zh-tw/cf-choose-better-ip` |
| `video.dmm.co.jp` | `不纳入` | 作品资料外链 | link；`https://kp.m-team.cc/browse/adult` |
| `wiki.js.org` | `不纳入` | Wiki 软件页脚链接 | link；`https://wiki.m-team.cc/zh-tw/home` |
| `www.dmm.co.jp` | `不纳入` | 作品资料外链 | link；`https://kp.m-team.cc/browse/adult` |
| `www.douban.com` | `不纳入` | 详情页可见的资料网站名称／链接 | visible_text；`https://kp.m-team.cc/detail/{id}` |
| `www.imdb.com` | `不纳入` | IMDb 资料目标链接 | nested_imdb；`https://kp.m-team.cc/browse/music` |
| `www.pescms.com` | `不纳入` | 工单软件页脚链接 | link；`https://ticket.m-team.io/` |
