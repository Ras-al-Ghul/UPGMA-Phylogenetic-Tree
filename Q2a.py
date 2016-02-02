import csv
source = open("Protein.txt", "r")
matrix = [[], [], [], [], [], []]

for x in range(6): 
	line = source.readline()
	while True:
		c = source.read(1)
		if c == '>' or c=='':
			break
		if (c!='\n' and c!='\r') :
			matrix[x].append(c)

compare = open("BLOSUM62.txt", "r")
compareator = [[0 for x in range(25)] for x in range(23)]
x=0
line = compare.readline()
for x in range(23): 
	line = compare.readline()
	compareator[x]=line.split()	
for x in range(23):
	compareator[x] = compareator[x][:-1]
	compareator[x] = compareator[x][1:]
		
distance = [[0 for x in range(6)] for x in range(6)]
keys={'A':0,'R':1,'N':2,'D':3,'C':4,'Q':5,'E':6,'G':7,'H':8,'I':9,'L':10,'K':11,'M':12,'F':13,'P':14,'S':15,'T':16,'W':17,'Y':18,'V':19,'B':20,'Z':21,'X':22 }
x=0
for x in range(6):
	for y in range(x+1,6):
		score=0
		p=len(matrix[x])
		q=len(matrix[y])
		for z in range(min(p,q)):
			a=matrix[x][z]
			b=matrix[y][z]
			score+=int(compareator[keys[a]][keys[b]])
		score=score-abs(p-q)*4
		distance[x][y]=score
		distance[y][x]=score

distance[0]=['Cow']+distance[0]
distance[1]=['Sheep']+distance[1]
distance[2]=['Worm']+distance[2]
distance[3]=['Rat']+distance[3]
distance[4]=['Frog']+distance[4]
distance[5]=['Pig']+distance[5]
Poutput = open("Pdistance.txt", "w")
print>>Poutput,"*,Cow,Sheep,Worm,Rat,Frog,Pig"
writer = csv.writer(Poutput)
for i in range(len(distance)):
	writer.writerow(distance[i])
Poutput.close()
