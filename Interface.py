# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Interface.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#

# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Interface.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
import sys

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

class Ui_Tela(object):
    def setupUi(self, Tela):
	#cor do quadrado de indicacao
	

        Tela.setObjectName(_fromUtf8("Tela"))
        Tela.resize(766, 628)

        self.centralwidget = QtGui.QWidget(Tela)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        
	self.horizontalLayoutWidget = QtGui.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(0, 40, 141, 51))
        self.horizontalLayoutWidget.setObjectName(_fromUtf8("horizontalLayoutWidget"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))

        self.filete_button = QtGui.QPushButton(self.horizontalLayoutWidget)
        self.filete_button.setEnabled(True)
        self.filete_button.setObjectName(_fromUtf8("filete_button"))
        self.horizontalLayout.addWidget(self.filete_button)

        self.horizontalLayoutWidget_2 = QtGui.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(250, 40, 161, 51))
        self.horizontalLayoutWidget_2.setObjectName(_fromUtf8("horizontalLayoutWidget_2"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.concentrado_button = QtGui.QPushButton(self.horizontalLayoutWidget_2)
        self.concentrado_button.setObjectName(_fromUtf8("concentrado_button"))
        self.horizontalLayout_2.addWidget(self.concentrado_button)

        self.horizontalLayoutWidget_3 = QtGui.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_3.setGeometry(QtCore.QRect(540, 40, 141, 51))
        self.horizontalLayoutWidget_3.setObjectName(_fromUtf8("horizontalLayoutWidget_3"))
        self.horizontalLayout_3 = QtGui.QHBoxLayout(self.horizontalLayoutWidget_3)
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.varredura_button = QtGui.QPushButton(self.horizontalLayoutWidget_3)
        self.varredura_button.setObjectName(_fromUtf8("varredura_button"))
        self.horizontalLayout_3.addWidget(self.varredura_button)

        self.gridLayoutWidget = QtGui.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(0, 90, 761, 481))
        self.gridLayoutWidget.setObjectName(_fromUtf8("gridLayoutWidget"))
        self.gridLayout = QtGui.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.editor_window = QtGui.QTextEdit(self.gridLayoutWidget)
        self.editor_window.setObjectName(_fromUtf8("editor_window"))
        self.gridLayout.addWidget(self.editor_window, 0, 0, 1, 1)

        Tela.setCentralWidget(self.centralwidget)
        
	self.menubar = QtGui.QMenuBar(Tela)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 766, 27))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        Tela.setMenuBar(self.menubar)
      
        self.statusbar = QtGui.QStatusBar(Tela)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        Tela.setStatusBar(self.statusbar)
		
	

        self.retranslateUi(Tela)
        QtCore.QMetaObject.connectSlotsByName(Tela)

    def retranslateUi(self, Tela):

        Tela.setWindowTitle(_translate("Tela", "Interface Estufa Probac", None))
        self.filete_button.setText(_translate("Tela", "Teste Filete", None))
        self.concentrado_button.setText(_translate("Tela", "Teste Concentrado", None))
        self.varredura_button.setText(_translate("Tela", "Varredura", None))

