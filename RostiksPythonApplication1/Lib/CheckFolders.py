# Check whether the input/output folders exist
import sys
import time
import os

def TestDirs(inDir, outDir):
    try:
        os.chdir(inDir)
    except Exception:
        print('Failed to open the inDir\n\t' + inDir + '\n')
        sys.exit
    else:
        print('The intput folder is found:\n\t' + inDir + '\n')
        inputFiles = os.listdir(inDir)
        print(str(len(inputFiles)) + ' files to process')
        for inputFileName in inputFiles:
            print '\t' + inputFileName

    if os.path.exists(outDir): 
        t = time.localtime()
        outDir = outDir + '_' + str(t[3]) + str(t[4]) + str(t[5])
        os.mkdir(outDir)
        print('The output folder is created:\n\t' + outDir + '\n')
    else:
        os.mkdir(outDir)
        print('The output folder is created:\n\t' + outDir + '\n')

    return outDir

