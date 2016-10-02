#! /usr/bin/env python
# -*- coding: utf-8 -*-


#####################################################
# PURPOSE:Funciones auxiliares                      #
#                                                   #
# Vilchis Dominguez Miguel Alonso                   #
#       <mvilchis@ciencias.unam.mx>                 #
#                                                   #
# Notes:                                            #
#                                                   #
# Copyright   16-08-2015                            #
#                                                   #
# Distributed under terms of the MIT license.       #
#####################################################
import socket

"""**************************************************
 Metodo auxiliar que hace uso de internet para
 conocer la ip con la que contamos como usuarios
**************************************************"""

def get_ip_address():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    return "%s"% (s.getsockname()[0])

"""**************************************************
 Clase auxiliar que implementa el metodo
stop, para que el hilo se detenga externamente
**************************************************"""
import threading


class MyThread(threading.Thread):

    def __init__(self,target,name):
        super(MyThread,self).__init__(target=target,name=name)
        self.__stop = threading.Event()

    def stopT(self):
        self.__stop.set()

    def isStop(self):
        return self.__stop.isSet()