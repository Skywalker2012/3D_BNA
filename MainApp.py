#!/usr/bin/env python
#By Gushu Li, E.E. Dept at Tsinghua University
#Created on 2013/7/30

import sys


from PyQt4 import QtCore
from MainWindow import *

try:
    from OpenGL.GL import *
except ImportError:
    app = QtGui.QApplication(sys.argv)
    QtGui.QMessageBox.critical(None, '3D Brain Network Analysis',
	    'PyOpenGL must be installed to run this programme.')
    sys.exit(1)

if __name__ == '__main__':
	app = QtGui.QApplication(sys.argv)
	mainWindow = MainWindow()
	mainWindow.show()
	sys.exit(app.exec_())
	
