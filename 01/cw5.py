# create list with numbers from 1 to 10
numbersList = list(range(1, 11))

leftPart = numbersList[:5]
rightPart = numbersList[5:]

numbersList = leftPart + rightPart

print(numbersList)

numbersList = [0] + numbersList

print(numbersList)

numbersListCopy = numbersList.copy()

numbersListCopy.sort(reverse=True)
print(numbersListCopy)