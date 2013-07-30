#Created by Gushu Li on 2013/7/30

from SceneNode import *

class SceneManager():
	def __init__(self):
		self.rootNode = SceneNode()

	def addSource(self, sourcemanager):
		self.rootNode.localObjectDict = sourcemanager.objectDict
