trueCount = 0
if not True or False:
    trueCount += 1
elif True and not False:
    trueCount += 1
if True or False:
    trueCount += 1
elif not True or not False:
    trueCount += 1
else:
    trueCount +=1
print(trueCount)

aSeq = [-1, 0, 1, 2]
add = aSeq[-1] + aSeq[0] + aSeq[1]
print(add)

nested = [0, [], 1]
print(nested[0:1])

ints = [-2, -1, 0, 1, 2]
negative = ints[:2]
positive = ints[-2:]
print(negative + positive)
