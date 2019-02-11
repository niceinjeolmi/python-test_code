import csv

with open('test.csv', mode='w') as csvFile:
	fieldnames = ['ep','seq','scene','shot','note']
	writer = csv.DictWriter(csvFile, fieldnames=fieldnames)
	writer.writeheader()
	writer.writerow({'ep':'1','seq':'CAR', 'scene':'FOO', 'shot':'0010', 'note':'cg car'})
	writer.writerow({'ep':'1','seq':'CAR', 'scene':'FOO', 'shot':'0020', 'note':'add dust'})
	writer.writerow({'ep':'1','seq':'CAR', 'scene':'BAR', 'shot':'0010', 'note':'cg car, add dust'})
