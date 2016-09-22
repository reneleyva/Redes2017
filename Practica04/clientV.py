#! /usr/bin/env python
# -*- coding: utf-8 -*-


#####################################################
# PURPOSE:                                          #
#                                                   #
# Vilchis Dominguez Miguel Alonso                   #
#       <mvilchis@ciencias.unam.mx>                 #
#                                                   #
# Notes:                                            #
#                                                   #
# Copyright   07-09-2015                            #
#                                                   #
# Distributed under terms of the MIT license.       #
#####################################################

"""
Cliente que graba y manda video
"""
import numpy as np
import cv2
import multiprocessing as mp
import time
import xmlrpclib
import numpy
from cStringIO import StringIO
import threading
CHUNK = 1024
CHANNELS = 1 
RATE = 44100
RECORD_SECONDS = 2 
cap = cv2.VideoCapture(0)
proxy = xmlrpclib.ServerProxy("http://localhost:9080/",allow_none = False)
from numpy.lib import format

def toString(data):
    f= StringIO()
    format.write_array(f,data)
    return f.getvalue()
    
def graba():
    while(True):
        ret, frame = cap.read()
        #Aqui en vez de mostar agarramos
        image = cv2.imread(toString(frame)) #Ahuevo
        cv2.imshow('Cliente',frame) ##graba cliente
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
        data = xmlrpclib.Binary(toString(frame))
        proxy.playVideo(data) 
    cap.release()
    cv2.destroyAllWindows()

#queue = mp.Queue()
#p = mp.Process(target=graba, args=(queue,))
p = threading.Thread(target=graba)
p.start()

