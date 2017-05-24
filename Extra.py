import pygame, httplib
def ArmSequence (Loaded, Even, Potato1, screen, font, Bigfont, Armed, num,StartFire, Tank2, Fire):
    if StartFire:
        pygame.draw.ellipse(screen, [225, 0, 0], [0, 0, 800, 480], 0)
        if Tank2:
            Render = Bigfont.render("Pressurize Tank", 1, (0, 0, 0))
            screen.blit(Render, [200, 175])
        elif Potato1:
            Render = Bigfont.render("Load Potato", 1, (0, 0, 0))
            screen.blit(Render, [200, 175])
        if Even:
            Render = font.render("- Press When Done - ", 1, (0, 0, 0))
            screen.blit(Render, [210, 275])
            Even = False
        else:
            Even = True
    elif Fire:
        num = num- .05
        if 3 < num < 4:
            Hugefont = pygame.font.Font(None, 700)
            Render = Hugefont.render("3", 1, (255, 0, 0))
            screen.blit(Render, [240, -50])
        if 2 < num < 3:
            Hugefont = pygame.font.Font(None, 700)
            Render = Hugefont.render("2", 1, (255, 0, 0))
            screen.blit(Render, [240, -50])
        if 1 < num < 2:
            Hugefont = pygame.font.Font(None, 700)
            Render = Hugefont.render("1", 1, (255, 0, 0))
            screen.blit(Render, [240, -50])
        if 0 < num < 1:
            Hugefont = pygame.font.Font(None, 700)
            Render = Hugefont.render("Fire", 1, (255, 0, 0))
            screen.blit(Render, [-50, -50])
    
    return Even, num, Fire
def WebsiteControl (screen, font, H, D, OLDHD, Fire, Potato1, StartFire):
    conn = httplib.HTTPConnection("www.lego.com")
    conn.request("HEAD", "/")
    r1 = conn.getresponse()
    #print r1.status, r1.reason 
    pygame.draw.rect(screen, [60,60,60], [625, 0, 175, 480], 0)

    Title = font.render("WebServer:", 1, (0,0,0))
    screen.blit(Title, [635, 5])
    Title = font.render("On", 1, (0,255,0))
    screen.blit(Title, [730, 5])
    Title = font.render("Reciving Requests", 1, (0,0,0))
    screen.blit(Title, [635, 40])
    if H != "NULL" and D != "NULL":
        pygame.draw.rect(screen, [0,0,0], [630, 75, 165, 125], 1)
        Title = font.render("Request", 1, (0,0,0))
        screen.blit(Title, [635, 80])
        txt = "Heading: "+str(OLDHD[0][0])
        Title = font.render(txt, 1, (0,0,0))
        screen.blit(Title, [635, 100])
        Title = font.render("Distance: "+str(OLDHD[0][1]), 1, (0,0,0))
        screen.blit(Title, [635, 120])
        #Fire=True
        #Potato1 = True
        #StartFire = True
        #del OLDHD[0]
        if len(OLDHD) > 1:
            pygame.draw.rect(screen, [0,0,0], [630, 205, 165, 125], 1)
            Title = font.render("Request", 1, (0,0,0))
            screen.blit(Title, [635, 210])
            txt = "Heading: "+str(OLDHD[1][0])
            Title = font.render(txt, 1, (0,0,0))
            screen.blit(Title, [635, 230])
            Title = font.render("Distance: "+str(OLDHD[1][1]), 1, (0,0,0))
            screen.blit(Title, [635, 250])
            if len(OLDHD) > 2:
                pygame.draw.rect(screen, [0,0,0], [630, 335, 165, 125], 1)
                Title = font.render("Request", 1, (0,0,0))
                screen.blit(Title, [635, 340])
                txt = "Heading: "+str(OLDHD[2][0])
                Title = font.render(txt, 1, (0,0,0))
                screen.blit(Title, [635, 360])
                Title = font.render("Distance: "+str(OLDHD[2][1]), 1, (0,0,0))
                screen.blit(Title, [635, 380])
    return Fire, Potato1, StartFire

  
 


