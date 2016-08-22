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


class ClientThread(MyThread):
    def __init__(self,client,server):
        MyThread.__init__(self)
        self.client = client
        self.server = server
        self.msg = ''


    def run(self):
        while not self.is_stop():
            try:   
                msg = self.server.Chat.get()
                self.client_thread.set_msg(msg)
            except socket.error, e:
                print(BBB)
            time.sleep(1)


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
    def __init__(self, contact_ip, my_port,contact_port):
        self.local = is_local
        if(is_local):
            self.my_port = 5000
            self.contact_ip = IP
        else:
            self.my_port = 5000
            self.contact_ip = contact_ip
        self.contact_port = contact_port
        self.client = Client()
        self.server = None
        self.thread_client = MyThread(self.client,self.server)

    def get_client_port(self):
        return self.contact_port

    def get_client_ip(self):
        return self.contact_ip

    def get_my_port(self):
        return self.get_my_port

    def get_thread_client(setlf):
        return self.thread_client
        

        """**************************************************
    Metodo que se encarga de mandar texto al contacto con
    el cual se estableció la conexion
    **************************************************"""
    def send_text(self, text):
        self.client.set_msg(txt)

