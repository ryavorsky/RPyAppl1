import shutil
import os

def MoveFiles(destFolder):
    sourceFolder = 'c:\\Direktor\\Tex\\'
    inputFiles = os.listdir(sourceFolder)
    for fileName in inputFiles:
        shutil.copy2(sourceFolder + fileName, destFolder)