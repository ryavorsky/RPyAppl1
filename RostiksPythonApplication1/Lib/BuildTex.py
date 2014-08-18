import shutil
import os
import subprocess

def MoveFiles(destFolder, projectDir):

    sourceFolder = projectDir + '\\Tex\\'
    inputFiles = os.listdir(sourceFolder)

    for fileName in inputFiles:
        shutil.copy2(sourceFolder + fileName, destFolder)


def SimplifyResult(subFolder):
    shutil.copy2(subFolder + '\\Result_simple.tex', subFolder + '\\Result.tex')


def CreatePdf(outputDir, subFolder, inputId, inputFileName) :

    print '\nProcessing Result.tex in ', subFolder

    os.chdir(subFolder)
    subprocess.call(['pdflatex', '-quiet', 'Result.tex'])

    # Copy the final report from the subfolder into the output folder to all reports
    shutil.copy2('Result.pdf', outputDir + '\\Res'+inputId+'.pdf')

    print '\nThe resulting PDF is created for', inputFileName


# append a TeX macro definition to the commands.tex file
def addMacros(subFolder, command, value) :

    print 'Macros:', subFolder, command, value
    fName = subFolder + '\\commands.tex'
    fileOfTexCommands = open(fName, 'a')
    line = '\\newcommand{\\' + command +'}{' + str(value) + '}\n'
    fileOfTexCommands.write(line)
    fileOfTexCommands.close()
    print 'Tex command added', '\\newcommand{\\' + command +'}{' + value + '}\n'


# Extract organization full name and Id
def MakeTitlePage(subFolder, statData) :
    data = statData[0].split('\t')
    p1 = subFolder.rfind('\\')
    p2 = subFolder.rfind('_')
    orgId = subFolder[(p1+1):p2]
    orgName = data[1].split('=')[1]
    orgName = orgName.replace('""','"').replace('""','"')
    orgName =  orgName.decode("CP1251").encode("UTF-8")

    addMacros(subFolder,'fullName', orgName)
    addMacros(subFolder,'internalId', orgId)


# Teacher names to be included in report
def buildNamesList(subFolder, statData):
    resFileName =  subFolder + '\\nameslist.tex' 
    f = open(resFileName, 'w')

    localId = 0

    for line in statData :
        localId += 1
        data = line.split('\t')
        name = data[6].split('=')[1]
        position = data[7].split('=')[1]
        resLine = '\item [' + str(localId) + '] ' + name + ', ' + position + '\n'
        f.write(resLine.decode("CP1251").encode("UTF-8"))

    f.close()


def addSizeComments(subFolder, numOfNodes) :
    if numOfNodes <= 7 :
        addMacros(subFolder, 'socioSizeComment', '\socioSizeCommentA')
    elif numOfNodes <= 11 :
        addMacros(subFolder, 'socioSizeComment', '\socioSizeCommentB')
    elif numOfNodes <= 16 :
        addMacros(subFolder, 'socioSizeComment', '\socioSizeCommentC')
    elif numOfNodes <= 21 :
        addMacros(subFolder, 'socioSizeComment', '\socioSizeCommentD')
    else :
        addMacros(subFolder, 'socioSizeComment', '\socioSizeCommentE')


def insertFileaAfterLine(fileName, addFileName, lineNum):
    f1 = open(fileName, 'r')
    f2 = open(addFileName, 'r')
    data = []
    i = 1
    for line in f1.readlines() :
        if i <> lineNum :
            data.append(line)
            i += 1
        else :
            data.append(line)
            for additionalLine in f2.readlines() :
                data.append(additionalLine)
            i += 1

    f1.close()
    f2.close()

    f1 = open(fileName, 'w')
    for dataLine in data:
        f1.write(dataLine)
    f1.close()

def replaceLineWithFile(fileName, addFileName, lineNum):
    f1 = open(fileName, 'r')
    f2 = open(addFileName, 'r')
    print 'Replacing line with a file:', fileName, addFileName, lineNum
    data = []
    i = 1
    for line in f1.readlines() :
        if i <> lineNum :
            data.append(line)
            i += 1
        else :
            for additionalLine in f2.readlines() :
                data.append(additionalLine)
            i += 1

    f1.close()
    f2.close()

    f1 = open(fileName, 'w')
    print 'Write result'
    for dataLine in data:
        print dataLine
        f1.write(dataLine)
    f1.close()
   
def insertTables(subFolder, orgSize):
    print '\nInserting tables'
    os.chdir(subFolder)
    specs = [['slide1b.tex','nameslist.tex', 5],['slide6_3.tex','table1.tex', 18],['slide7_3a.tex','table2.tex', 20],['slide7_3b.tex','table3.tex', 19],['slide7_3c.tex','table4.tex', 20],]
    for spec in specs :
        (fileName, addFileName, lineNum) = spec
        replaceLineWithFile(fileName, addFileName, lineNum)


def splitTables(subFolder, orgSize):
    print '\nInserting tables'
    os.chdir(subFolder)
    files = ['slide6_3.tex','slide7_3a.tex','slide7_3b.tex','slide7_3c.tex']

    insertFileaAfterLine('slide1b.tex', 'list_split.tex', 39)

    for fileName in files :
        insertFileaAfterLine(fileName, 'table_split.tex', 55)

    if orgSize > 76 :
        insertFileaAfterLine('slide1b.tex', 'list_split.tex', 85)

        for fileName in files :
            insertFileaAfterLine(fileName, 'table_split.tex', 105)

