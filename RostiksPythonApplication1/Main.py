# This is main file for the data analysis project

# The inputDir should countain the data files
# The outputDir will be created (with timestamp to avoid clushes)

import sys
import time
import os
import subprocess

import CheckFolders
import ParseInput
import BuildGraphs
import BuildTex

inputDir = 'c:\\Direktor\\Input\\4'
outputDir = 'c:\\Direktor\\Output\\4'

outputDir = CheckFolders.TestDirs(inputDir, outputDir)

for inputFileName in os.listdir(inputDir):

    print '\n Processing input file ' + inputFileName

    [inputId, subFolder, graphData] = ParseInput.dataFromFile(inputDir + '\\' + inputFileName, outputDir)

    # Create graphics for the reports 
    graphObject = BuildGraphs.makeGraph(graphData)
    BuildGraphs.vizualizeGraph(inputId, subFolder, graphObject)

    # Create resulting reports
    BuildTex.MoveFiles(subFolder)
    os.chdir(subFolder)
    print '\nProcessing Result.tex in ', subFolder
    subprocess.call(['pdflatex', '-quiet', 'Result.tex'])
    print inputFileName, ': done!'

# Done! Now can speak to the world
print('\nSee the results in ' + outputDir)

a = []

