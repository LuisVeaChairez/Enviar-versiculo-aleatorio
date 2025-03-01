from requests import get
from .randomNumber import getRandomNumber

def getRandomVerse (books) :
    ENDPOINT_READ = 'https://bible-api.deno.dev/api/read/'
    VERSION = 'rv1960'
    versos = []
    rango = False

    minBook = 0
    maxBook = 65
    numBook = getRandomNumber(minBook, maxBook)

    chosenBookCap = f'{books[numBook]['names'][0]}'
    chosenBook = chosenBookCap.lower()
    numberChaps = books[numBook]['chapters']

    getChapter = f'{getRandomNumber(1, numberChaps)}'

    minRangeOfVerses = f'{getRandomNumber(0, len(getChapter)) + 1}'
    maxRangeOfVerses = f'{getRandomNumber(0, len(getChapter)) + 1}'

    if minRangeOfVerses == maxRangeOfVerses:
        rango = False
        rangeOfVerses = minRangeOfVerses
        rangoCompleto = rangeOfVerses 
    else:
        if minRangeOfVerses < maxRangeOfVerses:
            rango = True
            rangeOfVerses = f'{minRangeOfVerses}-{maxRangeOfVerses}'
        else:
            rango = True
            rangeOfVerses = f'{maxRangeOfVerses}-{minRangeOfVerses}'
        rangoCompleto = rangeOfVerses

    ENDPOINT_CHOSEN_VERSE = f'{ENDPOINT_READ}{VERSION}/{chosenBook}/{getChapter}/{rangeOfVerses}'
    results = get(ENDPOINT_CHOSEN_VERSE).json()

    if rango:
        for i in results:
            versos.append(i['verse'])
    else:
        versos.append(results['verse'])

    return versos, chosenBookCap, rangoCompleto