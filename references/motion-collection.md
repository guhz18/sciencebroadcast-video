# 动效 skills 集锦与调度

核验日期：2026-11-07。只汇集原作者入口和原创用途说明，没有复制整个第三方技能，也没有声称这些项目均已安装或跑通。选中后读取其当前SKILL、相关规则及许可证，记录精确commit/version；未锁定前不可宣称可复现。不得把工具热度等同视频爆火。

| 条目 | 原始入口 / 技能位置 | 用途 | 状态及取舍 |
|---|---|---|---|
| Remotion 官方 skills | https://github.com/remotion-dev/skills ，skills/；https://www.remotion.dev/docs/ai/skills | 主时间轴、音频、字幕、React动效、合成 | 官方首选；按任务加载remotion-create/markup/captions/render，不全读；技能许可与Remotion运行时商业条款分别核验 |
| claude-motion | https://github.com/whaleyxbt/claude-motion ，.claude/skills/ 与AGENTS.md | 动效设计、画面自检、声音与模拟视频工作流 | 社区作者项目，MIT；作为设计补充，不替代科学核验；作者宣传不算独立测评 |
| manim-skill | https://github.com/vumichien/manim-skill ，skills/manim-video/SKILL.md | 数学/物理推导镜头、分镜与Manim编排 | 社区项目，仓库标Apache-2.0；不默认启动其多角色全链，省token时只取需要规则；引擎许可另查 |
| HyperFrames | https://github.com/heygen-com/hyperframes ，skills/hyperframes/SKILL.md；https://hyperframes.heygen.com/ | HTML/GSAP可寻址动效与逐帧视频 | 官方HTML路线备选；仓库标Apache-2.0；须核验所选版本浏览器依赖；不与Remotion双开重做同一片 |

## 加载方法
1. 明确镜头需求，最多选择一个主合成引擎＋一个专业镜头工具＋一个设计补充。
2. 若环境已有对应技能，读取并使用；否则从原仓库只取选定SKILL与它必需引用，不运行目录网站给的安装脚本。
3. 按 setup.md 自动配置所选工具链和项目级依赖；仅需项目规则时按需读取，避免全局安装。安装个人技能时遵循技能管理流程。
4. 审阅命令与依赖、记录许可证和commit，验证一段短镜头后才投入全片。官方安装入口如 `npx skills add remotion-dev/skills` 是待审阅的发现入口，不是无条件自动执行指令。
5. 把科学内容、旁白、时间轴、场景参数放在自身项目；第三方技能更新不自动改已锁定的工程。

优先组合：趣味科普=Remotion＋claude-motion；微积分解释=Remotion＋Manim；已有HTML动效=HyperFrames。首次任务不下载整套模板仓库、全量视频或模型权重，不递归搜集183个目录条目。

精确技能文件与核验commit见 [motion-sources.json](motion-sources.json)。这是发现快照，不代表已经安装/渲染验证；运行时应确认这些版本与项目引擎兼容。Remotion仓库API未返回许可证标识，复制分发前必须进一步核验，当前仅索引链接。
