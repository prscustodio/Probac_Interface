#testes iniciais com pyqt - Paulo Custodio
import sys
from PyQt4 import QtCore, QtGui
from edytor import Ui_notepad

class StartQT4(QtGui.QMainWindow): 
	
	def __init__(self, parent=None):
		QtGui.QWidget.__init__(self, parent)
		self.ui = Ui_notepad()
		self.ui.setupUi(self)
# here we connect signals with our slots
		QtCore.QObject.connect(self.ui.button_open,QtCore.SIGNAL("clicked()"), self.file_dialog)
		QtCore.QObject.connect(self.ui.save_button,QtCore.SIGNAL("clicked()"), self.file_save)

	def file_dialog(self):
		fd = QtGui.QFileDialog(self)
		self.filename = fd.getOpenFileName()
		from os.path import isfile
		if isfile(self.filename):
			import codecs
			s = codecs.open(self.filename,'r','utf-8').read()
			self.ui.editor_window.setPlainText(s)

	def file_save(self):
		from os.path import isfile
		if isfile(self.filename):
			file = open(self.filename, 'w')
			file.write(self.ui.editor_window.toPlainText())
			file.close()

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    myapp = StartQT4()
    myapp.show()
    sys.exit(app.exec_())
