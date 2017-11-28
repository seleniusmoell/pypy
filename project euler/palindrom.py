
# Largest number with 3-digit factors

startNbr = 999*999 
factorList = []
solution = 0

# Make a palindrome-check
def isPalindrome (list):
	for i in range (0, int(len(list)/2)):
		if list[i] != list[len(list)-i-1]:
			return False
	return True
	
# Test
# print isPalindrome(['1','0','0','1'])

# Decrease number until palindrome is found

def decrease (number):
	list = []
	for i in range(0, len(str(number))):
		list.append(str(number)[i])
		
	while not isPalindrome(list):
		number -= 1
		list[:] = []
		for i in range(0, len(str(number))):
			list.append(str(number)[i])
		
	return number		
			


# check if it has 3-digit factors 
def factors(n):
	factors = reduce(list.__add__, ([i, n//i] for i in range(1, int(n**0.5) + 1) if n%i ==0))
	result = []
	print factors
	for i in factors:
		if len(str(i)) == 3:
			result.append(i)
	
	return result
	

palindrome = decrease(startNbr)
print palindrome
factorList = factors(palindrome)
print factorList	

while solution == 0:
	palindrome = decrease(palindrome - 1)
	factorList = factors(palindrome)
	if len(factorList) > 2:
		for i in range(1, len(factorList)):
			if factorList[i]*factorList[i-1] == palindrome:
				solution = palindrome
	
print factorList
print solution


