# basic formatting

name = 'Michal'
surname = 'Gebicki'

fullname = '{} {}'.format(name, surname)

print(fullname)


# padding and aligning strings

text = 'my name is cena'

# text centered with '_' chosen as filler to empty spots
resultText = '{:_^20}'.format(text)

# text aligned to left
#resultText = '{:<20}'.format(text)

# text aligned to right
#resultText = '{:>20}'.format(text)

print(resultText)


# truncating long strings

print('{:.6}'.format('very very long text'))


# numbers (positive and negative). Add whitespace before the number
# so the minus sign will not break the alligned numbers

# positive number
print('{: d}'.format(42))
# negative number
print('{: d}'.format(-41))


# named placeholders

# we can select where to put each of format() method arguments
print('{firstValue} {lastValue}'.format(lastValue='what am I', firstValue="yeah"))