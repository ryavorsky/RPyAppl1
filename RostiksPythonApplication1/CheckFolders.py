import sys
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
            print('\t' + inputFileName + '\n')

    try:
        os.chdir(outDir)
        print('The output folder is found:\n\t' + outDir + '\n')
    except Exception:
        print('Failed to open the outDir:\n\t' + outDir + '\n')
        try: 
            os.mkdir(outDir)
            print('The output folder is created:\n\t' + outDir + '\n')
        except Exception:
            print('Failed to create the outDir:\n\t' + outDir + '\n')
            sys.exit