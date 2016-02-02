#UPGMA-Phylogenetic-Tree

To run,

####Question 1

`python Q1a.py`  
`python Q1b.py`  

####Question 2

`python Q2a.py`  
`python Q2b.py`  

The UPGMA algorithm used is the one from Wikipedia  
`https://en.wikipedia.org/wiki/UPGMA`

####Question 1

Construct a phylogenetic relationship for the given nucleotide sequences(Nucleotide.txt)
- Write a script to generate a distance matrix csv file for the sequences present in the data file. Name the distance matrix file as 'Ndistance.txt'  
For example:  
	seq1 = 'ATGCATGCAA'  
	seq2 = 'ATGCATGCTA'  
	Distance(seq1,seq2) = Mismatches/total length = 1/10 = 0.1
- Write a script that uses 'Ndistance.txt' and generate phylogenetic relationship between the organisms using UPGMA method.

####Question 2

Construct a phylogenetic relationship for the given protein sequences(Protein.txt)
- Write a script to generate a distance matrix csv file for the sequences present in the data file. Name the distance matrix file as 'Pdistance.txt'. Use 'BLOSUM62.txt' for getting score values.  
For example:  
	seq1 = 'AGYFKTP'  
	seq2 = 'GRKLYSK'  
	Score(AG) = 0, Score(GR) = -2 and so on  
	Distance(seq1,seq2) = Score(AG) + Score(GR) +....  
- Write a script that uses 'Pdistance.txt' and generate phylogenetic relationship between the organisms using UPGMA method.


