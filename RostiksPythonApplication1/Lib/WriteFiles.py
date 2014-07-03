def writeTestFiles(folder):
    inputList = ['1','3','5']

    for fileName in inputList:
        f = open(folder + '\\' + fileName + '.txt','w')
        f.write('test ' + fileName)
        f.close()
