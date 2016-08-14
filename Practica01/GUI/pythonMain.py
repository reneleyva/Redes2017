# -*- coding: utf-8 -*-

from PyQt4 import QtGui, QtCore
from PyQt4.QtGui import QWidget, QLabel, QMessageBox
from Calculadora_UI import Calculadora_UI

import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__),'..'))

cur_path = os.path.dirname(__file__)
new_path = os.path.relpath('../Code/input.txt',cur_path)

"""
file = open(new_path,'r+w')
file.write("root:114~111~111~121\n")
file.close()
"""
def decode(asciilist):
    c = asciilist[len(asciilist)-1]
    num = int(c)
    num = num-5
    password = ""
    cola = chr(num)
    for i in range(len(asciilist)-1):
        n = int(asciilist[i])
        password += chr(n)
       
    password += cola
        
    return password


    

def load_users():
    file = open(new_path,'r+w')
    lines = file.read().split('\n')
    users = []
    pswd = []
    for line in lines:
        aux = line.split(':')
        asciilist = aux[1].split('~')
        psd = decode(asciilist)
        users.append(aux[0])
        pswd.append(psd)
    return zip(users,pswd)

#Clase para la ventana de LogIn
class LoginWindow(QtGui.QWidget):

    def __init__(self):
        super(LoginWindow, self).__init__()
        self.initUI()


    def initUI(self):
        #elementos
        user_label = QtGui.QLabel('Usuario: ', self)
        user_input = QtGui.QLineEdit()
        password_label = QtGui.QLabel('Contraseña: ', self)
        password_input = QtGui.QLineEdit()
        login_button = QtGui.QPushButton('Acceder')

        #propiedades
        password_input.setEchoMode(QtGui.QLineEdit.Password)
        user_input.setFixedWidth(200)
        password_input.setFixedWidth(200)
        login_button.clicked.connect(lambda: self.access(user_input, password_input))
        
        
        #Layout
        grid = QtGui.QGridLayout()

        grid.addWidget(user_label, 0, 0)
        grid.addWidget(user_input, 0, 1)
        grid.addWidget(password_label, 1, 0)
        grid.addWidget(password_input, 1, 1)
        grid.addWidget(login_button, 3, 1)

        self.setLayout(grid)
        self.setGeometry(500, 200, 300, 100)
        self.setWindowTitle('Login')
        self.show()

    def access(self, user_input=None, password_input=None):

        usuario = user_input.text()
        password = password_input.text()
        lst = load_users()
        par = (usuario,password)
        esta_registrado = False
        i = 0
        while not esta_registrado and i < len(lst):
            if(par == lst[i]): esta_registrado = True
            i+=1

        if(esta_registrado):
               self.close()
               self.calc = Calculadora_UI()
               self.calc.show()
        else: 
            #Despliega un Mensaje de Error
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText("Contraseña o Usuario incorrectos")
            msg.setWindowTitle("Error")
            msg.setStandardButtons(QMessageBox.Ok)
            msg.exec_()
                #self.otro.show()


# MAIN
def main():
    app = QtGui.QApplication(sys.argv)
    QtGui.QFontDatabase.addApplicationFont('/home/rene/Documents/Code/Calculadora/digital.ttf')

    stylesheet = open('style.qss').read()
    app.setStyleSheet(stylesheet)
    mainWindow = LoginWindow()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()