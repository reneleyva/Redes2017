#! /usr/bin/env python
# -*- coding: utf-8 -*-
import os
import sys
import pyaudio
from threading import Thread
from Constants import Constants
from PyQt4 import QtGui, QtCore
from PyQt4.QtGui import QPixmap

sys.path.append(os.path.join(os.path.dirname(__file__),'..'))

class RecordAudio(Thread):

    def __init__(self):
        self.thread = Thread.__init__(self)

    def run(self):
        self.p = pyaudio.PyAudio()
        self.stream = self.p.open(format=self.p.get_format_from_width(Constants.WIDTH),
                channels=Constants.CHANNELS,
                rate=Constants.RATE,
                input=True,
                output=True,
                frames_per_buffer=Constants.CHUNK)

        print("* recording")
        while True:
            data = self.stream.read(Constants.CHUNK)
            self.stream.write(data, Constants.CHUNK)

        print("* done")

    def stop(self):
        self.stream.stop_stream()
        self.stream.close()
        self.p.terminate()
        Constants.RECORD_AUDIO = None 

"""
class Mensaje(QtGui.QWidget):
    def __init__(self):
        super(Mensaje, self).__init__()
        self.initUI()

    def initUI(self):
        self.etiqueta = QtGui.QLabel(QtGui.QApplication.translate("self", 'LLamada por Voz...', None, QtGui.QApplication.UnicodeUTF8), self)
        self.boton = QtGui.QPushButton('Cancelar')
        #self.micro = QtGui.QLabel()
        #self.micro.setPixmap(QPixmap(Constants.VOICE_IMG))
        self.boton.clicked.connect(self.onClickTerminar)
        grid = QtGui.QGridLayout()

        #grid.addWidget(self.micro, 0, 0)
        grid.addWidget(self.etiqueta, 0, 1)
        grid.addWidget(self.boton, 1, 1)
        self.setLayout(grid)
        self.setGeometry(500, 300, 100, 100)
        self.setWindowTitle('Terminar Llamada')
        self.show()

    def onClickTerminar(self):
        print "CLICKED!!"
        Constants.RECORD_AUDIO.stop()
        self.close()

class MensajeThread(Thread):
    def __init__(self):
        self.thread = Thread.__init__(self)

    def run(self):
        self.mensaje = Mensaje()
        self.mensaje.show()
"""
