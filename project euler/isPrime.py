import time

def isPrime (n):
	for x in range (3, int(n**0.5) +1, 2):
		if n % x == 0:
			return False
	return True

def primeFactor (n):
	
	largestFacor = 0
	
	for x in range (3, int(n**0.5) +1, 2):
		if n % x == 0:
			if x > largestFacor and isPrime(x):
				largestFacor = x
			
	return largestFacor

tStart = time.time()
print primeFactor(600851475143)
print "Runtime: " + str((time.time() - tStart))

 