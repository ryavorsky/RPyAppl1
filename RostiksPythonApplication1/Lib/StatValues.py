import BuildTex
import StatValues2

def computeValues(subFolder, statData) :

    computeBossTeacher(subFolder)
    computeManWomen(subFolder, statData)
    computeAge(subFolder, statData)
    computeEducation(subFolder, statData)
    computeWorkYears(subFolder, statData)
    computeWorkHereYears(subFolder, statData)
    computeTeachCat(subFolder, statData)

    StatValues2.ComputeAll(subFolder, statData)

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

def getAgeGroup(age) :
    if age < 25 :
        return 0
    elif age < 36 :
        return 1
    elif age < 56 :
        return 2
    else:
        return 3 

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
        if l > 80  :
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

def computeEducation(subFolder, statData) :
    values = extractAnswers(statData, [15])
    eduValues = []
    for v in values :
        v = v.replace('{','').replace('}','')
        eduList = v.split('=')
        for e in eduList :
            if len(e) > 1 :
                eduValues.append(e)

    keys = [str(i+16) for i in range(7)]
    eduStat = [eduValues.count(key) for key in keys]
    print 'Education values:', eduValues, eduStat
    BuildTex.addMacros(subFolder, 'numEduA', str(eduStat[0]))
    BuildTex.addMacros(subFolder, 'numEduB', str(eduStat[1]))
    BuildTex.addMacros(subFolder, 'numEduC', str(eduStat[2]))
    BuildTex.addMacros(subFolder, 'numEduD', str(eduStat[3]))
    BuildTex.addMacros(subFolder, 'numEduE', str(eduStat[4]))
    BuildTex.addMacros(subFolder, 'numEduF', str(eduStat[5]))
    BuildTex.addMacros(subFolder, 'numEduG', str(eduStat[6]))

def computeWorkYears(subFolder, statData) :
    values = extractAnswers(statData, [16])
    years = map(extractNumber, values)
    print '\nExperience:', values, years
    [expA, expB, expC, expD] = [0,0,0,0]
    for y in years :
        if y < 5 :
            expA += 1
        elif y < 11 :
            expB += 1
        elif y < 21 :
            expC += 1
        else:
            expD += 1 
    BuildTex.addMacros(subFolder, 'numExpA', str(expA))
    BuildTex.addMacros(subFolder, 'numExpB', str(expB))
    BuildTex.addMacros(subFolder, 'numExpC', str(expC))
    BuildTex.addMacros(subFolder, 'numExpD', str(expD))

def extractNumber(s) :
    try :
        res = int(s[0:2])
    except Exception:
        res = int(s[0:1])

    return res

def computeWorkHereYears(subFolder, statData):
    values = extractAnswers(statData, [17])
    years = map(extractNumber, values)
    print '\nExperience:', values, years
    [expA, expB, expC, expD] = [0,0,0,0]
    for y in years :
        if y < 5 :
            expA += 1
        elif y < 11 :
            expB += 1
        elif y < 21 :
            expC += 1
        else:
            expD += 1 
    BuildTex.addMacros(subFolder, 'numExpHereA', str(expA))
    BuildTex.addMacros(subFolder, 'numExpHereB', str(expB))
    BuildTex.addMacros(subFolder, 'numExpHereC', str(expC))
    BuildTex.addMacros(subFolder, 'numExpHereD', str(expD))

def computeTeachCat(subFolder, statData) :
    values = extractAnswers(statData, [19])
    keys = [str(i+55) for i in range(5)]
    stat = [values.count(key) for key in keys]
    print '\nTeacher categories:', values, stat
    BuildTex.addMacros(subFolder, 'numTechCatA', str(stat[0]))
    BuildTex.addMacros(subFolder, 'numTechCatB', str(stat[1]))
    BuildTex.addMacros(subFolder, 'numTechCatC', str(stat[2]))
    BuildTex.addMacros(subFolder, 'numTechCatD', str(stat[3]))
    BuildTex.addMacros(subFolder, 'numTechCatE', str(stat[4]))