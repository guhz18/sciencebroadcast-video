# 配音与本人声音

核验日期：2026-11-07。官方能力不等于当前环境已有账号。价格、模型可用性、商用权与数据保留在实际调用前以所选账号官方条款为准；不写死价格或保证最佳音质。

## 默认使用自动生成的旁白

优先已授权、可输出音频文件的生成工具。标准合成声线优先；只有用户明确要求真人录音才进入真人路线。接口受阻时切换其他自动生成工具；全部受阻时保留待自动配音预览。

## 按工作方式选工具

这是常见工作流的工具举例，依据官方功能说明，无市场份额排名。

| 工作方式 | 工具 | 选择理由 |
|---|---|---|
| 真人录制（仅明确要求时） | 手机录音、Audacity | 手机足以先试读；Audacity适合分段录制、补录、编辑和混音。https://support.audacityteam.org/basics/recording-your-voice-and-microphone |
| 剪辑器内生成 | 剪映专业版 | 已经在剪映剪片且无API时，可用文本朗读，按账号和版本实际可用性操作。https://www.jianying.com/web/professional |
| OpenAI 原生 TTS | OpenAI Speech API | gpt-4o-mini-tts 可按提示控制讲述风格，支持中文和 MP3/WAV。内置声线偏英语优化，中文需试听；成片清楚标注 AI 生成声音。https://developers.openai.com/api/docs/guides/text-to-speech |
| 批量TTS与授权复刻 | MiniMax、ElevenLabs | 现有适配器支持标准TTS；两家均提供本人复刻路线，按同一试读稿比较。https://platform.minimax.io/docs/api-reference/speech-t2a-http  https://elevenlabs.io/docs/api-reference/text-to-speech/convert |
| 已有云平台账号 | Azure Speech | 支持普通话及语音合成接口；适合复用既有账号。当前需走官方门户或另行接入。https://learn.microsoft.com/azure/cognitive-services/speech-service/language-support?tabs=tts |

## 真人录音（仅在用户明确要求时）

1. 先交可读稿。按镜头分段编号，旁白、屏幕公式、停顿和读音分开。例如屏幕写 T=3V/g，旁白先解释符号，再读“三倍喷口速度除以重力加速度”。
2. 用手机或电脑麦克风在安静、有软装的房间试录15–25秒。固定麦距，偏离麦克风正前方一点以减轻喷麦。试听底噪、回声、爆音和术语。优先重录有问题的段落，再考虑降噪。
3. 按段录制；错句停一下从句首重来，留少量环境底声供剪辑。原始文件保留。交付优先单声道48 kHz WAV；手机原始M4A等可直接导入，再按需统一格式。
4. 剪掉失误，保留自然停顿和呼吸，适度均衡响度。按实际录音逐句对齐画面和字幕。旁白替换时重算受影响的段落与字幕时间。
5. 用户不想自录时，可由用户安排真人配音员。交付脚本、术语读音、试读段、情绪参考和使用范围，收到录音后走同样的剪辑与质检流程。

用户明确选择真人录音但暂缺声音时，交付录音稿、读音表和可替换音轨的预览。可以用实拍环境声或合法音效标记动作；需要旁白解释的段落继续保持待配音状态。纯画面与字幕适合用户明确选择的静音设计，按静音设计另写节奏。

## 声线不是一个模糊“语音包”
保存provider、model、voice_id、language、speed、style、术语词典、consent_scope、sample_hash与试听结论。TTS默认自然普通话、清晰但不播音腔；每个账号的声线ID必须实际列出/用户选定，不能猜造ID。最多试听两种，确认后全片保持一致。

试听文字：“你小时候有没有把水管朝天举？水明明没停，水柱却一轮一轮地落下来。先别急着背公式：我们只问，每一秒，有多少水加入这个水团？最后，再用动量守恒算出它的节拍。”另单独测“线密度、微积分、三分之一、λ、每秒一点五米”。

## 本人复刻流程
1. 用户明确选择复刻并提供自己的声音/合法授权；说明会发送至哪家服务，授权范围包括上传、创建声线及本次生成。泛泛提到“支持克隆”不是上传具体样本的授权。
2. 提供录音方式：安静房间、单人、固定麦距、无音乐、正常讲述；初次建议60–120秒。ElevenLabs官方建议至少1分钟；MiniMax按其当前上传格式/时长/大小要求检查，不套用另一家的限制。
3. 有真实录音工具才录制；没有则请用户通过平台录音/上传文件。使用网页官方创建流程或已授权API，不假装在聊天里开启麦克风。
4. 先检查样本质量、提供商的数据处理条件和所需账户权限，再上传并记录返回voice_id。样本不提交到技能、公开工程或示例包。不要假称已经删除；按用户指示和服务实际能力处理。
5. 合成短样本，检查本人相似度、自然度、术语；复刻不合格时用标准声线，不静默改用其他人的声音。

## 可执行TTS接入
`scripts/tts.py` 支持 OpenAI、MiniMax 和 ElevenLabs 标准TTS接口，读取环境变量，不实现隐式上传/自动创建克隆。克隆完成的voice_id同样可作为输入。没有外部SDK依赖。

```
python scripts/tts.py --provider openai --model gpt-4o-mini-tts --voice coral --text-file narration.txt --output sample.mp3
python scripts/tts.py --provider minimax --model speech-2.8-hd --voice ACTUAL_VOICE_ID --text-file narration.txt --output sample.mp3
python scripts/tts.py --provider elevenlabs --model eleven_multilingual_v2 --voice ACTUAL_VOICE_ID --text-file narration.txt --output sample.mp3
```
默认只检查配置和密钥是否存在，不生成、不计费、不打印文本或密钥。实际调用追加 `--execute`，且须已具备任务授权/预算；通过安全配置提供 `OPENAI_API_KEY`、`MINIMAX_API_KEY` 或 `ELEVENLABS_API_KEY`。MiniMax国际站使用api.minimax.io；大陆账号须根据官方账号文档选择匹配地区端点，适配器未覆盖时不得盲试。

脚本是接入适配，不是已开通服务。失败只重试明确可重试错误；超时可能已计费，先检查服务记录，不能无限重发。按内容哈希缓存每个成功片段，再合成长音轨。

## 音频验收
实际试听短样片，术语/数字/公式读法正确，呼吸和停顿自然，情绪适度。最终常用目标：综合响度约−16 LUFS，true peak≤−1 dBTP（交付目标，非平台强制标准）；按目标平台调整，背景音乐在人声处压低。不靠补一条静音轨通过有声门槛。字幕使用真实对齐，不等分时长；无时间戳时按真实音频逐句对齐。无法监听时标未验收并提供试听文件。
