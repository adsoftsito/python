# for
# data examples
adn = "ATTAAAGGTTTATACCTTCCCAGGTAACAAACCAACCAACTTTCGATCTCTTGTAGATCTGTTCTCTAAA"
n = len(adn)

# ATT
# AAA
# GGT
# TTA


# A T
# C G

print " adn length = ", n
for i in range(0, n):
  print i+1,  adn[i]

print "\n  reverse \n" 
for i in range(n-1, -1, -1):
  print i+1, adn[i]

totalA=0
totalC=0
totalT=0
totalG=0
for i in range(0, n):
  if (adn[i] == "A"):
    totalA=totalA+1

  if (adn[i] == "C"):
    totalC=totalC+1

  if (adn[i] == "T"):
    totalT=totalT+1

  if (adn[i] == "G"):
    totalG=totalG+1

print "total A", totalA
print "total C", totalC
print "total T", totalT
print "total G", totalG
