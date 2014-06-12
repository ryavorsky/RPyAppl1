import csv

def readData(fileName):
    schoolData = csv.reader(open(fileName,'rb'), delimiter=';')
    print('Rows: ' + str(schoolData) )
    for row in schoolData:
        print len(row) 
        print '; '.join(row)