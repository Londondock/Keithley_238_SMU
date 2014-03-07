# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'hw.ui'
#
# Created: Sun Jun 23 21:47:45 2013
#      by: PyQt4 UI code generator 4.9.5
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(364, 385)
        self.cmdClear = QtGui.QPushButton(Dialog)
        self.cmdClear.setGeometry(QtCore.QRect(150, 40, 75, 23))
        self.cmdClear.setObjectName(_fromUtf8("cmdClear"))
        self.widget = QtGui.QWidget(Dialog)
        self.widget.setGeometry(QtCore.QRect(80, 80, 216, 25))
        self.widget.setObjectName(_fromUtf8("widget"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.widget)
        self.horizontalLayout.setMargin(0)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.txtLine = QtGui.QLineEdit(self.widget)
        self.txtLine.setObjectName(_fromUtf8("txtLine"))
        self.horizontalLayout.addWidget(self.txtLine)
        self.cmdWrite = QtGui.QPushButton(self.widget)
        self.cmdWrite.setObjectName(_fromUtf8("cmdWrite"))
        self.horizontalLayout.addWidget(self.cmdWrite)
        self.widget1 = QtGui.QWidget(Dialog)
        self.widget1.setGeometry(QtCore.QRect(60, 140, 258, 213))
        self.widget1.setObjectName(_fromUtf8("widget1"))
        self.verticalLayout = QtGui.QVBoxLayout(self.widget1)
        self.verticalLayout.setMargin(0)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.txtEdit = QtGui.QTextEdit(self.widget1)
        self.txtEdit.setObjectName(_fromUtf8("txtEdit"))
        self.verticalLayout.addWidget(self.txtEdit)
        self.lblShow = QtGui.QLabel(self.widget1)
        self.lblShow.setObjectName(_fromUtf8("lblShow"))
        self.verticalLayout.addWidget(self.lblShow)

        self.retranslateUi(Dialog)
        QtCore.QObject.connect(self.cmdClear, QtCore.SIGNAL(_fromUtf8("clicked()")), self.lblShow.clear)
        QtCore.QObject.connect(self.cmdClear, QtCore.SIGNAL(_fromUtf8("clicked()")), self.txtLine.clear)
        QtCore.QObject.connect(self.cmdClear, QtCore.SIGNAL(_fromUtf8("clicked()")), self.txtEdit.clear)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QtGui.QApplication.translate("Dialog", "Dialog", None, QtGui.QApplication.UnicodeUTF8))
        self.cmdClear.setText(QtGui.QApplication.translate("Dialog", "Clear", None, QtGui.QApplication.UnicodeUTF8))
        self.cmdWrite.setText(QtGui.QApplication.translate("Dialog", "Write", None, QtGui.QApplication.UnicodeUTF8))
        self.lblShow.setText(QtGui.QApplication.translate("Dialog", "TextLabel", None, QtGui.QApplication.UnicodeUTF8))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Dialog = QtGui.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

