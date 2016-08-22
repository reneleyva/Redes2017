#! /usr/bin/env python
# -*- coding: utf-8 -*-
from SimpleXMLRPCServer import SimpleXMLRPCServer
from SimpleXMLRPCServer import SimpleXMLRPCRequestHandler


class ApiServer():
    def __init__(self,server_port):
        self.server_port = server_port
        self.message = ''

    def get_port(self):
        return self.server_port
    
    def set_port(self,port):
        self.server_port = port


message = ''

def set_msg(msg):
    global message
    message = msg
def get_msg():
    return message
server = None
def init_local_server(apiserver):
    server = SimpleXMLRPCServer(('', apiserver.get_port()),allow_none=True)
    return server

