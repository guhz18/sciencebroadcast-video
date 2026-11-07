#!/usr/bin/env python3
"""Build a narration-led WAV master from a local JSON cue sheet."""

import argparse
import json
import math
from pathlib import Path
import subprocess
import tempfile


FORMAT = "aformat=sample_rates=48000:channel_layouts=stereo"


def number(value, name, minimum, maximum):
    if (
        type(value) not in (int, float)
        or not math.isfinite(value)
        or not minimum <= value <= maximum
    ):
        raise ValueError(f"{name} must be between {minimum} and {maximum}")
    return value


def mix(sheet, output):
    spec = json.loads(sheet.read_text(encoding="utf-8"))
    duration = number(spec["duration_s"], "duration_s", 0.1, 86400)
    if output.suffix.lower() != ".wav":
        raise ValueError("output must end in .wav")
    command = ["ffmpeg", "-hide_banner", "-nostdin", "-nostats", "-y"]
    inputs = []

    def add_input(filename, loop=False):
        path = (sheet.parent / filename).resolve()
        if not path.is_file() or path == output.resolve():
            raise ValueError(f"Invalid audio input: {path}")
        if loop:
            command.extend(["-stream_loop", "-1"])
        command.extend(["-i", str(path)])
        inputs.append(path)
        return len(inputs) - 1

    add_input(spec["voice"])
    voice_duration = subprocess.check_output(
        ["ffprobe", "-v", "error", "-select_streams", "a:0", "-show_entries",
         "stream=duration:format=duration", "-of", "json", str(inputs[0])],
        text=True,
    )
    metadata = json.loads(voice_duration)
    streams = metadata.get("streams", [])
    if not streams:
        raise ValueError("Voice input has no audio stream")
    length = streams[0].get("duration") or metadata.get("format", {}).get("duration")
    if length in (None, "N/A"):
        length = metadata.get("format", {}).get("duration")
    if length in (None, "N/A") or float(length) > duration + 0.05:
        raise ValueError("Set a measurable narration duration that fits the picture")

    voice_filter = f"[0:a:0]{FORMAT},asetpts=PTS-STARTPTS,apad,atrim=duration={duration}"
    filters = []
    tracks = ["[voice]"]
    if spec.get("music"):
        index = add_input(spec["music"], loop=True)
        gain = number(spec.get("music_db", -18), "music_db", -60, 0)
        fade = min(1.5, duration / 3)
        filters.extend([
            f"{voice_filter},asplit=2[voice][key]",
            f"[{index}:a:0]{FORMAT},asetpts=PTS-STARTPTS,atrim=duration={duration},"
            f"volume={gain}dB,afade=d={fade},afade=t=out:st={duration-fade}:d={fade}[bed]",
            "[bed][key]sidechaincompress=threshold=0.025:ratio=5:attack=20:release=300[music]",
        ])
        tracks.append("[music]")
    else:
        filters.append(f"{voice_filter}[voice]")

    for cue in spec.get("sfx", []):
        start = number(cue["at_s"], "at_s", 0, duration)
        if start >= duration:
            raise ValueError("An effect starts at or after the end of the picture")
        gain = number(cue.get("gain_db", -12), "gain_db", -60, 0)
        index = add_input(cue["file"])
        track = f"[effect{index}]"
        filters.append(
            f"[{index}:a:0]{FORMAT},asetpts=PTS-STARTPTS,volume={gain}dB,"
            f"adelay={round(start * 1000)}:all=1{track}"
        )
        tracks.append(track)

    filters.append(
        "".join(tracks)
        + f"amix=inputs={len(tracks)}:duration=first:normalize=0,"
        + "loudnorm=I=-16:TP=-2:LRA=11:print_format=summary[master]"
    )
    with tempfile.TemporaryDirectory(dir=output.parent) as temp:
        master = Path(temp) / "master.wav"
        subprocess.run(
            command + ["-filter_complex", ";".join(filters), "-map", "[master]",
                       "-ar", "48000", "-c:a", "pcm_s24le", "-t", str(duration), str(master)],
            check=True,
        )
        master.replace(output)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("cue_sheet", type=Path)
    parser.add_argument("output", type=Path)
    args = parser.parse_args()
    try:
        mix(args.cue_sheet, args.output)
    except (KeyError, TypeError, ValueError, OSError, subprocess.CalledProcessError) as exc:
        parser.exit(1, f"Mix failed: {exc}\n")
