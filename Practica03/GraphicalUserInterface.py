from PyQt4 import QtGui, QtCore
from PyQt4.QtGui import QWidget, QLabel, QMessageBox


import os
import sys
from Constants import Constants
from GUI.LoginWindow import LoginWindow


#style = os.path.join('./GUI/style.qss')
#send_imasge = os.path.join('./GUI/send.png')

import os
import sys


# MAIN
def main():
    Constants.MAIN_APP = QtGui.QApplication(sys.argv)

    stylesheet = open(Constants.STYLE).read()
    Constants.MAIN_APP.setStyleSheet(stylesheet)
    mainWindow = LoginWindow()
    sys.exit(Constants.MAIN_APP.exec_())


if __name__ == '__main__':
    main()
