# Write Html

def writeHtmlReport(folder, fileName):

    f = open(folder + '\\' + fileName,'w')
    f.write('<head></head><body><h1>The example report</h1><p>Text goes here... <img src="fig.png"></body>')
    f.close()
