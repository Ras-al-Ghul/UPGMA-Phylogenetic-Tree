import csv
SMALL_NUM = -1

def findminindex(matrix,numofrows,numofcols):
	mins = SMALL_NUM
	minx,miny = 0,0
	for i in range(1,numofrows):
		for j in range(1,numofcols):
			if matrix[i][j] > mins and matrix[i][j] != 0.0 :
				mins = matrix[i][j]
				minx,miny = i,j

	return minx,miny,mins

def findrowfromstr(matrix,numofrows,numofcols,strs):
	for i in range(1,numofrows):
		if matrix[i][0] == strs:
			return i
	return None

def findcolfromstr(matrix,numofrows,numofcols,strs):
	for i in range(1,numofcols):
		if matrix[0][i] == strs:
			return i
	return None

def calcnewdistmatrix(matrix,numofrows,numofcols,val):
	if val == numofrows-1:
		return

	minx,miny,mins = findminindex(matrix,numofrows,numofcols)
	firststr = matrix[minx][0]
	secondstr = matrix[0][miny]
	combinedstr = '('+matrix[minx][0]+','+matrix[0][miny]+')'
	firstsize = len(firststr)
	secondsize = len(secondstr)

	branchlength = mins/2

	for i in range(1,numofrows):
		if matrix[minx][i] != 0 and matrix[minx][i] != mins:
			diststr = (matrix[minx][i]*firstsize + matrix[i][findcolfromstr(matrix,numofrows,numofcols,secondstr)]*secondsize)/(firstsize+secondsize)
			matrix[minx][i] = diststr
			matrix[i][findcolfromstr(matrix,numofrows,numofcols,firststr)] = diststr

	matrix[0][minx] = combinedstr
	matrix[minx][0] = combinedstr

	#delete column
	for i in range(1,numofrows):
		matrix[i][findcolfromstr(matrix,numofrows,numofrows,secondstr)] = 0.0
	#delete rows
	for i in range(1,numofcols):
		matrix[findrowfromstr(matrix,numofrows,numofcols,secondstr)][i] = 0.0

	matrix[0][findcolfromstr(matrix,numofrows,numofcols,secondstr)] = 0.0
	matrix[findrowfromstr(matrix,numofrows,numofcols,secondstr)][0] = 0.0

	print combinedstr
	print "Branch Length Estimation: ",branchlength
	print "\n"

	calcnewdistmatrix(matrix,numofrows,numofcols,val+1)

	return matrix

if __name__ == "__main__":
	reader = csv.reader(open("Pdistance.txt","rb"), delimiter=',')
	distance = list(reader)

	distance = distance[1:]
	for i in range(len(distance)):
		distance[i] = distance[i][1:]

	Table = [[0.0,"Cow","Sheep","Worm","Rat","Frog","Pig"],["Cow",0.0,0.0,0.0,0.0,0.0,0.0],
	["Sheep",0.0,0.0,0.0,0.0,0.0,0.0],["Worm",0.0,0.0,0.0,0.0,0.0,0.0],
	["Rat",0.0,0.0,0.0,0.0,0.0,0.0],["Frog",0.0,0.0,0.0,0.0,0.0,0.0],
	["Pig",0.0,0.0,0.0,0.0,0.0,0.0]]

	for i in range(6):
		for j in range(6):
			Table[i+1][j+1] = float(distance[i][j])

	
	matrix = calcnewdistmatrix(Table,7,7,1)


