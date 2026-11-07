# 配乐、音效和混音

参考 MoneyPrinterTurbo 的 [任务编排](https://github.com/harry0703/MoneyPrinterTurbo/blob/main/app/services/task.py) 和 [视频合成](https://github.com/harry0703/MoneyPrinterTurbo/blob/main/app/services/video.py)。借鉴按实际旁白时长生成字幕和合成、旁白和音乐分别调节、音乐循环/淡出，以及明确报告背景音乐混合失败。继续使用本项目的逐镜头时间轴与科学核验。

1. 锁定实际自动旁白音频、字幕及时间轴。音乐按章节标注情绪与强度，例如开场低频脉冲、推导时轻薄铺底、结尾淡出。默认选无歌词、有明确使用许可或原创生成的素材；记录作者、来源、许可和署名。缺素材时先找已有许可资产，或用本地合成器生成原创氛围音与短脉冲，先试听再用。需要新增付费才交接。允许按镜头或用户要求有意留白。
2. 用事件表把音效绑定到帧或秒。公式抵消可用轻微短击，粒子穿过剖面可用渐强扫描音，揭晓可用轻低频过渡。把合成音效与实录区分；不要用音效暗示不存在的碰撞或物理事件。把连续环境声预制成已对齐的音效段。
3. 执行 `python3 scripts/mix_audio.py path/to/mix.json path/to/mix.wav`。路径相对 JSON 所在目录。旁白为必填，音乐可循环，事件音效按时间放置，旁白触发音乐压低。输出 48 kHz 立体声 WAV，保留旁白、音乐和音效原始分轨。调整下列示例到实际时间轴，音量仅作起点：

```json
{
  "duration_s": 60,
  "voice": "voice.wav",
  "music": "ambient.wav",
  "music_db": -18,
  "sfx": [
    {"file": "scan.wav", "at_s": 6.8, "gain_db": -12},
    {"file": "tick.wav", "at_s": 29.5, "gain_db": -16}
  ]
}
```

4. 合入成片，例如 `ffmpeg -i picture.mp4 -i mix.wav -map 0:v:0 -map 1:a:0 -c:v copy -c:a aac -b:a 192k final.mp4`。先核对两路实际时长，修正时间轴并重混，避免裁掉旁白或补黑帧。用 `ffmpeg -hide_banner -i final.mp4 -vn -af ebur128=peak=true -f null -` 测量导出后的综合响度和真峰值。默认混音目标约 −16 LUFS、母带真峰值 −2 dBTP，按平台实际要求调整。听检人声在手机和耳机上是否清楚、事件音效是否对帧、音乐循环是否跳变、结尾有无硬切，发现遮盖先降音乐或音效。
5. 用输入哈希及混音 JSON 缓存母带。改配乐或音效只重混和封装；遇缺失/坏音频或混合失败时修复并重试，保留已通过的其他阶段。标记任何仍缺的声音层，不把带一条空音轨的文件算作有声成片。
