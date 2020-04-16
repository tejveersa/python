"""
Tejveer Singh
CS 100 2015F Section 009 
HW 0, Sept 5, 2015
"""

print("Excercise 5b")
hoursInADay = 24
minutesInAnHour = 60
minutesInADay = (24*60)

print(hoursInADay)
print("\n")
print(minutesInAnHour)
print(minutesInADay)
print("\n")

print("Excercise 5c")
changeMoney = 5.54
currencyRate = .68
ouncesUsed = 16.44

print(changeMoney)
print(currencyRate)
print(ouncesUsed)
print("\n")

print("Excercise 5d")
name = "Tejveer Singh"
nickname = "TJ"
lastName = "Singh"

print(name)
print(nickname)
print(lastName)
print("\n")

""" 2.12 """
s1 = "-"
s2 = "+"
x = s2 + s1 + s2 * 2

a = s1 + s2
b = a + s1
c = s2 + s1 * 2
d = c * 2
e = d * 5
f = (x + c) * 5

print("2.12 Answers:")
print("A. " + a)
print("B. " + b)
print("C. " + c)
print("D. " + d)
print("E. " + e)
print("F. " + f + "\n")


""" 2.13 """
s = "abcdefghijklmnopqrstuvwxyz"

a = s[0]
b = s[2]
c = s[25]
d = s[24]
e = s[16]

print("2.13 Answers:")
print("A. " + a)
print("B. " + b)
print("C. " + c)
print("D. " + d)
print("E. " + e + "\n")


""" 2.14 """
s = "goodbye"

a = (s [0] == "g")
b = (s [6] == "g")
c = (s [0:1] == "ga")
d = (s [5] == "x")
e = (s [len(s)//2] == "d")
f = (s [0] == s[6])
g = (s [3:6] == "tion")

print("2.14 Answers:")
print(a)
print(b)
print(c)
print(d)
print(e)
print(f)
print(g)
print("\n")


""" 2.15 """

x = "floccinaucinihilipilification"
z = "anachronistically"
y = "counterintuitive"

a = ((len(z)) - (len(y))) == 1
b = ("misinterpretation" < "misrepresentation")
c = (x.count("e") == 0)
d = (len("counterrevolution") == (len("counter") + len("resolution")))

print("2.15 Answers:")
print(a)
print(b)
print(c)
print(d)
print("\n")


""" 2.16 """

""" a """
a = 6
b = 7

print("2.16 A Answer:")
print(a)
print(b)
print("\n")

""" b """
c = (a + b)/2

print("2.16 B Answer:")
print(c)
print("\n")

""" c """
inventory = ("paper", "staples", "pencils")

print("2.16 C Answer:")
print(inventory)
print("\n")

""" d """
first = "John"
middle = "Fitzgerald"
last = "Kennedy"

print("2.16 D Answer:")
print("First: " + first)
print("Middle: " + middle)
print("Last: " + last + "\n")

""" e """
fullName = first + " " + middle + " " + last
print("2.16 E Answer:")
print("Full Name: " + fullName)



