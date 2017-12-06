import csv

with open("Data/teams.csv", 'rb') as csvfile:
	reader = csv.reader(csvfile)
	outfile = open("teams.sql", 'w')
	for row in reader:
		sqlString = 'Insert into Team values('
		for part in row:
			part = part.replace('\'', '\\\'')
			if len(part) == 0:
				sqlString += ('NULL,')
			else:
				for_name_only = part.split('\\')
				sqlString += ('\'' + for_name_only[0] + '\'' + ',')
		sqlString = sqlString[:-1]
		sqlString += ');\n'
		outfile.write(sqlString)
	outfile.close()


