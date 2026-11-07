# 制作合同与批量记录

## 单片制作包
- brief：平台、受众、主问题、目标时长、比例、风格、预算、配音来源、交付阶段。
- evidence：claim_id、claim、source_url、locator、accessed_at、caveat、confidence。
- script：旁白、屏幕文字、对应 claim_id。短片只讲可在时长内兑现的一个论点。
- storyboard：shot_id、start/end、旁白、教学目标、画面对象、动画变化、镜头、字幕、安全区、素材许可、claim_id、实现方式。
- assets：asset_id、路径、作者、原始URL、授权/许可、修改说明；不要把可下载等同可商用。
- render_manifest：episode_id、version、引擎和锁定依赖、fps、尺寸、音频路径、scene哈希、状态、耗时、错误、产物。
- delivery：成片（若渲染成功）、SRT、封面、标题三个候选、来源说明、源码、复现命令、验证清单及未完成项。

状态顺序：researched → fact_checked → scripted → storyboarded → previewed → rendered → qa_passed。只有用户明确授权后进入 published。
预算超限/核心证据失败/关键资源缺失时将该任务标为 blocked，保留其他已完成任务。命令、密钥与用户私密信息不得进入公开字幕或片尾来源。

## 可调整的60秒叙事初稿
0–5秒：显示真实矛盾与明确问题。
5–15秒：让观众形成预测，交代模型条件。
15–40秒：一个主要视觉比喻逐步解释。
40–52秒：用对照或计算检验。
52–60秒：回答开头，注明最重要边界。
这是起草模板，不是平台算法结论。复杂推导应延长而非加速口播。

## 反馈记录
使用同批快照，不跨平台合并：episode_id, platform, format, publish_time, observed_at, hours_since_publish, impressions, ctr, retention_3s, retention_30s, avg_view_fraction, completion_rate, views, likes, shares, saves, corrections, changed_variable, control_id。
不同平台字段定义不同，保存定义。缺失=null，不反推私有数据。长片不强行与短片比完播；使用相同观察窗口。不设通用“爆款阈值”，先建立账号基线。
