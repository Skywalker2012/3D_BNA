#Created by Gushu Li on 2013/7/30

class SourceManager():

	def __init__(self):
		self.objectDict = {}

	def addObject(self,newName,newObject):
		self.objectDict[newName] = newObject
		print self.objectDict

	def delObject(self,del_Name):
		del self.objectDict[del_Name]
