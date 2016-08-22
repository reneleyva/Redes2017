#! /usr/bin/env python
# -*- coding: utf-8 -*-
import xmlrpclib as rpc
from ApiServer import *


class ApiClient:
    
    def __init__(self,my_port):
    	self.name = None
    	self.server = None
    	self.msg = None
    	self.my_port = my_port

    def set_msg(self,msg):
    	self.msg = msg
    def get_msg(self):
    	return self.msg

    def set_my_port(self,port):
    	self.my_port = port

    def get_my_port(self):
    	return self.my_port


    def set_name(self,name):
    	self.name = name
    def get_name(self):
    	return self.name
    
    def connect_server(self,url):
    	self.server = rpc.ServerProxy(url,allow_none=True)
    	#self.server.Session.start(client)
    
    def get_server(self):
    	return self.server

if __name__ == '__main__':
	cliente.connect_server('http://localhost:8000')
	server = cliente.get_server()
