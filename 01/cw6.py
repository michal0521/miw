import random

students = list()

majk = tuple(['111911', dict(name='Michal', surname='Gebicki')])
marcin = tuple(['111515', dict(name='Marcin', surname='Stefanski')])

students.append(majk)
students.append(marcin)

# print(students)

students = dict(students)

# print(students)

for studentIndex in students:
    studentData = students[studentIndex]
    
    studentData['age'] = random.randint(20, 31)
    studentData['email'] = 'email address'
    studentData['address'] = 'physical address'

# print(students)

def getTelephoneNumber():
    result = ''
    
    for _ in range(0, 10):
        result += str(random.randint(0, 9))
        
    return result

tel1 = getTelephoneNumber()
tel2 = getTelephoneNumber()
tel3 = getTelephoneNumber()
tel4 = getTelephoneNumber()
tel5 = getTelephoneNumber()

# create list of telephone numbers, tel2 appears twice
telephoneNumbers = list([tel1, tel2, tel3, tel4, tel2, tel5])

# set() will create a set from given list, remove duplicates
# print(set(telephoneNumbers))

# print numbers from 1 to 11 
# for i in range(1, 11):
    # print(i)
    
for i in range(100, 15, -5): 
    print(i)