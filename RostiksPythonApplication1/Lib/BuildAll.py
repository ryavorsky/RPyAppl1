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

# Make PDF report for a given input file and put it into the output folder
def makeReport(inputFileName, outputDir):

    print '\n Processing input file ' + inputFileName

    try :
        [inputId, subFolder] = CheckFolders.MakeSubfolder(inputFileName, outputDir)

        # Move the prefilled Tex files into the subfolder
        BuildTex.MoveFiles(subFolder)  

        # Parse the input file and create the subfolder for all the related files
        [graphData, socioData] = ParseInput.dataFromFile(inputFileName, inputId, outputDir, subFolder)

        # Process the input data to create charts, graphs, Tex and then PDF
        # Create graphs for the reports 
        graphObject = BuildGraphs.makeGraphObject(graphData)
        BuildGraphs.BuildAllGraphs(inputId, subFolder, graphObject)

        # Create charts and histograms for the reports 
        BuildCharts.BuildAllCharts(subFolder, socioData)

        # Create PDF
        BuildTex.CreatePdf(outputDir, subFolder, inputId, inputFileName)

    except Exception:
        print 'Creating PDF failed for ', inputId

    print '\n', '*'*70, '\n', '-'*70, '\n'