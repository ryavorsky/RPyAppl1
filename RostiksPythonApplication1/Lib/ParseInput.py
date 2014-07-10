import os

def dataFromFile(inputFileName, outputFolder):

    # extract input file Id and create folder for the results
    inputId = os.path.basename(inputFileName).split('.')[0].split('_')[1]
    subFolder = outputFolder + '\\' + inputId + '_files'
    os.mkdir(subFolder)
    print subFolder, ' is created for ', inputId

    # initialize all
    resFileName =  subFolder + '\\names.tex'
    f_in = open(inputFileName, 'r')
    f_out = open(resFileName, 'w')

    socioData = []
    localId = 0

    # use the first line to build title.tex
    MakeTitle(f_in.readline(), subFolder + '\\title.tex')

    for line in  f_in:
        
        seq =  line.split('\t') #  Id - LocalId - full name - answers - comment

        if (len(seq)>3): # exclude lines with comments
            if (len(seq[3])) > 20: # the answers
                id = seq[1]
                localId += 1
                name = seq[2]
                dataString = seq[3].replace('" ','"') 
                age = extractAge(dataString)
                edgeGroups = extractEdges(dataString) # nine sequences of edge targets for the nine questions

                socioData.append([ id, str(localId), name, age, edgeGroups ])

                resLine = '\item [' + str(localId) + '] ' + name + '\n'
                f_out.write(resLine.decode("CP1251").encode("UTF-8"))

    f_in.close()
    f_out.close()

    return [inputId,subFolder, socioData]


# extracxt age of the respondee
def extractAge(str):
    yearInd = str.find(':"19') + 2
    year = str[ yearInd : (yearInd+4) ]
    age = 2014 - int(year)
    return age


# extract connections for the current respondee
def extractEdges(str):

    edgeGroups = [] #list of lists of pairs
    
    seq = str.split('Q_6') # search for Q_60, Q_61, Q_61, ... and split

    for i in range(len(seq) - 1):   
        edgeTargets = [] # list of edge targets 
        for s in seq[i+1].split(';'):
            if len(s) > 9:
                target = s.replace('s:5:','').replace('s:4:','').replace('\"','')
                edgeTargets.append(target)
        edgeGroups.append(edgeTargets)
    
    if len(edgeGroups) == 8 :
        edgeGroups.insert(1,[])

    print 'Edge Groups size ', len(edgeGroups)
    return edgeGroups
        
def MakeTitle(str, fileName) :
    f = open(fileName, 'w')
    data = str.split('\t')
    res = '\\title[' + data[0] + '] {' + data[1] + '}'
    print fileName, res
    f.write(res.decode("CP1251").encode("UTF-8"))
    f.close()
