import os
import shutil
import BuildTex
import StatValues

def dataFromFile(inputFileName, inputId, outputFolder, subFolder):
    print '\nParsing file:', inputFileName
    print 'Input ID:', inputId
    print 'Folders:', outputFolder, subFolder

    keys = extractKeys(subFolder)
    print '\nKey:'
    for e in keys :
        print e

    f_in = open(inputFileName, 'r')
    f_data = open(subFolder + '\\data.txt', 'w')

    graphData = []
    statData = []
    toprow = f_in.readline()
    localId = 0

    for line in f_in.readlines() :
        dataline = extractDataLine(line, keys)
        statData.append(dataline)
        f_data.write(dataline + '\n')

        localId += 1
        graphline = extractGraphDataBlock(dataline, localId)
        graphData.append(graphline)

    f_in.close()
    f_data.close()

    # Filter graph data according to the Nodes number
    graphData = restrictOutEdges(graphData)

    return [graphData, statData]


def extractGraphDataBlock(dataline, localId) :

    id = StatValues.extractAnswers([dataline], [5])[0]
    name = StatValues.extractAnswers([dataline], [6])[0]
    position = StatValues.extractAnswers([dataline], [7])[0]
    year = StatValues.extractAnswers([dataline], [14])[0]
    if len(year) == 4 :
        age = 2014 - int(year)
    else :
        age = 0
        print 'Age is unknown for', id, name

    edgeGroups = extractEdgeGroups(dataline)

    return [ id, str(localId), name + position, age, edgeGroups ]


# nine sequences of edge targets for the nine questions
def extractEdgeGroups(dataline):
    data = dataline.split('\t')
    res = []
    for i in range(9) : # there are 9 quesions
        group = []
        for k in range(5) : # max 5 answers
            questionId = 62 + 10*i + k*2 + 1
            node = data[questionId].split('=')[1]
            if len(node) > 1 :
                group.append(node)
        res.append(group)
    print '\nEdge groups', res
    return res


# for small schools truncate the socio answers
def restrictOutEdges(graphData):
    # first, compute the restriction  
    numOfNodes = len(graphData)
    if numOfNodes <= 7 :
        maxNumOfEdges = 0
    elif numOfNodes <= 11 :
        maxNumOfEdges = 2
    elif numOfNodes <= 16 :
        maxNumOfEdges = 3
    elif numOfNodes <= 21 :
        maxNumOfEdges = 4
    else :
        maxNumOfEdges = 5

    for node in range(len(graphData)):
        for question in range(9) :
            graphData[node][4][question] = graphData[node][4][question][0:(maxNumOfEdges)]

    return graphData


def extractKeys(subFolder) :

    print '\nExtracting keys'
    res = []    
    f = open (subFolder + '\\key.txt', 'r')
    line = f.readline() # skip the table header
    for line in f.readlines() :
        res.append( line.split('\t') )
    f.close()
    return res


def extractDataLine(line, keys):
    res = line.split(';')

    if len(res) == len(keys) :
        for i in range(len(res)) :
            res[i] = extractDataValue(res[i], keys[i])
        print '\nExtracted data line', res
        return '\t'.join(res)
    else :
        print 'Keys lenght is wrong', len(res), len(keys)


def extractDataValue(value, key):
    listId = int(key[2])
    questionId = 'q' + key[0]

    res = value.strip()
    if listId != 0 and value != '':
        options = key[3].strip().split(';')
        optionId = [option.split(':')[0] for option in options]
        optionVal = [option.split(':')[1].strip() for option in options]
        for i in range(len(options)) :
            if res == optionVal[i] :
                res = optionId[i]
        
    return questionId + '=' + res


# Split the big input file into collection of files per school
def SplitBySchool():
    inFileName = 'C:\\Direktor\\tumen_clean.csv'
    resDir = 'C:\\Direktor\\Input\\All'
    f = open(inFileName, 'r')
    f1 = open(resDir + '\\topline.txt', 'w')

    toprow = f.readline()
    f1.write(toprow)

    school = ''
    schoolId = 0 

    for line in f.readlines() :
        data = line.split(';')
        schoolName = data[0] + data[1]
        if schoolName == school :
            f1.write(line)
        else :
            f1.close()
            schoolId += 1
            school = schoolName
            f1 = open(resDir + '\\exp_' + str(schoolId) + '.txt', 'w')
            print schoolId, schoolName
            f1.write(toprow)
            f1.write(line)

    f1.close()
    f.close()


def renameAndSortBySize() :
    inDir = 'C:\\Direktor\\Input\\All'
    smallDir = inDir + '\\Small\\'
    medDir = inDir + '\\Med\\'
    bigDir  = inDir + '\\Big\\'
    miscDir  = inDir + '\\Misc\\'
    os.mkdir(smallDir)
    os.mkdir(medDir)
    os.mkdir(bigDir)
    os.mkdir(miscDir)
    print 'A'
    for fileName in os.listdir(inDir):
        if fileName.find('.txt') > 0: 
            print 'Dir', inDir, 'File', fileName
            f0 = open(inDir + '\\' + fileName, 'r')
            size = len(f0.readlines()) - 1
            f0.close()
            print fileName, size
            if size > 35 :
                targetDir = bigDir
            elif size > 7 :
                targetDir = medDir
            elif size > 1 :
                targetDir = smallDir
            else :
                targetDir = miscDir
            shutil.copy2(inDir + '\\' + fileName, targetDir)


def getId():
    inDir = 'C:\\Direktor\\Input\\All'
    smallDir = inDir + '\\Small'
    medDir = inDir + '\\Med'
    bigDir  = inDir + '\\Big'
    miscDir  = inDir + '\\Misc'
    os.mkdir(smallDir)
    os.mkdir(medDir)
    os.mkdir(bigDir)
    os.mkdir(miscDir)

    inFile = 'C:\\Direktor\\Input\\oldcodes.txt'
    f2 = open(inFile, 'r')
    d = dict()
    for line in f2.readlines() :
        [code, id] = line.split('\t')
        d[code] = id.replace('\n','')
        print 'id', id

    f2.close()

    resFile = 'C:\\Direktor\\Input\\codes.txt'
    f1 = open(resFile, 'w')
    for fileName in os.listdir(inDir):
        if fileName.find('.txt') > 0: 

            # Classify the size
            print 'Dir', inDir, 'File', fileName
            f0 = open(inDir + '\\' + fileName, 'r')
            size = len(f0.readlines()) - 1
            f0.close()
            print fileName, size
            if size > 35 :
                targetDir = bigDir
            elif size > 7 :
                targetDir = medDir
            elif size > 1 :
                targetDir = smallDir
            else :
                targetDir = miscDir

            f0 = open(inDir + '\\' + fileName, 'r')
            header = f0.readline()
            data = f0.readline().split(';')
            f0.close()
            if len(data) >= 6 :
                code = data[1]+':'+data[6]+':'+data[0]
                code = code.replace(' ','')
                code = code.replace('&quot;','')
                code = code.replace('"','')
                newId = d.get(code, 'ERR')
                f1.write(code + '\n')

                if newId == 'ERR' :
                    shutil.copy2(inDir + '\\' + fileName, miscDir)
                else :
                    newName = targetDir +'\\export_'+newId+'.txt' 
                    shutil.copy2(inDir + '\\' + fileName, newName)
    f1.close()


def getMisc():
    inDir = 'C:\\Direktor\\Input\\All\\Misc'
    f0 = open('C:\\Direktor\\misc.txt', 'w')
    os.chdir(inDir)

    for fileName in os.listdir(inDir):
        f1 = open(fileName, 'r')
        head = f1.readline()
        line = f1.readline().split(';')
        size = len(f1.readlines()) + 1
        f1.close()
        f0.write(fileName + ';' + str(size) + ';' + ';'.join(line[0:7]) + '\n')

    f0.close()


def getMiscId():

    f0 = open('C:\\Direktor\\key_misc.txt', 'r')
    d = dict()
    for line in f0.readlines() :
        [code, id] = line.split('\t')
        d[code] = id.replace('\n','')
    f0.close()

    print d

    inDir = 'C:\\Direktor\\Input\\All\\Misc'
    os.chdir(inDir)

    for fileName in os.listdir(inDir):
        newName = d.get(fileName, 'ERR')
        print newName
        shutil.copy2(fileName, 'C:\\Direktor\\Input\\All\\Last\\' + newName)

