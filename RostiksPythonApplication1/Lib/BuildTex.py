import shutil
import os
import subprocess

def MoveFiles(destFolder):

    sourceFolder = 'c:\\Direktor\\Tex\\'
    inputFiles = os.listdir(sourceFolder)

    for fileName in inputFiles:
        shutil.copy2(sourceFolder + fileName, destFolder)

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
    orgName = data[0].split('=')[1]
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

