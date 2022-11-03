import re

class DNA:
    
    def __init__(self,string):
        
        self.nucleotides = string
        
    def validate(self):
        
        nucleotides = self.nucleotides
        count = 0

        for i in range(len(nucleotides)-1):
            
            if nucleotides[i] == 'A' or nucleotides[i] == 'C' or nucleotides[i] == 'T' or nucleotides[i] == 'G':

                count += 1
                
            else:
                
                count = count 
            
        if count == len(nucleotides)-1:
            return True
            
        else:
            return False
            
    
    def __str__(self):
        
        self.nucleotides = self.nucleotides.upper()
        return self.nucleotides

    def convert_to_rna(self):
    
        dna = self.nucleotides.upper()
        rna = ''
    
        for i in range(len(dna)):
        
            if dna[i] == 'T':
            
                rna = rna + 'U'
        
            else:
            
                rna += dna[i]
    
        return rna.upper()
    
    def reverse_complement(self):
    
        dna = self.nucleotides
        dna.upper()
        newDNA = ''
    
        for i in range(len(dna)):
        
            if dna[i] == 'A':
            
                newDNA += 'T'
        
            if dna[i] == 'T':
            
                newDNA += 'A'
            
            if dna[i] == 'G':
            
                newDNA += 'C'
        
            if dna[i] == 'C':
            
                newDNA += 'G'
    
        length =len(newDNA) 
        reverseNewDNA = newDNA[length::-1] 
        return reverseNewDNA

class RNA:
    
    def __init__(self,string):
        
        self.nucleotides = string
        
    def validate(self):
        
        nucleotides = self.nucleotides
        count = 0

        for i in range(len(nucleotides)-1):
            
            if nucleotides[i] == 'A' or nucleotides[i] == 'C' or nucleotides[i] == 'U' or nucleotides[i] == 'G':

                count += 1
                
            else:
                
                count = count 
            
        if count == len(nucleotides)-1:
            return True
            
        else:
            return False
            
    def __str__(self):
        
        self.nucleotides = self.nucleotides.upper()
        return self.nucleotides
    
    def to_protein(self,readingframe):
        
        CODON_DICT = {'GCA': 'A', 'GCC': 'A', 'GCG': 'A', 'GCU': 'A',
              'UGC': 'C', 'UGU': 'C',
              'GAC': 'D', 'GAU': 'D',
              'GAA': 'E', 'GAG': 'E',
              'UUC': 'F', 'UUU': 'F',
              'GGA': 'G', 'GGC': 'G', 'GGG': 'G', 'GGU': 'G',
              'CAC': 'H', 'CAU': 'H',
              'AUA': 'I', 'AUC': 'I', 'AUU': 'I',
              'AAA': 'K', 'AAG': 'K',
              'UUA': 'L', 'UUG': 'L', 'CUA': 'L', 'CUC': 'L', 'CUG': 'L', 'CUU': 'L',
              'AUG': 'M',
              'AAC': 'N', 'AAU': 'N',
              'CCA': 'P', 'CCC': 'P', 'CCG': 'P', 'CCU': 'P',
              'CAA': 'Q', 'CAG': 'Q',
              'AGA': 'R', 'AGG': 'R', 'CGA': 'R', 'CGC': 'R', 'CGG': 'R', 'CGU': 'R',
              'AGC': 'S', 'AGU': 'S', 'UCA': 'S', 'UCC': 'S', 'UCG': 'S', 'UCU': 'S',
              'ACA': 'T', 'ACC': 'T', 'ACG': 'T', 'ACU': 'T',
              'GUA': 'V', 'GUC': 'V', 'GUG': 'V', 'GUU': 'V',
              'UGG': 'W',
              'UAC': 'Y', 'UAU': 'Y'}
        
        protein = ''
        rna = self.nucleotides.upper()
        sequence = rna[readingframe:]
    
        while len(sequence) >= 3:
        
            codon = sequence[0:3]
            
            if codon == 'UAG' or codon == 'UAA' or codon == 'UGA':
                break
            
            protein += CODON_DICT.get(codon)
            
            sequence = sequence[3:]
        
        return protein


def read_dna_file(file):
    
    try:
        fp = open(file, 'r')
        line = fp.read()

        words = re.findall('[0-9a-zA-Z]+', line)
        
        for i in range(len(words)):
            
            if i%2 == 0:

                reading_frame = int(words[i])

                dna = DNA(words[i+1])
            
                if dna.validate() == True:
                
                    rna = RNA(dna.convert_to_rna())
                    proteins = rna.to_protein(reading_frame)
                    print(proteins)
                
                    if proteins == None:
                    
                        print("")
                
                else:
                    print("Invalid Sequence: " + words[i+1])
        
    
    except FileNotFoundError:
        
        print("File not found.")


def readthing(file):

    fp = open(file, 'r')
    line = fp.read()

    words = re.findall('[0-9a-zA-Z]+', line)
        
    for i in range(len(words)-1):

        print(str(i) + ": " + words[i])

#readthing("dnafile.csv")
read_dna_file("dnafile.csv")