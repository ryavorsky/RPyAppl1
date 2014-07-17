import os
# Standard libraries
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
    [inputId, subFolder, graphData] = ParseInput.dataFromFile(inputFileName, outputDir)

    # Process the input data to create charts, graphs, Tex and then PDF
    try :
        # Create graphs for the reports 
        graphObject = BuildGraphs.makeGraphObject(graphData)

        BuildGraphs.vizualizeGraph(inputId, subFolder, graphObject)

        # Move the prefilled Tex files into the subfolder
        BuildTex.MoveFiles(subFolder)  

        # Create PDF
        print '\nProcessing Result.tex in ', subFolder
        os.chdir(subFolder)
        subprocess.call(['pdflatex', '-quiet', 'Result.tex'])

        # Copy the final report from the subfolder into the output folder to all reports
        shutil.copy2('Result.pdf', outputDir + '\\Res'+inputId+'.pdf')
        print '\nThe resulting PDF is created for', inputFileName

    except Exception:
        print 'Creating PDF failed for ', inputId

    print '\n', '*'*70, '\n', '-'*70, '\n'