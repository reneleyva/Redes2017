# -*- coding: utf-8 -*-

from PyQt4 import QtGui, QtCore
from PyQt4.QtGui import QWidget, QLabel, QMessageBox
from NewUserWindow import NewUserWindow

import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__),'..'))
from Code.Calculator import Calculator
from Code.ScientificCalculator import ScientificCalculator
from Constants.Constants import *


class Calculadora_UI(QtGui.QWidget):
	def __init__(self ):
		super(Calculadora_UI, self).__init__()
		self._ScreenText_ = ""
		self.initUI()

	def initUI(self):
		self.pantalla = QtGui.QLineEdit("")
		self.pantalla.setObjectName(screen);
		nuevo_boton = QtGui.QPushButton('')
		botones = ['', CLEAR, MOD, EXP, SEVEN, EIGHT , NINE, MINUS, FOUR, 
					FIVE, SIX, DIV, ONE, TWO, THREE, MULT, ZERO, DOT, 
					EQUAL, SUM]


		grid = QtGui.QGridLayout()
		grid.addWidget(self.pantalla, 0, 0, 1, 5)
		#posiciones en el Grid
		posiciones = [(i, j) for i in range(1, 6) for j in range(0, 4)]
		#se agregan los botones.
		for i in range(1, 20):
			#se crea boton
			b = QtGui.QPushButton(botones[i])
			#Se aumenta el tamaño de fuente. 
			f = b.font()
			f.setPointSize(20) # Fuente a 27 pt. 
			b.setFont(f)
			#Se agrega el evento
			b.clicked.connect(self.onClick)
			#se le agrega un "ID"
			b.setObjectName(calc_button);
			#Se agrega al Grid
			grid.addWidget(b, posiciones[i][0], posiciones[i][1])

		#Le pone un icono al boton de nuevo usuario
		nuevo_boton.setIcon(QtGui.QIcon(user_image))
		nuevo_boton.setIconSize(QtCore.QSize(24,24))
		nuevo_boton.clicked.connect(self.nuevoOnClick)
		grid.addWidget(nuevo_boton, 1, 0)

		self.setLayout(grid)
		self.setGeometry(500, 200, 200, 200)
		self.setWindowTitle(title)
		self.show()

	def nuevoOnClick(self):
		self.ventanaNuevoUsuario = NewUserWindow()
		self.ventanaNuevoUsuario.show()

	def onClick(self):
		sender = self.sender().text()
		if (sender == CLEAR):
			self.pantalla.clear()
			self._ScreenText_ = ""
		elif (sender == EQUAL):
			scr = self.pantalla.text()
			cad = str(scr)
			calc = ScientificCalculator()
			res = calc.sc_evalue(cad)
			self.pantalla.clear()
			self.pantalla.setText(str(res))
			self._ScreenText_ = ""
			"""
			MORUBIO: Aqui el usuario presionó el boton '=' y tienes que llamar 
			a algo que calcule la expresion, después cambiar el texto de la pantalla con:
			self.pantalla.setText(resultado) 
			"""
			#print self.pantalla.text()
			#Limpia la pantalla y el string que lleva la expresion
			#self.pantalla.clear()
			#self._ScreenText_ = ""
			#self.pantalla.setText(resultado)
		else:
			self._ScreenText_ += sender
			self.pantalla.setText(self._ScreenText_)

"""def main():
	app = QtGui.QApplication(sys.argv)
	QtGui.QFontDatabase.addApplicationFont('/home/rene/Documents/Code/Calculadora/digital.ttf')

	stylesheet = open('style.qss').read()
	app.setStyleSheet(stylesheet)

	mainWindow = Calculadora_UI()
	sys.exit(app.exec_())


if __name__ == '__main__':
    main()"""