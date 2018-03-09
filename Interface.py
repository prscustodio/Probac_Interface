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
	
	#Window setup
        Tela.setObjectName(_fromUtf8("Tela"))
        Tela.resize(1030, 700)
	Tela.setStyleSheet("Background-color:  rgb(255,255,255)")
        self.centralwidget = QtGui.QWidget(Tela)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
	
	#logo probac setup
	pic = QtGui.QLabel(Tela)
	pic.setGeometry(270, 10, 300, 100)
	pic.setPixmap(QtGui.QPixmap("/home/pi/Desktop/Probac_Interface/LogoProbac.png"))
	#pic.setScaledContents(100,100)

	#grid filete setup
	self.horizontalLayoutWidget = QtGui.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(0, 110, 141, 51))
        self.horizontalLayoutWidget.setObjectName(_fromUtf8("horizontalLayoutWidget"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
	
        self.filete_button = QtGui.QPushButton(self.horizontalLayoutWidget)
        self.filete_button.setEnabled(True)
        self.filete_button.setObjectName(_fromUtf8("filete_button"))
        self.horizontalLayout.addWidget(self.filete_button)
	self.filete_button.setStyleSheet("Background-color:  rgb(0,155,255)")

	#setup grid e botao concentrado
        self.horizontalLayoutWidget_2 = QtGui.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(250, 110, 161, 51))
        self.horizontalLayoutWidget_2.setObjectName(_fromUtf8("horizontalLayoutWidget_2"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.concentrado_button = QtGui.QPushButton(self.horizontalLayoutWidget_2)
        self.concentrado_button.setObjectName(_fromUtf8("concentrado_button"))
        self.horizontalLayout_2.addWidget(self.concentrado_button)

	self.concentrado_button.setStyleSheet("Background-color:  rgb(0,155,255)")
	
	#setup grid e botao varredura
        self.horizontalLayoutWidget_3 = QtGui.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_3.setGeometry(QtCore.QRect(540, 110, 141, 51))
        self.horizontalLayoutWidget_3.setObjectName(_fromUtf8("horizontalLayoutWidget_3"))
        self.horizontalLayout_3 = QtGui.QHBoxLayout(self.horizontalLayoutWidget_3)
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.varredura_button = QtGui.QPushButton(self.horizontalLayoutWidget_3)
        self.varredura_button.setObjectName(_fromUtf8("varredura_button"))
        self.horizontalLayout_3.addWidget(self.varredura_button)
	
	self.varredura_button.setStyleSheet("Background-color:  rgb(0,155,255)")

	#setup grid e botao close
        self.horizontalLayoutWidget_4 = QtGui.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_4.setGeometry(QtCore.QRect(850, 20, 141, 51))
        self.horizontalLayoutWidget_4.setObjectName(_fromUtf8("horizontalLayoutWidget_4"))
        self.horizontalLayout_4 = QtGui.QHBoxLayout(self.horizontalLayoutWidget_4)
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.close_button = QtGui.QPushButton(self.horizontalLayoutWidget_4)
        self.close_button.setObjectName(_fromUtf8("close_button"))
        self.horizontalLayout_4.addWidget(self.close_button)
	self.close_button.setStyleSheet("Background-color:  rgb(0,155,255)")
	
	#definindo botao operacao
	self.horizontalLayoutWidget_5 = QtGui.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_5.setGeometry(QtCore.QRect(830, 140, 170, 51))
        self.horizontalLayoutWidget_5.setObjectName(_fromUtf8("horizontalLayoutWidget_5"))
        self.horizontalLayout_5 = QtGui.QHBoxLayout(self.horizontalLayoutWidget_5)
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        self.operacao_button = QtGui.QPushButton(self.horizontalLayoutWidget_5)
        self.operacao_button.setObjectName(_fromUtf8("operacao_button"))
        self.horizontalLayout_5.addWidget(self.operacao_button)
	self.operacao_button.setStyleSheet("Background-color:  rgb(0,155,255)")

	#definindo Qbox Opcoes sensor 1
	self.horizontalLayoutWidget_6 = QtGui.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_6.setGeometry(QtCore.QRect(900, 200, 141,51))
        self.horizontalLayoutWidget_6.setObjectName(_fromUtf8("horizontalLayoutWidget_6"))
        self.horizontalLayout_6 = QtGui.QHBoxLayout(self.horizontalLayoutWidget_6)
        self.horizontalLayout_6.setObjectName(_fromUtf8("horizontalLayout_6"))
        self.opcoes1 = QtGui.QComboBox(self.horizontalLayoutWidget_6)
        self.opcoes1.setObjectName(_fromUtf8("opcoes1"))
        self.opcoes1.addItem(_fromUtf8("OP-1"))
        self.opcoes1.addItem(_fromUtf8("OP-2"))
	self.opcoes1.setStyleSheet("Background-color:  rgb(0,155,255)")
	
	#Add Label sensor 1
	self.horizontalLayoutWidget_7 = QtGui.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_7.setGeometry(QtCore.QRect(825, 200, 65,51))
        self.horizontalLayoutWidget_7.setObjectName(_fromUtf8("horizontalLayoutWidget_7"))
        self.horizontalLayout_7 = QtGui.QHBoxLayout(self.horizontalLayoutWidget_7)
        self.horizontalLayout_7.setObjectName(_fromUtf8("horizontalLayout_7"))
        self.label1 = QtGui.QLabel(self.horizontalLayoutWidget_7)
	#self.label1 = QtGui.QLabel(self.centralwidget)
        self.label1.setObjectName(_fromUtf8("Opcção 1"))
	#self.label1.setStyleSheet("Background-color:  rgb(0,155,255)")

	#definindo Qbox Opcoes sensor 2
	self.horizontalLayoutWidget_8 = QtGui.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_8.setGeometry(QtCore.QRect(900, 270, 141,51))
        self.horizontalLayoutWidget_8.setObjectName(_fromUtf8("horizontalLayoutWidget_8"))
        self.horizontalLayout_8 = QtGui.QHBoxLayout(self.horizontalLayoutWidget_8)
        self.horizontalLayout_8.setObjectName(_fromUtf8("horizontalLayout_8"))
        self.opcoes2 = QtGui.QComboBox(self.horizontalLayoutWidget_8)
        self.opcoes2.setObjectName(_fromUtf8("opcoes2"))
        self.opcoes2.addItem(_fromUtf8("OP-1"))
        self.opcoes2.addItem(_fromUtf8("OP-2"))
	self.opcoes2.setStyleSheet("Background-color:  rgb(0,155,255)")
	
	#Add Label sensor 2
	self.horizontalLayoutWidget_9 = QtGui.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_9.setGeometry(QtCore.QRect(825, 270, 65,51))
        self.horizontalLayoutWidget_9.setObjectName(_fromUtf8("horizontalLayoutWidget_9"))
        self.horizontalLayout_9 = QtGui.QHBoxLayout(self.horizontalLayoutWidget_9)
        self.horizontalLayout_9.setObjectName(_fromUtf8("horizontalLayout_9"))
        self.label2 = QtGui.QLabel(self.horizontalLayoutWidget_9)
	#self.label1 = QtGui.QLabel(self.centralwidget)
        self.label2.setObjectName(_fromUtf8("Opcção 2"))
	#self.label1.setStyleSheet("Background-color:  rgb(0,155,255)")
	
	#definindo Qbox Opcoes sensor 3
	self.horizontalLayoutWidget_10 = QtGui.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_10.setGeometry(QtCore.QRect(900, 340, 141,51))
        self.horizontalLayoutWidget_10.setObjectName(_fromUtf8("horizontalLayoutWidget_10"))
        self.horizontalLayout_10 = QtGui.QHBoxLayout(self.horizontalLayoutWidget_10)
        self.horizontalLayout_10.setObjectName(_fromUtf8("horizontalLayout_10"))
        self.opcoes3 = QtGui.QComboBox(self.horizontalLayoutWidget_10)
        self.opcoes3.setObjectName(_fromUtf8("opcoes3"))
        self.opcoes3.addItem(_fromUtf8("OP-1"))
        self.opcoes3.addItem(_fromUtf8("OP-2"))
	self.opcoes3.setStyleSheet("Background-color:  rgb(0,155,255)")
	
	#Add Label sensor 3
	self.horizontalLayoutWidget_11 = QtGui.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_11.setGeometry(QtCore.QRect(825, 340, 65,51))
        self.horizontalLayoutWidget_11.setObjectName(_fromUtf8("horizontalLayoutWidget_11"))
        self.horizontalLayout_11 = QtGui.QHBoxLayout(self.horizontalLayoutWidget_11)
        self.horizontalLayout_11.setObjectName(_fromUtf8("horizontalLayout_11"))
        self.label3 = QtGui.QLabel(self.horizontalLayoutWidget_11)
	#self.label1 = QtGui.QLabel(self.centralwidget)
        self.label3.setObjectName(_fromUtf8("Opcção 3"))
	#self.label1.setStyleSheet("Background-color:  rgb(0,155,255)")

	#definindo Qbox Opcoes sensor 4
	self.horizontalLayoutWidget_12 = QtGui.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_12.setGeometry(QtCore.QRect(900, 410, 141,51))
        self.horizontalLayoutWidget_12.setObjectName(_fromUtf8("horizontalLayoutWidget_12"))
        self.horizontalLayout_12 = QtGui.QHBoxLayout(self.horizontalLayoutWidget_12)
        self.horizontalLayout_12.setObjectName(_fromUtf8("horizontalLayout_12"))
        self.opcoes4 = QtGui.QComboBox(self.horizontalLayoutWidget_12)
        self.opcoes4.setObjectName(_fromUtf8("opcoes4"))
        self.opcoes4.addItem(_fromUtf8("OP-1"))
        self.opcoes4.addItem(_fromUtf8("OP-2"))
	self.opcoes4.setStyleSheet("Background-color:  rgb(0,155,255)")
	
	#Add Label sensor 4
	self.horizontalLayoutWidget_13 = QtGui.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_13.setGeometry(QtCore.QRect(825, 410, 65,51))
        self.horizontalLayoutWidget_13.setObjectName(_fromUtf8("horizontalLayoutWidget_13"))
        self.horizontalLayout_13 = QtGui.QHBoxLayout(self.horizontalLayoutWidget_13)
        self.horizontalLayout_13.setObjectName(_fromUtf8("horizontalLayout_13"))
        self.label4 = QtGui.QLabel(self.horizontalLayoutWidget_13)
	#self.label1 = QtGui.QLabel(self.centralwidget)
        self.label4.setObjectName(_fromUtf8("Opcção 4"))
	#self.label1.setStyleSheet("Background-color:  rgb(0,155,255)")

	#definindo Qbox Opcoes sensor 5
	self.horizontalLayoutWidget_14 = QtGui.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_14.setGeometry(QtCore.QRect(900, 480, 141,51))
        self.horizontalLayoutWidget_14.setObjectName(_fromUtf8("horizontalLayoutWidget_14"))
        self.horizontalLayout_14 = QtGui.QHBoxLayout(self.horizontalLayoutWidget_14)
        self.horizontalLayout_14.setObjectName(_fromUtf8("horizontalLayout_14"))
        self.opcoes5 = QtGui.QComboBox(self.horizontalLayoutWidget_14)
        self.opcoes5.setObjectName(_fromUtf8("opcoes5"))
        self.opcoes5.addItem(_fromUtf8("OP-1"))
        self.opcoes5.addItem(_fromUtf8("OP-2"))
	self.opcoes5.setStyleSheet("Background-color:  rgb(0,155,255)")
	
	#Add Label sensor 5
	self.horizontalLayoutWidget_15 = QtGui.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_15.setGeometry(QtCore.QRect(825, 480, 65,51))
        self.horizontalLayoutWidget_15.setObjectName(_fromUtf8("horizontalLayoutWidget_15"))
        self.horizontalLayout_15 = QtGui.QHBoxLayout(self.horizontalLayoutWidget_15)
        self.horizontalLayout_15.setObjectName(_fromUtf8("horizontalLayout_15"))
        self.label5 = QtGui.QLabel(self.horizontalLayoutWidget_15)
	#self.label1 = QtGui.QLabel(self.centralwidget)
        self.label5.setObjectName(_fromUtf8("Opcção 5"))
	#self.label1.setStyleSheet("Background-color:  rgb(0,155,255)")

	#definindo Qbox Opcoes Endereço
	self.horizontalLayoutWidget_17 = QtGui.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_17.setGeometry(QtCore.QRect(900, 550, 141,51))
        self.horizontalLayoutWidget_17.setObjectName(_fromUtf8("horizontalLayoutWidget_17"))
        self.horizontalLayout_17 = QtGui.QHBoxLayout(self.horizontalLayoutWidget_17)
        self.horizontalLayout_17.setObjectName(_fromUtf8("horizontalLayout_17"))
        self.opcoes6 = QtGui.QComboBox(self.horizontalLayoutWidget_17)
        self.opcoes6.setObjectName(_fromUtf8("opcoes6"))
        self.opcoes6.addItem(_fromUtf8("OP-1"))
        self.opcoes6.addItem(_fromUtf8("OP-2"))
	self.opcoes6.setStyleSheet("Background-color:  rgb(0,155,255)")
	
	#Add Label Endereco
	self.horizontalLayoutWidget_18 = QtGui.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_18.setGeometry(QtCore.QRect(825, 550, 65,51))
        self.horizontalLayoutWidget_18.setObjectName(_fromUtf8("horizontalLayoutWidget_18"))
        self.horizontalLayout_18 = QtGui.QHBoxLayout(self.horizontalLayoutWidget_18)
        self.horizontalLayout_18.setObjectName(_fromUtf8("horizontalLayout_18"))
        self.label6 = QtGui.QLabel(self.horizontalLayoutWidget_18)
	#self.label1 = QtGui.QLabel(self.centralwidget)
        self.label6.setObjectName(_fromUtf8("Opcção 6"))
	#self.label1.setStyleSheet("Background-color:  rgb(0,155,255)")

	#setup grid e botao editor window
        self.gridLayoutWidget = QtGui.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(0, 160, 800, 481))
        self.gridLayoutWidget.setObjectName(_fromUtf8("gridLayoutWidget"))
        self.gridLayout = QtGui.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.editor_window = QtGui.QTextEdit(self.gridLayoutWidget)
        self.editor_window.setObjectName(_fromUtf8("editor_window"))
        self.gridLayout.addWidget(self.editor_window, 0, 0, 1, 1)
	self.editor_window.setStyleSheet("Background-color:  rgb(240,240,244)")

        Tela.setCentralWidget(self.centralwidget)
        
	self.menubar = QtGui.QMenuBar(Tela)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 766, 27))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        Tela.setMenuBar(self.menubar)
      
        self.statusbar = QtGui.QStatusBar(Tela)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        Tela.setStatusBar(self.statusbar)
	
        self.retranslateUi(Tela)
	#QtCore.QObject.connect(self.close_button, QtCore.SIGNAL(_fromUtf8("clicked()")).close)
        QtCore.QMetaObject.connectSlotsByName(Tela)


    def retranslateUi(self, Tela):

        Tela.setWindowTitle(_translate("Tela", "Interface Estufa Probac", None))
        self.filete_button.setText(_translate("Tela", "Teste Filete", None))
        self.concentrado_button.setText(_translate("Tela", "Teste Concentrado", None))
        self.varredura_button.setText(_translate("Tela", "Varredura", None))
	self.close_button.setText(_translate("Tela", "Close", None))
	self.operacao_button.setText(_translate("Tela", "Atualizar Operação", None))
	self.label1.setText(_translate("Tela", "Sensor 1:", None))
	self.label2.setText(_translate("Tela", "Sensor 2:", None))
	self.label3.setText(_translate("Tela", "Sensor 3:", None))
	self.label4.setText(_translate("Tela", "Sensor 4:", None))
	self.label5.setText(_translate("Tela", "Sensor 5:", None))
	self.label6.setText(_translate("Tela", "Endereço:", None))
