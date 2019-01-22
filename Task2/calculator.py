import sys

tt = " "
final = 0
total = 0
Avg = 0

try:

    tt = str(sys.argv[1])


    oldlist = str(tt).split(",")

    list = []
    for i in (oldlist):
        list.append(int(i))


    #print list

    sumEve = 0
    sumOdd = 0

    evenC = 0
    oddC = 0

    for i in list:
        if i % 2 == 0:
            evenC+=1
            sumEve+=i
        else:
            oddC+=1
            sumOdd+=i
except:


    print "Please enter valid integers."
differ = max(list) - min(list)

for i in list:
    total+=i

final = total - max(list) - min(list)

Avg = final / (len(list)-2)

print "The sum of all even numbers is " + str(sumEve) + ", the sum of all odd numbers is " + str(sumOdd) + ", the difference between the biggest and smallest number is " + str(differ) + ", the total number of even numbers is " + str(evenC) + ", the total number of odd numbers is " +str(oddC) + " the centered average is " + str(Avg) + "."

