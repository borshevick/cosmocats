import pygame
import pygame.freetype

class Korabl:
    def __init__(self):
        self.picture=pygame.image.load("pictures/korabl.png")
        picturex=self.picture.get_width()/5
        picturey=self.picture.get_height()/5
        self.picture=pygame.transform.scale(self.picture,[picturex,picturey])
        self.hitbox=pygame.rect.Rect([350,500],[picturex,picturey])
        self.speed=3
        self.HP=3
        self.hitboxhp=pygame.rect.Rect([350,500],[picturex//1.5,picturey//1.2])
    def print(self,window):
        # pygame.draw.rect(window,[200,0,0],self.hitboxhp)
        window.blit(self.picture,self.hitbox)
    def move(self):
        keys=pygame.key.get_pressed()
        if keys[pygame.K_a]:
            self.hitbox.x=self.hitbox.x-self.speed
        if keys[pygame.K_d]:
            self.hitbox.x=self.hitbox.x+self.speed
        self.hitboxhp.center=self.hitbox.center

class Laser():
    def __init__(self,xy,picture,speed):
        self.picture=picture
        self.hitbox=pygame.rect.Rect(xy,picture.get_size())
        self.speed=speed
        picturex=self.picture.get_width()
        picturey=self.picture.get_height()
        self.hitboxhp=pygame.rect.Rect([350,500],[picturex//1.5,picturey//1.5])
    def print(self,window):
        # pygame.draw.rect(window,[200,0,0],self.hitboxhp)
        window.blit(self.picture,self.hitbox)
    def move(self):
        self.hitbox.y=self.hitbox.y-self.speed
        self.hitboxhp.center=self.hitbox.center
        
class Meteorit():
    def __init__(self,xy,picture,speedx,speedy):
        self.picture=picture
        self.hitbox=pygame.rect.Rect(xy,picture.get_size())
        self.speedx=speedx
        self.speedy=speedy
        picturex=self.picture.get_width()
        picturey=self.picture.get_height()
        self.hitboxhp=pygame.rect.Rect([350,500],[picturex//1.5,picturey//1.5])
    def print(self,window):
        # pygame.draw.rect(window,[200,0,0],self.hitboxhp)
        window.blit(self.picture,self.hitbox)
    def move(self):
        self.hitbox.y=self.hitbox.y+self.speedy
        self.hitbox.x=self.hitbox.x+self.speedx
        self.hitboxhp.center=self.hitbox.center


class Button():
    def __init__(self,xy,picture,text):
        self.picture=picture
        self.hitbox=pygame.rect.Rect(xy,picture.get_size())
        picturex=self.picture.get_width()
        picturey=self.picture.get_height()
        self.text=text
        txt=pygame.freetype.Font("pictures/Marske.ttf",45)
        txt_list=txt.render(text)
        self.txt_picture=txt_list[0]
        self.txt_hitbox=txt_list[1]
        self.txt_hitbox.center=self.hitbox.center
    def print(self,window):
        window.blit(self.picture,self.hitbox)
        window.blit(self.txt_picture,self.txt_hitbox)
        

    
