# -*- coding: utf-8 -*-

from PyQt4 import QtGui, QtCore
from PyQt4.QtGui import QWidget, QLabel, QMessageBox, QTextEdit, QScrollBar

import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__),'..'))

from Channel.ApiServer import *
from Channel.ApiClient import *
from Channel.Channel import *




#Clase para la ventana de Chat
class ChatWindow(QtGui.QWidget):

    def __init__(self, puertoLocal, puertoContacto, ipLocal, ipContacto, channel):
        super(ChatWindow, self).__init__()
        self.initUI()
        """MORUBIO COMo puedes ver siempre se sabe los puertos y las ip's 
        para mostrarlos en los mensajes y que se vea chingón """
        self.puertoLocal = puertoLocal
        self.puertoContacto = puertoContacto
        self.ipLocal = ipLocal
        self.ipContacto = ipContacto
        self.channel = channel

    def initUI(self):
        #elementos
        self.textArea = QtGui.QTextEdit(self)
        self.msg_input = QtGui.QLineEdit(self)
        self.send_button = QtGui.QPushButton(self)


        #propiedades
        self.textArea.setObjectName("area")
        self.msg_input.setObjectName("msg")
        self.send_button.setObjectName("send")

        self.textArea.setReadOnly(True)
        self.textArea.append("\n"*16)
        # self.scroll_grid = QtGui.QGridLayout(self.textArea)
        self.msg_input.setPlaceholderText("Envia mensaje")
        self.send_button.setFlat(True)
        #Le pone un icono al boton de nuevo usuario
        self.send_button.setIcon(QtGui.QIcon("send.png"))
        self.send_button.setIconSize(QtCore.QSize(32,32))
        self.send_button.clicked.connect(self.escribeLocal)
        self.msg_input.returnPressed.connect(self.send_button.click) #Cuando se presiona ENTER
        
        #Layout
        grid = QtGui.QGridLayout()
        grid.addWidget(self.textArea, 0, 0, 5, 5)
        grid.addWidget(self.msg_input, 6, 0, 1, 5)
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
        self.textArea.setAlignment(QtCore.Qt.AlignRight)
        scroll = self.textArea.verticalScrollBar()
        scroll.setValue(scroll.maximum())
        self.textArea.append(QtGui.QApplication.translate("self", "<b  style=\"background: #86B2B3 ;\">Puerto "+ self.ipLocal + "/" + self.puertoLocal+"(Tú): </b>", None, QtGui.QApplication.UnicodeUTF8))
        self.textArea.append("%s\n" % text)
        self.msg_input.clear()

        self.channel.send_text(str(text))
        #str(self.channel.get_text())

    # Para escribir en el Area de texto los mensajes que vienen. 
    def escribeExterno(self, text):
        text = str(self.channel.get_text())
        if not text: return 
        self.textArea.setAlignment(QtCore.Qt.AlignLeft)
        scroll = self.textArea.verticalScrollBar()
        scroll.setValue(scroll.maximum())
        self.textArea.append("<b style=\"background: #FAA678;\">Puerto " + self.ipContacto + "/" + self.puertoContacto+": </b>")
        self.textArea.append("%s\n" % text)
        self.msg_input.clear()

        


# MAIN
# def main():
#     app = QtGui.QApplication(sys.argv)
#     stylesheet = open('style.qss').read()
#     app.setStyleSheet(stylesheet)
#     mainWindow = ChatWindow()
#     #Para joderte
    # mainWindow.escribeExterno("Estas por la verga Morua")
    # mainWindow.escribeExterno("Nadie te quiere")
    # mainWindow.escribeExterno("8::::::::::::::::::D~~~~")
    # mainWindow.msg_input.setText("8::::::::::::::::::D~~~~")
#     mainWindow.escribeLocal()
#     sys.exit(app.exec_())


# if __name__ == '__main__':
#     main()
