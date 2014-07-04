# This is main file for the data analysis project

# The inputDir should countain the data files
# The outputDir will be created (with timestamp to avoid clushes)

import sys
import time
import os
import CheckFolders
import BuildGraphs
import ParseInput
import BuildTex

inputDir = 'c:\\Direktor\\Input\\2'
outputDir = 'c:\\Direktor\\Output\\2'

outputDir = CheckFolders.TestDirs(inputDir, outputDir)

for inputFileName in os.listdir(inputDir):

    [inputId, subFolder, graphData] = ParseInput.dataFromFile(inputDir + '\\' + inputFileName, outputDir)
    graphObject = BuildGraphs.makeGraph(graphData)
    BuildGraphs.vizualizeGraph(inputId, subFolder, graphObject)
    BuildTex.MoveFiles(subFolder)


# Create resulting reports

#import WriteFiles
#WriteFiles.writeTestFiles(outputDir)

#import BuildHtml
#BuildHtml.writeHtmlReport(outputDir, 'testRes.htm')

# Create graphics for the reports 

#import BuildGraphs
#BuildGraphs.testDiagram(outputDir)


# Done! Now can speak to the world

print('Hello World!\n See the results in ' + outputDir)
