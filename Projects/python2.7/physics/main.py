#controls: Press up and down arrow for throttle
#press space for ignition and s to stop engine
#press d to deploy satellite
#press e to erase trail and press r to reset

import pygame, sys, random ,math
from pygame.locals import *
from math import atan2,pi
pygame.init()
FPS = 30
game_font = pygame.font.SysFont("engraversmt", 15)
fpsClock = pygame.time.Clock()
Display_Surface = pygame.display.set_mode((1024, 768))
#pygame.display.set_icon(pygame.image.load("icon.png"))
pygame.display.set_caption('Space')
#colours
White = (255, 255, 255)
Red = (255,0,0)
Black = ( 0, 0, 0)
Green = (0,255,30)
Blue = (153,255,255)
Grey = (217,217,217)
Yellow = (255,255,0)

#classes
global G
G = 6.674* 10 ** -11
global time
time = 1000
def draw(picx,picy,pic):
    Display_Surface.blit(pic,(picx,picy))
class Background:
    def __init__(self,x,y,img):
        self.img = img
        self.x = x
        self.y = y
    def newbg(self,img):
        self.img = img
    def drawbg(self):
        draw(self.x,self.y,self.img)   
class Spacecraft(pygame.sprite.Sprite):
    def __init__(self,x,y,image,name,thrust1,thrust2,mass):
        pygame.sprite.Sprite.__init__(self)
        self.img = image
        self.x = x
        self.y = y
        self.name = name
        self.thrust1 = thrust1
        self.thrust = 0
        self.mass = mass
        self.thrust2 = thrust2
        self.tfx = 0
        self.tfy = 0
        self.fx = 0
        self.fy = 0
        self.tx = 0
        self.ty = 0
        self.img2 = image
    def drawship(self):
        self.img = pygame.transform.rotate(self.img2,(-deg+90))
        draw(self.x,self.y,self.img)
    def calcforce(self,other):
        sx, sy = self.x+5, self.y+10
        ox, oy = other.x+25, other.y+25
        dx = (ox-sx)
        dy = (oy-sy)
       # print ox,oy,sx,sy,dx,dy
        d = math.sqrt(dx**2 + dy**2)
        f = G * self.mass * other.mass / (int(d*277000)**2) 
       
        theta = math.atan2(dy, dx)
        
        print f
        fc = game_font.render(str("Gravitiational Force: "+ str(f)+"N"), True, White)
        Display_Surface.blit(fc,(25, 70))
        
        f = .5
        
        fx = math.cos(theta) * f
        fy = math.sin(theta) * f
        #fx,fy,d,f,
        
        return fx, fy
    def force(self):
        self.fx,self.fy = Spacecraft.calcforce(self,earth)
        self.tfx = self.tfx + self.tx - self.fx
        self.tfy = self.tfy +  self.ty - self.fy
        #print self.tfx , self.fx , self.tx
        #print self.tfy , self.fy , self.ty
        
        self.x -= self.tfx
        self.y -= self.tfy
    def Throttle(self,percent):
        self.thrust = self.thrust1* percent
        th = game_font.render(str("Thrust: "+str(self.thrust2*percent)+"N"), True, White)
        Display_Surface.blit(th,(25, 85))
        self.tx = math.cos(math.radians(deg)) * self.thrust
        self.ty = math.sin(math.radians(deg)) * self.thrust
        
        #print self.thrust,self.tx,self.ty
#groups and variables
class otrail(pygame.sprite.Sprite):
    def __init__(self,x,y,img):
        pygame.sprite.Sprite.__init__(self)
        self.img = img
        self.x = x
        self.y = y
        
    def drawt(self):
        draw(self.x,self.y,self.img)
class Sat(pygame.sprite.Sprite):
    def __init__(self,x,y,image,tfx,tfy):
        pygame.sprite.Sprite.__init__(self)
        
        self.img = image
        self.x = x
        self.y = y
        
       
        self.mass = 500
        self.tfx = tfx
        self.tfy = tfy
        self.fx = 0
        self.fy = 0
        self.tx = 0
        self.ty = 0
        self.img2 = image
    def calcforce(self,other):
        sx, sy = self.x+5, self.y+10
        ox, oy = other.x+25, other.y+25
        dx = (ox-sx)
        dy = (oy-sy)
       # print ox,oy,sx,sy,dx,dy
        d = math.sqrt(dx**2 + dy**2)
        f = G * self.mass * other.mass / (d**2) * .0000000000000015
        
        
        theta = math.atan2(dy, dx)
        f = .5
        
        if f >2:
            f = 2
        fx = math.cos(theta) * f
        fy = math.sin(theta) * f
        #fx,fy,d,f,
        
        return fx, fy
    def force(self):
        self.fx,self.fy = Sat.calcforce(self,earth)
        self.tfx = self.tfx + self.tx - self.fx
        self.tfy = self.tfy +  self.ty - self.fy
        #print self.tfx , self.fx , self.tx
        #print self.tfy , self.fy , self.ty
        
        self.x -= self.tfx
        self.y -= self.tfy
    
    def draws(self):
        draw(self.x,self.y,self.img)
class Earth(pygame.sprite.Sprite):
    def __init__(self,x,y,img,mass):
        self.img = img
        self.x = x
        self.y = y
        self.mass = mass
    def drawe(self):
        draw(self.x,self.y,self.img)
all_sprites = pygame.sprite.Group()
trail = pygame.sprite.Group()
sats = pygame.sprite.Group()
click = False
menu = True
game = False
settings = False
maxfuel = 0
build = False
build1 = False
eng = 0
tank = 0
pay = 0
throttle = False
Stage1 = True
thr = .5
deg = 90
rotl = False
rotr = False
fuel = 0
earth = Earth(487,359,pygame.image.load("Earth.png"),5.972 * 10**24 )
bg = Background(0,0,pygame.image.load("bg.jpg"))
start1 = pygame.image.load("Start.png")
vabutton1 = pygame.image.load("Button1.png")
vabutton2 = pygame.image.load("Button2.png")
vabutton3 = pygame.image.load("Button3.png")
vabutton4 = pygame.image.load("Button4.png")
vabutton5 = pygame.image.load("Button5.png")
vabutton6 = pygame.image.load("Button6.png")
vabutton7 = pygame.image.load("Button7.png")
vabutton8 = pygame.image.load("Button8.png")
vabutton9 = pygame.image.load("Button9.png")
satc = 0
satct = 0
while True:
    if menu:
        Background.drawbg(bg)
        draw(412,250,start1)
       # draw(412,500,start1)
        #Menu stuff
        if click:
            if mx >= 412and mx <= 612 and my >= 250and my <=300:
                game = True
                build = True
                menu = False
                build1 = True
            elif mx >= 412and mx <= 612and my >= 500and my <=550:
                settings = True
      
        
      
        pass
    if game:
        if build:
            if build1:
                
                Background.newbg(bg,pygame.image.load("vab.png"))
                build1 = False
            Background.drawbg(bg)
            
            draw(75,25,vabutton1)
            draw(75,175,vabutton2)
            draw(75,325,vabutton3)
            draw(75,475,vabutton4)
            draw(75,625,vabutton5)
            draw(750,25,vabutton6)
            draw(750,175,vabutton7)
            draw(750,325,vabutton8)
            draw(750,475,vabutton9)
            draw(750,625,start1)
            if click:
                
                if mx >= 75 and mx <= 275 and my >= 25 and my <= 125:
                   eng = 1
                   thru = 6250000
                elif mx >= 75 and mx <= 275 and my >= 175 and my <= 275:
                   eng = 2
                   thru = 12500000
                elif mx >= 75 and mx <= 275 and my >= 325 and my <= 425:
                   eng = 3
                   thru = 25000000
                elif mx >= 75 and mx <= 275 and my >= 475 and my <= 575:
                    fuel = 100000
                    maxfuel = 100000
                elif mx >= 75 and mx <= 275 and my >= 625 and my <= 725:
                    fuel = 200000
                    maxfuel = 200000
                if mx >= 750 and mx <= 950 and my >= 25 and my <= 125:
                    fuel = 300000
                    maxfuel = 300000
                elif mx >= 750 and mx <= 950 and my >= 175 and my <= 275:
                    pay = 12500
                    satc = 10
                    satct = 10
                elif mx >= 750 and mx <= 950 and my >= 325 and my <= 425:
                    pay = 25000
                    satc = 20
                    satct = 20
                elif mx >= 750 and mx <= 950 and my >= 475 and my <= 575:
                    pay = 50000
                    satc = 30
                    satct = 30
                elif mx >= 750 and mx <= 950 and my >= 625 and my <= 675:
                    if eng != 0 and fuel != 0 and pay != 0:
                        rocket = Spacecraft(507,339,pygame.image.load("craft.png"),"Player",eng,thru,pay)
                        Background.newbg(bg,pygame.image.load("world.png"))
                        build = False



            
        else:
            Background.drawbg(bg)
            Display_Surface.fill(Black)
            Earth.drawe(earth)
            for tra in trail:
                tra.drawt()
            for sa in sats:
                sa.force()
                sa.draws()
            Spacecraft.drawship(rocket)
            tr = otrail(rocket.x+5, rocket.y+10,pygame.image.load("trail.png"))
            trail.add(tr)
            per = fuel *1.0/ maxfuel*1.0
            if per >.5:
                pygame.draw.rect(Display_Surface,Green, (90,20,278*per,23), 0)
            elif per > 0.25:
                pygame.draw.rect(Display_Surface,Yellow, (90,20,278*per,23), 0)
            else:
                pygame.draw.rect(Display_Surface,Red, (90,20,278*per,23), 0)
            draw(0,0,pygame.image.load("fuelbar.png"))
            satre = game_font.render(str("Satellites in cargo: "+ str(satc)), True, White)
            Display_Surface.blit(satre,(25, 100))
            if Stage1:
                if rotl:
                    deg -= 5
                if rotr:
                    deg += 5
                if throttle:
                    Spacecraft.Throttle(rocket,thr)
                
                    Spacecraft.force(rocket)
                    if thr >0:
                      fuel -= 500
            if fuel <=0 :
                thr = 0
    if settings:
        pass
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

        if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
                    mx,my = pygame.mouse.get_pos()
                
        if event.type == MOUSEBUTTONUP:
            if event.button == 1:
                    click = False
        if event.type == pygame.KEYDOWN:
            
                if event.key == K_SPACE and game and not build and fuel > 0:
                    throttle = True
                elif event.key == K_s and game and not build and throttle:
                    thr = 0
                if event.key == K_e and game and not build:
                    for tra in trail:
                        tra.kill()
                if event.key == K_r and game and not build:
                    for tra in trail:
                        tra.kill()
                    for sa in sats:
                        sa.kill()
                    rocket.kill()
                    
                    throttle = False
                    
                    thr = 1
                    deg = 90
                    rotl = False
                    rotr = False
                    fuel = maxfuel
                    rocket = Spacecraft(507,339,pygame.image.load("craft.png"),"Player",eng,thru,pay)
                    satc = satct
                if event.key == K_d and game and not build and satc > 0:
                    sata = Sat(rocket.x +5, rocket.y +10,pygame.image.load("sat.png"),rocket.tfx,rocket.tfy)
                    sats.add(sata)
                    satc -= 1
                #Throtle up or down
                if event.key == K_UP and game and not build and fuel > 0:
                    thr += .1
                    if thr >=1:
                        thr = 1
                if event.key == K_DOWN and game and not build:
                    thr -= .1
                    if thr <=0:
                        thr = 0
                #rotate
                if event.key == K_LEFT and game and not build:
                    rotl = True
                    
                    
                if event.key == K_RIGHT and game and not build:
                    rotr = True
        if event.type == pygame.KEYUP:
             if event.key == K_LEFT and game and not build:
                    rotl = False
                    
                    
             if event.key == K_RIGHT and game and not build:
                    rotr = False
    pygame.display.update()

    fpsClock.tick(FPS)
