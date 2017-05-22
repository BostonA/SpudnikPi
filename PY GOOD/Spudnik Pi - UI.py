import pygame, sys, time, Setup, Extra
def ToString (List): # Coverts List to String
    return ''.join(List)
KeyEntry = []
num = 3.5
StartFire = True
pygame.init()
screen =  pygame.display.set_mode([800,480])
screen.fill([105,105,105])
pygame.display.set_caption('Spudnik Pi')
a = pygame.image.load('Logo.png')
b = pygame.image.load('Logo.png')
a = pygame.transform.scale(a, (75, 75))
pygame.display.set_icon(b)
Smallfont = pygame.font.Font(None, 25)
font = pygame.font.Font(None, 50)
Bigfont = pygame.font.Font(None, 100)
Free = False
#Code = []
Expanded_Line =[]
reading_file=open('DataStore.txt', 'r') #Opens File 
lines=reading_file.readlines()
GoodLine = lines[len(lines) - 1]
OldGood = GoodLine
oldLinesGood = lines #Sets up lines for comparison
print "Waiting For Data..." #Fancy Command Line thing
Title = font.render("SpudNik Pi!", 1, (0, 0, 0))
TitlePos = [85, 30]
Key1 = font.render("1", 1, (0, 0, 0))
Key1Pos = [28, 275]
Key2 = font.render("2", 1, (0, 0, 0))
Key2Pos = [78, 275]
Key3 = font.render("3", 1, (0, 0, 0))
Key3Pos = [128, 275]
Key4 = font.render("4", 1, (0, 0, 0))
Key4Pos = [28, 325]
Key5 = font.render("5", 1, (0, 0, 0))
Key5Pos = [78, 325]
Key6 = font.render("6", 1, (0, 0, 0))
Key6Pos = [128, 325]
Key7 = font.render("7", 1, (0, 0, 0))
Key7Pos = [28, 375]
Key8 = font.render("8", 1, (0, 0, 0))
Key8Pos = [78, 375]
Key9 = font.render("9", 1, (0, 0, 0))
Key9Pos = [128, 375]
Key0 = font.render("0", 1, (0, 0, 0))
Key0Pos = [28, 422]
KeyBK = font.render("<-", 1, (0, 0, 0))
KeyBKPos = [72, 422]

ScreenPos = [15, 220]

pygame.display.flip()
Heading = "NULL"
Distance = "NULL"
OldHeadingDistance=[]
Even = True
Loaded = False
Armed = False
DoneWait = False
Potato1 = True
Tank2 = False
Fire = False
while True:
    if DoneWait:
        print "Infomation Receved From Server" 
        x = 0
        Heading = [] #list of everything in heading.
        Distance = [] #list of everything in distance. 
        #First Num
        for char in GoodLine:
            if char == " ": #Looking for spacebar
                break
            x = x + 1
        y = 0
        for char in GoodLine:
            if y == x: #When len is the same as the first loop
                break #END
            Heading.append(char) #adding it to a list
            y = y + 1
        OldY = y
        # Second Num
        x = 0
        y = 0
        z = False
        for char in GoodLine:
            if char == " ": #Skips the first space
                if z:
                    break # Then it breaks
                z = True
            x = x + 1
        for char in GoodLine:
            if y == x:
                break
            if y> OldY:
                Distance.append(char) #It only prints after the first space
            y = y + 1
        UserUnit = GoodLine[y+1]
        print ToString(Distance)
        if UserUnit == "F": # Converstion to Feet
            Distance = float(ToString(Distance)) * 0.3048
        elif UserUnit == "M":
            Distance = ToString(Distance)
        else:
            print "Error: Feet Meter Conversion" #Then Just Prints Stuff!
        print " - All In Meters - "
        print "Heading at " + ToString(Heading) + "degrees."
        print "Distance of " + str(Distance)
        OldHeadingDistance.append([ToString(Heading),Distance])
        DoneWait = False
    else:
        reading_file=open('DataStore.txt', 'r')
        lines=reading_file.readlines()
        #print lines
        GoodLine = lines[len(lines) - 1] #GoodLine is the last line of the file!
        if len(lines) > len(oldLinesGood): # If there are more lines in the new one one was added. So then that line should be read
            DoneWait = True
        else:
            DoneWait = False
        OldGood = GoodLine # Resets Vars For comparison
        oldLinesGood = lines

    pygame.draw.rect(screen, [75, 75, 75], [0, 0, 625, 100], 0)
    Setup.Shapes(screen)
    screen.blit(a,(5,12.5))
    screen.blit(Title, TitlePos)
    screen.blit(Key1, Key1Pos)
    screen.blit(Key2, Key2Pos)
    screen.blit(Key3, Key3Pos)
    screen.blit(Key4, Key4Pos)
    screen.blit(Key5, Key5Pos)
    screen.blit(Key6, Key6Pos)
    screen.blit(Key7, Key7Pos)
    screen.blit(Key8, Key8Pos)
    screen.blit(Key9, Key9Pos)
    screen.blit(Key0, Key0Pos)
    screen.blit(KeyBK, KeyBKPos)
    Fire,Potato1,StartFire=Extra.WebsiteControl(screen, Smallfont, ToString(Heading), Distance, OldHeadingDistance, Fire, Potato1, StartFire)

    Even,num = Extra.ArmSequence(Loaded,Even,Potato1, screen, font, Bigfont, Armed, num, StartFire,Tank2, Fire)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            #Screen = font.render("1", 1, (0, 0, 0))
            if not StartFire:
                x = Setup.CheckForButton(event.pos[0], event.pos[1], KeyEntry, StartFire)
                KeyEntry = x[0]
                StartFire = x[1]
            if StartFire:
                print Armed, Tank2, Potato1
                if Armed:
                    print "Firing"
                if Tank2:
                    print "loading"
                    Armed = True
                    StartFire = False
                    Potato1 = False
                    Tank2 = False
                    num=3.5
                elif Potato1:
                    print "STAGE 1"
                    Tank2 = True
                else:
                    print "HEY"
                    Potato1=True
    pygame.display.flip()
    screen.fill([105,105,105])
    
    if len(KeyEntry) < 8:
        Screenf = font.render(''.join(KeyEntry), 1, (0, 0, 0))
    else:
        Screenf = font.render("Ov.Flow", 1, (0, 0, 0))
    screen.blit(Screenf, ScreenPos)
    

                
