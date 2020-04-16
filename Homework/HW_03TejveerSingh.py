"""
Tejveer Singh
CS 100 2015F Section 009 
HW 03, Sept 15, 2015
"""

# 1
# i.
a = 3
b = 4
c = 5

# ii.

if a < b:
    print("OK")

# iii.
if c < b:
    print("OK")

# iv.
if (a + b) == c:
    print("OK")

# v.
if (a^2) + (b^2) == (c^2):
    print("OK")

# 2
# i.
a = 3
b = 4
c = 5

# ii.

if a < b:
    print("OK")

# iii.
if c < b:
    print("OK")
else:
    print("NOT OK")

# iv.
if (a + b) == c:
    print("OK")
else:
    print("NOT OK")

# v.
if (a^2) + (b^2) == (c^2):
    print("OK")

# 3
import turtle
s = turtle.Screen()
t = turtle.Turtle()

t.color(input("what color?"))

t.width(float(input("what line width?")))

pixels = float(input("what line length?"))

shape = input("line, triangle, or square?")
if shape == "line":
    t.forward(pixels)
elif shape == "triangle":
    t.forward(pixels)
    t.right(120)
    t.forward(pixels)
    t.right(120)
    t.forward(pixels)
elif shape == "square":
    t.forward(pixels)
    t.right(90)
    t.forward(pixels)
    t.right(90)
    t.forward(pixels)
    t.right(90)
    t.forward(pixels)
    
