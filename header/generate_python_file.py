import datetime
 
docname=input('Document name: ') +'.py'
description=input('File description: ') 
author=input('Author: ')
version=str(input('Python version: '))
while not (version[0] == '2' or version[0] == '3'):
	input('Please choose a valid version of Python. Eg: 3.0 \n Python version:')

now = datetime.datetime.now()
copyright = 'Copyright ' + str(now.year)
email=input('Email: ')

if email is not "" :
	while '@' not in email:
		email=input('That can\'t be right. Try again. \n Email:')
	
	
headerstrings = {'author':author, 'copyright':copyright, 'email':email}

with open(docname, 'w') as file:
	file.write('# ' + description + '\n')
	file.write('# This script is written by ' + author + ' in Python ' + version + '\n')

	for key, value in headerstrings.items():
		file.write('__' + key + '__' + ' = "' + value + '"\n')
		



