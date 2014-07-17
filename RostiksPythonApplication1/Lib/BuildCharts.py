from pylab import *
import matplotlib.pyplot as plt

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

def YesNoPieChart(fileName, yesNum = 11, noNum = 5) :

    fig = figure(1, figsize=(5,5))

    yes = int(yesNum * 100/(yesNum + noNum))
    fracs = [yes, 100 - yes]
    labels = [str(fracs[0]) + '%',str(fracs[1]) + '%']

    colors=['#00FF00', '#FF0000' ]

    pie(fracs, labels = labels, colors=colors, startangle=90)
    savefig(fileName)
    close(1)


def YesNoHist(fileName, yesData = [0,1,2,1,1], noData = [1,2,0,2], cat = ['A','B','C']) :
     
    # print 'Building yes-no bars:', data, ' cat:', cat
    fig = figure(1)
    left,bottom,width,height= 0.1 , 0.1, 0.85, 0.85
    axes([left,bottom,width,height])
    colors=['#FF0000','#00FF00']
    catNum = len(cat)
    n, bins, patches = hist([noData, yesData], range(catNum + 1), histtype='bar', stacked=False, color=colors)
    m = [max(n[0][i], n[1][i]) for i in range(len(cat))]
    print n, m
    xticks([i+0.5 for i in range(catNum)], cat)
    yticks([i for i in range(max(m)+2)])
    savefig(fileName)
    close(1)


def YesNoByAge(fileName, data = [['no',28],['no',28],['yes',28],['yes',56],['yes',54],['no',37]]):

    yesData = []
    noData = []
    cat = ['<25', '25-35', '36-55', '55<']

    for [v,age] in data :
        if age < 25 :
            c = 0
        elif age <= 35 :
            c = 1
        elif age <= 55 :
            c = 2
        else :
            c = 3

        if v == 'yes' :
            yesData.append(c)
        else :
            noData.append(c)

    YesNoHist(fileName, yesData, noData, cat)

def YesNoByCategory(fileName, data = [['yes',0],['no',2],['yes',2],['yes',2],['yes',1],['no',3],['yes',4]]) :
    yesData = []
    noData = []
    cat = ['HET AT.', 'ATTECT.', '2 KAT', '1 KAT','B. KAT']

    for [v,c] in data :
        if v == 'yes' :
            yesData.append(c)
        else :
            noData.append(c)

    YesNoHist(fileName, yesData, noData, cat)
