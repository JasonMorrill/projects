# This program simulates  sorting routines
import pygame, sys, random,time
from pygame.locals import *
pygame.init()
FPS = 100
game_font = pygame.font.SysFont("engraversmt", 50)
game_font2 = pygame.font.SysFont("engraversmt", 25)
fpsClock = pygame.time.Clock()
Display_Surface = pygame.display.set_mode((700, 400))
pygame.display.set_caption('Sorting Pygame')
White = (255, 255, 255)
Black = ( 0, 0, 0)
Blue = (0,0, 255)
Grey = ( 100, 100, 100)
Grey2 = ( 212, 212, 212)
Grey3 = ( 245, 245, 245)
reset = False
gen1 = True
numbers = []
select = False
shell = False
bubble = False
double = False
quick = False
insert = False
click = False
timecheck = False

for x in range(0,100):
                        numbers.append(random.randint(1,250))
def Quick(l,h):
   
    if l<h:
        new = part(l,h)
        
        Quick(l,new-1)
        Quick(new +1,h)
def part(l,r):
    global numbers
    sep = numbers[l]
    
    current = "left"
    while l < r:
        
        if current == "left":
            
            while numbers[r] <= sep and l <r:
                    r = r -1
            numbers[l] = numbers[r]
            current = "right"
        else:
            while numbers[l] >=sep and l<r:
                l = l+1
            numbers[r] = numbers[l]
            current = "left"
    loc = r
    numbers[loc]= sep
    draw()
    
    for z in range(0,100):
                        
        pygame.draw.rect(Display_Surface, Blue, (z*6,400,5,-numbers[z]),0)
    pygame.display.update()
    
    
    return loc
def insertion(al):
                for index in range(1,len(al)):
                       current = al[index]
                       position = index

                       while position>0 and al[position-1]<current:
                    
                            al[position]=al[position-1]
                            position = position-1
                            draw()
                            for z in range(0,100):
                        
                                    pygame.draw.rect(Display_Surface, Blue, (z*6,400,5,-numbers[z]),0)
                            pygame.display.update()
                       al[position]=current
def draw():
        Display_Surface.fill(Grey)
        pygame.draw.rect(Display_Surface, Grey2, (0,5,100,25), 0)
        s1 = game_font2.render(str("Selection"), True,White)
        Display_Surface.blit(s1,(5, 5))
        pygame.draw.rect(Display_Surface, Grey2, (105,5,50,25), 0)
        s1 = game_font2.render(str("Shell"), True,White)
        Display_Surface.blit(s1,(107, 5))
        pygame.draw.rect(Display_Surface, Grey2, (160,5,75,25), 0)
        s1 = game_font2.render(str("Bubble"), True,White)
        Display_Surface.blit(s1,(165, 5))
        pygame.draw.rect(Display_Surface, Grey2, (240,5,150,25), 0)
        s1 = game_font2.render(str("Double Bubble"), True,White)
        Display_Surface.blit(s1,(245, 5))
        pygame.draw.rect(Display_Surface, Grey2, (395,5,100,25), 0)
        s1 = game_font2.render(str("Insertion"), True,White)
        Display_Surface.blit(s1,(400, 5))
        pygame.draw.rect(Display_Surface, Grey2, (500,5,75,25), 0)
        s1 = game_font2.render(str("Quick"), True,White)
        Display_Surface.blit(s1,(508, 5))
        pygame.draw.rect(Display_Surface, Grey2, (580,5,75,25), 0)
        s1 = game_font2.render(str("Reset"), True,White)
        Display_Surface.blit(s1,(585, 5))
        global timecheck
        if timecheck:
                global timer
                s1 = game_font2.render(str("Time: "+str(timer) + " miliseconds"), True,White)
                Display_Surface.blit(s1,(20, 40)) 
while True:
        draw()

        
        if click:
                click = False
                if 0<mx<100 and 0<my<25:
                        select = True
                elif 105<mx<155 and  0<my<25:
                        shell = True
                elif 160<mx<235 and 0<my<25:
                        bubble = True
                elif 240<mx<390 and 0<my<25:
                        double = True
                elif 395<mx<495 and 0<my<25:
                        insert = True
                elif 500<mx<575 and 0<my<25:
                        quick = True
                elif 580<mx<655 and 0<my<25:
                        reset = True
        if reset or gen1:
                timecheck =False
                reset = False
                gen1 = False
                numbers = []
                for x in range(0,100):
                        numbers.append(random.randint(1,250))
        for z in range(0,100):
                
                pygame.draw.rect(Display_Surface, Blue, (z*6,400,5,-numbers[z]),0)
                
        pygame.display.update()
        if select:
                le = len(numbers)
                start = time.time()
                for a in range(0,le-1):
                       for b in range(a+1,le):
                               if numbers[b]>numbers[a]:
                                       te = numbers[a]
                                       numbers[a] = numbers[b]
                                       numbers[b] = te
                                       draw()
                                       
                                       for z in range(0,100):
                        
                                                pygame.draw.rect(Display_Surface, Blue, (z*6,400,5,-numbers[z]),0)
                                       pygame.display.update()
                end = time.time()
                print 1
                timer=str(round(((end-start)*1000),2))
                timecheck =True
                
                select = False
        if bubble:
                print 1
                start = time.time()
                ll = len(numbers)
                swap = True
                p = 1
                while swap:
                    swap = False
                    for j in range(0,ll- p):
                        if numbers[j] < numbers[j+1]:
                            swap = True
                            t = numbers[j]
                            numbers[j] = numbers[j+1]
                            numbers[j+1] = t

                            draw()
                            for z in range(0,100):
                    
                                pygame.draw.rect(Display_Surface, Blue, (z*6,400,5,-numbers[z]),0)
                            pygame.display.update()
                    p+=1

                end = time.time()
                    
                timer=str(round(((end-start)*1000),2))
                timecheck =True
                
                bubble = False

        if double:
            ll = len(numbers)
            swap = True
            pas = 1
            start = time.time()
            while swap:
                swap = False 
                for j in range(0,ll- pas):
                    
                    if numbers[j] < numbers[j+1]:
                       
                        swap = True
                        t = numbers[j]
                        numbers[j] = numbers[j+1]
                        numbers[j+1] = t
                        draw()
                        for z in range(0,100):
                    
                                pygame.draw.rect(Display_Surface, Blue, (z*6,400,5,-numbers[z]),0)
                        pygame.display.update()
                for k in range(ll-pas,1+pas,-1):
                    
                    if numbers[k] > numbers[k-1]:
                       
                        swap = True
                        t = numbers[k]
                        numbers[k] = numbers[k-1]
                        numbers[k-1] = t
                        draw()
                        for z in range(0,100):
                    
                                pygame.draw.rect(Display_Surface, Blue, (z*6,400,5,-numbers[z]),0)
                        pygame.display.update()
            end = time.time()
                    
            timer=str(round(((end-start)*1000),2))
            timecheck =True
                
            double = False
        if shell:
            start = time.time()
            ll = len(numbers)
            g = ll //2
            while g >=1:
                swap = True
                while swap:
                    swap = False
                    for i in range(0,ll-g):
                        if numbers[i] < numbers[i+g]:
                            swap = True
                            te = numbers[i]
                            numbers[i] = numbers[i+g]
                            numbers[i+g] =te
                            draw()
                            for z in range(0,100):
                    
                                pygame.draw.rect(Display_Surface, Blue, (z*6,400,5,-numbers[z]),0)
                            pygame.display.update()
                g = g//2
            end = time.time()
                    
            timer=str(round(((end-start)*1000),2))
            timecheck =True
                
            shell = False
        if insert:
            start = time.time()
            
                
            al = numbers
            insertion(al)
            end = time.time()
                    
            timer=str(round(((end-start)*1000),2))
            timecheck =True
            insert = False
        if quick:
            start = time.time()
            
            Quick(0,len(numbers)-1)
            end = time.time()
            timer=str(round(((end-start)*1000),2))
            timecheck =True
            quick = False
        for event in pygame.event.get():
            if event.type == MOUSEBUTTONDOWN:
                mx,my = pygame.mouse.get_pos()
                if event.button == 1:
                    click = True
                
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
                
        pygame.display.update()

        fpsClock.tick(FPS)
