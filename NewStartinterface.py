#testes iniciais com pyqt - Paulo Custodio
import sys
from PyQt4 import QtCore, QtGui
from Interface import Ui_Tela
import serial
import RPi.GPIO as GPIO
import time
#import I2C_LCD_driver
import socket
import fcntl
import struct

ra='ra'
rb='rb'
rc='rc'

#lcdi2c = I2C_LCD_driver.lcd()

GPIO.setmode(GPIO.BCM)
#GPIO.setwarnigs(False)
GPIO.setup(18,GPIO.OUT)
GPIO.output(18,GPIO.HIGH)

ser =serial.Serial('/dev/ttyACM0',9600)

class StartQT4(QtGui.QMainWindow): 
	
		def __init__(self, parent=None):
			QtGui.QWidget.__init__(self, parent)
			self.ui = Ui_Tela()
			self.ui.setupUi(self)
			
			# here we connect signals with our slots
			QtCore.QObject.connect(self.ui.operacao_L1Button,QtCore.SIGNAL("clicked()"), self.file_dialog_L1_Testar)
			QtCore.QObject.connect(self.ui.operacao_L2ButtonCU,QtCore.SIGNAL("clicked()"), self.file_dialog_L2_CU)
			QtCore.QObject.connect(self.ui.operacao_L2ButtonCL,QtCore.SIGNAL("clicked()"),self.file_dialog_L2_CL)
			QtCore.QObject.connect(self.ui.operacao_L2ButtonTC,QtCore.SIGNAL("clicked()"), self.file_dialog_L2_TC)
			QtCore.QObject.connect(self.ui.operacao_L2ButtonTCL,QtCore.SIGNAL("clicked()"), self.file_dialog_L2_TCL)
			QtCore.QObject.connect(self.ui.operacao_L3Button,QtCore.SIGNAL("clicked()"), self.file_dialog_L3_Testar)
			QtCore.QObject.connect(self.ui.operacao_L4X1Button1,QtCore.SIGNAL("clicked()"), self.file_dialog_L4X1_Consultar)
			QtCore.QObject.connect(self.ui.operacao_L4X1Button2,QtCore.SIGNAL("clicked()"), self.file_dialog_L4X1_Alterar)
			QtCore.QObject.connect(self.ui.operacao_L4X4Button1,QtCore.SIGNAL("clicked()"), self.file_dialog_L4X4_Consultar)
			QtCore.QObject.connect(self.ui.operacao_L4X4Button2,QtCore.SIGNAL("clicked()"), self.file_dialog_L4X4_Alterar)
			QtCore.QObject.connect(self.ui.operacao_L4X3Button1,QtCore.SIGNAL("clicked()"), self.file_dialog_L4X3_PS)
			QtCore.QObject.connect(self.ui.operacao_L4X3Button2,QtCore.SIGNAL("clicked()"), self.file_dialog_L4X3_TP)
			QtCore.QObject.connect(self.ui.operacao_L4X5Button1,QtCore.SIGNAL("clicked()"), self.file_dialog_L4X5_Testar)
			QtCore.QObject.connect(self.ui.operacao_L4X6Button1,QtCore.SIGNAL("clicked()"), self.file_dialog_L4X6_Testar)
			QtCore.QObject.connect(self.ui.close_button,QtCore.SIGNAL("clicked()"), self.close)

			#definindo quadrados
			self.colR= QtGui.QColor(255, 0, 0)
			self.colB= QtGui.QColor(0, 0, 0)
			self.colG= QtGui.QColor(0, 255, 0)

			self.square1 = QtGui.QFrame(self)
			self.square1.setGeometry(150, 125, 20, 20)
			self.square1.setStyleSheet("QWidget { background-color: %s }" %  self.colB.name())

			self.square2 = QtGui.QFrame(self)
			self.square2.setGeometry(420, 125, 20, 20)
			self.square2.setStyleSheet("QWidget { background-color: %s }" % self.colB.name())

			self.square3 = QtGui.QFrame(self)
			self.square3.setGeometry(680, 125, 20, 20)
			self.square3.setStyleSheet("QWidget { background-color: %s }" %  self.colB.name())
			#print self.ui.opcoes1.currentText()

		
		def file_dialog_L1_Testar(self):
			fd = QtGui.QFileDialog(self)
			endereco=self.ui.opcoes_B1End.currentText()
			sensor=self.ui.opcoes_B1S.currentText()
			operacao=self.ui.opcoes_B1O.currentText()
			print endereco
			print sensor
			print operacao

			#sensor
			if (sensor=='None'):
				 sensor='n'
			if (sensor=='S1'):
			 	sensor=0x04
			if (sensor=='S2'):
				 sensor=0x08
			if (sensor=='S3'):
				 sensor=0x12
			if (sensor=='S4'):
				 sensor=0x20
			if (sensor=='S5'):
				 sensor=0x40

			#operacao
			if (operacao=='None'):
				 operacao='n'
			if (operacao=='Pause'):
			 	operacao='B'
			if (operacao=='Start'):
				 operacao=0x05
			if (operacao=='Status'):
			 	operacao=0x00
			if (operacao=='Stop'):
				 operacao=0x03
			if (operacao=='Leitura'):
				 operacao=12

			#filete
			if (endereco=='None'):
				 endereco='n'
			if (endereco=='F1'):
			 	endereco=0x01
			if (endereco=='F2'):
				 endereco=0x02
			if (endereco=='F3'):
				 endereco=0x03
			if (endereco=='F4'):
				 endereco=0x04
			if (endereco=='F5'):
				 endereco=0x05

			#bytes='b'
			print operacao
			PackSensor = [endereco,sensor,operacao]
			print PackSensor
			#ser.write(struct.pack('>B',PackSensor))
			ser.write(PackSensor)
			#print(var_filete)
			#if(var_filete=="rd"):
			#	print ('ok')'''	

		def file_dialog_L2_CU(self):
			fd = QtGui.QFileDialog(self)
			cor=self.ui.opcoes_B2C.currentText()
			sensor=self.ui.opcoes_B2S.currentText()
			print cor
			print sensor 

		def file_dialog_L2_CL(self):
			fd = QtGui.QFileDialog(self)
			cor=self.ui.opcoes_B2C.currentText()
			sensor=self.ui.opcoes_B2S.currentText()			
			print cor
			print sensor 

		def file_dialog_L2_TC(self):
			fd = QtGui.QFileDialog(self)
			cor=self.ui.opcoes_B2C.currentText()
			sensor=self.ui.opcoes_B2S.currentText()
			print cor
			print sensor

		def file_dialog_L2_TCL(self):
			fd = QtGui.QFileDialog(self)
			cor=self.ui.opcoes_B2C.currentText()
			sensor=self.ui.opcoes_B2S.currentText()
			print cor
			print sensor

		def file_dialog_L3_Testar(self):
			fd = QtGui.QFileDialog(self)
			comando=self.ui.opcoes_B3C.currentText()
			intervalo=self.ui.editor_window_T3IS.toPlainText()
			print intervalo
			print comando 				

		def file_dialog_L4X1_Consultar(self):
			fd = QtGui.QFileDialog(self)
			sensor=self.ui.opcoes_B4X1S.currentText()
			cores=self.ui.opcoes_B4X1C.currentText()
			valorCalib=self.ui.editor_window_T4X1IS.toPlainText()
			print sensor
			print cores
			print valorCalib

		def file_dialog_L4X1_Alterar(self):
			fd = QtGui.QFileDialog(self)
			sensor=self.ui.opcoes_B4X1S.currentText()
			cores=self.ui.opcoes_B4X1C.currentText()
			valorCalib=self.ui.editor_window_T4X1IS.toPlainText()
			print sensor
			print cores
			print valorCalib

		def file_dialog_L4X4_Consultar(self):
			fd = QtGui.QFileDialog(self)
			sensor=self.ui.opcoes_B4X2S.currentText()
			sensibilidade=self.ui.spinBox4X2.value()
			print sensor
			print sensibilidade

		def file_dialog_L4X4_Alterar(self):
			fd = QtGui.QFileDialog(self)
			sensor=self.ui.opcoes_B4X2S.currentText()
			sensibilidade=self.ui.spinBox4X2.value()
			print sensor
			print sensibilidade

		def file_dialog_L4X3_PS(self):
			fd = QtGui.QFileDialog(self)
			placa=self.ui.opcoes_B4X2P.currentText()
			print placa

		def file_dialog_L4X3_TP(self):
			fd = QtGui.QFileDialog(self)
			placa=self.ui.opcoes_B4X2P.currentText()
			print placa

		def file_dialog_L4X5_Testar(self):
			fd = QtGui.QFileDialog(self)
		

		def file_dialog_L4X6_Testar(self):
			fd = QtGui.QFileDialog(self)


			
if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    myapp = StartQT4()
    myapp.show()
    sys.exit(app.exec_())
