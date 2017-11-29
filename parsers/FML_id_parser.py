# Script for parsing tpmadm.h for FML-id.
# This script is written by Tove Selenius Moell in Python 3
__author__ = "Tove Selenius Moell"
__copyright__ = "Copyright 2017"

field = ""
id = ""
enum = "public enum Ezx_FieldId \n {"

def addToCsharp(field, id, enum):
	enum = enum + field + ' = ' + id + ',\n'
	return enum

def isNumber(s):
	try:
		int(s)
		return True
	except ValueError:
		return False
	
with open('tpadm.h', 'r') as file:
#	print('opened file')
	
	for line in file:
		if("/*" in line and "#define" in line) :
	
			splitted = line.split()
			if len(splitted) >= 6 :
				field = splitted[1]
				id = splitted[5]
					
			#	print('Field: ' + field + ', id: ' + id)
			if isNumber(id):
				enum = addToCsharp(field, id, enum);
			

enum = enum + '}'			

with open('enum2.cs', 'w') as outfile:
	outfile.write(enum)