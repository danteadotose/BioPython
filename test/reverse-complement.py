'''
NAME
	reverse-complement.py
    
VERSION
    1.0
    
AUTHOR
	Hely Salgado, Dante Torres
    
DESCRIPTION
	Make the reverse complement of DNA sequence
    
CATEGORY
	Genomic Sequence
    
USAGE

    % python reverse-complement.py -i filename 
    
    Saca el reverse complement
    
    % python reverse-complement -i sequence.txt

'''

import argparse

# program arguments
parser = argparse.ArgumentParser(description="Make the reverse complement of DNA sequence")
parser.add_argument(
  "-i", "--input",
  help="genomic sequence file in raw or fastA format",
  required=True)
args = vars(parser.parse_args())

# Getting the dna sequence from the file
with open(args['input'],'r') as readFile:
    sequence = "";
    for line in readFile:
        # Ignore comments or FastA head line
        if line.startswith('#') or line.startswith('>'):
            continue
        else:
            sequence += line.strip()
    
sequence = sequence.upper()

# Dictionary containing the complement equivalents
sequence = sequence[::-1].translate(str.maketrans({'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}))
print ('{}'.format(sequence))
