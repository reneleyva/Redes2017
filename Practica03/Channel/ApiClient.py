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
from ApiServer import *
import multiprocessing
import threading
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
      self.thread_send = None
      self.thread_listen = None

        
    def init_extern_server(ip):
        self.server = xmlrpclib.Server('http://' + str(ip) + ':' + str(CHAT_PORT),allow_none=True)

    def set_msg(self,msg):
        self.msg = msg

    def get_msg(self):
        return self.msg

    def init_call(self):
      self.stack = multiprocessing.Queue(100000)
      #hilo para mandar audio
      
      self.thread_send = MyThread(target=self.send_audio, name= "send_thread")
      self.thread_send.start()
      #hilo para escuchar audio

      self.thread_listen = MyThread(target=self.play_audio, name = "listen_thread")
      self.thread_listen.start()


    def send_audio(self):
      while True:
        if self.thread_send.isStop():
          return 1
        d = self.stack.get()
        data = xmlrpclib.Binary(d)
        self.server.get_audio(data)
    
    def play_audio(self):
      p = pyaudio.PyAudio()
      FORMAT = p.get_format_from_width(WIDTH)
      stream = p.open(format=FORMAT,channels = CHANNELS,rate = RATE, input = True, frames_per_buffer = CHUNK)
      while True:
        if self.thread_send.isStop():
          return 1
        n = 50
        frame = []
        for i in range(0,n):
          frame.append(stream.read(CHUNK))

        binary_audio = numpy.fromstring(''.join(frame), dtype = numpy.uint8)
        if self.stack.full():
          self.stack.get_nowait()
        self.stack.put(binary_audio)
    
    def end_call(self):
      self.thread_send.stopT()
      self.thread_listen.stopT()


def main(args):
   contact_port = int(args[0])
   api_client = ApiClient(contact_port = contact_port).server
   api_client.sendMessage_wrapper("Mensaje de cliente a Servidor")

if __name__ == '__main__':
   main(sys.argv[1:])

