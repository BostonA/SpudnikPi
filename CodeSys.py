"""
Codes:
    Format
    1: Ma Full 2: SM 1212 3: Si Full 4: Go Full Free: Y 12:12
    
Pos: 3+4, 11+12 24+25, 35+36
Silver: 111
Gold: 100
Magic: 010
Giant: 110
Legendary: 001
Super Magic: 101

Time
xxxx xxxx

Y = 1

Time

xxxx: xxxx

Exsample
1: Si Full 2: SM 12:12 3: G0 Full 4: Go Full Free: Y 12:12
Ma    Full   SM    12:12  Go    Full    Go  Full
010 00000000 101 11001100 100 00000000 100 00000000
"""
import time
Code = []
Expanded_Line =[]
reading_file=open('newfile.txt', 'r')
lines=reading_file.readlines()
GoodLine = lines[len(lines) - 1]
for x in GoodLine:
    Expanded_Line.append(x)
#print Expanded_Line

if Expanded_Line[3] + Expanded_Line[4] == "Si":
    Code.append([1,1,1])
    print "Silver Chest"
elif Expanded_Line[3] + Expanded_Line[4] == "Go":
    Code.append([1,0,0])
    print "Golden Chest"
elif Expanded_Line[3] + Expanded_Line[4] == "Ma":
    Code.append([0,1,0])
    print "Magic Chest"
elif Expanded_Line[3] + Expanded_Line[4] == "Gi":
    Code.append([1,1,0])
    print "Giant Chest"
elif Expanded_Line[3] + Expanded_Line[4] == "Li":
    Code.append([0,0,1])
    print "Legendary Chest"
elif Expanded_Line[3] + Expanded_Line[4] == "SM":
    Code.append([1,0,1])
    print "Super Magical Chest"
elif Expanded_Line[3] + Expanded_Line[4] == "Ep":
    Code.append([0,1,1])
    print "Epic Chest"
else:
    print "Error: php format incorrect"

print "\n"
print Expanded_Line[6:10]
if Expanded_Line[6:10] == ['F', 'u', 'l', 'l']:
    Code.append([0,0,0,0])
else:
    print "Numbers"
    if Expanded_Line[6] + Expanded_Line[7] == "01"
    elif 
    elif 
print Expanded_Line[14] + Expanded_Line[15]
if Expanded_Line[13] + Expanded_Line[14] == "Si":
    Code.append([1,1,1])
    print "Silver Chest"
elif Expanded_Line[14] + Expanded_Line[15] == "Go":
    Code.append([1,0,0])
    print "Golden Chest"
elif Expanded_Line[14] + Expanded_Line[15] == "Ma":
    Code.append([0,1,0])
    print "Magic Chest"
elif Expanded_Line[14] + Expanded_Line[15] == "Gi":
    Code.append([1,1,0])
    print "Giant Chest"
elif Expanded_Line[14] + Expanded_Line[15] == "Le":
    Code.append([0,0,1])
    print "Legendary Chest"
elif Expanded_Line[14] + Expanded_Line[15] == "SM":
    Code.append([1,0,1])
    print "Super Magical Chest"
else:
    print "Error: php format incorrect"
print Code
    
    
    