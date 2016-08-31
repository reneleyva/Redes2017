#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""**************************************************
Las instancias de esta clase contendran los metodos
necesarios para hacer uso de los metodos
del api de un contacto. Internamente Trabajara
con una proxy apuntando hacia los servicios del
servidor xmlrpc del contacto
**************************************************"""
import threading
import sys
import time
import socket
import os
sys.path.append(os.path.join(os.path.dirname(__file__),'..'))

from Constants import Constants
from Constants.AuxiliarFunctions import *

from SimpleXMLRPCServer import SimpleXMLRPCServer
from SimpleXMLRPCServer import SimpleXMLRPCRequestHandler

from ApiServer import *
from ApiClient import *


"""
    Quedatele viendo a estos Threads y ya queda todo
"""
class ServerThread(MyThread):
    def __init__(self,server):
        MyThread.__init__(self)
        self.server = server

    def run(self):
        self.server.register_introspection_functions()
        self.server.register_function(set_msg,'Chat.post')
        self.server.register_function(get_msg,'Chat.get')
        print "listening port... 8000"
        self.server.serve_forever()


"""**************************************************
    Constructor de la clase
    @param <str> contact_ip: Si no se trabaja de manera local
                representa la ip del contacto con el que se
                establecera la conexion
    @param <int> my_port: De trabajar de manera local puerto
                de la instancia del cliente
    @param <int> contact_port: De trabajar de manera local
                representa el puerto de la instancia del contacto
**************************************************"""
class Channel:
    def __init__(self, contact_ip=None, contact_port=None,my_port=None):
        self.local = True
        self.my_ip = None
        self.contact_ip = None
        self.my_port = None
        self.apiserver = None
        self.api_server_thread = None
        self.server = None
        self.client = None

        self.msg = ""#PARA LA UI

        if contact_ip:
            self.my_ip = get_ip_address()
            self.contact_ip = contact_ip
            self.contact_port = CHAT_PORT
            self.my_port = CHAT_PORT
            self.local = False

        else:
            self.contact_port = contact_port
            self.my_port = my_port

        if(self.local):
            self.apiserver = ApiServer(self.contact_port,None)
            self.client = ApiClient(self.my_port,None)
            self.server = self.apiserver.server

        else:
            self.apiserver = ApiServer(None,my_ip)
            self.client = ApiClient(None,contact_ip)
            self.server = self.apiserver.server

        self.api_server_thread = Thread(target=self.server.serve_forever)
        self.api_server_thread.start()

    def get_client(self):
        return self.client

    def get_server(self):
        return self.server
        """**************************************************
    Metodo que se encarga de mandar texto al contacto con
    el cual se estableció la conexion
    **************************************************"""
    def send_text(self, text):
        client_server = self.client.server
        self.msg = client_server.sendMessage_wrapper(str(text))

    """def send_audio_data(self, data):
        client_server = self.client.server
        client_server.sendData_wrapper(str(data))"""

    """
        Metodo que agarra el mensaje que tiene el servidor
    """
    def get_text(self):
        client_server = self.client.server
        self.client.set_msg(str(client_server.echo()))
