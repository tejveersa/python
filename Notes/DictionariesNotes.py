grades = [95,96,100,85,95,90,95,100,100]

def gradeCounts(lst):
    count = {}
    for x in lst:
        if x not in count:
            count[x] = 1
        else:
            count[x] += 1
    return count

mydict = gradeCounts(grades)
mykeys = []
for x in mydict.keys():
    mykeys.append(x)

sortedmykeys = sorted(mykeys, reverse = True)
print(sortedmykeys)

for x in sortedmykeys:
    print("key: "  + str(x) + "  val: " + str(mydict[x]))
