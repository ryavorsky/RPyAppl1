# This is main file for the data analysis project

# The inputDir should countain the data files
# The outputDir will be created (with timestamp to avoid clushes)

inputDir = 'c:\\Direktor\\Input\\1'
outputDir = 'c:\\Direktor\\Output\\1'

import CheckFolders
outputDir = CheckFolders.TestDirs(inputDir, outputDir)

inputList = ['1','3','5']

for fileName in inputList:
    f = open(outputDir + '\\' + fileName + '.txt','w')
    f.write('test ' + fileName)
    f.close()

print('Hello World\n' + outputDir)
