# -*- coding: utf-8 -*-

import time

# Uppgift: Summera de två miljoner första primtalen. Jag använde en variant av Erathostenes såll
# för att lösa uppgiften.
# https://projecteuler.net/problem=10

def sieve(n):
	'''Sieve of Erathostenes'''
	sieve = [True]*n
	for i in xrange(3, int(n**0.5 + 1), 2):
		if sieve[i]:
			sieve[i*i::2*i] = [False]*((n-i*i-1)/(2*i)+1)
	return [2] + [x for x in xrange(3,n,2) if sieve[x]]
	
tStart = time.time()
list = sieve(2000000)
print "Time is: " + str(time.time() - tStart)
print "Sum is: " + str(sum(list))
	