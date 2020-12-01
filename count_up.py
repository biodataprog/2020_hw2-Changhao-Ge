#!/usr/bin/env python3

# this is a python script template
# this next line will download the file using curl

gff="Escherichia_coli_str_k_12_substr_mg1655.ASM584v2.37.gff3.gz"
fasta="Escherichia_coli_str_k_12_substr_mg1655.ASM584v2.dna.chromosome.Chromosome.fa.gz"

import os,gzip,itertools,csv,re

# this is code which will parse FASTA files
# define what a header looks like in FASTA format
def isheader(line):
    return line[0] == '>'

def aspairs(f):
    seq_id = ''
    sequence = ''
    for header,group in itertools.groupby(f, isheader):
        if header:
            line = next(group)
            seq_id = line[1:].split()[0]
        else:
            sequence = ''.join(line.strip() for line in group)
            yield seq_id, sequence



if not os.path.exists(gff):
    os.system("curl -O ftp://ftp.ensemblgenomes.org/pub/bacteria/release-45/gff3/bacteria_0_collection/escherichia_coli_str_k_12_substr_mg1655/Escherichia_coli_str_k_12_substr_mg1655.ASM584v2.37.gff3.gz")

if not os.path.exists(fasta):
    os.system("curl -O ftp://ftp.ensemblgenomes.org/pub/bacteria/release-45/fasta/bacteria_0_collection/escherichia_coli_str_k_12_substr_mg1655/dna/Escherichia_coli_str_k_12_substr_mg1655.ASM584v2.dna.chromosome.Chromosome.fa.gz")
number = 0
Length = 0
Flen = 0
numberC =0
LengthC =0
with gzip.open(gff,"rt") as fh:
    # now add code to process this
    gff = csv.reader(fh,delimiter="\t")
    for row in gff:
        if row[0].startswith("#"):
            continue
        elif row[2]=="gene" :
            number = number + 1
            Length = int(row[4])-int(row[3]) + Length
        elif row[2]=="CDS" :
            numberC = numberC + 1
            LengthC = int(row[4])-int(row[3]) + LengthC
            
           
            #Length = int(row[4]) - int(row[3])
            
print("number of genes:", number,"simply counting gene colum")
print("gene length:",Length,"sum Stop - Start of gene lines")
with gzip.open(fasta,"rt") as fa:
   pairs = aspairs(fa)
   fasta  = dict(pairs)
   for k,v in fasta.items():
    print( "genemo length in fasta file",len(v),"( it only have 1 sequence )")
    
print("coding sequence length",LengthC)
percentage = (int(LengthC) / int(len(v)))*100
print("percentage of the genome which is coding",percentage,"%")
 #for row in fasta:
  #      if row[0].startswith('>'):
   #         continue
    #    else:
            #Flen= Flen + len(str(row))
            #print(len(str(row))-4)
            

#print("total genmo length:",Flen)

         


     