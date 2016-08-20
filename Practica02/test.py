#!/usr/bin/env python
#-*- coding:utf-8 -*-
from PyQt4 import QtCore, QtGui

class myDialog(QtGui.QDialog):
    _buttons = 0

    def __init__(self, parent=None):
        super(myDialog, self).__init__(parent)

        self.pushButton = QtGui.QPushButton(self)
        self.pushButton.setText(QtGui.QApplication.translate("self", "Add Botón!", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton.clicked.connect(self.on_pushButton_clicked)

        self.scrollArea = QtGui.QScrollArea(self)
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QtGui.QWidget(self.scrollArea)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout = QtGui.QVBoxLayout(self)
        self.verticalLayout.addWidget(self.scrollArea)
        self.verticalLayout.addWidget(self.pushButton)

        self.verticalLayoutScroll = QtGui.QGridLayout(self.scrollAreaWidgetContents)

    @QtCore.pyqtSlot()
    def on_pushButton_clicked(self):
        self._buttons  += 1
        name = u"Button {0}".format(self._buttons)

        label = QtGui.QLabel(name, self.scrollAreaWidgetContents)
        label.setText(name)

        self.verticalLayoutScroll.addWidget(label, self._buttons, 0, 2, 15)


if __name__ == "__main__":
    import sys

    app = QtGui.QApplication(sys.argv)
    app.setApplicationName('myDialog')
    main = myDialog()
    main.setGeometry(500, 500, 500, 500)
    main.show()

    sys.exit(app.exec_())