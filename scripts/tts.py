#!/usr/bin/env python3
"""Explicit, opt-in TTS; no sample upload or voice cloning. Python stdlib only."""
import argparse,json,os,sys,urllib.request,urllib.error
from pathlib import Path
from urllib.parse import quote

def request_spec(provider,model,voice,text,key):
    if provider == 'openai':
        return (
            'https://api.openai.com/v1/audio/speech',
            {'Authorization': 'Bearer ' + key, 'Content-Type': 'application/json'},
            {'model': model, 'input': text, 'voice': voice, 'response_format': 'mp3'},
        )
    if provider=='minimax':
        return ('https://api.minimax.io/v1/t2a_v2',{'Authorization':'Bearer '+key,'Content-Type':'application/json'},
                {'model':model,'text':text,'stream':False,'output_format':'hex','voice_setting':{'voice_id':voice,'speed':1,'vol':1,'pitch':0},'audio_setting':{'sample_rate':32000,'bitrate':128000,'format':'mp3','channel':1}})
    return ('https://api.elevenlabs.io/v1/text-to-speech/'+quote(voice,safe='')+'?output_format=mp3_44100_128',{'xi-api-key':key,'Content-Type':'application/json'}, {'text':text,'model_id':model})

def decode_audio(provider,data):
    if provider=='minimax':
        obj=json.loads(data)
        if obj.get('base_resp',{}).get('status_code')!=0:raise ValueError('Provider rejected request; inspect account dashboard')
        data=bytes.fromhex(obj['data']['audio'])
    if not data or (not data.startswith(b'ID3') and not (data[0]==255 and len(data)>1 and data[1]&224==224)):
        raise ValueError('Response is not recognizable MP3 audio')
    return data

def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--provider',choices=['openai','minimax','elevenlabs'],required=True)
    for n in ['model','voice','text-file','output']:p.add_argument('--'+n,required=True)
    p.add_argument('--execute',action='store_true',help='Make a billable request only after task authorization')
    a=p.parse_args();text=Path(a.text_file).read_text().strip();out=Path(a.output)
    if not text:p.error('Empty narration')
    if len(text)>4000:p.error('Split narration into segments of at most 4000 characters')
    if out.suffix.lower()!='.mp3':p.error('Output must end with .mp3')
    if out.exists():p.error('Output already exists; reuse cached audio or select a new path')
    key_name = {'openai': 'OPENAI_API_KEY', 'minimax': 'MINIMAX_API_KEY', 'elevenlabs': 'ELEVENLABS_API_KEY'}[a.provider]
    key = os.environ.get(key_name, '')
    if not a.execute:
        print(json.dumps({'mode':'dry-run','provider':a.provider,'model':a.model,'characters':len(text),'credential_present':bool(key),'network_request':False}));return
    if not key:p.error('Configure provider credential securely; do not paste keys into chat')
    url,headers,body=request_spec(a.provider,a.model,a.voice,text,key)
    req=urllib.request.Request(url,data=json.dumps(body).encode(),headers=headers,method='POST')
    try:
        with urllib.request.urlopen(req,timeout=90) as r:data=r.read()
        data=decode_audio(a.provider,data)
        out.parent.mkdir(parents=True,exist_ok=True)
        with out.open('xb') as f:f.write(data)
        print(json.dumps({'status':'generated','bytes':len(data),'output':str(out)}))
    except urllib.error.HTTPError as e:
        print('TTS failed: HTTP '+str(e.code)+'. No automatic retry.',file=sys.stderr);sys.exit(1)
    except Exception as e:
        print('TTS failed: '+type(e).__name__+'. Check account status before retrying.',file=sys.stderr);sys.exit(1)
if __name__=='__main__':main()
