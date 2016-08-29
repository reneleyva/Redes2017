from PyQt4 import QtGui, QtCore
from PyQt4.QtGui import QWidget, QLabel, QMessageBox


import os
import sys

from GUI.LoginWindow import LoginWindow


style = os.path.join('./GUI/style.qss')
send_imasge = os.path.join('./GUI/send.png')

import os
import sys


# MAIN
def main():
    app = QtGui.QApplication(sys.argv)

    stylesheet = open(style).read()
    app.setStyleSheet(stylesheet)
    mainWindow = LoginWindow(send_imasge)
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
