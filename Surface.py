#Created by Gushu Li on 2013/7/30

from RenderObject import *
from OpenGL.GLU import *
class Surface(RenderableObject):
	def __init__(self):
		self.vertexNum = 0
		self.vertexList = []
		self.triangleNum = 0
		self.triangleList = []
		self.textureNum = None
		self.x = 130

	def LoadIn(self,fileName):
		self.surfaceFile = open(fileName)

		line = self.surfaceFile.readline()
		self.vertexNum = int(line,10)

		self.vertexList = []
		for i in xrange(self.vertexNum):
			line = self.surfaceFile.readline()
			templist = line.split()
			for j in xrange(3):
				self.vertexList.append( float(templist[j]) )

		line = self.surfaceFile.readline()
		self.triangleNum = int(line,10)

		self.triangleList = []
		for i in xrange(self.triangleNum):
			line = self.surfaceFile.readline()
			templist = line.split()
			for j in xrange(3):
				self.triangleList.append(int(templist[j],10)-1)
				#print self.triangleList[i*3 + j]

		glNewList(1,GL_COMPILE)
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
		glEndList()

	def Render(self):
		glLoadIdentity()
		gluLookAt(self.x, 130.0, 10.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0);
		glCallList(1)

		self.x +=1
	
