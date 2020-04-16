"""
Tejveer Singh
CS 100 2015F
Section 009 
HW 08
10/22/15
"""
"""
readlines()
read(
"""

#1
def fcopy(in1,in2):
    out1 = open(in1,'r+')
    out2 = open(in2,'w')
    out2.write(out1.read())
    out1.close()
    out2.close()
fcopy("test.py","test1.py")
print(open("test1.py").read())

#2
def stats(fileTxt):
    inputFile = open(fileTxt, 'r')
    txt = inputFile.read()
    lines = txt.split("\n")
    words = txt.split()
    for x in lines:
        x = x.strip("\n")
    counter = 0
    for x in lines:
        for char in x:
            if char != " ":
                counter += 1
    inputFile.close()
    print("line count: "+ str(len(lines)))
    print("word count: "+ str(len(words)))
    print("character count: "+ str(counter))
    
#3
def repeatWords(in1, out):
    in1 = open(in1, 'r')
    out = open(out,'w')
    content = in1.read()
    for word in content.split(' '):
        if content.count(word) > 1:
           out.write()
    return content
