import os,sys
from PyQt4 import QtGui

app = QtGui.QApplication(sys.argv)
window = QtGui.QMainWindow()
window.setGeometry(0, 0, 400, 400)

pic = QtGui.QLabel(window)
pic.setGeometry(0, 0, 259, 194)
#use full ABSOLUTE path to the image, not relative
pic.setPixmap(QtGui.QPixmap("/home/pi/Desktop/Probac_Interface/download.jpg"))

window.show()
sys.exit(app.exec_())
