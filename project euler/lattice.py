import time
import math

tStart = time.time()

def steps(n):
	sum = 0
	oldvalue = 1
	
	for i in range(0, n):
		print("Oldvalue " + str(oldvalue))	
		if i == 0:
			newvalue=n
			print("Newvalue " + str(newvalue))
			sum = oldvalue + newvalue
		else:
		
			newvalue = sum + oldvalue
			print("Newvalue " + str(newvalue))
		
			sum = sum + newvalue
		print("Sum " + str(sum))
		
		oldvalue = newvalue
		
		
	return sum
	
nbr = steps(3)
print("Time is: " + str(time.time() - tStart))
print ("n = 3 returns " + str(nbr))

		
			
		
	