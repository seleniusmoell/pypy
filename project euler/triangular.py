# -*- coding: utf-8 -*-
import time

# Uppgift: att hitta det första sk triangeltalet som har 500 faktorer
# https://projecteuler.net/problem=12

def getDivisors(n):
	divisors = [x for x in range(1, int(n**0.5 + 1)) if n%x == 0]
	for x in divisors[:len(divisors)]:
		divisors.append(n/x)
			
	return divisors


i = 0
j = 1
list=[]
tStart = time.time()

while len(list) < 500:
	i += j
	j += 1
	list = getDivisors(i)

print "Time is: " + str(time.time() - tStart)
print i