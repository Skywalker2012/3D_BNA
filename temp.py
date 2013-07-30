fp = open('BrainMesh_Ch2.nv')
line = fp.readline()
vertexNum = int(line,10)

vertexList = []
for i in xrange(vertexNum):
	line = fp.readline()
	templist = line.split()
	for j in xrange(3):
		vertexList.append(float(templist[j]))
	#	print str(i) + '  ' + str(j)
	#	print vertexList[i*3+j]

#print vertexNum
line = fp.readline()
triangleNum = int(line,10)
triangleList = []
for i in xrange(triangleNum):
	line = fp.readline()
	templist = line.split()
	for j in xrange(3):
		triangleList.append(int(templist[j],10))
		#print str(i) + '  ' + str(j)
	#	print triangleList[i*3+j]
		if triangleList[i*3+j] > 53468:
			print '!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!'
			print str(i) + '  ' + str(j)
			print triangleList[i*3+j]

print triangleNum
