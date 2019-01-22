import sys
from  collections import Counter


pp = " "

try:
    pp  = str(sys.argv[1])

except:

    print "Your input is invalid"


ww = Counter(str(pp.lower()))
count = 0
ldasdas= ""
gfdg = ww.most_common(5)
for i in gfdg:
    ldasdas=str(ldasdas)+str(i[0])+":"+str(i[1])+","
print ldasdas[:-1]