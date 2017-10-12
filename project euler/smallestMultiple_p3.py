import time

n = 0
biggestNbr = 1

def multipleCheck(n):
	for i in range (1, 20):
		if n % i != 0 or n == 0:
			print("i is:" + str(i) + ", n is:" + str(n))
			global biggestNbr
			if i > biggestNbr:
				biggestNbr = i
			return False	
	biggestNbr = i
	return True

tStart = time.time()
while not multipleCheck(n):
	n += 19*17*15*13*11
	
print("run time = " + str((time.time() - tStart)))
print("The number is: " + str(n))
print(biggestNbr)
	