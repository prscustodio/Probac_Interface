#testes iniciais com pyqt - Paulo Custodio
import sys
from PyQt4 import QtCore, QtGui
from Interface import Ui_Tela
import serial

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

	def file_dialog_varredura(self):
		fd = QtGui.QFileDialog(self)
		ser.write('v')
		file_varredura = open('/home/pi/Desktop/varredura.txt','r')
		ser.readline()
		if(ser.readline()=='rc'):
			texto_varredura=file_varredura.read()
			self.ui.editor_window.setText(texto_varredura)
		

	def file_dialog_concentrado(self):
		fd = QtGui.QFileDialog(self)
		ser.write('c')
		file_concentrado = open('/home/pi/Desktop/testeConcentrado.txt','r')
		
		#while (ser.readline()!='rb'):
		print(ser.readline())
		if(ser.readline()=='rb'):		
			texto_concentrado=file_concentrado.read()
			self.ui.editor_window.setText(texto_concentrado)

	def file_dialog_filete(self):n
		fd = QtGui.QFileDialog(self)
		ser.write('f')
		
		file_filete = open('/home/pi/Desktop/testeFilete.txt','r')
		texto_filete=file_filete.read()
		confirm_filete=ser.readline()
		print(confirm_filete)
		if(confirm_filete=='ra'):
			texto_filete=file_filete.read()
			self.ui.editor_window.setText(texto_filete)
	

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    myapp = StartQT4()
    myapp.show()
    sys.exit(app.exec_())
