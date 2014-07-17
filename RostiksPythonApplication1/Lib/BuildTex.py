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

def addMacros(subFolder, command, value) :

    print 'Macros:', subFolder, command, value
    fName = subFolder + '\\commands.tex'
    fileOfTexCommands = open(fName, 'a')
    line = '\\newcommand{\\' + command +'}{' + str(value) + '}\n'
    fileOfTexCommands.write(line)
    fileOfTexCommands.close()
    print 'Tex command added', '\\newcommand{\\' + command +'}{' + value + '}\n'
