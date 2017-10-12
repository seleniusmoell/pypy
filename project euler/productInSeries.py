import time

tStart = time.time()

inputFile = open('input_prodInSeries.txt')

series = [x for line in inputFile for x in line if x != '\n']

inputFile.close()

thirteen = map(int, series[:13])

print thirteen

product = reduce(lambda x, y: x*y, thirteen)

print product

for i in range (1, len(series)):
	thirteen = map(int, series[i:i + 13])
	
	tempProduct = reduce(lambda x, y: x*y, thirteen)
	if  tempProduct > product:
		product = tempProduct
		
	# print product
	# print i
		
print "Time is: " + str(time.time() - tStart)
print "Product is: " + str(product)
	
