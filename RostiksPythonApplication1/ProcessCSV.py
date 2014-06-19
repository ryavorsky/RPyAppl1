import csv

def readData(fileName):
    f = open(fileName,'rb')
    schoolData = csv.reader(f, delimiter='\t')
    print str(schoolData)
    for row in schoolData:
        print row

