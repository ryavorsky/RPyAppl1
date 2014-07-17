# Standard libraries
import os
import subprocess
import shutil

# The project modules
import ParseInput
import BuildGraphs
import BuildCharts
import BuildTex

# Make PDF report for a given input file and put it into the output folder
def makeReport(inputFileName, outputDir):

    print '\n Processing input file ' + inputFileName

    # Parse the input file and create the subfolder for all the related files
    [inputId, subFolder, graphData, socioData] = ParseInput.dataFromFile(inputFileName, outputDir)

    # Process the input data to create charts, graphs, Tex and then PDF
    try :
        # Create graphs for the reports 
        graphObject = BuildGraphs.makeGraphObject(graphData)
        BuildGraphs.BuildAllGraphs(inputId, subFolder, graphObject)

        # Create charts and histograms for the reports 
        BuildCharts.BuildAllCharts(subFolder, socioData)

        # Move the prefilled Tex files into the subfolder
        BuildTex.MoveFiles(subFolder)  

        # Create PDF
        BuildTex.CreatePdf(outputDir, subFolder, inputId, inputFileName)

    except Exception:
        print 'Creating PDF failed for ', inputId

    print '\n', '*'*70, '\n', '-'*70, '\n'