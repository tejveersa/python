"""
Tejveer Singh
CS 100 2015F Section 009 
HW 04, Sept 5, 2015
"""

#3.20
lst = ('January', 'February', 'March')
for x in range(0, 3):
    print(lst[x][0:3])

#3.21
lst = [2,3,4,5,6,7,8,9]
for x in range(0, 7, 2):
    print(lst[x])

#3.22
lst = [2,3,4,5,6,7,8,9]
for x in lst:
    if ((x*x)%8 == 0):
        print(x)

#3.23
for x in range(0,2):
    print(x)

for x in range(0,1):
    print(x)

for x in range(3,7):
    print(x)

for x in range(1,2):
    print(x)

for x in range(0,4,3):
    print(x)
    
for x in range(5,22,4):
    print(x)
