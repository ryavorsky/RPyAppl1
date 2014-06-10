# This is main file for the data analysis project

# The inputDir should countain the data files
# The outputDir will be created (with timestamp to avoid clushes)

inputDir = 'c:\\Direktor\\Input\\1'
outputDir = 'c:\\Direktor\\Output\\1'

import CheckFolders
outputDir = CheckFolders.TestDirs(inputDir, outputDir)

import WriteFiles
WriteFiles.writeTestFiles(outputDir)

import BuildGraphs
BuildGraphs.testDiagram(outputDir)

print('Hello World\n' + outputDir)
