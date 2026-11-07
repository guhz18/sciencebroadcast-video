# 公式推演与 3D 粒子

## Manim 公式镜头

参考 [3b1b/videos](https://github.com/3b1b/videos) 的原始场景和 [3b1b/manim](https://github.com/3b1b/manim) 的 ManimGL。新场景可用 Manim Community 的 MathTex 和 [TransformMatchingTex](https://docs.manim.community/en/stable/reference/manim.animation.transform_matching_parts.TransformMatchingTex.html)；按 TeX 子串显式切分并验证映射，必要时指定 key_map 或单独做消失、出现。移植原场景前核对 ManimGL 的提交版本和资源依赖，两个分支不混用。借鉴时优先写原创场景；引入上游代码时记录文件、提交与许可，分别核对外部图像、配音和音乐权利。

- 用可见对象提出问题。追踪具体量，先用颜色和标注建立量与画面的对应，再写符号。关键操作按“为什么需要这一步 → 哪一项变了 → 回到图上有什么后果”组织。保留关键中间式、边界条件、量纲和负号。给新项和抵消项各自的出现理由。
- 例如水喷泉在一维模型中，先让观众看见水团吸收来水，同时标记质量 M 和速度 U，再用匹配变形拆出 d(MU)/dt = M dU/dt + U dM/dt。将两项分别连回水团的速度和质量变化；外力及动量通量用独立镜头说明。正式使用仍需核对实际模型与符号约定。
- 转入 3D 后保持相同变量颜色，沿同一物理对象切镜。例如先让公式中的 U 对应速度箭头，再进入发光粒子视图；粒子颜色若表示速度，给带单位的图例，并固定比较范围。

## 3D 粒子镜头

先定每个粒子的语义（模拟采样、实测点、示意示踪或纯装饰），确定坐标、单位、步长、初边值、速度或密度映射。用已核验模型、公开数据或明确标注的示意生成位置序列。固定种子及坐标变换，并记录数据出处；3D 位置和遮挡不能暗示测到了额外物理量。

- 优先 Blender Geometry Nodes [实例化](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/instances.html) 渲染大量点。已有轨迹时直接导入帧数据；有状态且确实需要逐步推进时才用 [Simulation Zone](https://docs.blender.org/manual/en/4.4/modeling/geometry_nodes/simulation/simulation_zone.html)，先烘焙后并行出帧。版本按已安装的稳定版文档核对。
- 基础视觉为深色空间、轮廓光、两三层景深、少量发光尾迹。分开科学点和氛围点，用体积光提示深度，关键读数保持清楚。相机推进、环绕或剖切须揭示结构，定量对照使用一致镜头、时间尺度和色标。快慢放和夸张比例明确标示。镜头过密时先减装饰、尾迹和光晕。
- 先以少量粒子和短镜头预览。检查起末帧、遮挡、速度连续性、流量或其他适用的守恒量，再增实例数和分辨率。物理参数与视觉参数独立；改灯光或配色时复用模拟。批量缓存键含模型/数据哈希、种子、步长、帧范围与引擎版本。渲染帧序列允许只补失败帧。交付场景和参数，以共同帧率接入主时间轴。
