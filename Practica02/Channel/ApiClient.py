#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""**************************************************
Clase que genera un proxy para poder hacer uso de los 
procedimientos remotos que ofrece la api del contacto
 **************************************************"""
import xmlrpclib
import sys
import os
from ApiServer import *
sys.path.append(os.path.join(os.path.dirname(__file__),'..'))

from Constants.Constants import *
from Constants.AuxiliarFunctions import *

class ApiClient:
    def __init__(self, contact_port = None):
        if contact_port:
            self.server = xmlrpclib.Server('http://localhost' +':'+str(contact_port), allow_none = True)
        self.msg = ''
    def init_extern_server(ip):
        self.server = xmlrpclib.Server(ip,str(CHAT_PORT))

    def set_msg(self,msg):
        self.msg = msg

    def get_msg(self):
        return self.msg

def main(args):
   contact_port = int(args[0])
   api_client = ApiClient(contact_port = contact_port).server
   api_client.sendMessage_wrapper("Mensaje de cliente a Servidor")

if __name__ == '__main__':
   main(sys.argv[1:])

