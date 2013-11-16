prime_table = {2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31}
nbr = 600851475143
prime = 2

for i in prime_table:
	if nbr % i == 0:
		nbr = nbr / i
		prime = i
	
	
	
print(prime, nbr)