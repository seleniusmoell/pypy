# -*- coding: utf-8 -*-
import time

# Uppgift: Att i en matris hitta den största produkten av fyra tal som
# ligger bredvid varandra i sidled, vertikalt eller diagonalt.
# https://projecteuler.net/problem=11

tStart = time.time()
inputFile = open('grid.txt')
matrix = [map(int,line.split()) for line in inputFile]
inputFile.close()

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