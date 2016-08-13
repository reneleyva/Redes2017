# -*- coding: utf-8 -*-

from PyQt4 import QtGui, QtCore
from PyQt4.QtGui import QWidget, QLabel, QMessageBox
from Calculadora_UI import Calculadora_UI
import sys

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
        
        """
        MORUBIO: Aqui comprueba si las contraseñas 
        estan correctas e inicia la ventana de la calculadora, 
        acuerdate que las contraseñas estan cifradas en el archivo. 
        """
        if (usuario == "root" and password == "root"):
            self.close() #Cierra la ventana de Login 
            #inicia la ventana de la calculadora.
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