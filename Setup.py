import pygame
def Shapes(screen):
    pygame.draw.rect(screen, [0, 0, 0], [10, 225, 155, 40], 1)
    pygame.draw.rect(screen, [0, 0, 0], [10, 270, 155, 200], 1)
    pygame.draw.rect(screen, [0, 0, 0], [15,275, 45, 45], 1)
    pygame.draw.rect(screen, [0, 0, 0], [65,275, 45, 45], 1)
    pygame.draw.rect(screen, [0, 0, 0], [115,275, 45, 45], 1)
    pygame.draw.rect(screen, [0, 0, 0], [15,325, 45, 45], 1)
    pygame.draw.rect(screen, [0, 0, 0], [65,325, 45, 45], 1)
    pygame.draw.rect(screen, [0, 0, 0], [115,325, 45, 45], 1)
    pygame.draw.rect(screen, [0, 0, 0], [15,375, 45, 45], 1)
    pygame.draw.rect(screen, [0, 0, 0], [65,375, 45, 45], 1)
    pygame.draw.rect(screen, [0, 0, 0], [115,375, 45, 45], 1)
    pygame.draw.rect(screen, [0, 0, 0], [15,425, 45, 40], 1)
    pygame.draw.rect(screen, [0, 0, 0], [65,425, 45, 40], 1)
    pygame.draw.rect(screen, [0, 0, 0], [115,425, 45, 40], 1)
def CheckForButton (x, y, KeyEntry, StartFire, HeadingSel, DistanceSel,HeadingFirstTime,DistanceFirstTime, Adder):
    if 15 < x < 60 and 275 < y < 320:
        KeyEntry.append("1")
    elif 65 < x < 110 and 275 < y < 320:
        KeyEntry.append("2")
    elif 115 < x < 160 and 275 < y < 320:
        KeyEntry.append("3")
    elif 15 < x < 60 and 325 < y < 365:
        KeyEntry.append("4")
    elif 65 < x < 110 and 325 < y < 365:
        KeyEntry.append("5")
    elif 115 < x < 160 and 325 < y < 365:
        KeyEntry.append("6")
    elif 15 < x < 60 and 375 < y < 420:
        KeyEntry.append("7")
    elif 65 < x < 110 and 375 < y < 420:
        KeyEntry.append("8")
    elif 115 < x < 160 and 375 < y < 420:
        KeyEntry.append("9")
    elif 15 < x < 60 and 425 < y < 475:
        KeyEntry.append("0")
    elif 360 < x < 440 and 125 < y < 205:
        Adder = True
        print "FOOED"
    elif 15 < x < 170 and 145 < y < 190:
        HeadingSel = True
        HeadingFirstTime = True
        if DistanceSel:
            DistanceSel = False
    elif 175 < x < 340 and 145 < y < 190:
        DistanceSel = True
        DistanceFirstTime = True 
        if HeadingSel:
            HeadingSel = False
    elif 65 < x < 110 and 425 < y < 475:
        if len(KeyEntry) >0:
            del KeyEntry[len(KeyEntry)-1]
    elif 115 < x < 160 and 425 < y < 475:
        StartFire = True
    return KeyEntry, StartFire, HeadingSel, DistanceSel,HeadingFirstTime,DistanceFirstTime,Adder
