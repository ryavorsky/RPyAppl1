# Standard libraries
import os
import subprocess
import shutil

# The project modules
import ParseInput
import BuildGraphs
import BuildCharts
import BuildTex
import CheckFolders
import StatValues

# Make PDF report for a given input file and put it into the output folder
def makeReport(inputFileName, outputDir):

    print '\n Processing input file ' + inputFileName

    try :
        # For each input file create a separate subfolder for all the related files
        [inputId, subFolder] = CheckFolders.MakeSubfolder(inputFileName, outputDir)

        # Move the prefilled Tex files into the subfolder
        BuildTex.MoveFiles(subFolder)  

        # Parse the input file  
        [graphData, statData] = ParseInput.dataFromFile(inputFileName, inputId, outputDir, subFolder)

        # Compute the values  
        StatValues.computeValues(subFolder, statData)

        # Process the input data to create charts, graphs, Tex and then PDF
        # Create graphs for the reports 
        graphObject = BuildGraphs.makeGraphObject(graphData)
        BuildGraphs.BuildAllGraphs(inputId, subFolder, graphObject)

        # Create charts and histograms for the reports 
        BuildCharts.BuildAllCharts(subFolder, statData)

        # Create PDF
        BuildTex.CreatePdf(outputDir, subFolder, inputId, inputFileName)

    except Exception as e:
        print e.message
        print 'Creating PDF failed for ', inputId

    print '\n', '*'*70, '\n', '-'*70, '\n'