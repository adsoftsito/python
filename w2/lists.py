adnseq  = ["A", "C", "T", "G", "A", "T", "G", "T", "A", "C"]
adnseq2 = ["T", "G", "A", "T", "G"]

n = len(adnseq)
print adnseq
print " length = ",n
print " first position  = ",adnseq[0]
print " last  position = ",adnseq[n-1]
print " first 3  position = ",adnseq[0:3]
print " last 5  position = ",adnseq[-5:]

print "inserting one item..."
adnseq.append("T")
n = len(adnseq)
print adnseq
print " length = ",n

print "replace first position with T"
adnseq[0] = "T"
print adnseq

print "delete last position"
adnseq.pop(n-1)
print adnseq

print " newadnseq = seq1 + seq2"

newadnseq = adnseq + adnseq2

print adnseq
print adnseq2
print newadnseq
print " length = ", len(newadnseq)
