#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
ZetCode PyQt4 tutorial 

In this example, we create three toggle buttons.
They will control the background color of a 
QtGui.QFrame. 

author: Jan Bodnar
website: zetcode.com 
last edited: September 2011
"""

import sys
from PyQt4 import QtGui

class Example(QtGui.QWidget):
    
    def __init__(self):
        super(Example, self).__init__()
        
        self.initUI()
        
        
    def initUI(self):      
	#define tamanho e posicao em que janela inicia
	self.setGeometry(0, 0, 900, 900)
        self.setWindowTitle('Interface Estufa')

	#configuracao text editor
	#self.textfield=QtGui.TextEdit()
	#self.textfield.resize(400,500)
        
	#cor do quadrado de indicacao
	self.col = QtGui.QColor(255, 0, 0)
       
	#definindo botoes
        fileteb = QtGui.QPushButton('Filete', self)
        fileteb.setCheckable(True)
        fileteb.move(10, 10)

      #  fileteb.clicked[bool].connect(self.setColor)

        concentradob = QtGui.QPushButton('Concentrado', self)
        concentradob.setCheckable(True)
        concentradob.move(300, 10)

      #  concentradob.clicked[bool].connect(self.setColor)

        varredurab = QtGui.QPushButton('Varredura', self)
        varredurab.setCheckable(True)
        varredurab.move(600, 10)

        #varredurab.clicked[bool].connect(self.setColor)

	#definindo quadrados
        self.square1 = QtGui.QFrame(self)
        self.square1.setGeometry(10, 50, 20, 20)
        self.square1.setStyleSheet("QWidget { background-color: %s }" %  
            self.col.name())

	self.square2 = QtGui.QFrame(self)
        self.square2.setGeometry(300, 50, 20, 20)
        self.square2.setStyleSheet("QWidget { background-color: %s }" %  
            self.col.name())

	self.square3 = QtGui.QFrame(self)
        self.square3.setGeometry(600, 50, 20, 20)
        #self.square3.setStyleSheet("QWidget { background-color: %s }" %  
           # self.col.name())

     
        self.show()
        
        
 
        
def main():
    
    app = QtGui.QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main() 
