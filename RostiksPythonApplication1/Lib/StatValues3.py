# Statistics for chapter 3

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
    return []

def compute31b(subFolder, statData): # by age - q14
    print '\nComputing values for slide 3.1.2.'
    values = StatValues.extractAnswers(statData, [14, 43])
    return []

def compute31c(subFolder, statData): # by category - q19
    print '\nComputing values for slide 3.1.3.'
    values = StatValues.extractAnswers(statData, [19, 43])
    return []

def compute32a(subFolder, statData): # aggregate
    print '\nComputing values for slide 3.2.1.'
    values = StatValues.extractAnswers(statData, [40,41,42])
    return []

def compute32b(subFolder, statData): # by age - q14
    print '\nComputing values for slide 3.2.2.'
    values = StatValues.extractAnswers(statData, [14, 40,41,42])
    return []

def compute32c(subFolder, statData): # by category - q19
    print '\nComputing values for slide 3.2.3.'
    values = StatValues.extractAnswers(statData, [19, 40,41,42])
    return []

def compute32d(subFolder, statData): # by question
    print '\nComputing values for slide 3.2.4.'
    values = StatValues.extractAnswers(statData, [40,41,42])
    return []
