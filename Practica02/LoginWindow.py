# -*- coding: utf-8 -*-

from PyQt4 import QtGui, QtCore
from PyQt4.QtGui import QWidget, QLabel, QMessageBox
from ChatWindow import ChatWindow
import os
import sys
    
#Clase para la ventana de LogIn
class LoginWindow(QtGui.QWidget):

    def __init__(self):
        super(LoginWindow, self).__init__()
        self.initUI()


    def initUI(self):
        #elementos
        self.port_label = QtGui.QLabel(QtGui.QApplication.translate("self", '¿Cuál es mi puerto? ', None, QtGui.QApplication.UnicodeUTF8), self)
        self.port_input = QtGui.QLineEdit()
        self.contact_label = QtGui.QLabel(QtGui.QApplication.translate("self", '¿Cuál es el puerto del contacto? ', None, QtGui.QApplication.UnicodeUTF8),self)
        self.contact_input = QtGui.QLineEdit()
        self.login_button = QtGui.QPushButton('Acceder')


        #propiedades
        self.login_button.setObjectName("acceder")
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
        """MORUBIO: las variable 'puerto' es el puerto local y 
        contacto el puerto destino primero checo si es un numero 
        valido de puerto sino despliega error."""
        
        try: 
            puerto = int(port_input.text())
            contacto = int(contact_input.text())
            #Puerto en rango
            if (puerto < 0 or contacto < 0 or puerto > 65535 or contacto > 65535):
                raise ValueError()

            #MORUBIO Aquí haz tu desmadre yo muestro el chat directamente. 
            self.close()
            self.chat = ChatWindow(str(puerto), str(contacto)) #Recibe los puertos para imprimirlos en mensajes.
            self.chat.show()

            #Para Joderte BORRALO OBVIAMNETE
            self.chat.escribeExterno("Estas por la verga Morua")
            self.chat.escribeExterno("Nadie te quiere")
            self.chat.escribeExterno("8::::::::::::::::::D~~~~")

        except ValueError:
            #Despliega un Mensaje de Error
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText(QtGui.QApplication.translate("self", "Número de puerto no válido", None, QtGui.QApplication.UnicodeUTF8))
            msg.setWindowTitle("Error")
            msg.setStandardButtons(QMessageBox.Ok)
            msg.exec_()
            self.contact_input.clear()
            self.port_input.clear()
            self.port_input.setFocus()
        # print ("Tu puerto: %s" % puerto)
        # print ("Destino: %s" % contacto)

       
# MAIN
def main():
    app = QtGui.QApplication(sys.argv)

    stylesheet = open('style.qss').read()
    app.setStyleSheet(stylesheet)
    mainWindow = LoginWindow()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()