import time

sumOfSq = 0
sqOfSum = 0
tStart = time.time()
for i in range(1, 101):
	sumOfSq += i**2
	sqOfSum += i

sqOfSum = sqOfSum**2
print "run time = " + str((time.time() - tStart))
print "The sum of the squares is: " + str(sumOfSq)
print "The square of the sum is: " + str(sqOfSum)
print "The difference is: " + str(sumOfSq - sqOfSum) 
