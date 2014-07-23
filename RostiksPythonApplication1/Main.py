# This is main file for the data analysis project

# The inputDir should countain the data files
# The outputDir will be created (with timestamp to avoid clushes)

import os
import CheckFolders
import BuildAll

def main() :

    # Change here!
    inputDir = 'c:\\Direktor\\Input\\all'
    outputDir = 'c:\\Direktor\\Output\\all'

    outputDir = CheckFolders.TestDirs(inputDir, outputDir)

    for inputFileName in os.listdir(inputDir):

        BuildAll.makeReport(inputDir + '\\' + inputFileName, outputDir)

    print('\nSee the final results in ' + outputDir)

main()