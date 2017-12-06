import csv

files = ['Data/2014-15', 'Data/2015-16', 'Data/2016-17']

for file in files:
	with open(file+".csv", 'rb') as csvfile:
		reader = csv.reader(csvfile)
		outfile = open(file+".sql", 'w')
		for row in reader:
			sqlString = 'Insert into Player values('
			season = file.split('/')[1]
			sqlString += ('\'' + season +'\'' + ',')
			for part in row:
				part = part.replace('\'', '\\\'')
				if len(part) == 0:
					sqlString += ('NULL,')
				else :
					for_name_only = part.split('\\')
					sqlString += ('\'' + for_name_only[0] +'\'' + ',')
			sqlString = sqlString[:-1]
			sqlString += ');\n'
			outfile.write(sqlString)
		outfile.close()


