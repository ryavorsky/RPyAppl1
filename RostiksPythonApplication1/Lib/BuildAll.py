# Standard libraries
import os
import subprocess
import shutil
import time

# The project modules
import ParseInput
import BuildGraphs
import BuildCharts
import BuildTex
import CheckFolders
import StatValues


def Main(projectDir = 'c:\\Direktor') :
    
    print 'Start at', time.asctime()
    inputDir = projectDir + '\\Input\\All\\More'
    outputDir = projectDir + '\\Output\\More'

    outputDir = CheckFolders.TestDirs(inputDir, outputDir)

    for inputFileName in os.listdir(inputDir):

        makeReport(inputDir + '\\' + inputFileName, outputDir, projectDir)

    print('\nSee the final results in ' + outputDir)
    print 'Finish at', time.asctime()



# Make PDF report for a given input file and put it into the output folder
def makeReport(inputFileName, outputDir, projectDir):

    print '\n Processing input file ' + inputFileName, 'Time:', time.asctime()

    #try :
    # For each input file create a separate subfolder for all the related files
    [inputId, subFolder] = CheckFolders.MakeSubfolder(inputFileName, outputDir)

    # Move the prefilled Tex files into the subfolder
    BuildTex.MoveFiles(subFolder, projectDir)  

    # Parse the input file  
    [graphData, statData] = ParseInput.dataFromFile(inputFileName, inputId, outputDir, subFolder)

    # Compute the statistics values and build the charts
    StatValues.computeValues(subFolder, statData)

    orgSize = len(statData)
    if orgSize < 8 :
        print '\nNo graph data!'
        BuildTex.SimplifyResult(subFolder)
    else :
        try :
            # Create graphs for the reports 
            graphObject = BuildGraphs.makeGraphObject(graphData)
            BuildGraphs.BuildAllGraphs(inputId, subFolder, graphObject)
        except Exception as e:
            print e.message

    # Create PDF
    if orgSize > 37 :
        BuildTex.insertTables(subFolder, orgSize)
        BuildTex.splitTables(subFolder, orgSize)
    BuildTex.CreatePdf(outputDir, subFolder, inputId, inputFileName)

    #except Exception as e:
    #    print e.message
    #    print '\n Creating PDF failed for ', inputId
