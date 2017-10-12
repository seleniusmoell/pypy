# This was my first solution, which I knew would be cumbersome.
# It took around 32 seconds without breaking at the square of x.
# With the break, it timed to the more manageable 1.89s
# I have since then discovered many more elegant prime number algorithms, 
# but they are learned rather than constructed by me.

import time 
i = 3
primeList = [2]
# n = 3
# m = len(primeList)


tStart = time.time()
while len(primeList) <= 10000:
	#primeList = primeList | {i for i in range(n, m, 2) for x in primeList if i%x != 0 and i not in primeList}
	flag = True
	for x in primeList:
		if x > i**0.5 + 1: break
		if i % x == 0:
			flag = False		
	if flag and i not in primeList:
		primeList.append(i)
	i += 2


# primeList = list(primeList)
print "Time: " + str(time.time() - tStart)
print "Prime is: " + str(primeList[len(primeList)-1])
print "Number is: " + str(len(primeList))

