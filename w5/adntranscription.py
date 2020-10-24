# files
# dna example
#

nucleotides = ["A", "C", "T", "G"]

nucl_complement = {
               "A":"T", 
               "C":"G", 
               "T":"A",
               "G":"C" 
	      }

rna_transcription = {
	       "A":"U",
	       "C":"G",
               "T":"A",
               "G":"C"
	      }

codons = {
  "UUU": "Fenilalanina",
  "UUC": "Fenilalanina",
  "UUA": "Leucina",
  "UUG": "Leucina",
  "UCU": "Serina",
  "UCC": "Serina",
  "UCA": "Serina",
  "UCG": "Serina",
  "UAU": "Tirosina",
  "UAC": "Tirosina",
  "UAA": "Codon de terminacion ocre",
  "UAG": "Codon de terminacin Ambar",
  "UGU": "Cisteina",
  "UGC": "Cisteina",
  "UGA": "Codon de terminacion Opalo",
  "UGG": "Triptofano",
  "CUU": "Leucina",
  "CUC": "Leucina",
  "CUA": "Leucina",
  "CUG": "Leucina",
  "CCU": "Prolina",
  "CCC": "Prolina",
  "CCA": "Prolina",
  "CCG": "Prolina",
  "CAU": "Histidina",
  "CAC": "Histidina",
  "CAA": "Glutamina",
  "CAG": "Glutamina",
  "CGU": "Arginina",
  "CGC": "Arginina",
  "CGA": "Arginina",
  "CGG": "Arginina",
  "AUU": "Isoleucina",
  "AUC": "Isoleucina",
  "AUA": "Isoleucina",
  "AUG": "Metionina",
  "ACU": "Treonina",
  "ACC": "Treonina",
  "ACA": "Treonina",
  "ACG": "Treonina",
  "AAU": "Asparagina",
  "AAC": "Asparagina",
  "AAA": "Lisina",
  "AAG": "Lisina",
  "AGU": "Serina",
  "AGC": "Serina",
  "AGA": "Arginina",
  "AGG": "Arginina",
  "GUU": "Valina",
  "GUC": "Valina",
  "GUA": "Valina",
  "GUG": "Valina",
  "GCU": "Alanina",
  "GCC": "Alanina",
  "GCA": "Alanina",
  "GCG": "Alanina",
  "GAU": "acido asartico",
  "GAC": "acido asartico",
  "GAA": "acido glutamico",
  "GAG": "acido glutamico",
  "GGU": "Glicina",
  "GGC": "Glicina",
  "GGA": "Glicina",
  "GGG": "Glicina"
}

nucl_codon = [];

# A T
# C G
dna = ""
#dna = "ATTAAAGGTTTATACCTTCCCAGGTAACAAACCAACCAACTTTCGATCTCTTGTAGATCTGTTCTCTAA"
#dna = "TACTGCCTCGAAGCCTCGATC"
#dna = "ACCGTT"
dna_complement = ""
rna = ""

#n = len(dna)

# ATT
# AAA
# GGT
# TTA

#f = open("adn.txt", "r")
f = open("covid19.txt", "r")
for x in f:
  #print x
  #if x == 'A':
  # print x
  dna = dna + x

dna = dna.replace("\n","")
#print dna
#
# calculate the complementary sequence
#
for x in dna:
  dna_complement = dna_complement + nucl_complement[x]
  

n = len(dna)
print " dna length  = ", n

n = len(dna_complement)
print " dna length complementary  = ", n


for i in range(0, n):
#  if i < 15:
  print i, dna[i], dna_complement[i]

print "dna, dna complementary : "

print dna
print dna_complement


#
# rna transcription
#

for x in dna_complement:
  rna = rna + rna_transcription[x]

print "rna "
print rna[::-1]

#
# codon create
#
for i in range(0, n, 3):
  nucl_codon.append(rna[i:i+3])
#  nucl_codon.append(dna_complement[i:i+3])

n = len(nucl_codon)
print "total codons ", n
for i in range(0,n):
#  if nucl_codon[i] == "AUG":
  print i, nucl_codon[i], codons[nucl_codon[i]]

#print "\n  reverse \n" 
#for i in range(n-1, -1, -1):
#  print i+1, adn[i]

#totalA=0
#totalC=0
#totalT=0
#totalG=0
#total = 0
#for i in range(n-1, -1, -1):
#  if (adn[i] == "A"):
#    totalA=totalA+1
#    total = total + 1

#  if (adn[i] == "C"):
#    totalC=totalC+1
#    total = total + 1

#  if (adn[i] == "T"):
#    totalT=totalT+1
#    total = total + 1

#  if (adn[i] == "G"):
#    totalG=totalG+1
#    total = total + 1
#print "total A", totalA
#print "total C", totalC
#print "total T", totalT
#print "total G", totalG

#print "total adn = ", total
