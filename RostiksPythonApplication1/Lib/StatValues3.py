# Statistics for chapter 3

import BuildTex
import StatValues

def ComputeAll(subFolder, statData):

    compute31a(subFolder, statData)
    compute31b(subFolder, statData)
    compute31c(subFolder, statData)

    compute32a(subFolder, statData)
    compute32b(subFolder, statData)
    compute32c(subFolder, statData)
    compute32d(subFolder, statData)


def compute31a(subFolder, statData): # aggregate
    print '\nComputing values for slide 3.1.1.'
    values = StatValues.extractAnswers(statData, [43])

    yesNum = values.count('103') + values.count('104')
    noNum = values.count('105') + values.count('106')
    [yesNumP, noNumP] = StatValues.percent([yesNum,noNum])

    BuildTex.addMacros(subFolder, 'valCAAyesNum', str(yesNum))
    BuildTex.addMacros(subFolder, 'valCAAnoNum', str(noNum))
    BuildTex.addMacros(subFolder, 'valCAAyesNumP', str(yesNumP))
    BuildTex.addMacros(subFolder, 'valCAAnoNumP', str(noNumP))


def compute31b(subFolder, statData): # by age - q14
    print '\nComputing values for slide 3.1.2.'
    values = StatValues.extractAnswers(statData, [14, 43])
    values = StatValues.joinListsByAge(values)

    yesNum = [ val.count('103') + val.count('104') for val in values ]
    noNum = [ val.count('105') + val.count('106') for val in values ]

    BuildTex.addMacros(subFolder, 'valCAByesNumA', str(yesNum[0]))
    BuildTex.addMacros(subFolder, 'valCAByesNumB', str(yesNum[1]))
    BuildTex.addMacros(subFolder, 'valCAByesNumC', str(yesNum[2]))
    BuildTex.addMacros(subFolder, 'valCAByesNumD', str(yesNum[3]))
    BuildTex.addMacros(subFolder, 'valCABnoNumA', str(noNum[0]))
    BuildTex.addMacros(subFolder, 'valCABnoNumB', str(noNum[1]))
    BuildTex.addMacros(subFolder, 'valCABnoNumC', str(noNum[2]))
    BuildTex.addMacros(subFolder, 'valCABnoNumD', str(noNum[3]))


def compute31c(subFolder, statData): # by category - q19
    print '\nComputing values for slide 3.1.3.'
    values = StatValues.extractAnswers(statData, [19, 43])
    values = StatValues.joinListsByCategory(values)

    yesNum = [ val.count('103') + val.count('104') for val in values ]
    noNum = [ val.count('105') + val.count('106') for val in values ]

    BuildTex.addMacros(subFolder, 'valCACyesNumA', str(yesNum[0]))
    BuildTex.addMacros(subFolder, 'valCACyesNumB', str(yesNum[1]))
    BuildTex.addMacros(subFolder, 'valCACyesNumC', str(yesNum[2]))
    BuildTex.addMacros(subFolder, 'valCACyesNumD', str(yesNum[3]))
    BuildTex.addMacros(subFolder, 'valCACyesNumE', str(yesNum[4]))
    BuildTex.addMacros(subFolder, 'valCACnoNumA', str(noNum[0]))
    BuildTex.addMacros(subFolder, 'valCACnoNumB', str(noNum[1]))
    BuildTex.addMacros(subFolder, 'valCACnoNumC', str(noNum[2]))
    BuildTex.addMacros(subFolder, 'valCACnoNumD', str(noNum[3]))
    BuildTex.addMacros(subFolder, 'valCACnoNumE', str(noNum[4]))


def compute32a(subFolder, statData): # aggregate
    print '\nComputing values for slide 3.2.1.'
    values = StatValues.extractAnswers(statData, [40,41,42])
    values = StatValues.joinLists(values)

    yesNum = values.count('99') + values.count('100')
    noNum = values.count('101') + values.count('102')
    [yesNumP, noNumP] = StatValues.percent([yesNum,noNum])

    BuildTex.addMacros(subFolder, 'valCBAyesNum', str(yesNum))
    BuildTex.addMacros(subFolder, 'valCBAnoNum', str(noNum))
    BuildTex.addMacros(subFolder, 'valCBAyesNumP', str(yesNumP))
    BuildTex.addMacros(subFolder, 'valCBAnoNumP', str(noNumP))


def compute32b(subFolder, statData): # by age - q14
    print '\nComputing values for slide 3.2.2.'
    values = StatValues.extractAnswers(statData, [14, 40,41,42])
    values = StatValues.joinListsByAge(values)

    yesNum = [ val.count('99') + val.count('100') for val in values ]
    noNum = [ val.count('101') + val.count('102') for val in values ]

    BuildTex.addMacros(subFolder, 'valCBByesNumA', str(yesNum[0]))
    BuildTex.addMacros(subFolder, 'valCBByesNumB', str(yesNum[1]))
    BuildTex.addMacros(subFolder, 'valCBByesNumC', str(yesNum[2]))
    BuildTex.addMacros(subFolder, 'valCBByesNumD', str(yesNum[3]))
    BuildTex.addMacros(subFolder, 'valCBBnoNumA', str(noNum[0]))
    BuildTex.addMacros(subFolder, 'valCBBnoNumB', str(noNum[1]))
    BuildTex.addMacros(subFolder, 'valCBBnoNumC', str(noNum[2]))
    BuildTex.addMacros(subFolder, 'valCBBnoNumD', str(noNum[3]))


def compute32c(subFolder, statData): # by category - q19
    print '\nComputing values for slide 3.2.3.'
    values = StatValues.extractAnswers(statData, [19, 40,41,42])
    values = StatValues.joinListsByCategory(values)

    yesNum = [ val.count('99') + val.count('100') for val in values ]
    noNum = [ val.count('101') + val.count('102') for val in values ]

    BuildTex.addMacros(subFolder, 'valCBCyesNumA', str(yesNum[0]))
    BuildTex.addMacros(subFolder, 'valCBCyesNumB', str(yesNum[1]))
    BuildTex.addMacros(subFolder, 'valCBCyesNumC', str(yesNum[2]))
    BuildTex.addMacros(subFolder, 'valCBCyesNumD', str(yesNum[3]))
    BuildTex.addMacros(subFolder, 'valCBCyesNumE', str(yesNum[4]))
    BuildTex.addMacros(subFolder, 'valCBCnoNumA', str(noNum[0]))
    BuildTex.addMacros(subFolder, 'valCBCnoNumB', str(noNum[1]))
    BuildTex.addMacros(subFolder, 'valCBCnoNumC', str(noNum[2]))
    BuildTex.addMacros(subFolder, 'valCBCnoNumD', str(noNum[3]))
    BuildTex.addMacros(subFolder, 'valCBCnoNumE', str(noNum[4]))

def compute32d(subFolder, statData): # by question
    print '\nComputing values for slide 3.2.4.'
    values = StatValues.extractAnswers(statData, [40,41,42])
    values = StatValues.joinListsByQuestion(values)

    yesNum = [ val.count('99') + val.count('100') for val in values ]
    noNum = [ val.count('101') + val.count('102') for val in values ]

    BuildTex.addMacros(subFolder, 'valCBDyesNumA', str(yesNum[0]))
    BuildTex.addMacros(subFolder, 'valCBDyesNumB', str(yesNum[1]))
    BuildTex.addMacros(subFolder, 'valCBDyesNumC', str(yesNum[2]))
    BuildTex.addMacros(subFolder, 'valCBDnoNumA', str(noNum[0]))
    BuildTex.addMacros(subFolder, 'valCBDnoNumB', str(noNum[1]))
    BuildTex.addMacros(subFolder, 'valCBDnoNumC', str(noNum[2]))
