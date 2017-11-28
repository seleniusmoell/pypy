# Script för parsing the tpadm.h file of a Tuxedo installation for file ID:s,
# returning a C# enum
# This script is written by Tove Selenius Moell in Python 3
__author__ = "Tove Selenius Moell"
__copyright__ = "Copyright 2017"
__email__ = "seleniusmoell@gmail.com"

field = ""
id = ""
file = open('tpadm.h', r)

for line in file:
	if("#define" in line) {
		splitted = line.split()
		if (len(splitted) > 2){
			field = splitted[1]
			id = splitted[2]
			
			if ( 'FLDID' in splitted[2]){
				#tvätta
			}
			addToCsharp(field, id);
		}
			
	
