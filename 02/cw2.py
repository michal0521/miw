def removeCharFromString(char, string):
    if not char.isalpha():
        return string
    
    result = list()
    [result.append(letter) for letter in string if not letter == char]
    
    return ''.join([letter for letter in result])

print(removeCharFromString('M', 'Michal'))