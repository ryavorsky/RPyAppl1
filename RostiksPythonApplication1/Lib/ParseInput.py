import os

def dataFromFile(inputFileName, otputFolder):

    f1 = open(inputFileName, 'r')
    f1.readline()

    inputId = os.path.basename(inputFileName).split('.')[0].split('_')[1]
    subFolder = otputFolder + '\\' + inputId + '_files'
    os.mkdir(subFolder)

    resFileName =  subFolder + '\\res_' + inputId + '.txt'
    print subFolder, '--', inputId
    f2 = open(resFileName, 'w')
    graphData = []

    for line in  f1:
        
        seq =  line.split('\t') #  Id - LocalId - full name - answers - comment

        if len(seq[3]) > 20:

            id = seq[1]
            name = seq[2]
            age = extractAge(seq[3])
            edgeGroups = extractEdges(seq[3])

            graphData.append([ id, name, age, edgeGroups ])
            f2.write(str(graphData))

    f1.close()
    f2.close()

    return [inputId,subFolder, graphData]


# extracxt age of the respondee
def extractAge(str):
    yearInd = str.find(':"19') + 2
    year = str[ yearInd : (yearInd+4) ]
    age = 2014 - int(year)
    return age


# extract connections for the current respondee
def extractEdges(str):

    edgeGroups = [] #list of lists of pairs
    
    seq1 = str.split('Q_6') # search for Q_60, Q_61, Q_61, ...
    
    for i in range(len(seq1) - 1):
        edges = [] # list of pairs 
        for str1 in seq1[i+1].split(';'):
            if len(str1) > 9:
                edges.append(str1.replace('s:5:','').replace('\"',''))
        edgeGroups.append(edges)

    return edgeGroups
        