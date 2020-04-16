#Local Function
def function():
    a = 1
    a += 1
    print(a)

a = 5
function()
print(a)
#Output: 2/5

#Global Function
def function():
    global a
    a += 1
    print(a)

a = 5
function()
print(a)
#Output: 6/6
