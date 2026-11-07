# 起始研究快照

检索日期：2026-11-07，Asia/Shanghai。以下为公开检索快照，并非全网排名或实时API数据。不得把本表当作未来调用的当前数值；须重新获取。没有逐帧观看，案例叙事判断限于标题、简介、公开文字说明。

| 案例 | 播放/点赞快照 | 来源及局限 | 值得检验的机制 |
|---|---|---|---|
| 3Blue1Brown: But what is a neural network? | 24,354,709 / 561,000 | https://www.youtube.com/watch?v=aircAruvnKk 搜索返回视频元数据，2017-10-05发布 | 抽象热门概念通过可见结构降低理解门槛 |
| 3Blue1Brown: Why do colliding blocks compute pi? | 7,051,025 / 214,000 | https://www.youtube.com/watch?v=jsYwFizhncE 搜索元数据，2019-01-20发布；勿与2025新版合并 | 两个熟悉对象产生意外数学关系 |
| Veritasium: The Simplest Math Problem No One Can Solve | 46,616,673 / 944,044 | https://digitalcreators.jp/en/channel/en/UCHnyfMqiRRG1u-2MsSQLbXA/popular-videos/ 第三方2026年10月榜单，精确采集时刻未知 | 极低入门门槛与未解难题形成反差 |
| Kurzgesagt: The Coronavirus Explained & What You Should Do | 约88M / 约1.2M | https://filmot.com/sidebyside/BtN-goy9VOY/en/ko/English/Korean/The%2BCoronavirus%2BExplained%2B%26%2BWhat%2BYou%2BShould%2BDo 第三方摘要，取整，实际采集日期未知 | 公共事件相关性与解释需求；不能推断普通选题可复制其传播 |
| 毕导：这是什么妖术？酒在坛子里是绿色，舀出来瞬间变红！ | 约2216.6万 / null | https://search.bilibili.com/zh-Hans/all?keyword=%40%E6%AF%95%E5%AF%BC 原平台搜索结果；缺点赞和可靠年份，不纳入最高赞排行 | 日常现象、直接可见变化、反直觉疑问 |

这些不是已证实的成功因果；尚未完成匹配对照、账号体量控制或留存分析。疫情案例仅研究传播背景，不复用过期医疗建议。

## 公开制作流程（一手来源）
- https://kurzgesagt.org/what-we-do?visit=videos ：团队公开说明研究与专家核验、脚本、插画、配音动画、音乐音效。说明来源表和配音决定动画节奏。
- https://www.patreon.com/Kurzgesagt/posts/how-to-make-in-34029605 ：2020年官方帖子称一片约1200工时；是历史团队案例，不是今天每片成本或个人必需预算。
- https://github.com/3b1b/manim 与 https://github.com/3b1b/videos ：作者的动画引擎及视频代码。旧代码可能不兼容新版本；开源代码许可不自动赋予原视频/音乐权利。
- https://www.3blue1brown.com/lessons/colliding-blocks-v2/ ：2025新版文字解释；与2019视频是不同作品。模型需说明弹性碰撞、无摩擦等条件。

## 可复用 skills 和执行技术
- https://www.remotion.dev/docs/ai/skills ：Remotion 官方 agent skills 入口。
- https://github.com/remotion-dev/skills ：官方维护，检索页面约6.5k Stars；覆盖创建、动画版式、字幕、渲染等。Stars 是项目关注，不是视频点赞或质量测试。仅在本次比较候选中较高，不能称全网最高。
- https://github.com/adithya-s-k/manim_skill ：社区维护，检索页面约1.3k Stars；含 Manim CE/GL 技能。这不是3Blue1Brown官方技能，也不是爆款策略。
- https://docs.manim.community/en/stable/ ：Manim CE 官方文档。

本技能是原创编排层，借鉴公开工作流程与技术路线，未复制第三方技能正文，也未捆绑安装其依赖。执行时按需读取当前文档与许可；现有技能可直接调用，缺失则使用官方文档实现。渲染和配音能力需在目标环境验证。
