# -*- coding: utf-8 -*-
import time

# Uppgift: Hitta den längsta Collatz-sekvensen med startvärde < en miljon
# https://projecteuler.net/problem=14

tStart = time.time()
maxVal = (0, 0)
cache = {}

def collatzRecursion(n, i):
	if n in cache:
		return i + cache[n]

	if n == 1:
		return i
	elif n%2 == 0:
		n = n/2
	else:
		n = 3*n+1
	return collatzRecursion(n, i+1)
		

for x in range(1000000, 500000, -1):
	iter = collatzRecursion(x, 0)
	
	cache[x] = iter
	
	if iter > maxVal[0]:
		maxVal = (iter, x)
		

print "Time is: " + str(time.time() - tStart)
print maxVal


