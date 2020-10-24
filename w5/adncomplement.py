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


nucl_codon = [];

dna = "ACCGTT"
dna_complement = ""
rna = ""

# complementary seq 
#
for x in dna:
  dna_complement = dna_complement + nucl_complement[x]
  

n = len(dna)
print " dna length  = ", n

n = len(dna_complement)
print " dna length complementary  = ", n


for i in range(0, n):
  print i, dna[i], dna_complement[i]

print "dna, dna complementary : "
print dna
print dna_complement
