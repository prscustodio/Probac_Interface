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

#...................................................................................................................................................................................................................
	#Window setup
        Tela.setObjectName(_fromUtf8("Tela"))
        Tela.resize(1400, 830)
	Tela.setStyleSheet("Background-color:  rgb(255,255,255)")
        self.centralwidget = QtGui.QWidget(Tela)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
#...................................................................................................................................................................................................................
	#logo probac setup
	pic = QtGui.QLabel(Tela)
	pic.setGeometry(270, 10, 300, 100)
	pic.setPixmap(QtGui.QPixmap("/home/pi/Desktop/Probac_Interface/LogoProbac.png"))
	#pic.setScaledContents(100,100)

#...................................................................................................................................................................................................................
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

#...................................................................................................................................................................................................................
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

#...................................................................................................................................................................................................................
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

#...................................................................................................................................................................................................................
	#setup grid e botao close
        self.horizontalLayoutWidget_4 = QtGui.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_4.setGeometry(QtCore.QRect(1220, 20, 141, 51))
        self.horizontalLayoutWidget_4.setObjectName(_fromUtf8("horizontalLayoutWidget_4"))
        self.horizontalLayout_4 = QtGui.QHBoxLayout(self.horizontalLayoutWidget_4)
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.close_button = QtGui.QPushButton(self.horizontalLayoutWidget_4)
        self.close_button.setObjectName(_fromUtf8("close_button"))
        self.horizontalLayout_4.addWidget(self.close_button)
	self.close_button.setStyleSheet("Background-color:  rgb(0,155,255)")

#...................................................................................................................................................................................................................
	#setup grid e botao editor window
        self.gridLayoutWidget = QtGui.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(0, 160, 800, 625))
        self.gridLayoutWidget.setObjectName(_fromUtf8("gridLayoutWidget"))
        self.gridLayout = QtGui.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.editor_window = QtGui.QTextEdit(self.gridLayoutWidget)
        self.editor_window.setObjectName(_fromUtf8("editor_window"))
        self.gridLayout.addWidget(self.editor_window, 0, 0, 1, 1)
	self.editor_window.setStyleSheet("Background-color:  rgb(240,240,244)")

#...................................................................................................................................................................................................................
	#Add Label Linha 1 (Teste Solicitaçao Start, Stop)
	self.horizontalLayoutWidget_L1 = QtGui.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_L1.setGeometry(QtCore.QRect(795, 100, 575 ,51))
        self.horizontalLayoutWidget_L1.setObjectName(_fromUtf8("horizontalLayoutWidget_L1"))
        self.horizontalLayout_L1 = QtGui.QHBoxLayout(self.horizontalLayoutWidget_L1)
        self.horizontalLayout_L1.setObjectName(_fromUtf8("horizontalLayout_L1"))	
        self.label_L1 = QtGui.QLabel(self.horizontalLayoutWidget_L1)
	#self.label_L1 = QtGui.QLabel(self.centralwidget)
        self.label_L1.setObjectName(_fromUtf8("Opção L1"))
        self.horizontalLayout_L1.addWidget(self.label_L1)
	self.label_L1.setStyleSheet("Background-color:  rgb(0,155,255)")
	
	#definindo Qbox Opcoes endereços L1
	self.horizontalLayoutWidget_B1End = QtGui.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_B1End.setGeometry(QtCore.QRect(800, 180, 141,51))
        self.horizontalLayoutWidget_B1End.setObjectName(_fromUtf8("horizontalLayoutWidget_B1End"))
        self.horizontalLayout_B1End = QtGui.QHBoxLayout(self.horizontalLayoutWidget_B1End)
        self.horizontalLayout_B1End.setObjectName(_fromUtf8("horizontalLayout_B1End"))
        self.opcoes_B1End = QtGui.QComboBox(self.horizontalLayoutWidget_B1End)
        self.opcoes_B1End.setObjectName(_fromUtf8("opcoes_B1End"))
        self.opcoes_B1End.addItem(_fromUtf8("None"))
        self.opcoes_B1End.addItem(_fromUtf8("F1"))
        self.opcoes_B1End.addItem(_fromUtf8("F2"))
	self.opcoes_B1End.setStyleSheet("Background-color:  rgb(0,155,255)")

	#Add Label L1 endereços
	self.horizontalLayoutWidget_L1End = QtGui.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_L1End.setGeometry(QtCore.QRect(800, 150, 70,25))
        self.horizontalLayoutWidget_L1End.setObjectName(_fromUtf8("horizontalLayoutWidget_L1End"))
        self.horizontalLayout_L1End = QtGui.QHBoxLayout(self.horizontalLayoutWidget_L1End)
        self.horizontalLayout_L1End.setObjectName(_fromUtf8("horizontalLayout_L1End"))
        self.label_L1End = QtGui.QLabel(self.horizontalLayoutWidget_L1End)
	#self.label1 = QtGui.QLabel(self.centralwidget)
        self.label_L1End.setObjectName(_fromUtf8("Opcção L1End"))
	#self.label1.setStyleSheet("Background-color:  rgb(0,155,255)")

	#definindo Qbox Opcoes Operacao L1
	self.horizontalLayoutWidget_B1O = QtGui.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_B1O.setGeometry(QtCore.QRect(940, 180, 141,51))
        self.horizontalLayoutWidget_B1O.setObjectName(_fromUtf8("horizontalLayoutWidget_B1O"))
        self.horizontalLayout_B1O = QtGui.QHBoxLayout(self.horizontalLayoutWidget_B1O)
        self.horizontalLayout_B1O.setObjectName(_fromUtf8("horizontalLayout_B1O"))
        self.opcoes_B1O = QtGui.QComboBox(self.horizontalLayoutWidget_B1O)
        self.opcoes_B1O.setObjectName(_fromUtf8("opcoes_B1O"))
        self.opcoes_B1O.addItem(_fromUtf8("None"))
        self.opcoes_B1O.addItem(_fromUtf8("Start"))
        self.opcoes_B1O.addItem(_fromUtf8("Stop"))
        self.opcoes_B1O.addItem(_fromUtf8("Pause"))
        self.opcoes_B1O.addItem(_fromUtf8("Status"))
        self.opcoes_B1O.addItem(_fromUtf8("Leitura"))
	self.opcoes_B1O.setStyleSheet("Background-color:  rgb(0,155,255)")
	
	#Add Label Operacoes 1
	self.horizontalLayoutWidget_L1O = QtGui.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_L1O.setGeometry(QtCore.QRect(940, 150, 70,25))
        self.horizontalLayoutWidget_L1O.setObjectName(_fromUtf8("horizontalLayoutWidget_L1O"))
        self.horizontalLayout_L1O = QtGui.QHBoxLayout(self.horizontalLayoutWidget_L1O)
        self.horizontalLayout_L1O.setObjectName(_fromUtf8("horizontalLayout_L1O"))
        self.label_L1O = QtGui.QLabel(self.horizontalLayoutWidget_L1O)
	#self.label_L1O = QtGui.QLabel(self.centralwidget)
        self.label_L1O.setObjectName(_fromUtf8("Opcção L1O"))
	#self.label_L1O.setStyleSheet("Background-color:  rgb(0,155,255)")	

	#definindo Qbox Opcoes Sensor L1
	self.horizontalLayoutWidget_B1S = QtGui.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_B1S.setGeometry(QtCore.QRect(1090, 180, 141,51))
        self.horizontalLayoutWidget_B1S.setObjectName(_fromUtf8("horizontalLayoutWidget_B1S"))
        self.horizontalLayout_B1S = QtGui.QHBoxLayout(self.horizontalLayoutWidget_B1S)
        self.horizontalLayout_B1S.setObjectName(_fromUtf8("horizontalLayout_B1S"))
        self.opcoes_B1S = QtGui.QComboBox(self.horizontalLayoutWidget_B1S)
        self.opcoes_B1S.setObjectName(_fromUtf8("opcoes_B1S"))
        self.opcoes_B1S.addItem(_fromUtf8("None"))
        self.opcoes_B1S.addItem(_fromUtf8("S1"))
        self.opcoes_B1S.addItem(_fromUtf8("S2"))
        self.opcoes_B1S.addItem(_fromUtf8("S3"))
        self.opcoes_B1S.addItem(_fromUtf8("S4"))
        self.opcoes_B1S.addItem(_fromUtf8("S5"))
	self.opcoes_B1S.setStyleSheet("Background-color:  rgb(0,155,255)")
	
	#Add Label1 Sensor 
	self.horizontalLayoutWidget_L1S = QtGui.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_L1S.setGeometry(QtCore.QRect(1090, 150, 65,25))
        self.horizontalLayoutWidget_L1S.setObjectName(_fromUtf8("horizontalLayoutWidget_L1S"))
        self.horizontalLayout_L1S = QtGui.QHBoxLayout(self.horizontalLayoutWidget_L1S)
        self.horizontalLayout_L1S.setObjectName(_fromUtf8("horizontalLayout_L1S"))
        self.label_L1S = QtGui.QLabel(self.horizontalLayoutWidget_L1S)
	#self.label_L1S = QtGui.QLabel(self.centralwidget)
        self.label_L1S.setObjectName(_fromUtf8("Opcção L1S"))
	#self.label_L1S.setStyleSheet("Background-color:  rgb(0,155,255)")	

	#definindo botao operacao
	self.horizontalLayoutWidget_L1Button = QtGui.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_L1Button.setGeometry(QtCore.QRect(1220, 165, 150, 51))
        self.horizontalLayoutWidget_L1Button.setObjectName(_fromUtf8("horizontalLayoutWidget_L1Button"))
        self.horizontalLayout_L1Button = QtGui.QHBoxLayout(self.horizontalLayoutWidget_L1Button)
        self.horizontalLayout_L1Button.setObjectName(_fromUtf8("horizontalLayout_L1Button"))
        self.operacao_L1Button = QtGui.QPushButton(self.horizontalLayoutWidget_L1Button)
        self.operacao_L1Button.setObjectName(_fromUtf8("operacao_L1Button"))
        self.horizontalLayout_L1Button.addWidget(self.operacao_L1Button)
	self.operacao_L1Button.setStyleSheet("Background-color:  rgb(0,155,255)")
#...................................................................................................................................................................................................................
	#Add Label Linha 2 (Teste Frequencia de cor)
	self.horizontalLayoutWidget_L2 = QtGui.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_L2.setGeometry(QtCore.QRect(800, 225, 570 ,51))
        self.horizontalLayoutWidget_L2.setObjectName(_fromUtf8("horizontalLayoutWidget_L2"))
        self.horizontalLayout_L2 = QtGui.QHBoxLayout(self.horizontalLayoutWidget_L2)
        self.horizontalLayout_L2.setObjectName(_fromUtf8("horizontalLayout_L2"))	
        self.label_L2 = QtGui.QLabel(self.horizontalLayoutWidget_L2)
	#self.label_L2 = QtGui.QLabel(self.centralwidget)
        self.label_L2.setObjectName(_fromUtf8("Opção L2"))
        self.horizontalLayout_L2.addWidget(self.label_L2)
	self.label_L2.setStyleSheet("Background-color:  rgb(0,155,255)")
	
	#definindo QCombobox Opcoes cores L2
	self.horizontalLayoutWidget_B2C = QtGui.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_B2C.setGeometry(QtCore.QRect(795, 285, 130,65))
        self.horizontalLayoutWidget_B2C.setObjectName(_fromUtf8("horizontalLayoutWidget_B2C"))
        self.horizontalLayout_B2C = QtGui.QHBoxLayout(self.horizontalLayoutWidget_B2C)
        self.horizontalLayout_B2C.setObjectName(_fromUtf8("horizontalLayout_B2C"))
        self.opcoes_B2C = QtGui.QComboBox(self.horizontalLayoutWidget_B2C)
        self.opcoes_B2C.setObjectName(_fromUtf8("opcoes_B2C"))
        self.opcoes_B2C.addItem(_fromUtf8("None"))
        self.opcoes_B2C.addItem(_fromUtf8("Vermelho"))
        self.opcoes_B2C.addItem(_fromUtf8("Verde"))
        self.opcoes_B2C.addItem(_fromUtf8("Azul"))
        self.horizontalLayout_B2C.addWidget(self.opcoes_B2C)
	self.opcoes_B2C.setStyleSheet("Background-color:  rgb(0,155,255)")

	#Add Label L2 cores
	self.horizontalLayoutWidget_L2C = QtGui.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_L2C.setGeometry(QtCore.QRect(800, 275, 70,25))
        self.horizontalLayoutWidget_L2C.setObjectName(_fromUtf8("horizontalLayoutWidget_L2C"))
        self.horizontalLayout_L2C = QtGui.QHBoxLayout(self.horizontalLayoutWidget_L2C)
        self.horizontalLayout_L2C.setObjectName(_fromUtf8("horizontalLayout_L2C"))
        self.label_L2C = QtGui.QLabel(self.horizontalLayoutWidget_L2C)
	#self.label1 = QtGui.QLabel(self.centralwidget)
        self.label_L2C.setObjectName(_fromUtf8("Opcção L2C"))
	#self.label1.setStyleSheet("Background-color:  rgb(0,155,255)")

	#definindo Qbox Opcoes Sensor L2
	self.horizontalLayoutWidget_B2S = QtGui.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_B2S.setGeometry(QtCore.QRect(940, 300, 141,51))
        self.horizontalLayoutWidget_B2S.setObjectName(_fromUtf8("horizontalLayoutWidget_B2S"))
        self.horizontalLayout_B2S = QtGui.QHBoxLayout(self.horizontalLayoutWidget_B2S)
        self.horizontalLayout_B2S.setObjectName(_fromUtf8("horizontalLayout_B2S"))
        self.opcoes_B2S = QtGui.QComboBox(self.horizontalLayoutWidget_B2S)
        self.opcoes_B2S.setObjectName(_fromUtf8("opcoes_B2S"))
        self.opcoes_B2S.addItem(_fromUtf8("None"))
        self.opcoes_B2S.addItem(_fromUtf8("S1"))
        self.opcoes_B2S.addItem(_fromUtf8("S2"))
        self.opcoes_B2S.addItem(_fromUtf8("S3"))
        self.opcoes_B2S.addItem(_fromUtf8("S4"))
        self.opcoes_B2S.addItem(_fromUtf8("S5"))
	self.opcoes_B2S.setStyleSheet("Background-color:  rgb(0,155,255)")
	
	#Add Label2 Sensor 
	self.horizontalLayoutWidget_L2S = QtGui.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_L2S.setGeometry(QtCore.QRect(940, 275, 65,25))
        self.horizontalLayoutWidget_L2S.setObjectName(_fromUtf8("horizontalLayoutWidget_L2S"))
        self.horizontalLayout_L2S = QtGui.QHBoxLayout(self.horizontalLayoutWidget_L2S)
        self.horizontalLayout_L2S.setObjectName(_fromUtf8("horizontalLayout_L2S"))
        self.label_L2S = QtGui.QLabel(self.horizontalLayoutWidget_L2S)
	#self.label_L2S = QtGui.QLabel(self.centralwidget)
        self.label_L2S.setObjectName(_fromUtf8("Opcção L2S"))
	#self.label_L2S.setStyleSheet("Background-color:  rgb(0,155,255)")	

	#definindo botao cor unitaria
	self.horizontalLayoutWidget_L2ButtonCU = QtGui.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_L2ButtonCU.setGeometry(QtCore.QRect(1050, 270, 120, 41))
        self.horizontalLayoutWidget_L2ButtonCU.setObjectName(_fromUtf8("horizontalLayoutWidget_L2ButtonCU"))
        self.horizontalLayout_L2ButtonCU = QtGui.QHBoxLayout(self.horizontalLayoutWidget_L2ButtonCU)
        self.horizontalLayout_L2ButtonCU.setObjectName(_fromUtf8("horizontalLayout_L2ButtonCU"))
        self.operacao_L2ButtonCU = QtGui.QPushButton(self.horizontalLayoutWidget_L2ButtonCU)
        self.operacao_L2ButtonCU.setObjectName(_fromUtf8("operacao_L2ButtonCU"))
        self.horizontalLayout_L2ButtonCU.addWidget(self.operacao_L2ButtonCU)
	self.operacao_L2ButtonCU.setStyleSheet("Background-color:  rgb(0,155,255)")

	#definindo botao cor em lote
	self.horizontalLayoutWidget_L2ButtonCL = QtGui.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_L2ButtonCL.setGeometry(QtCore.QRect(1050, 305, 120, 41))
        self.horizontalLayoutWidget_L2ButtonCL.setObjectName(_fromUtf8("horizontalLayoutWidget_L2ButtonCL"))
        self.horizontalLayout_L2ButtonCL = QtGui.QHBoxLayout(self.horizontalLayoutWidget_L2ButtonCL)
        self.horizontalLayout_L2ButtonCL.setObjectName(_fromUtf8("horizontalLayout_L2ButtonCL"))
        self.operacao_L2ButtonCL = QtGui.QPushButton(self.horizontalLayoutWidget_L2ButtonCL)
        self.operacao_L2ButtonCL.setObjectName(_fromUtf8("operacao_L2ButtonCL"))
        self.horizontalLayout_L2ButtonCL.addWidget(self.operacao_L2ButtonCL)
	self.operacao_L2ButtonCL.setStyleSheet("Background-color:  rgb(0,155,255)")

	#definindo botao tadas cores 
	self.horizontalLayoutWidget_L2ButtonTC = QtGui.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_L2ButtonTC.setGeometry(QtCore.QRect(1190, 270, 175, 41))
        self.horizontalLayoutWidget_L2ButtonTC.setObjectName(_fromUtf8("horizontalLayoutWidget_L2ButtonTC"))
        self.horizontalLayout_L2ButtonTC = QtGui.QHBoxLayout(self.horizontalLayoutWidget_L2ButtonTC)
        self.horizontalLayout_L2ButtonTC.setObjectName(_fromUtf8("horizontalLayout_L2ButtonTC"))
        self.operacao_L2ButtonTC = QtGui.QPushButton(self.horizontalLayoutWidget_L2ButtonTC)
        self.operacao_L2ButtonTC.setObjectName(_fromUtf8("operacao_L2ButtonTC"))
        self.horizontalLayout_L2ButtonTC.addWidget(self.operacao_L2ButtonTC)
	self.operacao_L2ButtonTC.setStyleSheet("Background-color:  rgb(0,155,255)")

	#definindo botao tadas cores em lote
	self.horizontalLayoutWidget_L2ButtonTCL = QtGui.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_L2ButtonTCL.setGeometry(QtCore.QRect(1190, 305, 175, 41))
        self.horizontalLayoutWidget_L2ButtonTCL.setObjectName(_fromUtf8("horizontalLayoutWidget_L2ButtonTCL"))
        self.horizontalLayout_L2ButtonTCL = QtGui.QHBoxLayout(self.horizontalLayoutWidget_L2ButtonTCL)
        self.horizontalLayout_L2ButtonTCL.setObjectName(_fromUtf8("horizontalLayout_L2ButtonTCL"))
        self.operacao_L2ButtonTCL = QtGui.QPushButton(self.horizontalLayoutWidget_L2ButtonTCL)
        self.operacao_L2ButtonTCL.setObjectName(_fromUtf8("operacao_L2ButtonTCL"))
        self.horizontalLayout_L2ButtonTCL.addWidget(self.operacao_L2ButtonTCL)
	self.operacao_L2ButtonTCL.setStyleSheet("Background-color:  rgb(0,155,255)")
#...................................................................................................................................................................................................................
	#Add Label Linha 3 (Solicitaçao Intervalo)
	self.horizontalLayoutWidget_L3 = QtGui.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_L3.setGeometry(QtCore.QRect(795, 340, 570 ,51))
        self.horizontalLayoutWidget_L3.setObjectName(_fromUtf8("horizontalLayoutWidget_L3"))
        self.horizontalLayout_L3 = QtGui.QHBoxLayout(self.horizontalLayoutWidget_L3)
        self.horizontalLayout_L3.setObjectName(_fromUtf8("horizontalLayout_L3"))	
        self.label_L3 = QtGui.QLabel(self.horizontalLayoutWidget_L3)
	#self.label_L3 = QtGui.QLabel(self.centralwidget)
        self.label_L3.setObjectName(_fromUtf8("Opção L3"))
        self.horizontalLayout_L3.addWidget(self.label_L3)
	self.label_L3.setStyleSheet("Background-color:  rgb(0,155,255)")
	
	#definindo Qbox Opcoes comando L3
	self.horizontalLayoutWidget_B3C = QtGui.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_B3C.setGeometry(QtCore.QRect(800, 405, 181,51))
        self.horizontalLayoutWidget_B3C.setObjectName(_fromUtf8("horizontalLayoutWidget_B3C"))
        self.horizontalLayout_B3C = QtGui.QHBoxLayout(self.horizontalLayoutWidget_B3C)
        self.horizontalLayout_B3C.setObjectName(_fromUtf8("horizontalLayout_B3C"))
        self.opcoes_B3C = QtGui.QComboBox(self.horizontalLayoutWidget_B3C)
        self.opcoes_B3C.setObjectName(_fromUtf8("opcoes_B3C"))
        self.opcoes_B3C.addItem(_fromUtf8("None"))
        self.opcoes_B3C.addItem(_fromUtf8("Alterar intervalo"))
        self.opcoes_B3C.addItem(_fromUtf8("Valor Intervalo"))
        self.horizontalLayout_B3C.addWidget(self.opcoes_B3C)
	self.opcoes_B3C.setStyleSheet("Background-color:  rgb(0,155,255)")

	#Add Label L3 Comando
	self.horizontalLayoutWidget_L3C = QtGui.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_L3C.setGeometry(QtCore.QRect(800, 385, 100,30))
        self.horizontalLayoutWidget_L3C.setObjectName(_fromUtf8("horizontalLayoutWidget_L3C"))
        self.horizontalLayout_L3C = QtGui.QHBoxLayout(self.horizontalLayoutWidget_L3C)
        self.horizontalLayout_L3C.setObjectName(_fromUtf8("horizontalLayout_L3C"))
        self.label_L3C = QtGui.QLabel(self.horizontalLayoutWidget_L3C)
	#self.label3 = QtGui.QLabel(self.centralwidget)
        self.label_L3C.setObjectName(_fromUtf8("Opcção L3C"))
	self.horizontalLayout_L3C.addWidget(self.label_L3C)
	#self.label3.setStyleSheet("Background-color:  rgb(0,155,255)")

	#definindo Label Opcoes intervallo em segundos L3
	self.horizontalLayoutWidget_L3IS = QtGui.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_L3IS.setGeometry(QtCore.QRect(1000, 390, 150,61))
        self.horizontalLayoutWidget_L3IS.setObjectName(_fromUtf8("horizontalLayoutWidget_L3IS"))
        self.horizontalLayout_L3IS = QtGui.QHBoxLayout(self.horizontalLayoutWidget_L3IS)
        self.horizontalLayout_L3IS.setObjectName(_fromUtf8("horizontalLayout_L3IS"))
        self.label_L3IS = QtGui.QLabel(self.horizontalLayoutWidget_L3IS)
	#self.label3 = QtGui.QLabel(self.centralwidget)
        self.label_L3IS.setObjectName(_fromUtf8("Opcção L3IS"))
	self.horizontalLayout_L3IS.addWidget(self.label_L3IS)
	#self.label_L3IS.setStyleSheet("Background-color:  rgb(0,155,255)")
	
	#Add TextWindow Intervalo Segundos  L3
        self.gridLayoutWidget_T3IS = QtGui.QWidget(self.centralwidget)
        self.gridLayoutWidget_T3IS.setGeometry(QtCore.QRect(1120, 400, 100, 51))
        self.gridLayoutWidget_T3IS.setObjectName(_fromUtf8("gridLayoutWidget_T3IS"))
        self.gridLayout_T3IS = QtGui.QGridLayout(self.gridLayoutWidget_T3IS)
        self.gridLayout_T3IS.setObjectName(_fromUtf8("gridLayout_T3IS"))
        self.editor_window_T3IS = QtGui.QTextEdit(self.gridLayoutWidget_T3IS)
        self.editor_window_T3IS.setObjectName(_fromUtf8("editor_window_T3IS"))
        self.gridLayout_T3IS.addWidget(self.editor_window_T3IS)
	self.editor_window_T3IS.setStyleSheet("Background-color:  rgb(240,240,244)")

	#definindo botao Testar
	self.horizontalLayoutWidget_L3Button = QtGui.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_L3Button.setGeometry(QtCore.QRect(1220, 400, 150, 51))
        self.horizontalLayoutWidget_L3Button.setObjectName(_fromUtf8("horizontalLayoutWidget_L3Button"))
        self.horizontalLayout_L3Button = QtGui.QHBoxLayout(self.horizontalLayoutWidget_L3Button)
        self.horizontalLayout_L3Button.setObjectName(_fromUtf8("horizontalLayout_L3Button"))
        self.operacao_L3Button = QtGui.QPushButton(self.horizontalLayoutWidget_L3Button)
        self.operacao_L3Button.setObjectName(_fromUtf8("operacao_L3Button"))
        self.horizontalLayout_L3Button.addWidget(self.operacao_L3Button)
	self.operacao_L3Button.setStyleSheet("Background-color:  rgb(0,155,255)")
#...................................................................................................................................................................................................................

	#Add Label Linha 4x1 (Teste Calibracao)
	self.horizontalLayoutWidget_L4X1 = QtGui.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_L4X1.setGeometry(QtCore.QRect(795, 455, 170 ,51))
        self.horizontalLayoutWidget_L4X1.setObjectName(_fromUtf8("horizontalLayoutWidget_L4X1"))
        self.horizontalLayout_L4X1 = QtGui.QHBoxLayout(self.horizontalLayoutWidget_L4X1)
        self.horizontalLayout_L4X1.setObjectName(_fromUtf8("horizontalLayout_L4X1"))	
        self.label_L4X1 = QtGui.QLabel(self.horizontalLayoutWidget_L4X1)
	#self.label_L3 = QtGui.QLabel(self.centralwidget)
        self.label_L4X1.setObjectName(_fromUtf8("Opção L4X1"))
        self.horizontalLayout_L4X1.addWidget(self.label_L4X1)
	self.label_L4X1.setStyleSheet("Background-color:  rgb(0,155,255)")

	#definindo Qbox Opcoes Sensor L4x1
	self.horizontalLayoutWidget_B4X1S = QtGui.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_B4X1S.setGeometry(QtCore.QRect(805, 530, 141,51))
        self.horizontalLayoutWidget_B4X1S.setObjectName(_fromUtf8("horizontalLayoutWidget_B4X1S"))
        self.horizontalLayout_B4X1S = QtGui.QHBoxLayout(self.horizontalLayoutWidget_B4X1S)
        self.horizontalLayout_B4X1S.setObjectName(_fromUtf8("horizontalLayout_B4X1S"))
        self.opcoes_B4X1S = QtGui.QComboBox(self.horizontalLayoutWidget_B4X1S)
        self.opcoes_B4X1S.setObjectName(_fromUtf8("opcoes_B4X1S"))
        self.opcoes_B4X1S.addItem(_fromUtf8("None"))
        self.opcoes_B4X1S.addItem(_fromUtf8("S1"))
        self.opcoes_B4X1S.addItem(_fromUtf8("S2"))
        self.opcoes_B4X1S.addItem(_fromUtf8("S3"))
        self.opcoes_B4X1S.addItem(_fromUtf8("S4"))
        self.opcoes_B4X1S.addItem(_fromUtf8("S5"))
	self.opcoes_B4X1S.setStyleSheet("Background-color:  rgb(0,155,255)")
	
	#Add Label4X1 Sensor 
	self.horizontalLayoutWidget_L4X1S = QtGui.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_L4X1S.setGeometry(QtCore.QRect(805, 500, 70,25))
        self.horizontalLayoutWidget_L4X1S.setObjectName(_fromUtf8("horizontalLayoutWidget_L4X1S"))
        self.horizontalLayout_L4X1S = QtGui.QHBoxLayout(self.horizontalLayoutWidget_L4X1S)
        self.horizontalLayout_L4X1S.setObjectName(_fromUtf8("horizontalLayout_L4X1S"))
        self.label_L4X1S = QtGui.QLabel(self.horizontalLayoutWidget_L4X1S)
	#self.label_L4X1S = QtGui.QLabel(self.centralwidget)
        self.label_L4X1S.setObjectName(_fromUtf8("Opcção L4X1S"))
	#self.label_L4X1S.setStyleSheet("Background-color:  rgb(0,155,255)")

	#definindo QCombobox Opcoes cores B4X1
	self.horizontalLayoutWidget_B4X1C = QtGui.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_B4X1C.setGeometry(QtCore.QRect(795, 570, 141,61))
        self.horizontalLayoutWidget_B4X1C.setObjectName(_fromUtf8("horizontalLayoutWidget_B4X1C"))
        self.horizontalLayout_B4X1C = QtGui.QHBoxLayout(self.horizontalLayoutWidget_B4X1C)
        self.horizontalLayout_B4X1C.setObjectName(_fromUtf8("horizontalLayout_B4X1C"))
        self.opcoes_B4X1C = QtGui.QComboBox(self.horizontalLayoutWidget_B4X1C)
        self.opcoes_B4X1C.setObjectName(_fromUtf8("opcoes_B4X1C"))
        self.opcoes_B4X1C.addItem(_fromUtf8("None"))
        self.opcoes_B4X1C.addItem(_fromUtf8("Vermelho"))
        self.opcoes_B4X1C.addItem(_fromUtf8("Verde"))
        self.opcoes_B4X1C.addItem(_fromUtf8("Azul"))
        self.horizontalLayout_B4X1C.addWidget(self.opcoes_B4X1C)
	self.opcoes_B4X1C.setStyleSheet("Background-color:  rgb(0,155,255)")

	#Add Label L4X1 cores
	self.horizontalLayoutWidget_L4X1C = QtGui.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_L4X1C.setGeometry(QtCore.QRect(805, 560, 70,25))
        self.horizontalLayoutWidget_L4X1C.setObjectName(_fromUtf8("horizontalLayoutWidget_L4X1C"))
        self.horizontalLayout_L4X1C = QtGui.QHBoxLayout(self.horizontalLayoutWidget_L4X1C)
        self.horizontalLayout_L4X1C.setObjectName(_fromUtf8("horizontalLayout_L4X1C"))
        self.label_L4X1C = QtGui.QLabel(self.horizontalLayoutWidget_L4X1C)
	#self.label1 = QtGui.QLabel(self.centralwidget)
        self.label_L4X1C.setObjectName(_fromUtf8("Opcção L4X1C"))
	#self.label1.setStyleSheet("Background-color:  rgb(0,155,255)")

	#definindo Label Opcoes intervallo em segundos L4X1
	self.horizontalLayoutWidget_L4X1IS = QtGui.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_L4X1IS.setGeometry(QtCore.QRect(798, 615, 150,31))
        self.horizontalLayoutWidget_L4X1IS.setObjectName(_fromUtf8("horizontalLayoutWidget_L4X1IS"))
        self.horizontalLayout_L4X1IS = QtGui.QHBoxLayout(self.horizontalLayoutWidget_L4X1IS)
        self.horizontalLayout_L4X1IS.setObjectName(_fromUtf8("horizontalLayout_L4X1IS"))
        self.label_L4X1IS = QtGui.QLabel(self.horizontalLayoutWidget_L4X1IS)
	#self.label4X1 = QtGui.QLabel(self.centralwidget)
        self.label_L4X1IS.setObjectName(_fromUtf8("Opcção L4X1IS"))
	self.horizontalLayout_L4X1IS.addWidget(self.label_L4X1IS)
	#self.label_L4X1IS.setStyleSheet("Background-color:  rgb(0,155,255)")
	
	#Add TextWindow Intervalo Segundos  L4X1
        self.gridLayoutWidget_T4X1IS = QtGui.QWidget(self.centralwidget)
        self.gridLayoutWidget_T4X1IS.setGeometry(QtCore.QRect(798, 640, 100, 51))
        self.gridLayoutWidget_T4X1IS.setObjectName(_fromUtf8("gridLayoutWidget_T4X1IS"))
        self.gridLayout_T4X1IS = QtGui.QGridLayout(self.gridLayoutWidget_T4X1IS)
        self.gridLayout_T4X1IS.setObjectName(_fromUtf8("gridLayout_T4X1IS"))
        self.editor_window_T4X1IS = QtGui.QTextEdit(self.gridLayoutWidget_T4X1IS)
        self.editor_window_T4X1IS.setObjectName(_fromUtf8("editor_window_T4X1IS"))
        self.gridLayout_T4X1IS.addWidget(self.editor_window_T4X1IS)
	self.editor_window_T4X1IS.setStyleSheet("Background-color:  rgb(240,240,244)")

	#definindo botao1 L4X1
	self.horizontalLayoutWidget_L4X1Button1 = QtGui.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_L4X1Button1.setGeometry(QtCore.QRect(800, 690, 150, 51))
        self.horizontalLayoutWidget_L4X1Button1.setObjectName(_fromUtf8("horizontalLayoutWidget_L4X1Button1"))
        self.horizontalLayout_L4X1Button1 = QtGui.QHBoxLayout(self.horizontalLayoutWidget_L4X1Button1)
        self.horizontalLayout_L4X1Button1.setObjectName(_fromUtf8("horizontalLayout_L4X1Button1"))
        self.operacao_L4X1Button1 = QtGui.QPushButton(self.horizontalLayoutWidget_L4X1Button1)
        self.operacao_L4X1Button1.setObjectName(_fromUtf8("operacao_L4X1Button1"))
        self.horizontalLayout_L4X1Button1.addWidget(self.operacao_L4X1Button1)
	self.operacao_L4X1Button1.setStyleSheet("Background-color:  rgb(0,155,255)")

	#definindo botao2 L4X1
	self.horizontalLayoutWidget_L4X1Button2 = QtGui.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_L4X1Button2.setGeometry(QtCore.QRect(800, 740, 150, 51))
        self.horizontalLayoutWidget_L4X1Button2.setObjectName(_fromUtf8("horizontalLayoutWidget_L4X1Button2"))
        self.horizontalLayout_L4X1Button2 = QtGui.QHBoxLayout(self.horizontalLayoutWidget_L4X1Button2)
        self.horizontalLayout_L4X1Button2.setObjectName(_fromUtf8("horizontalLayout_L4X1Button2"))
        self.operacao_L4X1Button2 = QtGui.QPushButton(self.horizontalLayoutWidget_L4X1Button2)
        self.operacao_L4X1Button2.setObjectName(_fromUtf8("operacao_L4X1Button2"))
        self.horizontalLayout_L4X1Button2.addWidget(self.operacao_L4X1Button2)
	self.operacao_L4X1Button2.setStyleSheet("Background-color:  rgb(0,155,255)")
#...................................................................................................................................................................................................................
	#Add Label Linha 4x2 (Teste Sensibilidade)
	self.horizontalLayoutWidget_L4X2 = QtGui.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_L4X2.setGeometry(QtCore.QRect(955, 455, 420 ,51))
        self.horizontalLayoutWidget_L4X2.setObjectName(_fromUtf8("horizontalLayoutWidget_L4X2"))
        self.horizontalLayout_L4X2 = QtGui.QHBoxLayout(self.horizontalLayoutWidget_L4X2)
        self.horizontalLayout_L4X2.setObjectName(_fromUtf8("horizontalLayout_L4X2"))	
        self.label_L4X2 = QtGui.QLabel(self.horizontalLayoutWidget_L4X2)
	#self.label_L3 = QtGui.QLabel(self.centralwidget)
        self.label_L4X2.setObjectName(_fromUtf8("Opção L4X2"))
        self.horizontalLayout_L4X2.addWidget(self.label_L4X2)
	self.label_L4X2.setStyleSheet("Background-color:  rgb(0,155,255)")

	#Add Label4X2 Sensor 
	self.horizontalLayoutWidget_L4X2S = QtGui.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_L4X2S.setGeometry(QtCore.QRect(965, 500, 70,25))
        self.horizontalLayoutWidget_L4X2S.setObjectName(_fromUtf8("horizontalLayoutWidget_L4X2S"))
        self.horizontalLayout_L4X2S = QtGui.QHBoxLayout(self.horizontalLayoutWidget_L4X2S)
        self.horizontalLayout_L4X2S.setObjectName(_fromUtf8("horizontalLayout_L4X2S"))
        self.label_L4X2S = QtGui.QLabel(self.horizontalLayoutWidget_L4X2S)
	#self.label_L4X2S = QtGui.QLabel(self.centralwidget)
        self.label_L4X2S.setObjectName(_fromUtf8("Opcção L4X2S"))
	#self.label_L4X2S.setStyleSheet("Background-color:  rgb(0,155,255)")

	#definindo Qbox Opcoes Sensor L4x2
	self.horizontalLayoutWidget_B4X2S = QtGui.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_B4X2S.setGeometry(QtCore.QRect(965, 530, 141,51))
        self.horizontalLayoutWidget_B4X2S.setObjectName(_fromUtf8("horizontalLayoutWidget_B4X2S"))
        self.horizontalLayout_B4X2S = QtGui.QHBoxLayout(self.horizontalLayoutWidget_B4X2S)
        self.horizontalLayout_B4X2S.setObjectName(_fromUtf8("horizontalLayout_B4X2S"))
        self.opcoes_B4X2S = QtGui.QComboBox(self.horizontalLayoutWidget_B4X2S)
        self.opcoes_B4X2S.setObjectName(_fromUtf8("opcoes_B4X2S"))
        self.opcoes_B4X2S.addItem(_fromUtf8("None"))
        self.opcoes_B4X2S.addItem(_fromUtf8("S1"))
        self.opcoes_B4X2S.addItem(_fromUtf8("S2"))
        self.opcoes_B4X2S.addItem(_fromUtf8("S3"))
        self.opcoes_B4X2S.addItem(_fromUtf8("S4"))
        self.opcoes_B4X2S.addItem(_fromUtf8("S5"))
	self.opcoes_B4X2S.setStyleSheet("Background-color:  rgb(0,155,255)")

	#Add Label4X2 Sensibilidade
	self.horizontalLayoutWidget_L4X3Sens = QtGui.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_L4X3Sens.setGeometry(QtCore.QRect(1080, 497, 140,38))
        self.horizontalLayoutWidget_L4X3Sens.setObjectName(_fromUtf8("horizontalLayoutWidget_L4X3Sens"))
        self.horizontalLayout_L4X3Sens = QtGui.QHBoxLayout(self.horizontalLayoutWidget_L4X3Sens)
        self.horizontalLayout_L4X3Sens.setObjectName(_fromUtf8("horizontalLayout_L4X3Sens"))
        self.label_L4X3Sens = QtGui.QLabel(self.horizontalLayoutWidget_L4X3Sens)
	#self.label_L4X3Sens = QtGui.QLabel(self.centralwidget)
        self.horizontalLayout_L4X3Sens.addWidget(self.label_L4X3Sens)
        self.label_L4X3Sens.setObjectName(_fromUtf8("Opcção L4X3Sens"))
	#self.label_L4X3Sens.setStyleSheet("Background-color:  rgb(0,155,255)")

	#Add Spin4X2 Sensibilidade
	self.horizontalLayoutWidget_Spin4X2 = QtGui.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_Spin4X2.setGeometry(QtCore.QRect(1080, 524, 140,48))
        self.horizontalLayoutWidget_Spin4X2.setObjectName(_fromUtf8("horizontalLayoutWidget_Spin4X2"))
        self.horizontalLayout_Spin4X2 = QtGui.QHBoxLayout(self.horizontalLayoutWidget_Spin4X2)
        self.horizontalLayout_Spin4X2.setObjectName(_fromUtf8("horizontalLayout_Spin4X2"))
        self.spinBox4X2 = QtGui.QSpinBox(self.horizontalLayoutWidget_Spin4X2)
        self.horizontalLayout_Spin4X2.addWidget(self.spinBox4X2)
        self.spinBox4X2.setObjectName(_fromUtf8("spinBox"))

	#definindo botao1 L4X4 B1
	self.horizontalLayoutWidget_L4X4Button1 = QtGui.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_L4X4Button1.setGeometry(QtCore.QRect(1220, 497, 150, 41))
        self.horizontalLayoutWidget_L4X4Button1.setObjectName(_fromUtf8("horizontalLayoutWidget_L4X4Button1"))
        self.horizontalLayout_L4X4Button1 = QtGui.QHBoxLayout(self.horizontalLayoutWidget_L4X4Button1)
        self.horizontalLayout_L4X4Button1.setObjectName(_fromUtf8("horizontalLayout_L4X4Button1"))
        self.operacao_L4X4Button1 = QtGui.QPushButton(self.horizontalLayoutWidget_L4X4Button1)
        self.operacao_L4X4Button1.setObjectName(_fromUtf8("operacao_L4X4Button1"))
        self.horizontalLayout_L4X4Button1.addWidget(self.operacao_L4X4Button1)
	self.operacao_L4X4Button1.setStyleSheet("Background-color:  rgb(0,155,255)")

	#definindo botao1 L4X4 B2
	self.horizontalLayoutWidget_L4X4Button2 = QtGui.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_L4X4Button2.setGeometry(QtCore.QRect(1220, 529, 150, 41))
        self.horizontalLayoutWidget_L4X4Button2.setObjectName(_fromUtf8("horizontalLayoutWidget_L4X4Button2"))
        self.horizontalLayout_L4X4Button2 = QtGui.QHBoxLayout(self.horizontalLayoutWidget_L4X4Button2)
        self.horizontalLayout_L4X4Button2.setObjectName(_fromUtf8("horizontalLayout_L4X4Button2"))
        self.operacao_L4X4Button2 = QtGui.QPushButton(self.horizontalLayoutWidget_L4X4Button2)
        self.operacao_L4X4Button2.setObjectName(_fromUtf8("operacao_L4X4Button2"))
        self.horizontalLayout_L4X4Button2.addWidget(self.operacao_L4X4Button2)
	self.operacao_L4X4Button2.setStyleSheet("Background-color:  rgb(0,155,255)")
#...................................................................................................................................................................................................................
	#Add Label Linha 4x3 (Teste SensibiliFirmware filete e concentrador)
	self.horizontalLayoutWidget_L4X3 = QtGui.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_L4X3.setGeometry(QtCore.QRect(955, 570, 420 ,51))
        self.horizontalLayoutWidget_L4X3.setObjectName(_fromUtf8("horizontalLayoutWidget_L4X3"))
        self.horizontalLayout_L4X3 = QtGui.QHBoxLayout(self.horizontalLayoutWidget_L4X3)
        self.horizontalLayout_L4X3.setObjectName(_fromUtf8("horizontalLayout_L4X3"))	
        self.label_L4X3 = QtGui.QLabel(self.horizontalLayoutWidget_L4X3)
	#self.label_L3 = QtGui.QLabel(self.centralwidget)
        self.label_L4X3.setObjectName(_fromUtf8("Opção L4X3"))
        self.horizontalLayout_L4X3.addWidget(self.label_L4X3)
	self.label_L4X3.setStyleSheet("Background-color:  rgb(0,155,255)")

	self.horizontalLayoutWidget_L4X3P = QtGui.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_L4X3P.setGeometry(QtCore.QRect(965, 614, 70,25))
        self.horizontalLayoutWidget_L4X3P.setObjectName(_fromUtf8("horizontalLayoutWidget_L4X3P"))
        self.horizontalLayout_L4X3P = QtGui.QHBoxLayout(self.horizontalLayoutWidget_L4X3P)
        self.horizontalLayout_L4X3P.setObjectName(_fromUtf8("horizontalLayout_L4X3P"))
        self.label_L4X3P = QtGui.QLabel(self.horizontalLayoutWidget_L4X3P)
	#self.label_L4X3P = QtGui.QLabel(self.centralwidget)
        self.label_L4X3P.setObjectName(_fromUtf8("Opcção L4X3P"))
	#self.label_L4X3P.setStyleSheet("Background-color:  rgb(0,155,255)")

	#definindo Qbox Opcoes Sensor L4x3F
	self.horizontalLayoutWidget_B4X2P = QtGui.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_B4X2P.setGeometry(QtCore.QRect(955, 635, 141,55))
        self.horizontalLayoutWidget_B4X2P.setObjectName(_fromUtf8("horizontalLayoutWidget_B4X2P"))
        self.horizontalLayout_B4X2P = QtGui.QHBoxLayout(self.horizontalLayoutWidget_B4X2P)
        self.horizontalLayout_B4X2P.setObjectName(_fromUtf8("horizontalLayout_B4X2P"))
        self.opcoes_B4X2P = QtGui.QComboBox(self.horizontalLayoutWidget_B4X2P)
        self.horizontalLayout_B4X2P.addWidget(self.opcoes_B4X2P)
        self.opcoes_B4X2P.setObjectName(_fromUtf8("opcoes_B4X2P"))
        self.opcoes_B4X2P.addItem(_fromUtf8("Concentrado"))
        self.opcoes_B4X2P.addItem(_fromUtf8("F1"))
        self.opcoes_B4X2P.addItem(_fromUtf8("F2"))
        self.opcoes_B4X2P.addItem(_fromUtf8("F3"))
        self.opcoes_B4X2P.addItem(_fromUtf8("F4"))
        self.opcoes_B4X2P.addItem(_fromUtf8("F5"))
        self.opcoes_B4X2P.addItem(_fromUtf8("F6"))
        self.opcoes_B4X2P.addItem(_fromUtf8("F7"))
        self.opcoes_B4X2P.addItem(_fromUtf8("F8"))
        self.opcoes_B4X2P.addItem(_fromUtf8("F9"))
        self.opcoes_B4X2P.addItem(_fromUtf8("F10"))
        self.opcoes_B4X2P.addItem(_fromUtf8("F11"))
        self.opcoes_B4X2P.addItem(_fromUtf8("F12"))
        self.opcoes_B4X2P.addItem(_fromUtf8("F13"))
        self.opcoes_B4X2P.addItem(_fromUtf8("F14"))
        self.opcoes_B4X2P.addItem(_fromUtf8("F15"))
        self.opcoes_B4X2P.addItem(_fromUtf8("F16"))
        self.opcoes_B4X2P.addItem(_fromUtf8("F17"))
	self.opcoes_B4X2P.setStyleSheet("Background-color:  rgb(0,155,255)")

	#definindo botao1 L4X3 B1
	self.horizontalLayoutWidget_L4X3Button1 = QtGui.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_L4X3Button1.setGeometry(QtCore.QRect(1095, 628, 130, 61))
        self.horizontalLayoutWidget_L4X3Button1.setObjectName(_fromUtf8("horizontalLayoutWidget_L4X3Button1"))
        self.horizontalLayout_L4X3Button1 = QtGui.QHBoxLayout(self.horizontalLayoutWidget_L4X3Button1)
        self.horizontalLayout_L4X3Button1.setObjectName(_fromUtf8("horizontalLayout_L4X3Button1"))
        self.operacao_L4X3Button1 = QtGui.QPushButton(self.horizontalLayoutWidget_L4X3Button1)
        self.operacao_L4X3Button1.setObjectName(_fromUtf8("operacao_L4X3Button1"))
        self.horizontalLayout_L4X3Button1.addWidget(self.operacao_L4X3Button1)
	self.operacao_L4X3Button1.setStyleSheet("Background-color:  rgb(0,155,255)")

	#definindo botao1 L4X3 B2
	self.horizontalLayoutWidget_L4X3Button2= QtGui.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_L4X3Button2.setGeometry(QtCore.QRect(1225, 628, 130, 61))
        self.horizontalLayoutWidget_L4X3Button2.setObjectName(_fromUtf8("horizontalLayoutWidget_L4X3Button2"))
        self.horizontalLayout_L4X3Button2= QtGui.QHBoxLayout(self.horizontalLayoutWidget_L4X3Button2)
        self.horizontalLayout_L4X3Button2.setObjectName(_fromUtf8("horizontalLayout_L4X3Button2"))
        self.operacao_L4X3Button2 = QtGui.QPushButton(self.horizontalLayoutWidget_L4X3Button2)
        self.operacao_L4X3Button2.setObjectName(_fromUtf8("operacao_L4X3Button2"))
        self.horizontalLayout_L4X3Button2.addWidget(self.operacao_L4X3Button2)
	self.operacao_L4X3Button2.setStyleSheet("Background-color:  rgb(0,155,255)")
#...................................................................................................................................................................................................................
	#Add Label Linha 4x5 (Solicitacao status)
	self.horizontalLayoutWidget_L4X5 = QtGui.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_L4X5.setGeometry(QtCore.QRect(955, 675, 200 ,71))
        self.horizontalLayoutWidget_L4X5.setObjectName(_fromUtf8("horizontalLayoutWidget_L4X5"))
        self.horizontalLayout_L4X5 = QtGui.QHBoxLayout(self.horizontalLayoutWidget_L4X5)
        self.horizontalLayout_L4X5.setObjectName(_fromUtf8("horizontalLayout_L4X5"))	
        self.label_L4X5 = QtGui.QLabel(self.horizontalLayoutWidget_L4X5)
        self.label_L4X5.setObjectName(_fromUtf8("Opção L4X5"))
        self.horizontalLayout_L4X5.addWidget(self.label_L4X5)
	self.label_L4X5.setStyleSheet("Background-color:  rgb(0,155,255)")

	#definindo botao1 L4X5 B1
	self.horizontalLayoutWidget_L4X5Button1 = QtGui.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_L4X5Button1.setGeometry(QtCore.QRect(985, 738, 130, 55))
        self.horizontalLayoutWidget_L4X5Button1.setObjectName(_fromUtf8("horizontalLayoutWidget_L4X5Button1"))
        self.horizontalLayout_L4X5Button1 = QtGui.QHBoxLayout(self.horizontalLayoutWidget_L4X5Button1)
        self.horizontalLayout_L4X5Button1.setObjectName(_fromUtf8("horizontalLayout_L4X5Button1"))
        self.operacao_L4X5Button1 = QtGui.QPushButton(self.horizontalLayoutWidget_L4X5Button1)
        self.operacao_L4X5Button1.setObjectName(_fromUtf8("operacao_L4X5Button1"))
        self.horizontalLayout_L4X5Button1.addWidget(self.operacao_L4X5Button1)
	self.operacao_L4X5Button1.setStyleSheet("Background-color:  rgb(0,155,255)")
#...................................................................................................................................................................................................................
	#Add Label Linha 4x6 (Solicitacao status)
	self.horizontalLayoutWidget_L4X6 = QtGui.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_L4X6.setGeometry(QtCore.QRect(1155, 675, 200 ,71))
        self.horizontalLayoutWidget_L4X6.setObjectName(_fromUtf8("horizontalLayoutWidget_L4X6"))
        self.horizontalLayout_L4X6 = QtGui.QHBoxLayout(self.horizontalLayoutWidget_L4X6)
        self.horizontalLayout_L4X6.setObjectName(_fromUtf8("horizontalLayout_L4X6"))	
        self.label_L4X6 = QtGui.QLabel(self.horizontalLayoutWidget_L4X6)
        self.label_L4X6.setObjectName(_fromUtf8("Opção L4X6"))
        self.horizontalLayout_L4X6.addWidget(self.label_L4X6)
	self.label_L4X6.setStyleSheet("Background-color:  rgb(0,155,255)")

	#definindo botao1 L4X6 B1
	self.horizontalLayoutWidget_L4X6Button1 = QtGui.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_L4X6Button1.setGeometry(QtCore.QRect(1185, 738, 130, 55))
        self.horizontalLayoutWidget_L4X6Button1.setObjectName(_fromUtf8("horizontalLayoutWidget_L4X6Button1"))
        self.horizontalLayout_L4X6Button1 = QtGui.QHBoxLayout(self.horizontalLayoutWidget_L4X6Button1)
        self.horizontalLayout_L4X6Button1.setObjectName(_fromUtf8("horizontalLayout_L4X6Button1"))
        self.operacao_L4X6Button1 = QtGui.QPushButton(self.horizontalLayoutWidget_L4X6Button1)
        self.operacao_L4X6Button1.setObjectName(_fromUtf8("operacao_L4X6Button1"))
        self.horizontalLayout_L4X6Button1.addWidget(self.operacao_L4X6Button1)
	self.operacao_L4X6Button1.setStyleSheet("Background-color:  rgb(0,155,255)")
#...................................................................................................................................................................................................................
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
#...................................................................................................................................................................................................................	
	self.label_L1.setText(_translate("Tela", " Teste Solicitação Start e Stop :", None))
	self.operacao_L1Button.setText(_translate("Tela", "Testar", None))
	self.label_L1End.setText(_translate("Tela", "Endereço", None))
	self.label_L1O.setText(_translate("Tela", "Operação", None))
	self.label_L1S.setText(_translate("Tela", "Sensor", None))
#...................................................................................................................................................................................................................
	self.label_L2.setText(_translate("Tela", " Teste Frequencia de Cor:", None))
	self.operacao_L2ButtonCU.setText(_translate("Tela", "Cor Unitaria", None))
	self.operacao_L2ButtonCL.setText(_translate("Tela", "Cor em Lote", None))
	self.operacao_L2ButtonTC.setText(_translate("Tela", "Todas Cores", None))
	self.operacao_L2ButtonTCL.setText(_translate("Tela", "Todas Cores em Lote", None))
	self.label_L2S.setText(_translate("Tela", "Sensor", None))
	self.label_L2C.setText(_translate("Tela", "Cor", None))
#...................................................................................................................................................................................................................
	self.label_L3.setText(_translate("Tela", " Teste Frequencia de Cor:", None))
	self.operacao_L3Button.setText(_translate("Tela", "Testar:", None))
	self.label_L3C.setText(_translate("Tela", "Comandos:", None))
	self.label_L3IS.setText(_translate("Tela", "Intervalo em \n   Segundos:", None))
#...................................................................................................................................................................................................................
	self.label_L4X1.setText(_translate("Tela", " Teste Calibracao:", None))
	self.label_L4X1S.setText(_translate("Tela", "Sensores:", None))
	self.label_L4X1C.setText(_translate("Tela", "Cores:", None))
	self.label_L4X1IS.setText(_translate("Tela", "Valor Calibracao:", None))
	self.operacao_L4X1Button1.setText(_translate("Tela", "Consultar:", None))
	self.operacao_L4X1Button2.setText(_translate("Tela", "Alterar:", None))
#...................................................................................................................................................................................................................
	self.label_L4X2.setText(_translate("Tela", " Teste Calibracao:", None))
	self.label_L4X2S.setText(_translate("Tela", "Sensores:", None))
	self.label_L4X3Sens.setText(_translate("Tela", "% Sensibilidade:", None))
	self.operacao_L4X4Button1.setText(_translate("Tela", "Consultar:", None))
	self.operacao_L4X4Button2.setText(_translate("Tela", "Alterar:", None))
	
#...................................................................................................................................................................................................................
	self.label_L4X3.setText(_translate("Tela", " Teste Firmware filete e concentrador:", None))
	self.label_L4X3P.setText(_translate("Tela", "Placa:", None))
	self.operacao_L4X3Button1.setText(_translate("Tela", "Placa Selec.", None))
	self.operacao_L4X3Button2.setText(_translate("Tela", "Todas Placas", None))
#...................................................................................................................................................................................................................
	self.label_L4X5.setText(_translate("Tela", " Teste Status Solicitacao\n        Todos Sensores", None))
	self.operacao_L4X5Button1.setText(_translate("Tela", "Testar", None))
#...................................................................................................................................................................................................................
	self.label_L4X6.setText(_translate("Tela", "   Teste Porta Aberta\n    Agitacao Revercao", None))
	self.operacao_L4X6Button1.setText(_translate("Tela", "Testar", None))


