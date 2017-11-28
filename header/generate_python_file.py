import datetime
 
docname=input('Document name: ') +'.py'
description=input('File description') 
author=input('Author: ')
version=str(input('Python version: '))
while not (version[0] == '2' or version[0] == '3'):
	input('Please choose a valid version of Python. Eg: 3.0 \n Python version:')

now = datetime.datetime.now()
copyright = 'Copyright ' + str(now.year)
email=input('Email: ')

if email is not "" {
	while '@' not in email:
		email=input('That can\'t be right. Try again. \n Email:')
	}
	
headerstrings = {'description':description, 'version':version, 'author':author, 'copyright':copyright, 'email':email}
file = open(docname, 'w')

for key, value in headerstrings.items():
	
	hs = ''
	if 'version' not in key:
		hs = '__' + key + '__' + ' = "' + value + '"\n'
	else:
		hs = '# This script is written by ' + author + ' in Python ' + value + '\n'
	
	file.write(hs)
	



