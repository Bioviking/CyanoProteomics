
#####################################################3
#Creating a parsed file for the extraction of features for the original dataset.
#import numpy as np


# Load the data from file.
first_dataset = open('../data/Cyanogenes.fasta', 'r+')
#C:\Users\Admin\Documents\GitHub\CyanoProteomics\docs\Diary

parsed_fasta = open('../data/fasta/parsed_fasta.fasta', 'w')

#createing Lists for Ids sequences and features

fname = first_dataset
idlist = []
#seqlist = []
#feat_list = []

for line in fname:
	#print(line)
	line = line.strip('\n').split
	line = line[1]
	idlist.append(line)
	line = line.split('\n')
    line = line[0]
    
    idlist.append(line)
    print(idlist)    
    #Printing the 3 lists to a text file 
    parsed_fasta.write(line + '\n')



fname.close()
parsed_fasta.close()