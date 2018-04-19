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
			bytes='a'
			self.square1.setStyleSheet("QWidget { background-color: %s }" %  self.colB.name())
			self.square2.setStyleSheet("QWidget { background-color: %s }" %  self.colB.name())
			self.square3.setStyleSheet("QWidget { background-color: %s }" %  self.colB.name())
			ser.write(bytes)
			ser.write(dadoVarredura)
			print dadoVarredura
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
				#lcdi2c.lcd_clear()
				#lcdi2c.lcd_display_string(texto_varredura, 1,1)
				GPIO.output(18,GPIO.LOW)
				time.sleep(1)	
				GPIO.output(18,GPIO.HIGH)	

		#controle eventos botao concentrado
		def file_dialog_concentrado(self):
			fd = QtGui.QFileDialog(self)
			dadoConcentrado = 'c'
			bytes='a'
			ser.write(bytes)
			ser.write(dadoConcentrado)
			print dadoConcentrado
			self.square1.setStyleSheet("QWidget { background-color: %s }" %  self.colB.name())
			self.square2.setStyleSheet("QWidget { background-color: %s }" %  self.colR.name())
			self.square3.setStyleSheet("QWidget { background-color: %s }" %  self.colB.name())
			file_concentrado = open('/home/pi/Desktop/Probac_Interface/testeConcentrado.txt','r')
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
				#lcdi2c.lcd_clear()
				#lcdi2c.lcd_display_string(texto_concentrado, 1,1)
				GPIO.output(18,GPIO.LOW)
				time.sleep(1)
				GPIO.output(18,GPIO.HIGH)

		#controle eventos botao varredura
		def file_dialog_filete(self):
			fd = QtGui.QFileDialog(self)
			dadoFilete='f'
			bytes='a'
			ser.write(bytes)
			ser.write(dadoFilete)
			print(dadoFilete)
			self.square1.setStyleSheet("QWidget { background-color: %s }" %  self.colB.name())
			self.square2.setStyleSheet("QWidget { background-color: %s }" %  self.colB.name())
			self.square3.setStyleSheet("QWidget { background-color: %s }" %  self.colB.name())
			#time.sleep(0.5)	
			file_filete = open('/home/pi/Desktop/Probac_Interface/testeFilete.txt','r')
			texto_filete=file_filete.read()
			#print(texto_filete)
			var_filete=ser.readline(2)
			print(var_filete)
			if(var_filete==ra):
				print ('ok')	
				self.square1.setStyleSheet("QWidget { background-color: %s }" %  self.colG.name())
				self.square2.setStyleSheet("QWidget { background-color: %s }" %  self.colB.name())
				self.square3.setStyleSheet("QWidget { background-color: %s }" %  self.colB.name())
				self.ui.editor_window.setText(texto_filete) 
				#lcdi2c.lcd_clear()
				#lcdi2c.lcd_display_string(texto_filete, 1,1)
				GPIO.output(18,GPIO.LOW)
				time.sleep(1)
				GPIO.output(18,GPIO.HIGH)
		
		def file_dialog_operacao(self):
			fd = QtGui.QFileDialog(self)

			endereco=self.ui.opcoes1.currentText()
			if (endereco=='None'):
				 endereco='n'
			if (endereco=='F1'):
			 	endereco=0x01
			if (endereco=='F2'):
			 	endereco=2

			sensor1=self.ui.opcoes2.currentText()
			if (sensor1=='None'):
				 sensor1='n'
			if (sensor1=='Pause'):
			 	sensor1='B'
			if (sensor1=='Start'):
				 sensor1=0x05
			if (sensor1=='Status'):
			 	sensor1=0x00
			if (sensor1=='Stop'):
				 sensor1=0x03
			if (sensor1=='Leitura'):
				 sensor1=12

			sensor2=self.ui.opcoes3.currentText()
			if (sensor2=='None'):
				 sensor2='n'
			if (sensor2=='Pause'):
			 	sensor2='B'
			if (sensor2=='Start'):
			 	sensor2=0x05
			if (sensor2=='Status'):
			 	sensor2=0x00
			if (sensor2=='Stop'):
			 	sensor2=0x03
			if (sensor2=='Leitura'):
				 sensor2=12

			sensor3=self.ui.opcoes4.currentText()
			if (sensor3=='None'):
			 	sensor3='n'
			if (sensor3=='Pause'):
			 	sensor3='B'
			if (sensor3=='Start'):
			 	sensor3=0x05
			if (sensor3=='Status'):
			 	sensor3=0x00
			if (sensor3=='Stop'):
			 	sensor3=0x03
			if (sensor3=='Leitura'):
				 sensor3=12

			sensor4=self.ui.opcoes5.currentText()
			if (sensor4=='None'):
			 	sensor4='n'
			if (sensor4=='Pause'):
			 	sensor4='B'
			if (sensor4=='Start'):
			 	sensor4=0x05
			if (sensor4=='Status'):
			 	sensor4=0x00
			if (sensor4=='Stop'):
			 	sensor4=0x03
			if (sensor4=='Leitura'):
				 sensor4=12

			sensor5=self.ui.opcoes6.currentText()
			if (sensor5=='None'):
				 sensor5='n'
			if (sensor5=='Pause'):
			 	sensor5='B'
			if (sensor5=='Start'):
				 sensor5=0x05
			if (sensor5=='Status'):
				 sensor5=0x00
			if (sensor5=='Stop'):
				 sensor5=0x03
			if (sensor5=='Leitura'):
				 sensor5=0x0C
	
			bytes='b'
			PackSensor = ['A','F',endereco,'S',1,sensor1,'S',2,sensor2,'S',3,sensor3,'S',4,sensor4,'S',5,sensor5]
			print PackSensor
			ser.write(bytes)
			ser.write(PackSensor)
			if ((sensor1==0x00) or (sensor2==0x00) or (sensor3==0x00) or (sensor4==0x00) or (sensor5==0x00 )):
				print ("entrou")
				leitura_filete=ser.readline(3)	
				self.ui.editor_window.setText(leitura_filete) 		
			if ((sensor1==12) or (sensor2==12) or (sensor3==12) or (sensor4==12) or (sensor5==12 )):
				print ("entrou")
				leitura_filete=ser.readline()	
				self.ui.editor_window.setText(leitura_filete) 	
			#var_filete=ser.readline(2)
			#print(var_filete)
			#if(var_filete=="rd"):
			#	print ('ok')	

			
if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    myapp = StartQT4()
    myapp.show()
    sys.exit(app.exec_())
