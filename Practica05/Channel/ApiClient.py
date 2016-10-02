#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""**************************************************
Clase que genera un proxy para poder hacer uso de los 
procedimientos remotos que ofrece la api del contacto
 **************************************************"""
import xmlrpclib
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__),'..'))
import pyaudio
import numpy
import cv2
from cStringIO import StringIO
from ApiServer import *
import multiprocessing
import threading
from numpy.lib import format
from Constants.AuxiliarFunctions import *


from Constants.Constants import *
from Constants.AuxiliarFunctions import *

class ApiClient:
    def __init__(self, contact_port = None, ip = None):
      self.server = None
      if contact_port:
        self.server = xmlrpclib.Server('http://localhost' +':'+str(contact_port), allow_none = True)
      if ip:
        self.server = xmlrpclib.Server('http://' + str(ip) + ':' + str(CHAT_PORT),allow_none=True)

      self.msg = ''
      self.stack = None
      self.thread_audio_send = None
      self.thread_audio_listen = None
      self.thread_video_send = None
      self.thread_video_listen = None
      self.image = None 
      #self.cap = cv2.VideoCapture(0)


        
    def init_extern_server(ip):
        self.server = xmlrpclib.Server('http://' + str(ip) + ':' + str(CHAT_PORT),allow_none=True)

    def set_msg(self,msg):
        self.msg = msg

    def get_msg(self):
        return self.msg

    def init_call(self):
      self.stack = multiprocessing.Queue(100000)
      #hilo para mandar audio
      
      self.thread_audio_send = MyThread(target=self.send_audio, name= "audio_send_thread")
      self.thread_audio_send.start()
      #hilo para escuchar audio

      self.thread_audio_listen = MyThread(target=self.play_audio, name = "audio_listen_thread")
      self.thread_audio_listen.start()

    def init_video_call(self):
      self.stack = multiprocessing.Queue(100000)
      #hilo para escuchar audio
      #self.thread_audio_listen = MyThread(target=self.play_audio, name = "audio_listen_thread")
      #self.thread_audio_listen.start()

      #hilo para mandar audio
      #elf.thread_audio_send = MyThread(target=self.send_audio, name= "audio_send_thread")
      #self.thread_audio_send.start()

      #hilo para mandar video
      self.thread_video_send = MyThread(target=self.send_video, name = "send_video")

      #hilo para recibir video
      self.thread_video_listen = MyThread(target=self.server.reproduce(), name = "video_listen_thread")
      self.thread_video_listen.setDaemon(True)
      self.thread_video_listen.start()
      

      

    def toString(self,data):
      f = StringIO()
      format.write_array(f,data)
      return f.getvalue()

    def send_video(self):
      self.cap = cv2.VideoCapture(0)
      while True:
        if self.thread_video_send.isStop(): 
          return 1
        ret ,frame = self.cap.read()
        self.image = cv2.imread(toString(frame))
        cv2.imshow('Yo',frame)
        data = xmlrpclib.Binary(self.toString(frame))
        self.server.play_video(data)

      self.cap.release()
      cv2.destroyAllWindows()


    def send_audio(self):
      while True:
        if self.thread_audio_send.isStop():
          return 1
        d = self.stack.get()
        data = xmlrpclib.Binary(d)
        self.server.get_audio(data)
    
    def play_audio(self):
      p = pyaudio.PyAudio()
      FORMAT = p.get_format_from_width(WIDTH)
      stream = p.open(format=FORMAT,channels = CHANNELS,rate = RATE, input = True, frames_per_buffer = CHUNK)
      while True:
        if self.thread_audio_listen.isStop():
          return 1
        n = 50
        frame = []
        for i in range(0,n):
          frame.append(stream.read(CHUNK))

        binary_audio = numpy.fromstring(''.join(frame), dtype = numpy.uint8)
        if self.stack.full():
          self.stack.get_nowait()
        self.stack.put(binary_audio)


    def play_video(self):
      self.server.reproduce()
    def end_call(self):
      self.thread_audio_send.stopT()
      self.thread_audio_listen.stopT()

    def end_video_call(self):
      #self.thread_audio_send.stopT()
      self.thread_video_listen.stopT()
      #self.thread_audio_listen.stopT()
      self.thread_video_send.stopT()


def main(args):
   contact_port = int(args[0])
   api_client = ApiClient(contact_port = contact_port).server
   api_client.sendMessage_wrapper("Mensaje de cliente a Servidor")

if __name__ == '__main__':
   main(sys.argv[1:])

