import BuildTex

def computeValues(subFolder, statData) :

    computeBossTeacher(subFolder)
    computeManWomen(subFolder, statData)
    computeAge(subFolder, statData)

    return

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

    print 'Extracted answers for', questionNumbers, res
    return res

def computeManWomen(subFolder, statData) :
    values = extractAnswers(statData, [9])
    men = values.count('14')
    women = values.count('15')
    BuildTex.addMacros(subFolder, 'numMen', str(men))
    BuildTex.addMacros(subFolder, 'numWomen', str(women))

def computeBossTeacher(subFolder) :
    fileName =  subFolder + '\\nameslist.tex' # Teacher names to be included in report
    f = open(fileName, 'r')
    boss = 0
    teacher = 0
    for line in f.readlines() :
        pos = line.find(',')
        l = len(line) - pos
        print 'Boss:', pos, l, line
        if l > 30  :
            boss += 1
        else :
            teacher += 1

    BuildTex.addMacros(subFolder, 'numBoss', str(boss))
    BuildTex.addMacros(subFolder, 'numTeacher', str(teacher))

    f.close()

def computeAge(subFolder, statData) :
    values = extractAnswers(statData, [14])
    years = map(int, values)
    print '\nYears:', years
    ages = [(2014 - y) for y in years]
    print 'Ages:', ages
    [young, mid, senior, old] = [0,0,0,0]
    for age in ages :
        if age < 25 :
            young += 1
        elif age < 36 :
            mid += 1
        elif age < 56 :
            senior += 1
        else:
            old += 1 
    BuildTex.addMacros(subFolder, 'numYoung', str(young))
    BuildTex.addMacros(subFolder, 'numMidAge', str(mid))
    BuildTex.addMacros(subFolder, 'numSenior', str(senior))
    BuildTex.addMacros(subFolder, 'numOld', str(old))
