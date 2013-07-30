#Created by Gushu Li on 2013/7/30

from PyQt4 import QtCore, QtGui
from GLWidget import *
from RenderSystem import *
from SourceManager import *
from SceneManager import *
from Surface import *

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
		self.resize(800, 600)

		self.renderSystem = RenderSystem()
		self.sourceManager = SourceManager()
		self.sceneManager = SceneManager()
		self.renderSystem.setRenderWidget(self.glWidget)
		self.renderSystem.setSceneManager(self.sceneManager)
		self.sceneManager.addSource(self.sourceManager)

		self.glWidget.addRenderSystem(self.renderSystem)
	def loadFile(self):
		fileName = QtGui.QFileDialog.getOpenFileName(self,'Open file','./',
				'Surface Template(*.nv)')
		self.surface = Surface()
		self.surface.LoadIn(fileName)
		self.sceneManager.rootNode.localObjectDict['Surface'] = self.surface
		

	def about(self):
		QtGui.QMessageBox.about(self, "About 3D Brain Network Analysis Tool",
				"The <b>3D Brain Network Analysis Tool</b> is developed by Gushu Li, "
				"from NICS Lab in E.E. Dept at Tsinghua University. "
				"If you find any problem, "
				"please email me at <b>lgs930420@gmail.com</b>.")


	def grabFrameBuffer(self):
		image = self.glWidget.grabFrameBuffer()
		pixmap = QtGui.QPixmap.fromImage(image)
		filename = QtGui.QFileDialog.getSaveFileName(self,'Save file','./',
				'Image Files (*.png)')
		pixmap.save(filename)


	def createActions(self):
		self.loadAct = QtGui.QAction('Load', self, shortcut = 'Ctrl+L',
				triggered = self.loadFile)

		self.exitAct = QtGui.QAction('Exit', self, shortcut = 'Ctrl+Q',
				triggered = self.close)

		self.grabFrameBufferAct = QtGui.QAction('&Grab Frame Buffer', self,
				shortcut = 'Ctrl+G', triggered = self.grabFrameBuffer)

		self.aboutAct = QtGui.QAction("&About", self, triggered=self.about)

		self.aboutQtAct = QtGui.QAction("About &Qt", self,
				triggered=QtGui.qApp.aboutQt)


	def createMenus(self):
		self.fileMenu = self.menuBar().addMenu('&File')
		self.fileMenu.addAction(self.loadAct)
		self.fileMenu.addSeparator()
		self.fileMenu.addAction(self.exitAct)

		self.editMenu = self.menuBar().addMenu('&Edit')
		self.editMenu.addAction(self.grabFrameBufferAct)

		self.helpMenu = self.menuBar().addMenu("&Help")
		self.helpMenu.addAction(self.aboutAct)
		self.helpMenu.addSeparator()
		self.helpMenu.addAction(self.aboutQtAct)

