'''NAME
       AT-percentage

VERSION
        1.0

AUTHOR
        Hely Salgado

DESCRIPTION
        Calculate percentage of AT on a genome sequence

CATEGORY
        Genomic sequence

USAGE

    % python AT-percentage.py -i filename
    
    example
    
    % python AT-percentage.py -i sequence.txt
        
'''
import argparse

# program arguments
parser = argparse.ArgumentParser(description="Calculate percentage of AT on a genome sequence")
parser.add_argument(
  "-i", "--input",
  help="genomic sequence file in raw format",
  required=True)
args = vars(parser.parse_args())

# Getting the dna sequence from the file
with open(args['input'],'r') as readFile:
    sequence = "";
    for line in readFile:
        sequence = sequence + line.strip()
        
# Sequence in uppercase to count including the lowercase letters
sequence = sequence.upper()

#get "A" frequency
a_content = sequence.count('A')

#get "T" frequency
t_content = sequence.count('T')

#calculate percentage of AT in the sequence
frequency = ((a_content + t_content)*100) / len(sequence)

#show calculation
print("\nA({}) + T({}) =  {}\tAT content = {:.2f}%\n".format(a_content, t_content, a_content+t_content, frequency))
print(sequence + "\n")

