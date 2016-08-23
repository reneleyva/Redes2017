#! /usr/bin/env python
# -*- coding: utf-8 -*-
from SimpleXMLRPCServer import SimpleXMLRPCServer
from SimpleXMLRPCServer import SimpleXMLRPCRequestHandler
import sys
from threading import Thread
from Constants.AuxiliarFunctions import *
from Constants.Constants import *


class ApiServer():
    def __init__(self,server_port, chatWindow):
        
        self.port = server_port if server_port else CHAT_PORT
        self.server = SimpleXMLRPCServer(('localhost',int(self.port)),allow_none= True)
        self.server.register_introspection_functions()
        self.server.register_multicall_functions()
        self.funtionWrapper = FunctionWrapper()
        self.server.register_instance(self.funtionWrapper)
        self.msg = ''
        self.chatWindow = chatWindow



class FunctionWrapper:
    """ **************************************************
    Constructor de la clase
    ************************************************** """
    def __init__(self):
        print "Se construye las funciones"
   
    """ **************************************************
    Procedimiento que ofrece nuestro servidor, este metodo sera llamado
    por el cliente con el que estamos hablando, debe de
    hacer lo necesario para mostrar el texto en nuestra pantalla.
    ************************************************** """
    def sendMessage_wrapper(self, chat, message):
        self.msg = message
        chatWindow.escribeExterno(message)
        print "El:"+ message+"\n"
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


