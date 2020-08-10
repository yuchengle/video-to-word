#!/usr/bin/env python
# coding: utf-8

# In[2]:


# -*- coding: utf-8 -*-
from moviepy.editor import VideoFileClip
from aip import AipSpeech


# # 视频转音频

# In[3]:


video_file = 'https://v2.addnewer.com/media/2020/08/1596606940740.mp4'
audio_file = '/data/jupyterCode/yucl/videotoword/out.wav'
video = VideoFileClip(video_file)
video.audio.write_audiofile(audio_file,ffmpeg_params=['-ar','16000','-ac','1'])


# # 音频转文件

# In[4]:


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

 


# In[5]:


res = get_text()
res


# In[ ]:




