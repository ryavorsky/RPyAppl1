import os
import BuildTex

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

    for line in f_in.readlines() :
        dataline = extractDataLine(line, keys)
        statData.append(dataline)
        f_data.write(dataline + '\n')

    f_in.close()
    f_data.close()

    return [graphData, statData]


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



def dataFromFile_old(inputFileName, inputId, outputFolder, subFolder):

    print 'Parsing', inputFileName

    # extract input file Id 
    inputId = os.path.basename(inputFileName).split('.')[0].split('_')[1]
    subFolder = outputFolder + '\\' + inputId + '_files'
    
    resFileName =  subFolder + '\\nameslist.tex' # Teacher names to be included in report
    f_in = open(inputFileName, 'r')
    f_namelist = open(resFileName, 'w')
    f_data = open(subFolder + '\\data.txt', 'w')
  
    graphData = []
    statData = []

    localId = 0 # id of a peson in his orhanization

    # use the first line of the input file to build title page
    firstLine = f_in.readline()
    MakeTitlePage(firstLine, subFolder)

    for line in  f_in:
        
        seq =  line.split('\t') #  Id - LocalId - full name - answers - comment

        if (len(seq)>3): # exclude lines with no data
            if (len(seq[3])) > 20: # the answers
                id = seq[1]
                localId += 1
                name = seq[2]
                dataString = seq[3].replace('" ','"') 
                age = extractAge(dataString)
                edgeGroups = extractEdges(dataString) # nine sequences of edge targets for the nine questions

                graphData.append([ id, str(localId), name, age, edgeGroups ])

                # Save the name list into the Tex file
                resLine = '\item [' + str(localId) + '] ' + name + '\n'
                f_namelist.write(resLine.decode("CP1251").encode("UTF-8"))

                # Now extract the statistical data
                data = seq[3]
                for i in range(20):
                    s = 's:'+str(i+1) + ':'
                    data = data.replace(s,'')
                data = data.replace('i:0;','').replace('i:1;','').replace('i:2;','').replace('i:3;','').replace('i:4;','').replace('i:5;','')
                data = data.replace('a:0:','').replace('a:1:','').replace('a:2:','').replace('a:3:','').replace('a:4:','').replace('a:5:','')
                data = data.replace(';"Q_','*"q').replace(';','=').replace('*',';').replace('}"Q_','};"q').replace('{"Q_','{;"q').replace(';','\t')
                ln = data.find('q6') - 2
                data = data[7:ln]
                data = data.replace('"','')

                statData.append(data)

                f_data.write( data + '\n')
   
    print '\nStat data', statData

    f_in.close()
    f_namelist.close()
    f_data.close()

    # Save the number of participated
    BuildTex.addMacros(subFolder, 'nParticipated', str(len(graphData)))

    return [graphData, statData]


# extract connections for the current respondee
def extractEdges(s0):

    edgeGroups = [] #list of lists of pairs
    
    seq = s0.split('Q_6') # search for Q_60, Q_61, Q_61, ... and split

    for i in range(len(seq) - 1):   
        edgeTargets = [] # list of edge targets 
        for s in seq[i+1].split(';'):
            if len(s) > 9:
                target = s.replace('s:5:','').replace('s:4:','').replace('\"','')
                edgeTargets.append(target)
        edgeGroups.append(edgeTargets)
    
    if len(edgeGroups) == 8 :
        edgeGroups.insert(1,[])

    print 'Edge groups size ', len(edgeGroups), 'parsed for', s0[0:32] + '...'
    return edgeGroups


# Extract organization full name and Id
def MakeTitlePage(firstLine, subFolder) :

    [orgId, orgName] = firstLine.split('\t')

    orgName.replace('quot;','')
    orgName =  orgName.decode("CP1251").encode("UTF-8")
    BuildTex.addMacros(subFolder,'fullName', orgName)

    orgId = orgId.split('=')[1]
    BuildTex.addMacros(subFolder,'internalId', orgId)
    
# extract age of the respondee
def extractAge(str):
    yearInd = str.find(':"19') + 2
    year = str[ yearInd : (yearInd+4) ]
    age = 2014 - int(year)
    return age

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

