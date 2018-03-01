#testes iniciais com pyqt - Paulo Custodio
import sys
from PyQt4 import QtCore, QtGui
from Interface import Ui_Tela
import serial
import RPi.GPIO as GPIO
import time
import I2C_LCD_driver
import socket
import fcntl
import struct

ra='ra'
rb='rb'
rc='rc'

lcdi2c = I2C_LCD_driver.lcd()

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
			QtCore.QObject.connect(self.ui.varredura_button,QtCore.SIGNAL("clicked()"), self.file_dialog_varredura)
			QtCore.QObject.connect(self.ui.filete_button,QtCore.SIGNAL("clicked()"), self.file_dialog_filete)
			QtCore.QObject.connect(self.ui.concentrado_button,QtCore.SIGNAL("clicked()"), self.file_dialog_concentrado)
			QtCore.QObject.connect(self.ui.close_button,QtCore.SIGNAL("clicked()"), self.close)
			QtCore.QObject.connect(self.ui.operacao_button,QtCore.SIGNAL("clicked()"), self.file_dialog_operacao)

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

		#controle eventos botao varredura
		def file_dialog_varredura(self):
			fd = QtGui.QFileDialog(self)
			dadoVarredura='v'
			ser.write(dadoVarredura)
			print dadoVarredura
			self.square1.setStyleSheet("QWidget { background-color: %s }" %  self.colB.name())
			self.square2.setStyleSheet("QWidget { background-color: %s }" %  self.colB.name())
			self.square3.setStyleSheet("QWidget { background-color: %s }" %  self.colR.name())
			file_varredura = open('/home/pi/Desktop/Probac_Interface/varredura.txt','r')
			#time.sleep(0.5)
			varVarredura=ser.readline(2)
			print(varVarredura)
			if(varVarredura==rc):
				print ('ok')	
				self.square1.setStyleSheet("QWidget { background-color: %s }" %  self.colB.name())
				self.square2.setStyleSheet("QWidget { background-color: %s }" %  self.colB.name())
				self.square3.setStyleSheet("QWidget { background-color: %s }" %  self.colG.name())
				texto_varredura=file_varredura.read()
				self.ui.editor_window.setText(texto_varredura)
				lcdi2c.lcd_clear()
				lcdi2c.lcd_display_string(texto_varredura, 1,1)
				GPIO.output(18,GPIO.LOW)
				time.sleep(1)	
				GPIO.output(18,GPIO.HIGH)	

		#controle eventos botao concentrado
		def file_dialog_concentrado(self):
			fd = QtGui.QFileDialog(self)
			dadoConcentrado = 'c'
			ser.write(dadoConcentrado)
			print dadoConcentrado
			self.square1.setStyleSheet("QWidget { background-color: %s }" %  self.colB.name())
			self.square2.setStyleSheet("QWidget { background-color: %s }" %  self.colR.name())
			self.square3.setStyleSheet("QWidget { background-color: %s }" %  self.colB.name())
			file_concentrado = open('/home/pi/Desktop/Probac_Interface/testeFilete.txt','r')#open('/home/pi/Desktop/Probac_Interface/testeConcentrado.txt','r')
			#time.sleep(0.5)
			varConcentrado=ser.readline(2)
			print(varConcentrado)
			if(varConcentrado==rb):	
				print ('ok')	
				self.square1.setStyleSheet("QWidget { background-color: %s }" %  self.colB.name())
				self.square2.setStyleSheet("QWidget { background-color: %s }" %  self.colG.name())
				self.square3.setStyleSheet("QWidget { background-color: %s }" %  self.colB.name())
				texto_concentrado=file_concentrado.read()
				self.ui.editor_window.setText(texto_concentrado)
				lcdi2c.lcd_clear()
				lcdi2c.lcd_display_string(texto_concentrado, 1,1)
				GPIO.output(18,GPIO.LOW)
				time.sleep(1)
				GPIO.output(18,GPIO.HIGH)

		#controle eventos botao varredura
		def file_dialog_filete(self):
			fd = QtGui.QFileDialog(self)
			dadoFilete='f'
			ser.write(dadoFilete)
			print(dadoFilete)
			self.square1.setStyleSheet("QWidget { background-color: %s }" %  self.colR.name())
			self.square2.setStyleSheet("QWidget { background-color: %s }" %  self.colB.name())
			self.square3.setStyleSheet("QWidget { background-color: %s }" %  self.colB.name())
			#time.sleep(0.5)	
			file_filete = open('/home/pi/Desktop/Probac_Interface/testeConcentrado.txt','r')#open('/home/pi/Desktop/Probac_Interface/testeFilete.txt','r')
			texto_filete=file_filete.read()
			var_filete=ser.readline(2)
			print(var_filete)
			if(var_filete==ra):
				print ('ok')	
				self.square1.setStyleSheet("QWidget { background-color: %s }" %  self.colG.name())
				self.square2.setStyleSheet("QWidget { background-color: %s }" %  self.colB.name())
				self.square3.setStyleSheet("QWidget { background-color: %s }" %  self.colB.name())
				texto_filete=file_filete.readline()
				print texto_filete
				self.ui.editor_window.setText(texto_filete) 
				lcdi2c.lcd_clear()
				lcdi2c.lcd_display_string(texto_filete, 1,1)
				GPIO.output(18,GPIO.LOW)
				time.sleep(1)
				GPIO.output(18,GPIO.HIGH)
		
		def file_dialog_operacao(self):
			fd = QtGui.QFileDialog(self)
			sensor1=self.ui.opcoes1.currentText()
			sensor2=self.ui.opcoes2.currentText()
			sensor3=self.ui.opcoes3.currentText()
			sensor4=self.ui.opcoes4.currentText()
			sensor5=self.ui.opcoes5.currentText()
			print sensor1
			

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    myapp = StartQT4()
    myapp.show()
    sys.exit(app.exec_())
