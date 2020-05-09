def weirdConcatLists(aList, bList):
    return [value for index, value in enumerate(aList) if index % 2 == 0] + [value for index, value in enumerate(bList) if index % 2 == 1]

aList = ['np1', 'p1', 'np2', 'p2', 'np3', 'p3']
bList = ['np1', 'p1', 'np2', 'p2', 'np3', 'p3']

# print(weirdConcatLists(aList, bList))

def getWordData(word):
    wordLetters = list()
    [wordLetters.append(letter) for letter in word if letter not in wordLetters]
    wordLength = len(word)
    bigLetters = word.upper()
    smallLetters = word.lower()
    
    return dict(
        length=wordLength,
        letters=wordLetters,
        big_letters=bigLetters,
        small_letters=smallLetters,
    )
    
print(getWordData('Michalinio'))