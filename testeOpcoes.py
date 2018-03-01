# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'testeOpcoes.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(800, 600)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.Comando1 = QtGui.QPushButton(self.centralwidget)
        self.Comando1.setGeometry(QtCore.QRect(30, 30, 101, 31))
        self.Comando1.setObjectName(_fromUtf8("Comando1"))
        self.opcoes1 = QtGui.QComboBox(self.centralwidget)
        self.opcoes1.setGeometry(QtCore.QRect(140, 30, 171, 31))
        self.opcoes1.setObjectName(_fromUtf8("opcoes1"))
        self.opcoes1.addItem(_fromUtf8(""))
        self.opcoes1.addItem(_fromUtf8(""))
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(320, 40, 67, 21))
        self.label.setObjectName(_fromUtf8("label"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 27))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.Comando1.setText(_translate("MainWindow", "C-1", None))
        self.opcoes1.setItemText(0, _translate("MainWindow", "OP-1", None))
        self.opcoes1.setItemText(1, _translate("MainWindow", "OP-2", None))
        self.label.setText(_translate("MainWindow", "TEste", None))

