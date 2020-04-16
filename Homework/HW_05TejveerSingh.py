"""
Tejveer Singh
CS 100 2015F Section 009 
HW 05, Sept 15, 2015
"""

#Intitial answer: E
boolsSeen = 0
bools = [not True, not False, True, False, True and False, True or False]
for expr in bools:
    if expr:
        boolsSeen += 1
print(boolsSeen)
#Generated answer: D
#The answers are different because i was not aware that the variable conditon (expr) meant True. The variable was not defined for the block of code.


#Initial answer: A
aSeq = [2, 1, 0, -1, -2]
sum = aSeq[0] + aSeq[-1] + aSeq[-2]
print(sum)
#Generated answer: A


#Initial answer: D
mix = ['zero', 0, ['two'], -1]
print(mix[0:-1])
#Generated answer: C
#I forgot that the end interval stopped one before what you place it as.


#Initial answer: E
aList = ['one', -1, 2]
prefix = aList[:2]
suffix = aList[-1:]
print(prefix + suffix)
#Generated answer: E


#Initial answer: D
import turtle
s = turtle.Screen()
t = turtle.Turtle()
for i in range(4):
    if i%2 == 0:
        t.right(60)
        t.forward(100)
        t.right(60)
#Generated answer: D


#Question 11 Part A
s.bye()
s = turtle.Screen()
t = turtle.Turtle()
tickLen = float(input("What is the length of the tick you prefer? "))
def drawTick(t, tickLen):
    t.right(90)
    t.forward(tickLen)
    t.bk(tickLen)
    t.left(90)
drawTick(t, tickLen)
s.bye()


#Question 11 Part B
s = turtle.Screen()
t = turtle.Turtle()
tickLen = float(input("What is the length of the tick you prefer? "))
numTicks = int(input("How many ticks do you want? "))
distance = float(input("How far apart should the ticks be? "))
def drawTicks(t, tickLen, numTicks, distance):
    for x in range(numTicks):
        t.right(90)
        t.forward(tickLen)
        t.bk(tickLen)
        t.left(90)
        t.up()
        t.forward(distance)
        t.down()
drawTicks(t, tickLen, numTicks, distance)
