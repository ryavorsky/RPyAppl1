# Statistics for chapter 5

import BuildTex
import BuildCharts
import StatValues

def  ComputeAll(subFolder, statData):

    compute71(subFolder, statData)
    compute72(subFolder, statData)
    compute73(subFolder, statData)
    compute74(subFolder, statData)

def compute71(subFolder, statData) :  # aggregate
    print '\nComputing values for slide 7.1.'
    values = StatValues.extractAnswers(statData, [56,57])
    values = StatValues.joinLists(values)

    yesNum = values.count('87') + values.count('88')
    noNum = values.count('89') + values.count('90')
    [yesNumP, noNumP] = StatValues.percent([yesNum,noNum])

    BuildTex.addMacros(subFolder, 'valGAyesNum', str(yesNum))
    BuildTex.addMacros(subFolder, 'valGAnoNum', str(noNum))
    BuildTex.addMacros(subFolder, 'valGAyesNumP', str(yesNumP))
    BuildTex.addMacros(subFolder, 'valGAnoNumP', str(noNumP))

    BuildCharts.YesNoPie(subFolder + '\\pie71.png', yesNumP, noNumP)


def compute72(subFolder, statData): # by age - q14
    print '\nComputing values for slide 7.2.'
    values = StatValues.extractAnswers(statData, [14, 56,57])
    values = StatValues.joinListsByAge(values)

    yesNum = [ val.count('87') + val.count('88') for val in values ]
    noNum = [ val.count('89') + val.count('90') for val in values ]

    BuildTex.addMacros(subFolder, 'valGByesNumA', str(yesNum[0]))
    BuildTex.addMacros(subFolder, 'valGByesNumB', str(yesNum[1]))
    BuildTex.addMacros(subFolder, 'valGByesNumC', str(yesNum[2]))
    BuildTex.addMacros(subFolder, 'valGByesNumD', str(yesNum[3]))
    BuildTex.addMacros(subFolder, 'valGBnoNumA', str(noNum[0]))
    BuildTex.addMacros(subFolder, 'valGBnoNumB', str(noNum[1]))
    BuildTex.addMacros(subFolder, 'valGBnoNumC', str(noNum[2]))
    BuildTex.addMacros(subFolder, 'valGBnoNumD', str(noNum[3]))

    BuildCharts.YesNoPie(subFolder + '\\pie72a.png', yesNum[0], noNum[0])
    BuildCharts.YesNoPie(subFolder + '\\pie72b.png', yesNum[1], noNum[1])
    BuildCharts.YesNoPie(subFolder + '\\pie72c.png', yesNum[2], noNum[2])
    BuildCharts.YesNoPie(subFolder + '\\pie72d.png', yesNum[3], noNum[3])


def compute73(subFolder, statData): # by category - q19
    print '\nComputing values for slide 7.3.'
    values = StatValues.extractAnswers(statData, [19, 56,57])
    values = StatValues.joinListsByCategory(values)

    yesNum = [ val.count('87') + val.count('88') for val in values ]
    noNum = [ val.count('89') + val.count('90') for val in values ]

    BuildTex.addMacros(subFolder, 'valGCyesNumA', str(yesNum[0]))
    BuildTex.addMacros(subFolder, 'valGCyesNumB', str(yesNum[1]))
    BuildTex.addMacros(subFolder, 'valGCyesNumC', str(yesNum[2]))
    BuildTex.addMacros(subFolder, 'valGCyesNumD', str(yesNum[3]))
    BuildTex.addMacros(subFolder, 'valGCyesNumE', str(yesNum[4]))
    BuildTex.addMacros(subFolder, 'valGCnoNumA', str(noNum[0]))
    BuildTex.addMacros(subFolder, 'valGCnoNumB', str(noNum[1]))
    BuildTex.addMacros(subFolder, 'valGCnoNumC', str(noNum[2]))
    BuildTex.addMacros(subFolder, 'valGCnoNumD', str(noNum[3]))
    BuildTex.addMacros(subFolder, 'valGCnoNumE', str(noNum[4]))

    BuildCharts.YesNoPie(subFolder + '\\pie73a.png', yesNum[0], noNum[0])
    BuildCharts.YesNoPie(subFolder + '\\pie73b.png', yesNum[1], noNum[1])
    BuildCharts.YesNoPie(subFolder + '\\pie73c.png', yesNum[2], noNum[2])
    BuildCharts.YesNoPie(subFolder + '\\pie73d.png', yesNum[3], noNum[3])
    BuildCharts.YesNoPie(subFolder + '\\pie73e.png', yesNum[4], noNum[4])


def compute74(subFolder, statData): # by question
    print '\nComputing values for slide 7.4.'
    values = StatValues.extractAnswers(statData, [56,57])
    values = StatValues.joinListsByQuestion(values)

    yesNum = [ val.count('87') + val.count('88') for val in values ]
    noNum = [ val.count('89') + val.count('90') for val in values ]

    BuildTex.addMacros(subFolder, 'valGDyesNumA', str(yesNum[0]))
    BuildTex.addMacros(subFolder, 'valGDyesNumB', str(yesNum[1]))
    BuildTex.addMacros(subFolder, 'valGDnoNumA', str(noNum[0]))
    BuildTex.addMacros(subFolder, 'valGDnoNumB', str(noNum[1]))

    BuildCharts.YesNoPie(subFolder + '\\pie74a.png', yesNum[0], noNum[0])
    BuildCharts.YesNoPie(subFolder + '\\pie74b.png', yesNum[1], noNum[1])
