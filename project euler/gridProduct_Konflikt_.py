# -- coding: utf-8 --

import time
import sys

# Det här problemet handlar om att hitta dens största produkten av fyra tal i en matris.
# Produkten kan tas mellan vilka tal som helst i bredvid varandra i sidled, uppåt/nedåt
# eller diagonalt. https://projecteuler.net/problem=11



tStart = time.time()

# Jag har lagt matrisen i en textfil
try:
	inputFile = open('grid.txt', 'r')
	matrix = [map(int,line.split()) for line in inputFile]
	inputFile.close()
except IOError as e:
	print "File error"
	
# Sök igenom matrisen
def getProduct (grid, n):
	product = 0
	for row in range(0, len(grid)):
		for i in range(0, len(grid)):
			p1 = reduce(lambda x, y: x*y,[grid[row][x] for x in range(i, i+n) if x<len(grid)])
			if p1 > product:
				product = p1
			p2 = reduce(lambda x, y: x*y,[grid[x][i] for x in range(row, row+n) if x<len(grid)])
			if p2 > product:
				product = p2
			p3 = reduce(lambda x, y: x*y, [grid[x+row][x+i] for x in range(0, n) if x<len(grid) and x+i<len(grid) and x+row<len(grid)])
			if p3 > product:
				product = p3
			p4 = reduce(lambda x, y: x*y,[grid[row+x][len(grid)-x-i-1] for x in range(0,n) if x<len(grid) and x+i<len(grid) and row+x<len(grid)])
			if p4 > product:
				product = p4
				
	return product

print "Time is: " + str(time.time() - tStart)
print getProduct(matrix, 4)