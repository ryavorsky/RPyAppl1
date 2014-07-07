import os

def dataFromFile(inputFileName, outputFolder):

    # extract input file Id and create folder for the results
    inputId = os.path.basename(inputFileName).split('.')[0].split('_')[1]
    subFolder = outputFolder + '\\' + inputId + '_files'
    os.mkdir(subFolder)
    print subFolder, ' is created for ', inputId

    resFileName =  subFolder + '\\res_' + inputId + '.txt'
    f_out = open(resFileName, 'w')

    f_in = open(inputFileName, 'r')
    f_in.readline() 

    graphData = []

    for line in  f_in:
        
        seq =  line.split('\t') #  Id - LocalId - full name - answers - comment

        if (len(seq)>3):
            if (len(seq[3])) > 20: # the answers
                id = seq[1]
                name = seq[2]
                dataString = seq[3].replace('" ','"') 
                age = extractAge(dataString)
                edgeGroups = extractEdges(dataString)

                graphData.append([ id, name, age, edgeGroups ])

                f_out.write(str([ id, age, edgeGroups ]) + '\n')

    f_in.close()
    f_out.close()

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
        