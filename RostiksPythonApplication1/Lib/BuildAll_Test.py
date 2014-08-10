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


def Main(projectDir = 'c:\\Direk_0') :
    
    print 'Start at', time.asctime()
    inputDir = projectDir + '\\Input\\88'
    outputDir = projectDir + '\\Output\\88'

    outputDir = CheckFolders.TestDirs(inputDir, outputDir)


    fsocio = open (projectDir + '\\socio_table.txt','w')
    header = ['SchoolId', '6', '6s', '71', '71s', '72', '72s', 'Nodes']
    fsocio.write('\t'.join(header) + '\n')
    fsocio.close()
    for inputFileName in os.listdir(inputDir):

        makeReport(inputDir + '\\' + inputFileName, outputDir, projectDir)

    print('\nSee the final results in ' + outputDir)
    print 'Finish at', time.asctime()


# Make PDF report for a given input file and put it into the output folder
def makeReport(inputFileName, outputDir, projectDir):

    print '\n Processing input file ', inputFileName, 'Time:', time.asctime()

    #try :
    # For each input file create a separate subfolder for all the related files
    [inputId, subFolder] = CheckFolders.MakeSubfolder(inputFileName, outputDir)

    # Move the prefilled Tex files into the subfolder
    BuildTex.MoveFiles(subFolder, projectDir)  

    # Parse the input file  
    [graphData, statData] = ParseInput.dataFromFile(inputFileName, inputId, outputDir, subFolder)

    # Compute the statistics values and build the charts
    # StatValues.computeValues(subFolder, statData)

    try :
        # Create graphs for the reports 
        graphObject = BuildGraphs.makeGraphObject(graphData)
        BuildGraphs.BuildAllGraphs(inputId, subFolder, graphObject)
    except Exception as e:
        print e.message

    # get socio numbers
    fsocio = open (projectDir + '\\socio_table.txt','a')
    ftex = open(subFolder  + '\\commands.tex', 'r')
    data = statData[0].split('\t')
    schoolInfo = [data[i].split('=')[1] for i in range(7) ]
    fsocio.write(inputId + '\t' + '\t'.join(schoolInfo))
    for i1 in range(7) :
        ftex.readline()
    for line in ftex.readlines() :
        res = line.split('}')
        res[0] = res[0].replace('\\newcommand{\\links','')
        res[1] = res[1].replace('{','')
        print 'Socio numbers', res
        fsocio.write('\t' + res[1])

    fsocio.write('\n')
    ftex.close()
    fsocio.close()
