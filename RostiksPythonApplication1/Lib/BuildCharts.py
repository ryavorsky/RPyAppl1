from pylab import *
import matplotlib.pyplot as plt
import matplotlib as mpl
import shutil

def BuildAllCharts(subFolder, socioData):
    print '\nBuilding charts in', subFolder, 'from', socioData
    return

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

def YesNoPie(fileName, yesNum = 11, noNum = 5) :

    print '\nBuilding Yes/No pie:', yesNum, noNum, fileName

    if (yesNum == 0) and (noNum == 0) :
        shutil.copy2('empty.png', fileName)
    else :

        mpl.rcParams['font.size'] = 32.0
        mpl.rcParams['font.family'] = 'Times New Roman'
        fig = figure(1, figsize=(5.5,5.5))

        yes = int(yesNum * 100/(yesNum + noNum))
        fracs = [100 - yes, yes]
        labels = [str(fracs[0]) + '%',str(fracs[1]) + '%']

        if fracs[0] == 0 :
            labels[0] = ''
        if fracs[1] == 0 :
            labels[1] = ''

        colors=['#FF0000' ,'#00BB00']

        pie(fracs, labels = labels, colors=colors, startangle=90)
        savefig(fileName)
        close(1)

def Pie(fileName, data):
    print '\nBuilding big pie for:', data, fileName
    mpl.rcParams['font.size'] = 32.0
    mpl.rcParams['font.family'] = 'Times New Roman'
    fig = figure(1, figsize=(5.5,5.5))

    s = 0.0
    for val in data :
        s = s + int(val)
    print sum
    fracs = [int(val*100.0/s) for val in data]
    print fracs
    labels = [str(p) + '%' for p in fracs ]
    colors=['g','b','c','r']
    pie(fracs, labels = labels, colors=colors, startangle=90)
    savefig(fileName)
    close(1)

# Building histogram from two raws of data classifies by several categories
def YesNoHist(fileName, yesData = [0,1,2,1,1], noData = [1,2,0,2], cat = ['A','B','C']) :
     
    fig = figure(1)
    left,bottom,width,height= 0.1 , 0.1, 0.85, 0.85
    axes([left,bottom,width,height])
    colors=['#FF0000','#00FF00'] # red for 'no', green for 'yes'
    catNum = len(cat)
    n, bins, patches = hist([noData, yesData], range(catNum + 1), histtype='bar', stacked=False, color=colors)
    m = [max(n[0][i], n[1][i]) for i in range(len(cat))] # compute the 
    print n, m
    xticks([i+0.5 for i in range(catNum)], cat)
    yticks([i for i in range(max(m)+2)])
    savefig(fileName)
    close(1)


def YesNoHistByAge(fileName, data = [['no',28],['no',28],['yes',28],['yes',56],['yes',54],['no',37]]):

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

# Use the previous function to build diagram from not so refined data
def YesNoHistByTeacherCat(fileName, data = [['yes',0],['no',2],['yes',2],['yes',2],['yes',1],['no',3],['yes',4]]) :
    yesData = []
    noData = []
    cat = ['HET AT.', 'ATTECT.', '2 KAT', '1 KAT','B. KAT']

    for [v,c] in data :
        if v == 'yes' :
            yesData.append(c)
        else :
            noData.append(c)

    YesNoHist(fileName, yesData, noData, cat)
