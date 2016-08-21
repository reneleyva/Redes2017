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
        #Despliega un Mensaje 
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Question)
        msg.setText(QtGui.QApplication.translate("self", "Elije una opción de comunicación", None, QtGui.QApplication.UnicodeUTF8))
        msg.setWindowTitle("Opciones")
        msg.addButton(QtGui.QPushButton('Local'), QtGui.QMessageBox.YesRole)
        msg.addButton(QtGui.QPushButton('Externa'), QtGui.QMessageBox.NoRole)
        res = msg.exec_()

        #Decide cual se presiono y que dialogo mostrar
        if res == 0:
            self.init_dialog_local()
            msg.close()
        else:
            self.init_dialog_externo()
            msg.close()

    def init_dialog_local(self):
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
        self.login_button.clicked.connect(lambda: self.access_port(self.port_input, self.contact_input))
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

    def init_dialog_externo(self):

        #elementos
        self.port_label = QtGui.QLabel(QtGui.QApplication.translate("self", '¿Cuál es mi IP?', None, QtGui.QApplication.UnicodeUTF8), self)
        self.port_input = QtGui.QLineEdit()
        self.contact_label = QtGui.QLabel(QtGui.QApplication.translate("self", '¿Cuál es la IP del contacto? ', None, QtGui.QApplication.UnicodeUTF8),self)
        self.contact_input = QtGui.QLineEdit()
        self.login_button = QtGui.QPushButton('Acceder')


        #propiedades
        self.login_button.setObjectName("acceder")
        self.port_input.setFixedWidth(200)
        self.contact_input.setFixedWidth(200)
        self.login_button.clicked.connect(lambda: self.access_ip(self.port_input, self.contact_input))
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

    #despliega un mensaje de error con un mensaje
    def despliegaDialogoError(self, mensaje):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Critical)
        msg.setText(QtGui.QApplication.translate("self", mensaje, None, QtGui.QApplication.UnicodeUTF8))
        msg.setWindowTitle("Error")
        msg.setStandardButtons(QMessageBox.Ok)
        msg.exec_()
        self.contact_input.clear()
        self.port_input.clear()
        self.port_input.setFocus()

    def access_ip(self, ip_input, contact_ip):

        #Si son vacios 
        if not ip_input or not contact_ip:
            self.despliegaDialogoError("Número de IP no válido")
            return 

        ip1 = ip_input.text().split('.')
        ip2 = contact_ip.text().split('.')

        #Le hace pruebas a las IP's
        if (len(ip1) != 4 or len(ip2) != 4):
            self.despliegaDialogoError("Numero de IP no válido")
            return 

        #Checa si son numeros y si están en rango
        for n in ip1:
            try:
                i = int(n)
                if i > 255 or i < 0:
                    raise ValueError() 
            except ValueError:
                self.despliegaDialogoError("Numero de IP no válido")
                return 

        for n in ip2:
            try:
                i = int(n)
                if i > 255 or i < 0:
                    raise ValueError() 
            except ValueError:
                self.despliegaDialogoError("Numero de IP no válido")
                return 
        
        """MORUBIO aquí las ip's pasaron las prubeas y son validas aquí haz tus 
        desmadre yo mando a llamar a ChatWindow directamente"""
        self.close()
        #MORUBIO ChatWindow recibe también las Ip's como argumento, ver el constructor de ChatWindow 
        #No sé que puertos esten por defecto, si quieres cambialos. 
        self.chat = ChatWindow("80", "80", ip_input.text(), contact_ip.text())
        self.chat.show()


    def access_port(self, port_input=None, contact_input=None):
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
            #MORUBIO ChatWindow recibe también las Ip's como argumento, ver el constructor de ChatWindow 
            self.chat = ChatWindow(str(puerto), str(contacto), "127.0.0.1", "127.0.0.1")
            self.chat.show()

            #Para Joderte BORRALO OBVIAMNETE
            self.chat.escribeExterno("Estas por la verga Morua")
            self.chat.escribeExterno("Nadie te quiere")
            self.chat.escribeExterno("8::::::::::::::::::D~~~~")

        except ValueError:
            #Despliega un Mensaje de Error
            self.despliegaDialogoError("Número de puerto no válido")
            
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