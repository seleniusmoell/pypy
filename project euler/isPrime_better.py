def factors(n):
	return reduce(list.__add__, ([i, n//i] for i in range(1, int(n**0.5) + 1) if n%i ==0))
	
print factors(600851475143)