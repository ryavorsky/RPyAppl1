import os
import math

import BuildTex
import StatValues1
import StatValues2
import StatValues3
import StatValues4
import StatValues5

def computeValues(subFolder, statData) :

    print '\nCompute the statistics values and build the charts'

    os.chdir(subFolder)

    StatValues1.ComputeAll(subFolder, statData)
    StatValues2.ComputeAll(subFolder, statData)
    StatValues3.ComputeAll(subFolder, statData)
    StatValues4.ComputeAll(subFolder, statData)
    StatValues5.ComputeAll(subFolder, statData)

def extractAnswers(statData, questionNumbers) :
    res = []
    for line in statData :
        ans = []
        for n in questionNumbers :
            que = 'q'+str(n)+ '='
            pos1 = line.find(que) + len(que)
            value = line[pos1:(pos1+10)].split('\t')[0]
            ans.append(value)
        if len(questionNumbers) == 1 :
            res.append(ans[0])
        else :
            res.append(ans)

    print 'Extracted answers for', questionNumbers, ':\n', res
    return res


# join list of lists into one big list
def joinLists(lst) : 
    res = []
    for l in lst :
        res = res + l
    return res


def joinListsByAge(lst) : 
    print 'Join by age'
    res = [[],[],[],[]]
    for l in lst :
        age = 2014 - toNumber(l[0])
        tail = [l[j+1] for j in range(len(l)-1)]
        group = getAgeGroup(age)
        if group < 5 :
            res[group] = res[group] + tail
    print res
    return res


def joinListsByCategory(lst) : 
    print 'Join by category'
    res = [[],[],[],[],[]]
    for l in lst :
        tail = [l[j+1] for j in range(len(l)-1)]
        cat = toNumber(l[0]) - 55
        if cat >= 0 and cat < 5 :
            res[cat] = res[cat] + tail
    print res
    return res


def joinListsByQuestion(lst) : 
    print 'Join by question'
    n = len(lst[0]) # the number of questions
    res = [[] for i in range(n)]
    for answers in lst :
        for i in range(n) :
            res[i].append(answers[i])
    print res
    return res


# compute percentage of values in the list
def percent(lst) : 
    s = 0
    for val in lst :
        s+=val

    if s == 0 :
        res = [0 for val in lst]
    else :
        res = [int(math.floor(val*100/s + 0.5)) for val in lst]

        sp = 0
        for p in res :
            sp += p
        delta = 100 - sp

        imax = 0
        for i in range(len(res) - 1) :
            if res[i+1] > res[imax] :
                imax = i + 1
        res[imax] += delta

    return res


# compute age group 
def getAgeGroup(age) :
    
    if age>0 and age < 25 :
        return 0
    elif age < 36 :
        return 1
    elif age < 56 :
        return 2
    elif age >= 56 and age < 120:
        return 3
    else :
        return 99

def toNumber(value) :
    try :
        res = int(value)
    except Exception as e :
        res = -1
    return res