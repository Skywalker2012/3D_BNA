#Created by Gushu Li on 2013/7/30

class SceneNode():
	def __init__(self):
		self.localMatrix = None
		self.childrenDict = {}
		self.localObjectDict = {}

	def addChildren(self, name, new_children):
		self.childrenDict[name] = new_children

	def addLocalObject(self, name, new_object):
		self.localObjectDict[name] = new_object

	def delChildren(self, del_name):
		del self.childrenDict[del_name]

	def delLocalObject(self, del_name):
		del self.localObjectDict[del_name]
