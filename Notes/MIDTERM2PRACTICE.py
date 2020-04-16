'''
MIDTERM 2 PRACTICE
D
E
A
B
D
E
B
C
E
D
'''

def rectangle(t, size1, size2):
    t.down()
    for i in range(2):
        t.forward(size1)
        t.left(90)
        t.forward(size2)
        t.left(90)
def panels(t, initSize, delta, numPanels, angle):
    for i in range(numPanels):
        rectangle(t, initSize + delta * i,2* (initSize + delta * i))
        t.left(angle)

import turtle
s = turtle.Screen()
shelly = turtle.Turtle()
panels(shelly, 20, 15, 8, 20)

def vowelUseDict(t):
    vowels = 'aeiou'
    d = {}
    wordlist = t.split()
    for vowel in vowels:
        for word in wordlist:
            if vowel in word:
                if vowel not in d:
                    d[vowel] = 1
                else:
                    d[vowel] +=1
    return d

text = 'like a vision she dances across the porch as the radio plays'
print(vowelUseDict(text))
