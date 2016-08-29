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

from Constants.Constants import *
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
            self.apiserver = ApiServer(self.contact_port)
            self.client = ApiClient(self.my_port)
            self.server = self.apiserver.server
            self.api_server_thread = Thread(target=self.server.serve_forever)
            self.api_server_thread.start()
        else:
            self.apiserver = ApiServer()
            self.client = ApiClient()
            self.client.init_extern_server(str(contact_ip))
            self.server = self.apiserver.server
            self.api_server_thread = Thread(target=self.server.serve_forever)
            self.api_server_thread.start()




        """**************************************************
    Metodo que se encarga de mandar texto al contacto con
    el cual se estableció la conexion
    **************************************************"""
    def send_text(self, text):
        client_server = self.client.server
        self.msg = client_server.sendMessage_wrapper(str(text))
    """
        Metodo que agarra el mensaje que tiene el servidor
    """
    def get_text(self):
        client_server = self.client.server
        self.client.set_msg(str(client_server.echo()))

    # Tiene como único proposito pasarle la UI a 
    # ApiServer para que pueda imprimir cuando reciba un mensaje
    def setUI(self, chatUI):
        self.chatUI = chatUI
        self.apiserver.setUI(chatUI)
    







