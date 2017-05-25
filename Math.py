def ToString (List): # Coverts List to String
    return ''.join(List)
def Math (x):
    reading_file=open('Formula.txt', 'r')
    lines=reading_file.readlines()
    Formula = lines[1]
    m = int(Formula[2])
    m1 = 2 # The Last # used for this
    if Formula[3] != "x":
        m1 = 3
        m = int(Formula[2] + Formula[3])
        if Formula[4] != "x":
            m1 = 3
            m = int(Formula[2] + Formula[3] + Formula[4])
    b = int(Formula[4+m1])
    print b
    if len(Formula)-1 >= 5+m1:
        b = int(Formula[4+m1]+Formula[5+m1])
        if len(Formula)-1 >= 6+m1:
            b = int(Formula[6+m1] +Formula[5+m1]+Formula[4+m1])
    print "m =", m
    print "b =", b
    print "x =", x
    y = m*x + b
    print " == ", y
    # y = Angle
    # x = Distance
    
    #return Angle

Math(10)
