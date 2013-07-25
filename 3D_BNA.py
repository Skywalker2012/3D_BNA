#!/usr/bin/env python

import sys
import math

from PyQt4 import QtCore, QtGui, QtOpenGL

try:
    from OpenGL.GL import *
except ImportError:
    app = QtGui.QApplication(sys.argv)
    QtGui.QMessageBox.critical(None, '3D Brain Network Analysis',
	    'PyOpenGL must be installed to run this programme.')
    sys.exit(1)

class GLWidget(QtOpenGL.QGLWidget):

    def __init__(self, parent = None):
	super(GLWidget, self).__init__(parent)

    def initializeGL(self):
	lightPos = (5.0, 5.0, 10.0, 1.0)

	glLightfv(GL_LIGHT0, GL_POSITION, lightPos)
	glEnable(GL_LIGHTING)
	glEnable(GL_LIGHT0)
	glEnable(GL_DEPTH_TEST)

	glEnable(GL_NORMALIZE)
	glClearColor(0.0, 0.0, 0.0, 1.0)

    def paintGL(self):
	glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    def resizeGL(self, width, height):
	side = min(width, height)
	if side < 0:
	    return
	
    def mousePressEvent(self, event):
	pass

    def mouseMoveEvent(self, event):
	pass


class MainWindow(QtGui.QMainWindow):
    def __init__(self):
	super(MainWindow, self).__init__()

	centralWidget = QtGui.QWidget()
	self.setCentralWidget(centralWidget)

	self.glWidget = GLWidget()
	
	self.glWidgetArea = QtGui.QScrollArea()
	self.glWidgetArea.setWidget(self.glWidget)
	self.glWidgetArea.setWidgetResizable(True)
	self.glWidgetArea.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
	self.glWidgetArea.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
	self.glWidgetArea.setSizePolicy(QtGui.QSizePolicy.Ignored, 
		QtGui.QSizePolicy.Ignored)
	self.glWidgetArea.setMinimumSize(50,50)

	self.createActions()
        self.createMenus()

        centralLayout = QtGui.QGridLayout()
        centralLayout.addWidget(self.glWidgetArea, 0, 0)
        centralWidget.setLayout(centralLayout)

	self.setWindowTitle("3D Brain Network Analysis Tool")
        self.resize(400, 300)

    def about(self):
        QtGui.QMessageBox.about(self, "About 3D Brain Network Analysis Tool",
                "The <b>3D Brain Network Analysis Tool</b> is developed by Gushu Li, "
		"from NICS Lab in E.E. Dept at Tsinghua University. "
		"If you find any problem, "
		"please email me at <b>lgs930420@gmail.com</b>.")


    def createActions(self):
	self.exitAct = QtGui.QAction('Exit', self, shortcut = 'Ctrl+Q', 
		triggered = self.close)

	self.aboutAct = QtGui.QAction("&About", self, triggered=self.about)

        self.aboutQtAct = QtGui.QAction("About &Qt", self,
                triggered=QtGui.qApp.aboutQt)
	
    def createMenus(self):
	self.fileMenu = self.menuBar().addMenu('&File')
	self.fileMenu.addSeparator()
	self.fileMenu.addAction(self.exitAct)

	self.helpMenu = self.menuBar().addMenu("&Help")
        self.helpMenu.addAction(self.aboutAct)
	self.helpMenu.addSeparator()
        self.helpMenu.addAction(self.aboutQtAct)

if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()
    sys.exit(app.exec_())
