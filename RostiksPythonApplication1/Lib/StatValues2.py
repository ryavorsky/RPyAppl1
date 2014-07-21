# Statistics for chapter 2

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

def compute21a(subFolder, statData): # aggregate
    print '\nComputing values for slide 2.1.1.'
    values = StatValues.extractAnswers(statData, [38,39])
    return []

def compute21b(subFolder, statData): # by age - q14
    print '\nComputing values for slide 2.1.2.'
    values = StatValues.extractAnswers(statData, [14, 38,39])
    return []

def compute21c(subFolder, statData): # by category - q19
    print '\nComputing values for slide 2.1.3.'
    values = StatValues.extractAnswers(statData, [19, 38,39])
    return []

def compute21d(subFolder, statData): # by question
    print '\nComputing values for slide 2.1.4.'
    values = StatValues.extractAnswers(statData, [35,38,39,50,55])
    return []

def compute22a(subFolder, statData): # aggregate
    print '\nComputing values for slide 2.2.1.'
    values = StatValues.extractAnswers(statData, [28,29,46,47])
    return []

def compute22b(subFolder, statData): # by age
    print '\nComputing values for slide 2.2.2.'
    values = StatValues.extractAnswers(statData, [14, 28,29,46,47])
    return []

def compute22c(subFolder, statData): # by category - q19
    print '\nComputing values for slide 2.2.3.'
    values = StatValues.extractAnswers(statData, [19, 28,29,46,47])
    return []

def compute22d(subFolder, statData): # by question
    print '\nComputing values for slide 2.2.4.'
    values = StatValues.extractAnswers(statData, [28,29,46,47])
    return []

def compute22e(subFolder, statData): # aggregate (1 question)
    print '\nComputing values for slide 2.2.5.'
    values = StatValues.extractAnswers(statData, [49])
    return []

