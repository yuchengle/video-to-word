#!/usr/bin/env python
# coding: utf-8

from moviepy.editor import VideoFileClip
from aip import AipSpeech


# # 视频转音频

video_file = 'https://v2.addnewer.com/media/2020/08/1596606940740.mp4'
audio_file = '/data/jupyter/yucl/videotoword/out.wav'
video = VideoFileClip(video_file)
video.audio.write_audiofile(audio_file,ffmpeg_params=['-ar','16000','-ac','1'])


# # 音频转文本

'''
百度语音识别：https://console.bce.baidu.com/ai/?_=1597039403602#/ai/speech/overview/index
'''
#从百度AI开放平台创建应用处获取
APP_ID = '***'
API_KEY = '***'
SECRET_KEY = '***'

client = AipSpeech(APP_ID, API_KEY, SECRET_KEY)

# 读取文件
def get_file_content(audio_file):
    with open(audio_file, 'rb') as fp:
        return fp.read()

# 识别本地文件
def get_text():
    result = client.asr(get_file_content(audio_file), 'wav', 16000, {'dev_pid': 1537,})
    #print(result)
    text = result['result'][0]
    return text

res = get_text()
print (res)

'''紫熨斗全新的文体验波色因欧莱雅集团专利成本协同，玻尿酸生锈，石伟有一段话拽文，抬头纹和法令纹，眼部的全脸细纹，青森淡季功能鸭子熨斗。'''
