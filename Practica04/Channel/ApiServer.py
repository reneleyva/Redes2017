#! /usr/bin/env python
# -*- coding: utf-8 -*-
from SimpleXMLRPCServer import SimpleXMLRPCServer
from SimpleXMLRPCServer import SimpleXMLRPCRequestHandler
import sys
from threading import Thread
from Constants.AuxiliarFunctions import *
from Constants import Constants
from Constants.Constants import *
import pyaudio
from cStringIO import StringIO
from numpy.lib import format


class ApiServer():
    def __init__(self, server_port=None, ip = None):

        self.port = server_port if server_port else CHAT_PORT
        if(server_port):
            self.server = SimpleXMLRPCServer(('localhost',int(self.port)),allow_none= True)
        else:
            self.server = SimpleXMLRPCServer((str(ip), CHAT_PORT),allow_none=True)

        self.server.register_introspection_functions()
        self.server.register_multicall_functions()
        self.funtionWrapper = FunctionWrapper()
        self.server.register_instance(self.funtionWrapper)
        self.stream = None
        self.playVThread = None

class FunctionWrapper:
    """ **************************************************
    Constructor de la clase
    ************************************************** """
    def __init__(self):
        self.buffer = list()
        self.stream = None
        print "Se construye las funciones"
        self.frames = []

    def toArray(self,s):
        f = StringIO(s)
        arr = format.read_array(f)
        return arr

    def play_video(self,video):
        self.frames.append(self.toArray(video.data))

    def reproduce(self):
        while True:
            if len(self.frames) > 0:
                cv2.imshow('Servidor',fames.pop(0))
                if cv2.waitKey(1) & 0xFF == ord('q'):
                    break
        cv2.destroyAllWindows()

    """ **************************************************
    Procedimiento que ofrece nuestro servidor, este metodo sera llamado
    por el cliente con el que estamos hablando, debe de
    hacer lo necesario para mostrar el texto en nuestra pantalla.
    ************************************************** """
    def sendMessage_wrapper(self, message):
        Constants.CHAT_WINDOW.escribeExterno(message)
        #print "El:"+ message+"\n"

    def get_audio(self,audio):
        p = pyaudio.PyAudio()
        FORMAT = p.get_format_from_width(2)
        stream = p.open(format = FORMAT, channels = CHANNELS, rate = RATE, output= True, frames_per_buffer = CHUNK)
        data = audio.data
        stream.write(data)
        stream.close()
        p.terminate()

    """ **************************************************
    Procedimiento que ofrece nuestro servidor, este metodo sera llamado
    por el cliente con el que estamos hablando, debe de
    hacer lo necesario para regresar el texto
    ************************************************** """
    def echo(self):
        return self.msg




def main(args):
   myPort = int(args[0])
   server = MyApiServer(myPort).server
   api_server_thread = Thread(target=server.serve_forever)
   api_server_thread.start()

if __name__ == '__main__':
   main(sys.argv[1:])
