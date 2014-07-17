import os
import BuildTex

def dataFromFile(inputFileName, inputId, outputFolder, subFolder):

    # extract input file Id 
    inputId = os.path.basename(inputFileName).split('.')[0].split('_')[1]
    subFolder = outputFolder + '\\' + inputId + '_files'
    
    resFileName =  subFolder + '\\nameslist.tex' # Teacher names to be included in report
    f_in = open(inputFileName, 'r')
    f_namelist = open(resFileName, 'w')
    f_data = open(subFolder + '\\data.txt', 'w')
  
    graphData = []
    statData = []

    statDataDict = dict()
    for i in range(9,60) :
        statDataDict['q' + str(i)] = []
    localId = 0 # id of a peson in his orhanization


    print 'Parse input initialized'

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
                data = data.replace('s:1:','').replace('s:2:','').replace('s:3:','').replace('s:4:','').replace('s:5:','').replace('s:6:','').replace('s:7:','').replace('s:8:','')
                data = data.replace('i:0;','').replace('i:1;','').replace('i:2;','').replace('i:3;','').replace('i:4;','').replace('i:5;','')
                data = data.replace('a:0:','').replace('a:1:','').replace('a:2:','').replace('a:3:','').replace('a:4:','').replace('a:5:','')
                data = data.replace(';"Q_','*"q').replace(';','=').replace('*',';').replace('}"Q_','};"q').replace('{"Q_','{;"q').replace(';','\t')
                ln = data.find('q6') - 2
                data = data[7:ln]
                data = data.replace('"','')

                statData.append(data)

                f_data.write( data + '\n')

                for i in range(9,60) :
                    q = 'q' + str(i)
                    p_start = data.find(q)
                    if p_start >= 0 :
                        s = data[p_start:(p_start+100)].split('\t')[0]
                        s = s.split('=')[1]
                        if s.find('{') == -1 :
                            statDataDict[q]= statDataDict[q] + [s]
    
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
    
# extracxt age of the respondee
def extractAge(str):
    yearInd = str.find(':"19') + 2
    year = str[ yearInd : (yearInd+4) ]
    age = 2014 - int(year)
    return age
