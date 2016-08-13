# -*- coding: utf-8 -*-

from PyQt4 import QtGui, QtCore
from PyQt4.QtGui import QWidget, QLabel, QMessageBox

import sys

#Clase para la ventana de LogIn
class NewUserWindow(QtGui.QWidget):

    def __init__(self ):
        super(NewUserWindow, self).__init__()
        self.initUI()


    def initUI(self):
        #elementos
        user_label = QtGui.QLabel('Usuario: ', self)
        user_input = QtGui.QLineEdit()
        password_label = QtGui.QLabel('Contraseña: ', self)
        password_input = QtGui.QLineEdit()
        login_button = QtGui.QPushButton('Crear')

        #propiedades
        password_input.setEchoMode(QtGui.QLineEdit.Password)
        user_input.setFixedWidth(200)
        password_input.setFixedWidth(200)
        login_button.clicked.connect(lambda: self.creaUsuario(user_input, password_input))
        
        
        #Layout
        grid = QtGui.QGridLayout()

        grid.addWidget(user_label, 0, 0)
        grid.addWidget(user_input, 0, 1)
        grid.addWidget(password_label, 1, 0)
        grid.addWidget(password_input, 1, 1)
        grid.addWidget(login_button, 3, 1)

        self.setLayout(grid)
        self.setGeometry(500, 200, 300, 100)
        self.setWindowTitle('Crear Nuevo Usuario')
        self.show()

    def creaUsuario(self, user_input=None, password_input=None):

        usuario = user_input.text()
        password = password_input.text()
        
        """
        MORUBIO: Aquí debes crear al usuario y guardarlo 
        en un archivo con el cifrado raro este if checa 
        si el usuario o password es vacio son vacios, si lo son manda un dialogo
        sino los imprime
        """
        if (not usuario or not password):
            #Despliega un Mensaje de Error
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText("Contraseña o Usuario incorrectos")
            msg.setWindowTitle("Error")
            msg.setStandardButtons(QMessageBox.Ok)
        else:
            print usuario
            print password
        
        
        self.close()


# MAIN
def main():
    app = QtGui.QApplication(sys.argv)
    mainWindow = NewUserWindow()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()