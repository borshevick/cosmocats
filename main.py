import pygame
import settings
import sprites
import random
pygame.init()
menu=0
meteorit_pictures=[]
game_laser=[]
game_meteorit=[]
gametime=pygame.time.Clock()
for i in range(1,11):
    Meteorit=pygame.image.load("pictures/meteorit1.png")
    razmer=random.randint(40,150)
    Meteorit=pygame.transform.scale(Meteorit,[razmer,razmer])
    meteorit_pictures.append(Meteorit)
korablhp=pygame.image.load("pictures/korabl.png")
korablhp=pygame.transform.scale(korablhp,[40,40])
buttonblue=pygame.image.load("pictures/assets/png/UI/buttonBlue.png")
buttonred=pygame.image.load("pictures/assets/png/UI/buttonRed.png")
fon=pygame.image.load("pictures/fon.png")
Laser=pygame.image.load("pictures/Laser.png")
Laser=pygame.transform.scale(Laser,[20,40])
fon=pygame.transform.scale(fon,[settings.WINDOWX,settings.WINDOWY])
window=pygame.display.set_mode([settings.WINDOWX,settings.WINDOWY])
korabl=sprites.Korabl()
Buttonblue=sprites.Button([450,450],buttonblue,"Играть")
Buttonred=sprites.Button([450,550],buttonred,"Выйти")
laser_sound=pygame.mixer.Sound("pictures/Lazer_sound.wav")
Music=pygame.mixer.Sound("pictures/music.wav")
Music.set_volume(0.1)
whilee=0
meteoritevent=pygame.USEREVENT
pygame.time.set_timer(meteoritevent,1000)
Music.play(-1)
while 1>whilee:
    events=pygame.event.get()
    for event in events:
        if event.type==pygame.QUIT: 
            whilee=whilee+1
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_SPACE:
                game_laser.append(sprites.Laser([korabl.hitbox.centerx-10,korabl.hitbox.centery],Laser,5))
                laser_sound.play()
        if event.type==pygame.MOUSEBUTTONDOWN:
            if menu==0:
                game_laser.append(sprites.Laser([korabl.hitbox.centerx-10,korabl.hitbox.centery],Laser,5)) 
            else:
                if Buttonblue.hitbox.collidepoint(event.pos):
                    menu=0
                    korabl.HP=3
                    game_laser.clear()
                    game_meteorit.clear()
                    korabl.hitbox.center=[350,500]
                if Buttonred.hitbox.collidepoint(event.pos):
                    whilee=1
        if event.type==meteoritevent:
            meteorit=sprites.Meteorit([random.randint(0,settings.WINDOWX),-100],meteorit_pictures[random.randint(0,9)],random.randint(-1,1),random.randint(1,5))
            game_meteorit.append(meteorit)
    

    
    for i in game_meteorit:
        i.move()
    if menu==0:
        korabl.move() 
        for i in game_laser:
            i.move()
        for i in game_meteorit:
            i.move()
        for i in game_meteorit:
            if i.hitboxhp.colliderect(korabl.hitboxhp):
                korabl.HP=korabl.HP-1
                game_meteorit.remove(i)
        for a in game_meteorit:
            for b in game_laser:
                if b.hitboxhp.colliderect(a.hitboxhp): 
                    game_meteorit.remove(a)
                    game_laser.remove(b)
        if korabl.HP<=0:
            menu=menu+1
    window.blit(fon,[0,0])
    
    for i in game_meteorit:
        i.print(window)
    if menu==0:
        x=100
        for i in game_laser:
            i.print(window)
        korabl.print(window)
        for i in range(0,korabl.HP):
            window.blit(korablhp,[x,0])
            x=x+50
    else:
        Buttonblue.print(window)
        Buttonred.print(window)
    pygame.display.update()
    gametime.tick(60)
meteorit
    