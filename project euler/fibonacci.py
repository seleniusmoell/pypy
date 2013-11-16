sum = 0
iCurr = 0
iNext = 1
temp = 0

while ( iNext < 4000000):
	temp = iCurr
	iCurr = iNext
	iNext = temp + iNext
	
	if iNext % 2 == 0:
		sum = sum + iNext

print (sum)