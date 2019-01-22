import sys
leapYears = []

try:

    startYear = int(sys.argv[1])
    endYear = int(sys.argv[2])

except:
    print ("Your input is invalid!")

for i in range(startYear, endYear + 1):

    if (i % 4) == 0:
        leapYears.append(i)

    elif ( i % 100 == 0) and (i % 400 != 0):

        leapYears.append(i)

        print (i)



print ("The number of Leap Years is {}, the Leap Years are {}".format(len(leapYears),str(leapYears)[1:-1]))


