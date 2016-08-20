# -*- coding: utf-8 -*-

from PyQt4 import QtGui, QtCore
from PyQt4.QtGui import QWidget, QLabel, QMessageBox

import os
import sys
    
#Clase para la ventana de LogIn
class LoginWindow(QtGui.QWidget):

    def __init__(self):
        super(LoginWindow, self).__init__()
        self.initUI()


    def initUI(self):
        #elementos
        self.port_label = QtGui.QLabel('Cual es mi puerto?: ', self)
        self.port_input = QtGui.QLineEdit()
        self.contact_label = QtGui.QLabel('Cual es el puerto de contacto?: ', self)
        self.contact_input = QtGui.QLineEdit()
        self.login_button = QtGui.QPushButton('Acceder')


        #propiedades
        self.port_input.setFixedWidth(200)
        self.contact_input.setFixedWidth(200)
        self.login_button.clicked.connect(lambda: self.access(self.port_input, self.contact_input))
        self.contact_input.returnPressed.connect(self.login_button.click) #Cuando se presiona ENTER
        
        #Layout
        grid = QtGui.QGridLayout()

        grid.addWidget(self.port_label, 0, 0)
        grid.addWidget(self.port_input, 0, 1)
        grid.addWidget(self.contact_label, 1, 0)
        grid.addWidget(self.contact_input, 1, 1)
        grid.addWidget(self.login_button, 3, 1)

        self.setLayout(grid)
        self.setGeometry(500, 200, 300, 100)
        self.setWindowTitle('Login')
        self.show()

    def access(self, port_input=None, contact_input=None):

        puerto = port_input.text()
        contacto = contact_input.text()
        print ("Tu puerto: %s" % puerto)
        print ("Destino: %s" % contacto)
        #Despliega un Mensaje de Error
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Critical)
        msg.setText("Wut??")
        msg.setWindowTitle("Error")
        msg.setStandardButtons(QMessageBox.Ok)
        msg.exec_()
        #self.otro.show()

# MAIN
def main():
    app = QtGui.QApplication(sys.argv)

    # stylesheet = open('style.qss').read()
    # app.setStyleSheet(stylesheet)
    mainWindow = LoginWindow()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()