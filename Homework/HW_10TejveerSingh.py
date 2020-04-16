#Group 6

def square(t, size):
    t.down()
    for i in range(4):
        t.forward(size)
        t.left(90)
def squares(t, size, num, increment):
    for i in range(num):
        square(t, size)
        size += increment

#Group 3
def circle(t, diam):
    t.down()
    t.circle(diam)

def donut(t, diams, space, rep, deg):
    for i in range(rep):
        circle(t, diams)
        t.up()
        t.forward(space)
        t.left(deg)

#Group 2

def halfCircle(t, rad):
## This is what the picture shows
##    for x in range(180):
##        t.forward(1)
##        t.left(1)
## This is what the answer should be (the question is wrongly displayed - give them points off)
    t.circle(rad, 180)

def spiral(t, rad, incr, reps):
    for i in range(reps):
        t.circle(rad, 180)
        rad += incr


