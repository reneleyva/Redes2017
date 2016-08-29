#! /usr/bin/env python
# -*- coding: utf-8 -*-
from SimpleXMLRPCServer import SimpleXMLRPCServer
from SimpleXMLRPCServer import SimpleXMLRPCRequestHandler
import sys
from threading import Thread
from Constants.AuxiliarFunctions import *
from Constants import Constants
from Constants import Constants


class ApiServer():
    def __init__(self, server_port=None):

        self.port = server_port if server_port else CHAT_PORT
        self.server = SimpleXMLRPCServer(('localhost',int(self.port)),allow_none= True)
        self.server.register_introspection_functions()
        self.server.register_multicall_functions()
        self.funtionWrapper = FunctionWrapper()
        self.server.register_instance(self.funtionWrapper)


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
    def sendMessage_wrapper(self, message):
        self.msg = message
        Constants.CHAT_WINDOW.escribeExterno(message)
        #print "El:"+ message+"\n"

    def sendData_wrapper(self, data):
        print data
        #print type(data)
        #self.record.stream.write(str(data), 1024)
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
