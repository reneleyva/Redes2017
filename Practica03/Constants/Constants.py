#! /usr/bin/env python
import os
from AuxiliarFunctions import *

CHANNEL = None
CHAT_WINDOW = None
MAIN_APP = None
SEND_IMG = os.path.join('./GUI/send.png')
VOICE_IMG = os.path.join('./GUI/vol.png')
MUTE_IMG = os.path.join('./GUI/mute.png')
STYLE = './GUI/style.qss'
RECORD_AUDIO = None
#PARA RecordAudio
CHUNK = 1024
WIDTH = 2
CHANNELS = 2
RATE = 84100
RECORD_SECONDS = 5


CHAT_PORT = 5000
