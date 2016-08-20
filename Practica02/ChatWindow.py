# -*- coding: utf-8 -*-

from PyQt4 import QtGui, QtCore
from PyQt4.QtGui import QWidget, QLabel, QMessageBox, QTextEdit

import os
import sys
    
#Clase para la ventana de LogIn
class ChatWindow(QtGui.QWidget):

    def __init__(self):
        super(ChatWindow, self).__init__()
        self.initUI()


    def initUI(self):
        #elementos
        self.textArea = QtGui.QTextEdit(self)
        self.msg_input = QtGui.QLineEdit(self)
        self.send_button = QtGui.QPushButton(self)


        #propiedades
        self.textArea.setReadOnly(True)
        self.textArea.append("\n"*16)
        # self.scroll_grid = QtGui.QGridLayout(self.textArea)
        self.msg_input.setPlaceholderText("Envia mensaje")
        self.send_button.setFlat(True)
        #Le pone un icono al boton de nuevo usuario
        self.send_button.setIcon(QtGui.QIcon("send.png"))
        self.send_button.setIconSize(QtCore.QSize(32,32))
        self.send_button.clicked.connect(self.escribe)
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

    # Escribe el mensaje en el Area de texto. 
    def escribe(self):
        text = self.msg_input.text()
        if not text: return 
        self.textArea.setAlignment(QtCore.Qt.AlignRight)
        self.textArea.append("<p style=\"background: #78A6FA; border-radius: 10px;\"></p>" % text)
        self.msg_input.clear()



# MAIN
def main():
    app = QtGui.QApplication(sys.argv)

    stylesheet = open('style.qss').read()
    app.setStyleSheet(stylesheet)
    mainWindow = ChatWindow()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()