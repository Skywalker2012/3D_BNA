#Created by Gushu Li on 2013/7/30

from OpenGL.GL import *

class RenderableObject():
	def __init__(self):
		self.vertexNum = 0
		self.vertexList = []
		self.triangleNum = 0
		self.triangleList = []
		self.textureNum = None

	def Render(self):
		i = 0
		while (i<self.triangleNum * 3):
			glBegin(GL_TRIANGLES)
			glVertex3f(self.vertexList[self.triangleList[i]*3],
					self.vertexList[self.triangleList[i]*3+1],
					self.vertexList[self.triangleList[i]*3+2])
			glVertex3f(self.vertexList[self.triangleList[i+1]*3],
					self.vertexList[self.triangleList[i+1]*3+1],
					self.vertexList[self.triangleList[i+1]*3+2])
			glVertex3f(self.vertexList[self.triangleList[i+2]*3],
					self.vertexList[self.triangleList[i+2]*3+1],
					self.vertexList[self.triangleList[i+2]*3+2])
			glEnd()
			i += 3
