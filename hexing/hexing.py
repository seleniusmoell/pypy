import csv

opened_file = open("loggning.csv", "rt")

readerObject = csv.reader(opened_file)
#writerObject = csv.writer(open("loggning2.csv", "wt"))

parsed_data = []
fields = readerObject.next()

for row in readerObject:
	parsed_data.append(row)

for item in parsed_data:
	if


opened_file.close()