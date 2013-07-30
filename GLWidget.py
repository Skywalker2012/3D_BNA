#Created by Gushu Li on 2013/7/30

from PyQt4 import QtOpenGL
from PyQt4 import QtCore
from OpenGL.GL import *

class GLWidget(QtOpenGL.QGLWidget):

	def __init__(self, parent = None):
		super(GLWidget, self).__init__(parent)

		timer = QtCore.QTimer(self)
		timer.timeout.connect(self.updateGL)
		timer.start(100)

	def addRenderSystem(self, rendersystem):
		self.renderSystem = rendersystem

	def initializeGL(self):
		glClearColor(0.0, 0.0, 0.0, 1.0)

	def paintGL(self):
		self.renderSystem.RenderOneFrame()

	def resizeGL(self, width, height):
		self.renderSystem.WindowResized(width, height)

	def mousePressEvent(self, event):
		pass

	def mouseMoveEvent(self, event):
		pass
