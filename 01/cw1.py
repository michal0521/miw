text = """Lorem Ipsum jest tekstem stosowanym jako przykladowy wypelniacz w przemysle poligraficznym. Zostal po raz pierwszy uzyty w XV w.
    przez nieznanego drukarza do wypelnienia tekstem probnej ksiazki. Piec wiekow pozniej zaczal byc uzywany przemysle elektronicznym, 
    pozostajac praktycznie niezmienionym. Spopularyzowal sie w latach 60. XX w. wraz z publikacja arkuszy Letrasetu, zawierajacych fragmenty 
    Lorem Ipsum, a ostatnio z zawierajacym rozne wersje Lorem Ipsum oprogramowaniem przeznaczonym do realizacji drukow na komputerach 
    osobistych, jak Aldus PageMaker"""

def addLetterToResult(letter, result):
    # if letter is not a number and is not a character exit
    if not letter.isalpha():
        return
    
    if (letter in result):
        result[letter] += 1
    else:
        result[letter] = 1 

def countLetters(text):
    result = dict()
    
    for i in range(len(text)):
        # we want L and l to be counted as 1 letter, lowercase it
        letter = text[i].lower()
    
        #add letter to letters counter
        addLetterToResult(letter, result)
    
    return result

def getLetterCountsMessage(letterCounts):
    message = 'W tekscie jest '

    for index, key in enumerate(letterCounts):
        message += f'{str(letterCounts[key])} liter "{key}"'
        
        # if this letter count is not the last one add 'oraz'
        # before next letter count, add '.' otherwise as the end of message
        if index != len(letterCounts) - 1:
            message += ' oraz '
        else:
            message += '.'
    
    return message

# count how many each of letters in text occur
letterCounts = countLetters(text)
        
# get human readable description of how many letters of each type occur
message = getLetterCountsMessage(letterCounts)
    
print(message)

