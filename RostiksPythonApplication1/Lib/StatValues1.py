import BuildTex
import StatValues

def ComputeAll(subFolder, statData) :

    BuildTex.MakeTitlePage(subFolder, statData)
    BuildTex.buildNamesList(subFolder, statData)

    computeAllBossTeacher(subFolder, statData)
    computeParticipatedManWomen(subFolder, statData)
    computeAge(subFolder, statData)
    computeEducation(subFolder, statData)
    computeWorkYears(subFolder, statData)
    computeWorkHereYears(subFolder, statData)
    computeTeachCat(subFolder, statData)


def computeAllBossTeacher(subFolder, statData) :
    values = StatValues.extractAnswers(statData, [8])
    boss = values.count('201') + values.count('202')
    teacher = values.count('203')

    BuildTex.addMacros(subFolder, 'nTotal', str(len(statData)))
    BuildTex.addMacros(subFolder, 'numBoss', str(boss))
    BuildTex.addMacros(subFolder, 'numTeacher', str(teacher))


def computeParticipatedManWomen(subFolder, statData) :
    values = StatValues.extractAnswers(statData, [9])
    men = values.count('14')
    women = values.count('15')
    BuildTex.addMacros(subFolder, 'nParticipated', str(men+women))
    BuildTex.addMacros(subFolder, 'numMen', str(men))
    BuildTex.addMacros(subFolder, 'numWomen', str(women))


def computeAge(subFolder, statData) :
    values = StatValues.extractAnswers(statData, [14])
    years = map(StatValues.toNumber, values)
    print '\nYears:', years
    ages = [(2014 - y) for y in years]
    print 'Ages:', ages
    [young, mid, senior, old] = [0,0,0,0]
    for age in ages :
        if age < 25 and age > 12:
            young += 1
        elif age < 36 :
            mid += 1
        elif age < 56 :
            senior += 1
        elif age >= 56 and age < 120:
            old += 1 
    BuildTex.addMacros(subFolder, 'numYoung', str(young))
    BuildTex.addMacros(subFolder, 'numMidAge', str(mid))
    BuildTex.addMacros(subFolder, 'numSenior', str(senior))
    BuildTex.addMacros(subFolder, 'numOld', str(old))


def computeEducation(subFolder, statData) :
    values = StatValues.extractAnswers(statData, [15])
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
    values = StatValues.extractAnswers(statData, [16])
    years = map(StatValues.toNumber, values)
    print '\nExperience:', values, years
    [expA, expB, expC, expD] = [0,0,0,0]
    for y in years :
        if y<0 :
            expA = expA
        elif y < 5 :
            expA += 1
        elif y < 11 :
            expB += 1
        elif y < 21 :
            expC += 1
        elif y>=21 and y<100:
            expD += 1 
    BuildTex.addMacros(subFolder, 'numExpA', str(expA))
    BuildTex.addMacros(subFolder, 'numExpB', str(expB))
    BuildTex.addMacros(subFolder, 'numExpC', str(expC))
    BuildTex.addMacros(subFolder, 'numExpD', str(expD))

def computeWorkHereYears(subFolder, statData):
    values = StatValues.extractAnswers(statData, [17])
    years = map(StatValues.toNumber, values)
    print '\nExperience:', values, years
    [expA, expB, expC, expD] = [0,0,0,0]
    for y in years :
        if y<0 :
            expA = expA
        elif y < 5 :
            expA += 1
        elif y < 11 :
            expB += 1
        elif y < 21 :
            expC += 1
        elif y>=21 and y<100:
            expD += 1 
    BuildTex.addMacros(subFolder, 'numExpHereA', str(expA))
    BuildTex.addMacros(subFolder, 'numExpHereB', str(expB))
    BuildTex.addMacros(subFolder, 'numExpHereC', str(expC))
    BuildTex.addMacros(subFolder, 'numExpHereD', str(expD))


def computeTeachCat(subFolder, statData) :
    values = StatValues.extractAnswers(statData, [19])
    keys = [str(i+55) for i in range(5)]
    stat = [values.count(key) for key in keys]
    print '\nTeacher categories:', values, stat
    BuildTex.addMacros(subFolder, 'numTechCatA', str(stat[0]))
    BuildTex.addMacros(subFolder, 'numTechCatB', str(stat[1]))
    BuildTex.addMacros(subFolder, 'numTechCatC', str(stat[2]))
    BuildTex.addMacros(subFolder, 'numTechCatD', str(stat[3]))
    BuildTex.addMacros(subFolder, 'numTechCatE', str(stat[4]))

