#
# while with if example
# 
nucleotide = ""
while (nucleotide != "X"):
  nucleotide = raw_input("Input X for exit,  nucleotide A, C, T, G :")
  print nucleotide

  if (nucleotide == "A"):
    print ("ADENINA")
  elif (nucleotide == "C"):
    print ("CITOSINA")
  elif (nucleotide == "T"):
    print ("TIMINA")
  elif (nucleotide == "G"):
    print("GUANINA")
  elif (nucleotide == "X"):
    print("Bye..")
  else:
    print("ERROR in input")


