#!/usr/bin/env python
#This script is written by tove in Python 3.0

__author__ = "tove"
__copyright__ = "Copyright 2017"
__email__ = "seleniusmoell@gmail.com"

def interestCalc(investment, interest, term):
	sum = int(investment)
	interest = int(interest)*0.01
	for i in range(0, int(term)):
		sum = sum + sum*interest
	
	return sum
	
investment = input("What is the investment? ")
interest = input("What is the yearly interest (in percent)? ")
term = input("Over how many years? ")

result = interestCalc(investment, interest, term)

print ("The investment will grow to " + str(result))


	
