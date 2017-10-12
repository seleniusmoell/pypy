import time 

tStart = time.time()
inputFile = open('largeSum.txt', 'r')
list = []

for line in inputFile:
	list.append(int(line))

inputFile.close()

nbr = 0
for line in list:
	nbr += int("%11d" % line) 

print "Time is: " + str(time.time() - tStart)
print nbr