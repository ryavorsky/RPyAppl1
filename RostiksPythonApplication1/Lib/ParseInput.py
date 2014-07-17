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
    f_title = open(resFileName, 'w')
    f_data = open(subFolder + '\\data.txt', 'w')
  

    graphData = []
    statData = dict()
    for i in range(9,60) :
        statData['q' + str(i)] = []
    localId = 0
    print 'Parse input initialized'

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

                graphData.append([ id, str(localId), name, age, edgeGroups ])

                resLine = '\item [' + str(localId) + '] ' + name + '\n'
                f_title.write(resLine.decode("CP1251").encode("UTF-8"))

                data = seq[3]
                data = data.replace('s:1:','').replace('s:2:','').replace('s:3:','').replace('s:4:','').replace('s:5:','').replace('s:6:','').replace('s:7:','').replace('s:8:','')
                data = data.replace('i:0;','').replace('i:1;','').replace('i:2;','').replace('i:3;','').replace('i:4;','').replace('i:5;','')
                data = data.replace('a:0:','').replace('a:1:','').replace('a:2:','').replace('a:3:','').replace('a:4:','').replace('a:5:','')
                data = data.replace(';"Q_','*"q').replace(';','=').replace('*',';').replace('}"Q_','};"q').replace('{"Q_','{;"q').replace(';','\t')
                ln = data.find('q6') - 2
                data = data[7:ln]
                data = data.replace('"','')

                f_data.write( data + '\n')

                for i in range(9,60) :
                    q = 'q' + str(i)
                    p_start = data.find(q)
                    if p_start >= 0 :
                        s = data[p_start:(p_start+100)].split('\t')[0]
                        s = s.split('=')[1]
                        if s.find('{') == -1 :
                            statData[q]= statData[q] + [s]
                            f_data.write( s + '\n')
    
    print '\nStat data'
    for i in range(9,60) :
        q = 'q' + str(i)
        print '\t', q, ' => ', statData[q]

    f_in.close()
    f_title.close()
    f_data.close()

    socioData = []
    return [inputId, subFolder, graphData, socioData]



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
        
def MakeTitle(str, fileName) :
    f = open(fileName, 'w')
    data = str.split('\t')
    res = '\\title[' + data[0].replace('OrgId=','\docId\  \No\  T-') + '] {' + data[1].replace('quot;','') + '}'
    f.write(res.decode("CP1251").encode("UTF-8"))
    f.close()

    
# extracxt age of the respondee
def extractAge(str):
    yearInd = str.find(':"19') + 2
    year = str[ yearInd : (yearInd+4) ]
    age = 2014 - int(year)
    return age
