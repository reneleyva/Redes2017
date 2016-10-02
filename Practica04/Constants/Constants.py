#! /usr/bin/env python
import os
from AuxiliarFunctions import *

CHANNEL = None
CHAT_WINDOW = None
MAIN_APP = None
SEND_IMG = os.path.join('./GUI/send.png')
VOICE_IMG = os.path.join('./GUI/vol.png')
CALL_IMG = os.path.join('./GUI/call.png')
MUTE_IMG = os.path.join('./GUI/mute.png')
STYLE = './GUI/style.qss'
END_CALL = False
#PARA RecordAudio
CHUNK = 1024
WIDTH = 2
CHANNELS = 2
RATE = 44100

RECORD_SECONDS = 2

DELAY_LEN = RECORD_SECONDS * RATE/(1000*CHUNK)

CHAT_PORT = 5000
