import csv
source = open("Nucleotide.txt", "r")

matrix = [[], [], [], [], [], []]

for x in range(6): 
	line = source.readline()
	while True:
		c = source.read(1)
		if c == '>' or c=='':
			break
		if (c!='\n' and c!='\r') :
			matrix[x].append(c)

distance = [[0 for x in range(6)] for x in range(6)]

x=0
for x in range(6):
	for y in range(x+1,6):
		mismatch=0
		for z in range(1679):
			if(matrix[x][z]!=matrix[y][z]):
				mismatch+=1
		distance[x][y]=mismatch/1679.0
		distance[y][x]=mismatch/1679.0
	
distance[0]=['Cow']+distance[0]
distance[1]=['Sheep']+distance[1]
distance[2]=['Worm']+distance[2]
distance[3]=['Rat']+distance[3]
distance[4]=['Frog']+distance[4]
distance[5]=['Pig']+distance[5]
Poutput = open("Ndistance.txt", "w")
print>>Poutput,"*,Cow,Sheep,Worm,Rat,Frog,Pig"
writer = csv.writer(Poutput)
for i in range(len(distance)):
	writer.writerow(distance[i])
Poutput.close()

