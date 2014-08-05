# Statistics for chapter 4

import BuildTex
import BuildCharts
import StatValues

def ComputeAll(subFolder, statData):
    
    compute41(subFolder, statData)

    compute42a(subFolder, statData)
    compute42b(subFolder, statData)
    compute42c(subFolder, statData)

def compute41(subFolder, statData): # one question 
    print '\nComputing values for slide 4.1.'
    values = StatValues.extractAnswers(statData, [36])
    ansA = values.count('91') 
    ansB = values.count('92')
    ansC = values.count('93') 
    ansD = values.count('94')
    [ansAp, ansBp, ansCp, ansDp] = StatValues.percent([ansA, ansB, ansC, ansD])

    BuildTex.addMacros(subFolder, 'valDAansA', str(ansA))
    BuildTex.addMacros(subFolder, 'valDAansB', str(ansB))
    BuildTex.addMacros(subFolder, 'valDAansC', str(ansC))
    BuildTex.addMacros(subFolder, 'valDAansD', str(ansD))
    BuildTex.addMacros(subFolder, 'valDAansAp', str(ansAp))
    BuildTex.addMacros(subFolder, 'valDAansBp', str(ansBp))
    BuildTex.addMacros(subFolder, 'valDAansCp', str(ansCp))
    BuildTex.addMacros(subFolder, 'valDAansDp', str(ansDp))
    
    BuildCharts.Pie(subFolder + '\\pie41.png', [ansAp, ansBp, ansCp, ansDp])


def compute42a(subFolder, statData): # one question 
    print '\nComputing values for slide 4.2.a'
    values = StatValues.extractAnswers(statData, [37])
    ansA = values.count('95') 
    ansB = values.count('96')
    ansC = values.count('97') 
    ansD = values.count('98')
    [ansAp, ansBp, ansCp, ansDp] = StatValues.percent([ansA, ansB, ansC, ansD])

    BuildTex.addMacros(subFolder, 'valDBAansA', str(ansA))
    BuildTex.addMacros(subFolder, 'valDBAansB', str(ansB))
    BuildTex.addMacros(subFolder, 'valDBAansC', str(ansC))
    BuildTex.addMacros(subFolder, 'valDBAansD', str(ansD))
    BuildTex.addMacros(subFolder, 'valDBAansAp', str(ansAp))
    BuildTex.addMacros(subFolder, 'valDBAansBp', str(ansBp))
    BuildTex.addMacros(subFolder, 'valDBAansCp', str(ansCp))
    BuildTex.addMacros(subFolder, 'valDBAansDp', str(ansDp))
    
    BuildCharts.Pie(subFolder + '\\pie42_a_.png', [ansAp, ansBp, ansCp, ansDp])


def compute42b(subFolder, statData): # one question 
    print '\nComputing values for slide 4.2.b.'
    values = StatValues.extractAnswers(statData, [45])
    ansA = values.count('107') 
    ansB = values.count('108')
    ansC = values.count('109') 
    ansD = values.count('110')
    ansE = values.count('111')
    [ansAp, ansBp, ansCp, ansDp, ansEp] = StatValues.percent([ansA, ansB, ansC, ansD, ansE])

    BuildTex.addMacros(subFolder, 'valDBBansA', str(ansA))
    BuildTex.addMacros(subFolder, 'valDBBansB', str(ansB))
    BuildTex.addMacros(subFolder, 'valDBBansC', str(ansC))
    BuildTex.addMacros(subFolder, 'valDBBansD', str(ansD))
    BuildTex.addMacros(subFolder, 'valDBBansE', str(ansE))
    BuildTex.addMacros(subFolder, 'valDBBansAp', str(ansAp))
    BuildTex.addMacros(subFolder, 'valDBBansBp', str(ansBp))
    BuildTex.addMacros(subFolder, 'valDBBansCp', str(ansCp))
    BuildTex.addMacros(subFolder, 'valDBBansDp', str(ansDp))
    BuildTex.addMacros(subFolder, 'valDBBansEp', str(ansEp))
    
    BuildCharts.Pie(subFolder + '\\pie42_b_.png', [ansAp, ansBp, ansCp, ansDp, ansEp])


def compute42c(subFolder, statData): # one question 
    print '\nComputing values for slide 4.2.c.'
    values = StatValues.extractAnswers(statData, [54])

    yesNum = values.count('87') + values.count('88')
    noNum = values.count('89') + values.count('90')
    [yesNumP, noNumP] = StatValues.percent([yesNum,noNum])

    BuildTex.addMacros(subFolder, 'valDBCyesNum', str(yesNum))
    BuildTex.addMacros(subFolder, 'valDBCnoNum', str(noNum))
    BuildTex.addMacros(subFolder, 'valDBCyesNumP', str(yesNumP))
    BuildTex.addMacros(subFolder, 'valDBCnoNumP', str(noNumP))

    BuildCharts.YesNoPie(subFolder + '\\pie42_c_.png', yesNum, noNum)

