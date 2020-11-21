# files
# adn example
adn = ""

f = open("covid19.txt", "r")
for x in f:
  adn = adn + x

adn = adn.replace('\n','')

n = len(adn)
print " adn length = ", n
print adn

#for i in range(0, n):
#  print i+1,  adn[i]

