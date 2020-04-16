"""
Tejveer Singh
CS 100 2015F Section 009 
HW 04, Oct 13, 2015
"""

#Problem 1
def twoWords(length,firstLetter):
    rtn = []
    while True:
        word=input("A "+str(length)+"-letter word please: ")
        if len(word) == length:
            rtn.append(word)
            break
    while True:
        wordTwo= input("A word beginning with "+firstLetter+" please: ")
        if wordTwo[0] == firstLetter or wordTwo[0] == firstLetter.upper():
            rtn.append(wordTwo)
            break
    return(rtn)

#Problem 2

def twoWordsV2(length, firstLetter):
    rtn= []
    word=input("A "+str(length)+"-letter word please: ")
    while len(word) != length:
       word=input("A "+str(length)+"-letter word please: ")
    rtn.append(word)

    wordTwo= input("A word beginning with "+firstLetter+" please: ")
    while wordTwo[0] != firstLetter or wordTwo[0] != firstLetter.upper():
           wordTwo= input("A word beginning with "+firstLetter+" please: ")
    rtn.append(wordTwo)
    return(rtn)

#Problem 3

def lastfirst(argument):
    
    firstNames = []
    lastNames = []
    for i in argument:
        x = 0
        while i[x] != ",":
            x+=1
        l = i[:x]
        f = i[(x+2):]
        lastNames.append(l)
        firstNames.append(f)
    return(firstNames, lastNames)

#Problem 4

def mystery(n):
    x = 0
    while n != 1:
        n = n//2
        x +=1
    return(x)


#Problem 5

def enterNewPassword():
    
    password = input("Enter a password: ")
    while len(password) < 8 or len(password) > 15:
        for x in password:
            if x in "0123456789":
                print("You failed one test. Enter a password between 8-15 characters including one digit.")
                enterNewPassword()
            else:
                print("You failed both tests. Enter a password between 8-15 characters including one digit.")
                enterNewPassword()
    
    for x in password:
        if x in "0123456789":
            break
        else:
            print("You failed one test. Enter a password between 8-15 characters including one digit.")
            enterNewPassword()
enterNewPassword()
