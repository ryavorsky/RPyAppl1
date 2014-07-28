# Ratings tables for sections 5, 6

import BuildTex
import StatValues

def computeTable(subFolder, fileName, G) :
    print '\nBuilding table ', fileName
    names = extractNames(subFolder)
    f = open(subFolder + '\\' + fileName,'a')
    
    res = []
    for n in G.nodes() :
        id = G.node[n]['number']
        fullName = names[id][0]
        position = names[id][1]
        score = G.in_degree(n)
        res.append([id,fullName,position,score])

    res.sort(cmp = cmp)

    for t in res :
        resLine = t[0] + ' & ' + t[1] + ' & ' + t[2] + ' & ' + str(t[3]) + '\\\\ \n'
        f.write(resLine)

    f.close()

def cmp(x, y) : 
    if x[3] < y[3] :
        return 1
    elif x[3] > y[3] :
        return -1
    elif int(x[0]) > int(y[0]) :
        return 1
    elif int(x[0]) < int(y[0]) :
        return -1
    else :
        return 0

def extractNames(subFolder) :
    names = dict()
    f = open(subFolder + '\\nameslist.tex','r')

    for line in f.readlines() :
        p1 = line.find('[')
        p2 = line.find(']')
        p3 = line.find(',')
        p4 = len(line)
        p4a = line.find('(')
        if p4a > 0 :
            p4 = p4a
        num = line[(p1+1):p2]
        name = line[(p2+2):p3]
        position = line[(p3+2):(p4-1)]

        names[num] = [name,position]

    f.close()
    return names
