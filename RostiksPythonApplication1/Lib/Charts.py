from pylab import *

def BuildChart(subFolder, dataList, values = []) :
    figure(0, figsize=(5,5))
    axes([0.01, 0.01, 0.99, 0.99])

    if values == [] :
        values = list(set(dataList))
        values.sort()

    fracs = [int(dataList.count(i)*100.0/len(dataList)) for i in values ]
    labels = [str(i) + ':' + str(dataList.count(i)) for i in values ]

    print 'Building chart for data', dataList, ' values, fracs, labels:', values, fracs, labels

    mycolors=['#FFAAAA', '#FFFF99', '#55FFAA', '#55AAFF']

    pie(fracs,labels=labels,colors=mycolors, startangle=90)

    savefig(subFolder + '\\pie3.png')