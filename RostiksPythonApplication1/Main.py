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

def main() :
    inputDir = 'c:\\Direktor\\Input\\all'
    outputDir = 'c:\\Direktor\\Output\\all'

    outputDir = CheckFolders.TestDirs(inputDir, outputDir)

    for inputFileName in os.listdir(inputDir):

        print '\n Processing input file ' + inputFileName

        [inputId, subFolder, graphData] = ParseInput.dataFromFile(inputDir + '\\' + inputFileName, outputDir)

        # Create graphs for the reports 
        graphObject = BuildGraphs.makeGraphObject(graphData)

        try :
            BuildGraphs.vizualizeGraph(inputId, subFolder, graphObject)
            #Charts.BuildChart(subFolder, [1,2,3,2,3,1,0,2,3,2,1,0])

            # Create resulting reports
            BuildTex.MoveFiles(subFolder) # First, move the Tex files to the subfolder 

            print '\nProcessing Result.tex in ', subFolder
            os.chdir(subFolder)
            subprocess.call(['pdflatex', '-quiet', 'Result.tex'])
            shutil.copy2('Result.pdf', outputDir + '\\Res'+inputId+'.pdf')
            print inputFileName, ': the resulting PDF is created'

        except Exception:
            print 'Creating PDF failed for ', inputId


    # Done!
    print('\nSee the final results in ' + outputDir)

main()