import csv
"""
This is a simple csv-parser meant to take comma separated data is hexadecimal format
and output sorted data in decimal format. Note that the inputted csv-file must not
be opened in microsoft excel before running this parser, as excel destroys the original
comma-separated format
"""

opened_file = open("log.csv", "rt") # open the file

readerObject = csv.reader(opened_file)
writerObject = csv.writer(open("log_output.csv", "wt"))

parsed_data = []  # data will be saved in an array of lists 

for row in readerObject:
	parsed_data.append(row)

for list in parsed_data:
	temp_list = []
	for item in list:
		if isinstance(item, str):
			if item [:4] != 'Idle': # every list that is not a comment will be written to the output file
				print(int(item, 16))
				temp_list.append(int(item, 16))
	writerObject.writerow(temp_list)

opened_file.close() # close file