# -*- coding: utf-8 -*-

from PyQt4 import QtGui, QtCore
from PyQt4.QtGui import QWidget, QLabel, QMessageBox, QTextEdit, QScrollBar, QPixmap

import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__),'..'))

from Channel.ApiServer import *
from Channel.ApiClient import *
from Channel.Channel import *
from Channel.RecordAudio import *
from threading import Thread


#Clase para la ventana de Chat
class ChatWindow(QtGui.QWidget):

    def __init__(self, puertoLocal, puertoContacto, ipLocal, ipContacto, channel,send_image):
        super(ChatWindow, self).__init__()
        self.initUI(send_image)
        """MORUBIO COMo puedes ver siempre se sabe los puertos y las ip's
        para mostrarlos en los mensajes y que se vea chingón """
        self.puertoLocal = puertoLocal
        self.puertoContacto = puertoContacto
        self.ipLocal = ipLocal
        self.ipContacto = ipContacto
        self.channel = channel
        self.send_image = send_image

    def initUI(self, send_image):
        #elementos
        self.textArea = QtGui.QTextEdit(self)
        self.msg_input = QtGui.QLineEdit(self)
        self.send_button = QtGui.QPushButton(self)
        self.voice_button = QtGui.QPushButton(self)

        #propiedades
        self.textArea.setObjectName("area")
        self.msg_input.setObjectName("msg")
        self.send_button.setObjectName("send")
        self.voice_button.setObjectName("voice")

        self.textArea.setReadOnly(True)
        self.textArea.append("\n"*16)
        # self.scroll_grid = QtGui.QGridLayout(self.textArea)
        self.msg_input.setPlaceholderText("Envia mensaje")
        self.send_button.setFlat(True)
        #Le pone un icono al boton de nuevo usuario
        self.send_button.setIcon(QtGui.QIcon(str(send_image)))
        self.send_button.setIconSize(QtCore.QSize(32,32))
        self.send_button.clicked.connect(self.escribeLocal)
        self.msg_input.returnPressed.connect(self.send_button.click) #Cuando se presiona ENTER

        voice_image = os.path.join('./GUI/vol.png')
        self.voice_button.setIcon(QtGui.QIcon(voice_image))
        self.voice_button.setFlat(True)
        self.voice_button.setIconSize(QtCore.QSize(32,32))
        self.voice_button.clicked.connect(self.voice)

        #Layout
        grid = QtGui.QGridLayout()
        grid.addWidget(self.textArea, 0, 0, 5, 5)
        grid.addWidget(self.msg_input, 6, 0, 1, 5)
        grid.addWidget(self.voice_button, 6, 3)
        grid.addWidget(self.send_button, 6, 4)

        self.setLayout(grid)
        self.setGeometry(400, 100, 700, 500)
        self.setWindowTitle('Login')
        self.show()

    # Escribe el mensaje en el Area de texto de
    # lo que se escribe en la ventana
    def escribeLocal(self):
        text = self.msg_input.text()
        if not text: return
        text = text.toUtf8()
        scroll = self.textArea.verticalScrollBar()
        scroll.setValue(scroll.maximum())
        self.textArea.setAlignment(QtCore.Qt.AlignRight)
        self.textArea.append(QtGui.QApplication.translate("self", "<p style=\"background: white ;\"><b  style=\"background: #86B2B3 ;\">Puerto "+ self.ipLocal + "/" + self.puertoLocal+"(Tú): </b>"+'<br>'+str(text)+"</p><br>", None, QtGui.QApplication.UnicodeUTF8))
        self.msg_input.clear()
        self.textArea.setAlignment(QtCore.Qt.AlignRight)
        self.channel.send_text(text)

    # Para escribir en el Area de texto los mensajes que vienen.
    def escribeExterno(self, text):
        # text = self.channel.get_text()
        if not text: return
        self.textArea.setAlignment(QtCore.Qt.AlignLeft)
        self.textArea.append(QtGui.QApplication.translate("self", "<p style=\"background: white ;\"><b style=\"background: #FAA678;\">Puerto " + self.ipContacto + "/" + self.puertoContacto+": </b> "+'<br>'+text+"</p><br>", None, QtGui.QApplication.UnicodeUTF8))
        scroll = self.textArea.verticalScrollBar()
        scroll.setValue(scroll.maximum())
        self.textArea.setAlignment(QtCore.Qt.AlignLeft)
        # self.textArea.append("%s" % text)
        # scroll.setValue(scroll.maximum())
        self.msg_input.clear()


    #Cuando se presiona el boton para llamada de Voz.
    def voice(self):
        record = RecordAudio()
        self.msg = Mensaje(record)
        self.msg.show()
        record.start()
        #print "#"*100

"""
Clase para desplegar Mensaje de llamada, Es necesaria esta clase para que reciba
Un objecto RecordAudio y lo pueda detener cuando se presione "Terminar LLamada"
"""
class Mensaje(QtGui.QWidget):
    def __init__(self, record):
        super(Mensaje, self).__init__()
        self.initUI()
        self.record = record

    def initUI(self):
        self.etiqueta = QtGui.QLabel(QtGui.QApplication.translate("self", 'LLamada por Voz...', None, QtGui.QApplication.UnicodeUTF8), self)
        self.boton = QtGui.QPushButton('Cancelar')
        voice_image = os.path.join('./GUI/vol.png')
        self.micro = QtGui.QLabel()
        self.micro.setPixmap(QPixmap(voice_image))
        self.boton.clicked.connect(self.onClick)
        grid = QtGui.QGridLayout()

        grid.addWidget(self.micro, 0, 0)
        grid.addWidget(self.etiqueta, 0, 1)
        grid.addWidget(self.boton, 1, 1)
        self.setLayout(grid)
        self.setGeometry(500, 300, 100, 100)
        self.setWindowTitle('Terminar Llamada')
        self.show()

    def onClick(self):
        print "CLICKED!!"
        self.record.stop()
        self.close()
