# Statistics for chapter 8

import BuildTex
import BuildCharts
import StatValues

def  ComputeAll(subFolder, statData):

    compute81(subFolder, statData)
    compute82a(subFolder, statData)
    compute82b(subFolder, statData)
    compute82c(subFolder, statData)
    compute83(subFolder, statData)
    compute84(subFolder, statData)


def compute81(subFolder, statData) :  # aggregate
    print '\nComputing values for slide 8.1.'
    values = StatValues.extractAnswers(statData, [34])

    yesNum = values.count('87') + values.count('88')
    noNum = values.count('89') + values.count('90')
    [yesNumP, noNumP] = StatValues.percent([yesNum,noNum])

    BuildTex.addMacros(subFolder, 'valHAyesNum', str(yesNum))
    BuildTex.addMacros(subFolder, 'valHAnoNum', str(noNum))
    BuildTex.addMacros(subFolder, 'valHAyesNumP', str(yesNumP))
    BuildTex.addMacros(subFolder, 'valHAnoNumP', str(noNumP))

    BuildCharts.YesNoPie(subFolder + '\\pie81.png', yesNum, noNum)


def compute82a(subFolder, statData): # aggregate
    print '\nComputing values for slide 8.2.1.'
    values = StatValues.extractAnswers(statData, [47])

    yesNum = values.count('83') + values.count('84')
    noNum = values.count('85') + values.count('86')
    [yesNumP, noNumP] = StatValues.percent([yesNum,noNum])

    BuildTex.addMacros(subFolder, 'valHBAyesNum', str(yesNum))
    BuildTex.addMacros(subFolder, 'valHBAnoNum', str(noNum))
    BuildTex.addMacros(subFolder, 'valHBAyesNumP', str(yesNumP))
    BuildTex.addMacros(subFolder, 'valHBAnoNumP', str(noNumP))

    BuildCharts.YesNoPie(subFolder + '\\pie821.png', yesNum, noNum)


def compute82b(subFolder, statData): # by age - q14
    print '\nComputing values for slide 8.2.2.'
    values = StatValues.extractAnswers(statData, [14, 47])
    values = StatValues.joinListsByAge(values)

    yesNum = [ val.count('83') + val.count('84') for val in values ]
    noNum = [ val.count('85') + val.count('86') for val in values ]

    BuildTex.addMacros(subFolder, 'valHBByesNumA', str(yesNum[0]))
    BuildTex.addMacros(subFolder, 'valHBByesNumB', str(yesNum[1]))
    BuildTex.addMacros(subFolder, 'valHBByesNumC', str(yesNum[2]))
    BuildTex.addMacros(subFolder, 'valHBByesNumD', str(yesNum[3]))
    BuildTex.addMacros(subFolder, 'valHBBnoNumA', str(noNum[0]))
    BuildTex.addMacros(subFolder, 'valHBBnoNumB', str(noNum[1]))
    BuildTex.addMacros(subFolder, 'valHBBnoNumC', str(noNum[2]))
    BuildTex.addMacros(subFolder, 'valHBBnoNumD', str(noNum[3]))

    BuildCharts.YesNoPie(subFolder + '\\pie822a.png', yesNum[0], noNum[0])
    BuildCharts.YesNoPie(subFolder + '\\pie822b.png', yesNum[1], noNum[1])
    BuildCharts.YesNoPie(subFolder + '\\pie822c.png', yesNum[2], noNum[2])
    BuildCharts.YesNoPie(subFolder + '\\pie822d.png', yesNum[3], noNum[3])


def compute82c(subFolder, statData): # by category - q19
    print '\nComputing values for slide 8.2.3.'
    values = StatValues.extractAnswers(statData, [19, 47])
    values = StatValues.joinListsByCategory(values)

    yesNum = [ val.count('83') + val.count('84') for val in values ]
    noNum = [ val.count('85') + val.count('86') for val in values ]

    BuildTex.addMacros(subFolder, 'valHBCyesNumA', str(yesNum[0]))
    BuildTex.addMacros(subFolder, 'valHBCyesNumB', str(yesNum[1]))
    BuildTex.addMacros(subFolder, 'valHBCyesNumC', str(yesNum[2]))
    BuildTex.addMacros(subFolder, 'valHBCyesNumD', str(yesNum[3]))
    BuildTex.addMacros(subFolder, 'valHBCyesNumE', str(yesNum[4]))
    BuildTex.addMacros(subFolder, 'valHBCnoNumA', str(noNum[0]))
    BuildTex.addMacros(subFolder, 'valHBCnoNumB', str(noNum[1]))
    BuildTex.addMacros(subFolder, 'valHBCnoNumC', str(noNum[2]))
    BuildTex.addMacros(subFolder, 'valHBCnoNumD', str(noNum[3]))
    BuildTex.addMacros(subFolder, 'valHBCnoNumE', str(noNum[4]))

    BuildCharts.YesNoPie(subFolder + '\\pie823a.png', yesNum[0], noNum[0])
    BuildCharts.YesNoPie(subFolder + '\\pie823b.png', yesNum[1], noNum[1])
    BuildCharts.YesNoPie(subFolder + '\\pie823c.png', yesNum[2], noNum[2])
    BuildCharts.YesNoPie(subFolder + '\\pie823d.png', yesNum[3], noNum[3])
    BuildCharts.YesNoPie(subFolder + '\\pie823e.png', yesNum[4], noNum[4])


def compute83(subFolder, statData): # one question 
    print '\nComputing values for slide 8.3.'
    values = StatValues.extractAnswers(statData, [48])
    ansA = values.count('112') 
    ansB = values.count('113')
    ansC = values.count('114') 
    ansD = values.count('123')
    [ansAp, ansBp, ansCp, ansDp] = StatValues.percent([ansA, ansB, ansC, ansD])

    BuildTex.addMacros(subFolder, 'valHCansA', str(ansA))
    BuildTex.addMacros(subFolder, 'valHCansB', str(ansB))
    BuildTex.addMacros(subFolder, 'valHCansC', str(ansC))
    BuildTex.addMacros(subFolder, 'valHCansD', str(ansD))
    BuildTex.addMacros(subFolder, 'valHCansAp', str(ansAp))
    BuildTex.addMacros(subFolder, 'valHCansBp', str(ansBp))
    BuildTex.addMacros(subFolder, 'valHCansCp', str(ansCp))
    BuildTex.addMacros(subFolder, 'valHCansDp', str(ansDp))
    
    BuildCharts.Pie(subFolder + '\\pie83.png', [ansA, ansB, ansC, ansD])

def compute84(subFolder, statData): # one question 
    print '\nComputing values for slide 8.4.'
    values = StatValues.extractAnswers(statData, [49])
    ansA = values.count('115') 
    ansB = values.count('116')
    ansC = values.count('117') 
    ansD = values.count('118')
    [ansAp, ansBp, ansCp, ansDp] = StatValues.percent([ansA, ansB, ansC, ansD])

    BuildTex.addMacros(subFolder, 'valHDansA', str(ansA))
    BuildTex.addMacros(subFolder, 'valHDansB', str(ansB))
    BuildTex.addMacros(subFolder, 'valHDansC', str(ansC))
    BuildTex.addMacros(subFolder, 'valHDansD', str(ansD))
    BuildTex.addMacros(subFolder, 'valHDansAp', str(ansAp))
    BuildTex.addMacros(subFolder, 'valHDansBp', str(ansBp))
    BuildTex.addMacros(subFolder, 'valHDansCp', str(ansCp))
    BuildTex.addMacros(subFolder, 'valHDansDp', str(ansDp))
    
    BuildCharts.Pie(subFolder + '\\pie84.png', [ansA, ansB, ansC, ansD])
