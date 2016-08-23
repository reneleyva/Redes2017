from PyQt4 import QtGui, QtCore
from PyQt4.QtGui import QWidget, QLabel, QMessageBox
from LoginWindow import LoginWindow


import os
import sys


# MAIN
def main():
    app = QtGui.QApplication(sys.argv)

    stylesheet = open('style.qss').read()
    app.setStyleSheet(stylesheet)
    mainWindow = LoginWindow()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
