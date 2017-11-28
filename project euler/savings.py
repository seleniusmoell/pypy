theOneString = "<html> \n"

'''
 Head element
'''
theOneString += " <head> \n <title> \n  Sparande </title> \n </head> \n"
theOneString += "<link rel='stylesheet' type='text/css' href='sparande.css'>"

'''
 Body element
'''
theOneString += " <body> \n"

# Header
theOneString += "<h1> Tove och Viktors sparande </h1> \n"

'''
 Stapel
'''
goal = 500000

# Make dictionary based on variables.txt
v = open('variables.csv', 'r+')
variables = {}
for line in v:
	items = line.split()
	key, value = items[0], int(items[1])
	variables[key] = value
print(variables)
current_amount = variables['current_amount']
procent_factor = 3
stapel_full_width  = 100 * 3
stapel_current_width = current_amount / goal * 100

theOneString += '<style> stapel_yttre { width: ' + stapel_full_width + ';} </style> \n'

theOneString += '<div class = "stapel_yttre"> </div> \n'



'''
End tags
'''

theOneString += "</body> \n <html>"

html_file = open('sparande.html','w')
html_file.write(theOneString)
html_file.close()