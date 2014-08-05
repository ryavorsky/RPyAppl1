# Statistics for chapter 2

import BuildTex
import BuildCharts
import StatValues

def  ComputeAll(subFolder, statData):

    compute21a(subFolder, statData)
    compute21b(subFolder, statData)
    compute21c(subFolder, statData)
    compute21d(subFolder, statData)

    compute22a(subFolder, statData)
    compute22b(subFolder, statData)
    compute22c(subFolder, statData)
    compute22d(subFolder, statData)
    compute22e(subFolder, statData)

    compute23a(subFolder, statData)
    compute23b(subFolder, statData)
    compute23c(subFolder, statData)
    compute23d(subFolder, statData)


def compute21a(subFolder, statData): # aggregate
    print '\nComputing values for slide 2.1.1.'
    values = StatValues.extractAnswers(statData, [38,39])
    values = StatValues.joinLists(values)

    yesNum = values.count('87') + values.count('88')
    noNum = values.count('89') + values.count('90')
    [yesNumP, noNumP] = StatValues.percent([yesNum,noNum])

    BuildTex.addMacros(subFolder, 'valBAAyesNum', str(yesNum))
    BuildTex.addMacros(subFolder, 'valBAAnoNum', str(noNum))
    BuildTex.addMacros(subFolder, 'valBAAyesNumP', str(yesNumP))
    BuildTex.addMacros(subFolder, 'valBAAnoNumP', str(noNumP))

    BuildCharts.YesNoPie(subFolder + '\\pie211.png', yesNum, noNum)


def compute21b(subFolder, statData): # by age - q14
    print '\nComputing values for slide 2.1.2.'
    values = StatValues.extractAnswers(statData, [14, 38,39])
    values = StatValues.joinListsByAge(values)

    yesNum = [ val.count('87') + val.count('88') for val in values ]
    noNum = [ val.count('89') + val.count('90') for val in values ]

    BuildTex.addMacros(subFolder, 'valBAByesNumA', str(yesNum[0]))
    BuildTex.addMacros(subFolder, 'valBAByesNumB', str(yesNum[1]))
    BuildTex.addMacros(subFolder, 'valBAByesNumC', str(yesNum[2]))
    BuildTex.addMacros(subFolder, 'valBAByesNumD', str(yesNum[3]))

    BuildTex.addMacros(subFolder, 'valBABnoNumA', str(noNum[0]))
    BuildTex.addMacros(subFolder, 'valBABnoNumB', str(noNum[1]))
    BuildTex.addMacros(subFolder, 'valBABnoNumC', str(noNum[2]))
    BuildTex.addMacros(subFolder, 'valBABnoNumD', str(noNum[3]))

    BuildCharts.YesNoPie(subFolder + '\\pie212a.png', yesNum[0], noNum[0])
    BuildCharts.YesNoPie(subFolder + '\\pie212b.png', yesNum[1], noNum[1])
    BuildCharts.YesNoPie(subFolder + '\\pie212c.png', yesNum[2], noNum[2])
    BuildCharts.YesNoPie(subFolder + '\\pie212d.png', yesNum[3], noNum[3])

def compute21c(subFolder, statData): # by category - q19
    print '\nComputing values for slide 2.1.3.'
    values = StatValues.extractAnswers(statData, [19, 38,39])
    values = StatValues.joinListsByCategory(values)

    yesNum = [ val.count('87') + val.count('88') for val in values ]
    noNum = [ val.count('89') + val.count('90') for val in values ]

    BuildTex.addMacros(subFolder, 'valBACyesNumA', str(yesNum[0]))
    BuildTex.addMacros(subFolder, 'valBACyesNumB', str(yesNum[1]))
    BuildTex.addMacros(subFolder, 'valBACyesNumC', str(yesNum[2]))
    BuildTex.addMacros(subFolder, 'valBACyesNumD', str(yesNum[3]))
    BuildTex.addMacros(subFolder, 'valBACyesNumE', str(yesNum[4]))
    BuildTex.addMacros(subFolder, 'valBACnoNumA', str(noNum[0]))
    BuildTex.addMacros(subFolder, 'valBACnoNumB', str(noNum[1]))
    BuildTex.addMacros(subFolder, 'valBACnoNumC', str(noNum[2]))
    BuildTex.addMacros(subFolder, 'valBACnoNumD', str(noNum[3]))
    BuildTex.addMacros(subFolder, 'valBACnoNumE', str(noNum[4]))

    BuildCharts.YesNoPie(subFolder + '\\pie213a.png', yesNum[0], noNum[0])
    BuildCharts.YesNoPie(subFolder + '\\pie213b.png', yesNum[1], noNum[1])
    BuildCharts.YesNoPie(subFolder + '\\pie213c.png', yesNum[2], noNum[2])
    BuildCharts.YesNoPie(subFolder + '\\pie213d.png', yesNum[3], noNum[3])
    BuildCharts.YesNoPie(subFolder + '\\pie213e.png', yesNum[4], noNum[4])

def compute21d(subFolder, statData): # by question
    print '\nComputing values for slide 2.1.4.'
    values = StatValues.extractAnswers(statData, [35,38,39,50,55])
    values = StatValues.joinListsByQuestion(values)

    yesNum = [ val.count('87') + val.count('88') for val in values ]
    noNum = [ val.count('89') + val.count('90') for val in values ]

    BuildTex.addMacros(subFolder, 'valBADyesNumA', str(yesNum[0]))
    BuildTex.addMacros(subFolder, 'valBADyesNumB', str(yesNum[1]))
    BuildTex.addMacros(subFolder, 'valBADyesNumC', str(yesNum[2]))
    BuildTex.addMacros(subFolder, 'valBADyesNumD', str(yesNum[3]))
    BuildTex.addMacros(subFolder, 'valBADyesNumE', str(yesNum[4]))
    BuildTex.addMacros(subFolder, 'valBADnoNumA', str(noNum[0]))
    BuildTex.addMacros(subFolder, 'valBADnoNumB', str(noNum[1]))
    BuildTex.addMacros(subFolder, 'valBADnoNumC', str(noNum[2]))
    BuildTex.addMacros(subFolder, 'valBADnoNumD', str(noNum[3]))
    BuildTex.addMacros(subFolder, 'valBADnoNumE', str(noNum[4]))

    BuildCharts.YesNoPie(subFolder + '\\pie214a.png', yesNum[0], noNum[0])
    BuildCharts.YesNoPie(subFolder + '\\pie214b.png', yesNum[1], noNum[1])
    BuildCharts.YesNoPie(subFolder + '\\pie214c.png', yesNum[2], noNum[2])
    BuildCharts.YesNoPie(subFolder + '\\pie214d.png', yesNum[3], noNum[3])
    BuildCharts.YesNoPie(subFolder + '\\pie214e.png', yesNum[4], noNum[4])

def compute22a(subFolder, statData): # aggregate
    print '\nComputing values for slide 2.2.1.'
    values = StatValues.extractAnswers(statData, [28,29,46,47])
    values = StatValues.joinLists(values)

    yesNum = values.count('83') + values.count('84')
    noNum = values.count('85') + values.count('86')
    [yesNumP, noNumP] = StatValues.percent([yesNum,noNum])

    BuildTex.addMacros(subFolder, 'valBBAyesNum', str(yesNum))
    BuildTex.addMacros(subFolder, 'valBBAnoNum', str(noNum))
    BuildTex.addMacros(subFolder, 'valBBAyesNumP', str(yesNumP))
    BuildTex.addMacros(subFolder, 'valBBAnoNumP', str(noNumP))

    BuildCharts.YesNoPie(subFolder + '\\pie221.png', yesNum, noNum)


def compute22b(subFolder, statData): # by age
    print '\nComputing values for slide 2.2.2.'
    values = StatValues.extractAnswers(statData, [14, 28,29,46,47])
    values = StatValues.joinListsByAge(values)

    yesNum = [ val.count('83') + val.count('84') for val in values ]
    noNum = [ val.count('85') + val.count('86') for val in values ]

    BuildTex.addMacros(subFolder, 'valBBByesNumA', str(yesNum[0]))
    BuildTex.addMacros(subFolder, 'valBBByesNumB', str(yesNum[1]))
    BuildTex.addMacros(subFolder, 'valBBByesNumC', str(yesNum[2]))
    BuildTex.addMacros(subFolder, 'valBBByesNumD', str(yesNum[3]))

    BuildTex.addMacros(subFolder, 'valBBBnoNumA', str(noNum[0]))
    BuildTex.addMacros(subFolder, 'valBBBnoNumB', str(noNum[1]))
    BuildTex.addMacros(subFolder, 'valBBBnoNumC', str(noNum[2]))
    BuildTex.addMacros(subFolder, 'valBBBnoNumD', str(noNum[3]))

    BuildCharts.YesNoPie(subFolder + '\\pie222a.png', yesNum[0], noNum[0])
    BuildCharts.YesNoPie(subFolder + '\\pie222b.png', yesNum[1], noNum[1])
    BuildCharts.YesNoPie(subFolder + '\\pie222c.png', yesNum[2], noNum[2])
    BuildCharts.YesNoPie(subFolder + '\\pie222d.png', yesNum[3], noNum[3])

def compute22c(subFolder, statData): # by category - q19
    print '\nComputing values for slide 2.2.3.'
    values = StatValues.extractAnswers(statData, [19, 28,29,46,47])
    values = StatValues.joinListsByCategory(values)

    yesNum = [ val.count('83') + val.count('84') for val in values ]
    noNum = [ val.count('85') + val.count('86') for val in values ]

    BuildTex.addMacros(subFolder, 'valBBCyesNumA', str(yesNum[0]))
    BuildTex.addMacros(subFolder, 'valBBCyesNumB', str(yesNum[1]))
    BuildTex.addMacros(subFolder, 'valBBCyesNumC', str(yesNum[2]))
    BuildTex.addMacros(subFolder, 'valBBCyesNumD', str(yesNum[3]))
    BuildTex.addMacros(subFolder, 'valBBCyesNumE', str(yesNum[4]))
    BuildTex.addMacros(subFolder, 'valBBCnoNumA', str(noNum[0]))
    BuildTex.addMacros(subFolder, 'valBBCnoNumB', str(noNum[1]))
    BuildTex.addMacros(subFolder, 'valBBCnoNumC', str(noNum[2]))
    BuildTex.addMacros(subFolder, 'valBBCnoNumD', str(noNum[3]))
    BuildTex.addMacros(subFolder, 'valBBCnoNumE', str(noNum[4]))

    BuildCharts.YesNoPie(subFolder + '\\pie223a.png', yesNum[0], noNum[0])
    BuildCharts.YesNoPie(subFolder + '\\pie223b.png', yesNum[1], noNum[1])
    BuildCharts.YesNoPie(subFolder + '\\pie223c.png', yesNum[2], noNum[2])
    BuildCharts.YesNoPie(subFolder + '\\pie223d.png', yesNum[3], noNum[3])
    BuildCharts.YesNoPie(subFolder + '\\pie223e.png', yesNum[4], noNum[4])


def compute22d(subFolder, statData): # by question
    print '\nComputing values for slide 2.2.4.'
    values = StatValues.extractAnswers(statData, [28,29,46,47])
    values = StatValues.joinListsByQuestion(values)

    yesNum = [ val.count('83') + val.count('84') for val in values ]
    noNum = [ val.count('85') + val.count('86') for val in values ]

    BuildTex.addMacros(subFolder, 'valBBDyesNumA', str(yesNum[0]))
    BuildTex.addMacros(subFolder, 'valBBDyesNumB', str(yesNum[1]))
    BuildTex.addMacros(subFolder, 'valBBDyesNumC', str(yesNum[2]))
    BuildTex.addMacros(subFolder, 'valBBDyesNumD', str(yesNum[3]))
    BuildTex.addMacros(subFolder, 'valBBDnoNumA', str(noNum[0]))
    BuildTex.addMacros(subFolder, 'valBBDnoNumB', str(noNum[1]))
    BuildTex.addMacros(subFolder, 'valBBDnoNumC', str(noNum[2]))
    BuildTex.addMacros(subFolder, 'valBBDnoNumD', str(noNum[3]))

    BuildCharts.YesNoPie(subFolder + '\\pie224a.png', yesNum[0], noNum[0])
    BuildCharts.YesNoPie(subFolder + '\\pie224b.png', yesNum[1], noNum[1])
    BuildCharts.YesNoPie(subFolder + '\\pie224c.png', yesNum[2], noNum[2])
    BuildCharts.YesNoPie(subFolder + '\\pie224d.png', yesNum[3], noNum[3])


def compute22e(subFolder, statData): # aggregate (1 question)
    print '\nComputing values for slide 2.2.5.'
    values = StatValues.extractAnswers(statData, [49])

    ansA = values.count('115') 
    ansB = values.count('116')
    ansC = values.count('117') 
    ansD = values.count('118')
    [ansAp, ansBp, ansCp, ansDp] = StatValues.percent([ansA, ansB, ansC, ansD])

    BuildTex.addMacros(subFolder, 'valBBEansA', str(ansA))
    BuildTex.addMacros(subFolder, 'valBBEansB', str(ansB))
    BuildTex.addMacros(subFolder, 'valBBEansC', str(ansC))
    BuildTex.addMacros(subFolder, 'valBBEansD', str(ansD))
    BuildTex.addMacros(subFolder, 'valBBEansAp', str(ansAp))
    BuildTex.addMacros(subFolder, 'valBBEansBp', str(ansBp))
    BuildTex.addMacros(subFolder, 'valBBEansCp', str(ansCp))
    BuildTex.addMacros(subFolder, 'valBBEansDp', str(ansDp))
    
    BuildCharts.Pie(subFolder + '\\pie225.png', [ansAp, ansBp, ansCp, ansDp])


def compute23a(subFolder, statData): # aggregate
    print '\nComputing values for slide 2.3.1.'
    values = StatValues.extractAnswers(statData, [23])

    yesNum = values.count('61')
    noNum = values.count('62')
    [yesNumP, noNumP] = StatValues.percent([yesNum,noNum])

    BuildTex.addMacros(subFolder, 'valBCAyesNum', str(yesNum))
    BuildTex.addMacros(subFolder, 'valBCAnoNum', str(noNum))
    BuildTex.addMacros(subFolder, 'valBCAyesNumP', str(yesNumP))
    BuildTex.addMacros(subFolder, 'valBCAnoNumP', str(noNumP))

    BuildCharts.YesNoPie(subFolder + '\\pie231.png', yesNumP, noNumP)


def compute23b(subFolder, statData): # aggregate
    print '\nComputing values for slide 2.3.2.'
    values = StatValues.extractAnswers(statData, [52])

    yesNum = values.count('99') + values.count('100')
    noNum = values.count('101') + values.count('102')
    [yesNumP, noNumP] = StatValues.percent([yesNum,noNum])

    BuildTex.addMacros(subFolder, 'valBCByesNum', str(yesNum))
    BuildTex.addMacros(subFolder, 'valBCBnoNum', str(noNum))
    BuildTex.addMacros(subFolder, 'valBCByesNumP', str(yesNumP))
    BuildTex.addMacros(subFolder, 'valBCBnoNumP', str(noNumP))

    BuildCharts.YesNoPie(subFolder + '\\pie232.png', yesNumP, noNumP)


def compute23c(subFolder, statData): # aggregate (1 question)
    print '\nComputing values for slide 2.3.3.'
    values = StatValues.extractAnswers(statData, [53])

    ansA = values.count('120') 
    ansB = values.count('121')
    ansC = values.count('122') 
    [ansAp, ansBp, ansCp] = StatValues.percent([ansA, ansB, ansC])

    BuildTex.addMacros(subFolder, 'valBCCansA', str(ansA))
    BuildTex.addMacros(subFolder, 'valBCCansB', str(ansB))
    BuildTex.addMacros(subFolder, 'valBCCansC', str(ansC))
    BuildTex.addMacros(subFolder, 'valBCCansAp', str(ansAp))
    BuildTex.addMacros(subFolder, 'valBCCansBp', str(ansBp))
    BuildTex.addMacros(subFolder, 'valBCCansCp', str(ansCp))
    
    BuildCharts.Pie(subFolder + '\\pie233.png', [ansAp, ansBp, ansCp])


def compute23d(subFolder, statData): # aggregate
    print '\nComputing values for slide 2.3.4.'
    values = StatValues.extractAnswers(statData, [30])

    yesNum = values.count('83') + values.count('84')
    noNum = values.count('85') + values.count('86')
    [yesNumP, noNumP] = StatValues.percent([yesNum,noNum])

    BuildTex.addMacros(subFolder, 'valBCDyesNum', str(yesNum))
    BuildTex.addMacros(subFolder, 'valBCDnoNum', str(noNum))
    BuildTex.addMacros(subFolder, 'valBCDyesNumP', str(yesNumP))
    BuildTex.addMacros(subFolder, 'valBCDnoNumP', str(noNumP))

    BuildCharts.YesNoPie(subFolder + '\\pie234.png', yesNumP, noNumP)


