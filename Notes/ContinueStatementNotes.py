#Continue Statement:
#   used inside the body of a for or while loop
#   interrupts the current iteration of the loop
#   transfers execution to the top of the loop

for x in range(10):
    if x == 0:
        continue
    print(str(1/x))
