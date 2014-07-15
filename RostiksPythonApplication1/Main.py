# This is main file for the data analysis project

# The inputDir should countain the data files
# The outputDir will be created (with timestamp to avoid clushes)

import sys
import time
import os
import subprocess
import shutil

import CheckFolders
import ParseInput
import BuildGraphs
import Charts
import BuildTex

inputDir = 'c:\\Direktor\\Input\\1'
outputDir = 'c:\\Direktor\\Output\\1'

outputDir = CheckFolders.TestDirs(inputDir, outputDir)

for inputFileName in os.listdir(inputDir):

    print '\n Processing input file ' + inputFileName

    [inputId, subFolder, socioData] = ParseInput.dataFromFile(inputDir + '\\' + inputFileName, outputDir)

    # Create graphics for the reports 
    graphObject = BuildGraphs.makeGraphObject(socioData)
    BuildGraphs.vizualizeGraph(inputId, subFolder, graphObject)

    Charts.BuildChart(subFolder, [1,2,3,2,3,1,0,2,3,2,1,0])

    # Create resulting reports
    BuildTex.MoveFiles(subFolder) # First, move the Tex files to the subfolder 

    print '\nProcessing Result.tex in ', subFolder
    os.chdir(subFolder)
    subprocess.call(['pdflatex', '-quiet', 'Result.tex'])
    shutil.copy2('Result.pdf', outputDir + '\\Res'+inputId+'.pdf')
    print inputFileName, ': the resulting PDF is created!'

# Done! Now can speak to the world
print('\nSee the final results in ' + outputDir)

a = []

