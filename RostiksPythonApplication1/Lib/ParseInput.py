import os
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

    return [graphData, statData]


def extractGraphDataBlock(dataline, localId) :

    id = StatValues.extractAnswers([dataline], [5])[0]
    name = StatValues.extractAnswers([dataline], [6])[0]
    position = StatValues.extractAnswers([dataline], [7])[0]
    year = StatValues.extractAnswers([dataline], [14])[0]
    age = 2014 - int(year)

    edgeGroups = extractEdgeGroups(dataline)

    return [ id, str(localId), name + position, age, edgeGroups ]


# nine sequences of edge targets for the nine questions
def extractEdgeGroups(dataline):
    data = dataline.split('\t')
    res = []
    for i in range(9) :
        group = []
        for k in range(5) :
            questionId = 62 + 10*i + k*2 + 1
            node = data[questionId].split('=')[1]
            if len(node) > 1 :
                group.append(node)
        res.append(group)
    print '\nEdge groups', res
    return res


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
def SplitBySchool(inFileName, outputDir) :
    f = open(inFileName, 'r')
    f1 = open(outputDir + 'topline.txt', 'w')

    toprow = f.readline()
    f1.write(toprow)

    school = ''
    schoolId = 0 

    for line in f.readlines() :
        data = line.split(';')
        schoolName = data[1]
        if schoolName == school :
            f1.write(line)
        else :
            f1.close()
            schoolId += 1
            school = schoolName
            f1 = open(outputDir + 'exp_' + str(schoolId) + '.txt', 'w')
            print schoolId, schoolName
            f1.write(toprow)
            f1.write(line)

    f.close()

