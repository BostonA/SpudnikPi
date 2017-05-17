"""
Yo
"""
import RPi.GPIO as GPIO
import time
"""
open('/tmp/newfile.txt', 'w+')
afile = open('/tmp/newfile.txt', 'w')
afile.write("00 00 00 00 N")
afile.close()
Foo
"""
restTime = .5
flashPattern = [12, 3, 8, 3]
GPIO.setmode(GPIO.BCM)
GPIO.setup(4,GPIO.OUT)
def flashLEDon ():
    print "LED on"
    GPIO.output(4, GPIO.HIGH)
def flashLEDoff ():
    print "LED off"
    GPIO.output(4, GPIO.LOW)
while True:
    Free = False
    Code = []
    Expanded_Line =[]

    reading_file=open('/tmp/newfile.txt', 'r')

    lines=reading_file.readlines()
    GoodLine = lines[len(lines) - 1]
    OldGood = GoodLine
    oldLinesGood = lines
    while True:
        time.sleep(1)
        # Change the Loacation Not sure where
        reading_file=open('/tmp/newfile.txt', 'r')
        lines=reading_file.readlines()
        print lines
        GoodLine = lines[len(lines) - 1]
        print
        if len(GoodLine)==14 and len(lines) > len(oldLinesGood):
            break
        OldGood = GoodLine
        oldLinesGood = lines
    for x in GoodLine:
        Expanded_Line.append(x)
        #print Expanded_Line
    if Expanded_Line[0] + Expanded_Line[1] == "03":
        Code.append(3)
        print "3 Hours"
    elif Expanded_Line[0] + Expanded_Line[1] == "08":
        Code.append(8)
        print "8 Hours"
    elif Expanded_Line[0] + Expanded_Line[1] == "12":
        Code.append(12)
        print "12 Hours"
    elif Expanded_Line[0] + Expanded_Line[1] == "24":
        Code.append(24)
        print "24 Hours"
    else:
        Code.append(0)
        print "Empty"
    if Expanded_Line[3] + Expanded_Line[4] == "03":
        Code.append(3)
        print "3 Hours"
    elif Expanded_Line[3] + Expanded_Line[4] == "08":
        Code.append(8)
        print "8 Hours"
    elif Expanded_Line[3] + Expanded_Line[4] == "12":
        Code.append(12)
        print "12 Hours"
    elif Expanded_Line[3] + Expanded_Line[4] == "24":
        Code.append(24)
        print "24 Hours"
    else:
        Code.append(0)
        print "Empty"
    if Expanded_Line[6] + Expanded_Line[7] == "03":
        Code.append(3)
        print "3 Hours"
    elif Expanded_Line[6] + Expanded_Line[7] == "08":
        Code.append(8)
        print "8 Hours"
    elif Expanded_Line[6] + Expanded_Line[7] == "12":
        Code.append(12)
        print "12 Hours"
    elif Expanded_Line[6] + Expanded_Line[7] == "24":
        Code.append(24)
        print "24 Hours"
    else:
        Code.append(0)
        print "Empty"
    if Expanded_Line[9] + Expanded_Line[10] == "03":
        Code.append(3)
        print "3 Hours"
    elif Expanded_Line[9] + Expanded_Line[10] == "08":
        Code.append(8)
        print "8 Hours"
    elif Expanded_Line[9] + Expanded_Line[10] == "12":
        Code.append(12)
        print "12 Hours"
    elif Expanded_Line[9] + Expanded_Line[10] == "24":
        Code.append(24)
        print "24 Hours"
    else:
        Code.append(0)
        print "Empty"
    if Expanded_Line[12] == "Y":
        print "Free: on"
        Free = True
    elif Expanded_Line[12] == "N":
        Free = False
        print "Free: off"
    else:
        print "Error: php formating incorrect"
    print Code
    flashLEDon()
    time.sleep(1)
    flashLEDoff()
    time.sleep(1)
    for x in Code:
        print x
        flashLEDon ()
        if x == 3:
            time.sleep(1)
            print "on for 1 sec"
        elif x == 8:
            time.sleep(2)
            print "on for 2 sec"
        elif x == 12:
            time.sleep(3)
            print "on for 3 sec"
        elif x == 24:
            time.sleep(4)
            print "on for 4 sec"
        elif x == 0:
            time.sleep(5)
            print "on for 5 sec"
        else:
            print "error"
        flashLEDoff()
        time.sleep(1)
    flashLEDon()
    if Free:
        time.sleep(2)
        print "on for 2 sec"
    else:
        time.sleep(1)
        print "on for 1 sec"
    flashLEDoff()
