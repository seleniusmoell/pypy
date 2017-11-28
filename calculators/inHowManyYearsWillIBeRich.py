#!/usr/bin/env python
#This script is written by tove in Python 3.0

__author__ = "tove"
__copyright__ = "Copyright 2017"
__email__ = "seleniusmoell@gmail.com"

investment = int(input("What is the initial investment? "))
interest = int(input("What yearly interest can you expect (in percent)? "))
sum = int(input("What is the sum you are aiming at? "))
willSave = input("Will you be saving during the time? y/n ")

if willSave == "y" or willSave == "yes" or willSave == "Y" or willSave == "YES":
	additionalSavings = int(input("What amount will you save yearly? "))
elif willSave == "n" or willSave == "no" or willSave == "N" or willSave =="NO":
	additionalSavings = 0
else:
	willSave = input("Please answer yes or no")

years = 0

while investment < sum:
	investment = investment + investment*(interest*0.01) + additionalSavings
	years = years + 1
	
print ("You will have reached your desired sum in " + str(years) + " years")