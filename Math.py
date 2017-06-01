##You need to edit the formula in the file named 'Formula.txt' to the desmos formula
##
##Created By Boston Abrams
##
##With Help from Martin ( :
##
##                        
def Maths (x):
    reading_file=open('Formula.txt', 'r')
    lines=reading_file.readlines()
    Formula = lines[1]
    m1 = 0
    count = 0
    m = ""
    while True:
        if Formula[count+2] != "x":
            m1 = count+2
            m = m + Formula[count+2]
        else:
            break
        count = count + 1
    m = float(m)
    b = ""
    print b
    print count
    while True:
        if len(Formula)-1 >= count+3:
            b = b + Formula[count+3]
        else:
            break
        count=count+1
    b = float(b)
    print "m =", m
    print "b =", b
    print "x =", x
    y = float(m)*int(x) + float(b)
    #print " == ", y
    # y = Angle
    # x = Distance
    
    return y
print Maths(10)
## ---------------------------------------------------------
## Extra Bonus Code -> Old Versions ( :
##def Mathing(x):
##    m = 2
##    b = 1
##    return float(m)*int(x) + float(b)
##  
##def ToString (List): # Coverts List to String
##    return ''.join(List)
##def Math (x):
##    reading_file=open('Formula.txt', 'r')
##    lines=reading_file.readlines()
##    Formula = lines[1]
##    m = float(Formula[2])
##    m1 = 2 # The Last # used for this
##    if Formula[3] != "x":
##        m1 = 3
##        m = float(Formula[2] + Formula[3])
##        if Formula[4] != "x":
##            m1 = 4
##            m = float(Formula[2] + Formula[3] + Formula[4])
##    print m
##    b = int(Formula[3+m1])
##    print b
##    if len(Formula)-1 >= 5+m1:
##        b = float(Formula[3+m1]+Formula[4+m1]+Formula[5+m1])
##        if len(Formula)-1 >= 6+m1:
##            b = float(Formula[3+m1] +Formula[4+m1]+Formula[5+m1]+ Formula[6+m1])
##    print "m =", m
##    print "b =", b
##    print "x =", x
##    y = float(m)*int(x) + float(b)
##    #print " == ", y
##    # y = Angle
##    # x = Distance
##    
##    return y
