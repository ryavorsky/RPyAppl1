# This is main file for the data analysis project

# The inputDir should countain the data files
# The outputDir will be created (with timestamp to avoid clushes)

inputDir = 'c:\\Direktor\\Input\\1'
outputDir = 'c:\\Direktor\\Output\\1'

import CheckFolders
outputDir = CheckFolders.TestDirs(inputDir, outputDir)

import ProcessCSV
ProcessCSV.readData(inputDir + '\\38408_FCA.csv' )

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
