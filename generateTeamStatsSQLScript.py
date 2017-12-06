import csv

with open("Data/[Team]2014-17.csv", 'rb') as csvfile:
	reader = csv.reader(csvfile)
	outfile = open("teamstats.sql", 'w')
	for row in reader:
		sqlString = 'Insert into TeamStats values('
		for part in row:
			part = part.replace('\'', '\\\'')
			if len(part) == 0:
				continue
			else:
				for_name_only = part.split('\\')
				sqlString += ('\'' + for_name_only[0] + '\'' + ',')
		sqlString = sqlString[:-1]
		sqlString += ');\n'
		outfile.write(sqlString)
	outfile.close()


