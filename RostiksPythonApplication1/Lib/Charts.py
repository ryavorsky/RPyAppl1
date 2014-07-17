from pylab import *

def BuildChart(subFolder, dataList, values = []) :
    figure(1, figsize=(5,5))
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
    close(1)

def YesNoPieChart(fileName, yesNum, noNum) :

    figure(1, figsize=(5,5))
    axes([0.1, 0.1, 0.8, 0.8])

    yes = int(yesNum * 100/(yesNum + noNum))
    fracs = [yes, 100 - yes]
    labels = [str(fracs[0]),str(fracs[1])]

    print 'Building yes-no chart:values, labels:', yesNum, noNum, labels

    colors=['#00FF00', '#FF0000' ]

    pie(fracs, labels = labels, colors=colors, startangle=90)
    savefig(fileName)
    close(1)


def YesNoBarChart(fileName, data = [[],[]], cat = []) :
     
    # print 'Building yes-no bars:', data, ' cat:', cat
    yesData = [0,1,2,1,2,3,2,3,2,1,2,3,2,2,3,2,1,2] # categories of the answers
    noData = [0,3,2,3,3,3,1] 
    cat = ['Young', 'Mid', 'Senior', 'Old']

    figure(1)
    axes([0.1, 0.1, 0.8, 0.8])
    colors=['#FF0000','#00FF00']
    n, bins, patches = hist([noData, yesData], range(5), histtype='bar', stacked=False, color=colors)
    xticks([i+0.5 for i in range(4)], cat)
    savefig(fileName)
    close(1)
	
	