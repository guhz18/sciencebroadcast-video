#!/usr/bin/env python3
"""Mechanical delivery gate, not a content/voice/native-resolution quality judgment."""
import argparse,json,subprocess,sys
from fractions import Fraction

def inspect(probe,allow_silent=False):
    errors=[];vs=[s for s in probe.get('streams',[]) if s.get('codec_type')=='video'];audio=[s for s in probe.get('streams',[]) if s.get('codec_type')=='audio']
    if not vs:return ['No video stream']
    v=vs[0];dims=sorted([v.get('width',0),v.get('height',0)])
    if dims[0]<1080 or dims[1]<1920:errors.append('Below default 1080p delivery dimensions')
    try:fps=float(Fraction(v.get('avg_frame_rate','0/1')))
    except (ValueError,ZeroDivisionError):fps=0
    if fps<29.9:errors.append('Below default 30fps delivery rate')
    if not audio and not allow_silent:errors.append('Missing narration audio stream')
    if v.get('codec_name') not in ['h264','hevc','av1']:errors.append('Review delivery codec compatibility')
    return errors

def main():
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('video');p.add_argument('--allow-silent',action='store_true',help='Only when user explicitly requests silent output');a=p.parse_args()
    try:d=json.loads(subprocess.check_output(['ffprobe','-v','error','-show_streams','-show_format','-of','json',a.video]))
    except Exception as e:print(json.dumps({'pass':False,'error':type(e).__name__}));return 1
    errors=inspect(d,a.allow_silent)
    print(json.dumps({'pass':not errors,'errors':errors,'manual_checks_required':['native render dimensions','audible meaningful narration','pronunciation and synchronization','scientific accuracy','purposeful motion and pacing']},ensure_ascii=False,indent=2));return bool(errors)
if __name__=='__main__':sys.exit(main())
