"""
Tejveer Singh
CS 100 2015F Section 009 
HW 01, Sept 11, 2015
"""

flowers = ["rose", "bougainvillea", "yucca", "marigold", "daylilly", "lilly of the valley"]
print(flowers)

print("potato" in flowers)

thorny = [flowers[0:2]]
print(thorny)

poisonous = [flowers[-1]]
print(poisonous)

dangerous = thorny + poisonous
print(dangerous)

answers = ['N', 'N', 'N', 'Y', 'Y', 'N', 'N', 'Y', 'Y', 'N', 'N', 'Y']

numYes = answers.count('Y')
print(numYes)

numNo = answers.count('N')
print(numNo)

percentYes = (numYes/(numYes+numNo))
print(percentYes)

answers.sort()
print(answers)

print(answers.index('Y'))

lastName = "Perchovik"
firstName = "Luis"

s = lastName[0]
t = firstName[0]
print(t + s)
