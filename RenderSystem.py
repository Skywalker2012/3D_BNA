#Created by Gushu Li on 2013/7/30
from OpenGL.GL import *
from OpenGL.GLU import *

class RenderSystem():
	def __init__(self):
		pass

	def setRenderWidget(self, RenderWidget):
		self.renderWidget = RenderWidget
	
	def setSceneManager(self, SceneManager):
		self.sceneManager = SceneManager

	def WindowResized(self,width, height):
		side = min(width, height)
		if side < 0:
			return

		glViewport(0,0,width,height)
		glMatrixMode(GL_PROJECTION)
		glLoadIdentity()

		gluPerspective(54.0, float(width)/float(height),1.0,1000.0)

		glMatrixMode(GL_MODELVIEW)
		glLoadIdentity()

	def RenderOneFrame(self):
		glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
		self.sceneManager.rootNode.localObjectDict['Surface'].Render()
