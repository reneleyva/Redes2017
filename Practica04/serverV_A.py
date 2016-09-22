#! /usr/bin/env python


#####################################################
# PURPOSE:                                          #
#                                                   #
# Vilchis Dominguez Miguel Alonso                   #
#       <mvilchis@ciencias.unam.mx>                 #
#                                                   #
# Notes:                                            #
#                                                   #
# Copyright   31-08-2015                            #
#                                                   #
# Distributed under terms of the MIT license.       #
#####################################################

"""
Servidor, recibira audio lo guardara para 
despues reproducirlo
"""
from SimpleXMLRPCServer import SimpleXMLRPCServer
import pyaudio
import cv2
import numpy as np
import numpy 
import threading
CHUNK = 1024
CHANNELS = 1 
RATE = 44100
DELAY_SECONDS = 5 

frames = []
from cStringIO import StringIO
from numpy.lib import format
def toArray(s):
    f=StringIO(s)
    arr=format.read_array(f)
    return arr 


def playAudio(audio):
    p = pyaudio.PyAudio()
    FORMAT = p.get_format_from_width(2)
    stream = p.open(format=FORMAT,
                    channels=CHANNELS,
                    rate=RATE,
                    output=True,
                    frames_per_buffer=CHUNK)

    data = audio.data
    stream.write(data)
    stream.close()
    p.terminate()

def playVideo(video):
     frames.append(toArray(video.data))
def reproduce():
    while True:
        if len(frames) > 0:
            ##EN vez de mostrarlo pintarlo en la otra ventana. 
            cv2.imshow('Servidor',frames.pop(0))
        if cv2.waitKey(1) & 0xFF == ord('q'):
        	break
    cv2.destroyAllWindows()


server = SimpleXMLRPCServer(("localhost", 9080), allow_none = True)
playVThread = threading.Thread(target=reproduce)
playVThread.setDaemon(True)
playVThread.start()

print "escuchando por el puerto 8000..."
server.register_function(playAudio, 'playAudio') 
server.register_function(playVideo, 'playVideo') 
server.serve_forever()

