# This program simulates Minesweeper using pygame.
import pygame, sys, random
from pygame.locals import *
pygame.init()
FPS = 100

def Clear(x,y):
    global grid
    global grid2
    global grid3
    grid2[x][y] = True
    grid3[x][y] = False
                   
    if grid[x][y] == 0:
      
        if grid2[x-1][y] == False:
         
            Clear(x-1,y)
            
        if grid2[x+1][y] == False:
            
            Clear(x+1,y)
        if grid2[x][y-1] == False:
           
            Clear(x,y-1)
        if grid2[x][y+1] == False:
            
            Clear(x,y+1)
        if grid2[x-1][y-1] == False:
          
            Clear(x-1,y-1)
        if grid2[x-1][y+1] == False:
        
            Clear(x-1,y+1)
        if grid2[x+1][y-1] == False:
          
            Clear(x+1,y-1)
        if grid2[x+1][y+1] == False:
          
            Clear(x+1,y+1)

game_font = pygame.font.SysFont("engraversmt", 50)
game_font2 = pygame.font.SysFont("engraversmt", 35)
fpsClock = pygame.time.Clock()
Display_Surface = pygame.display.set_mode((400, 400))
pygame.display.set_caption('Minesweeper')
White = (255, 255, 255)
Black = ( 0, 0, 0)
Blue = (0,0, 255)
Grey = ( 100, 100, 100)
Grey2 = ( 212, 212, 212)
Grey3 = ( 245, 245, 245)
win = False
game = False
click = False
click2 = False
first = True
lose = False
while True:
    if not game and lose == False and win == False:
         Display_Surface.fill(Grey)
         pygame.draw.rect(Display_Surface, Grey2, (75,140,235,50), 0)
         start = game_font.render(str("Click to Start"), True, White)
         Display_Surface.blit(start,(85, 150))
         if click:
             click = False
             if 75< mx < 310 and 140 <my <190:
                grid = [["-" for x in range(18)]for y in range(18)]
                grid2 = [[False for x in range(18)]for y in range(18)]
                grid3 = [[False for x in range(18)]for y in range(18)]
                
                game = True
                brem = 40
                
    if click and first:
        first = False
        x2 = mx - 20
        x2 = x2 // 20
        y2 = my - 30
        y2 = y2 // 20
        
        for x in range(0,40):
            while True:
                a = random.randint(1,16)
                b = random.randint(1,16)
                if a != x2 and b!= y2:
                    if grid[a][b] != "b":
                        grid[a][b] = "b"
                        break
        
        for x in range(1,17):
                for y in range(1,17):
                    if grid[x][y] != "b":
                        count = 0
                        if grid[x-1][y] == "b":
                            count +=1

                        if grid[x-1][y-1] == "b":
                            count +=1

                        if grid[x-1][y+1] == "b":
                            count +=1

                        if grid[x][y-1] == "b":
                            count +=1

                        if grid[x][y+1] == "b":
                            count +=1
                        if grid[x+1][y] == "b":
                            count +=1

                        if grid[x+1][y-1] == "b":
                            count +=1

                        if grid[x+1][y+1] == "b":
                            count +=1
                        grid[x][y] = count
                        
            
    if game:
        
        Display_Surface.fill(Grey)
        
        for x in range(1,17):
                for y in range(1,17):
                    x1 = x *20 + 20
                    y1 = y * 20 + 30
                    if grid3[x][y] == True:
                        start = game_font2.render(str("!"), True, Black)
                        Display_Surface.blit(start,(x1+5, y1))
                    else:
                        if grid2[x][y] == True:
                            
                            if grid[x][y] == "b":
                                pygame.draw.rect(Display_Surface, Grey, (x1,y1,20,20), 0)
                            elif grid[x][y] != 0:
                                pygame.draw.rect(Display_Surface, Grey3, (x1,y1,20,20), 0)
                                start = game_font2.render(str(grid[x][y]), True, Black)
                                Display_Surface.blit(start,(x1+2.5, y1))
                            else:
                                pygame.draw.rect(Display_Surface, Grey3, (x1,y1,20,20), 0)
                        else:
                            
                            pygame.draw.rect(Display_Surface, Grey2, (x1,y1,20,20), 0)
                            pygame.draw.rect(Display_Surface, Black, (x1,y1,20,20), 1)
        start = game_font2.render(str(brem), True, White)
        Display_Surface.blit(start,(0, 10))
        if click and lose == False and win == False:
            
            if 20< mx < 360 and 30< my <370:
                x2 = mx - 20
                x2 = x2 // 20
                y2 = my - 30
                y2 = y2 // 20
                
                Clear(x2,y2)
                if grid[x2][y2]== "b":
                    
                    lose = True
            click = False
        if click2 and lose == False:
            
            if 20< mx < 360 and 30< my <370:
                x2 = mx - 20
                x2 = x2 // 20
                y2 = my - 30
                y2 = y2 // 20
                
                if grid3[x2][y2] == False and brem >0 and grid2[x2][y2] == False:
                    grid3[x2][y2] = True
                    brem -=1
                elif grid3[x2][y2] == True:
                    grid3[x2][y2] = False
                    brem +=1
            click2 = False
        if lose:
            start = game_font.render(str("You Lose"), True,White)
            Display_Surface.blit(start,(120, 10))
            if click:
                game = False
        
        if brem == 0:
             w = True
             for x in range(1,17):
                for y in range(1,17):
                    if grid[x][y] == "b":
                        if grid3[x][y] != True:
                            w = False
             if w:
                
                win = True
                
        if win:
            start = game_font.render(str("You Win!"), True,White)
            Display_Surface.blit(start,(120, 10))
            if click:
                print "a"
                game = False
    if win and game == False:
            Display_Surface.fill(Grey)
            
            pygame.draw.rect(Display_Surface, Grey2, (75,140,235,50), 0)
            start = game_font.render(str("Click to Start"), True, White)
            Display_Surface.blit(start,(85, 150))

            
            
            if click:
                
                click = False
                if 75< mx < 310 and 140 <my <190:
                    grid = [["-" for x in range(18)]for y in range(18)]
                    grid2 = [[False for x in range(18)]for y in range(18)]
                    grid3 = [[False for x in range(18)]for y in range(18)]
                    game = True
                    click = False
                    click2 = False
                    first = True
                    lose = False
                    win = False
                    game = True
                    brem = 40
    if lose and game == False:
            Display_Surface.fill(Grey)
            
            pygame.draw.rect(Display_Surface, Grey2, (75,140,235,50), 0)
            start = game_font.render(str("Click to Start"), True, White)
            Display_Surface.blit(start,(85, 150))

            
            
            if click:
                
                click = False
                if 75< mx < 310 and 140 <my <190:
                    grid = [["-" for x in range(18)]for y in range(18)]
                    grid2 = [[False for x in range(18)]for y in range(18)]
                    grid3 = [[False for x in range(18)]for y in range(18)]
                    game = True
                    click = False
                    click2 = False
                    first = True
                    lose = False
                    win = False
                    game = True
                    brem = 40

    for event in pygame.event.get():
            if event.type == MOUSEBUTTONDOWN:
                mx,my = pygame.mouse.get_pos()
                if event.button == 1:
                    click = True
                if event.button == 3:
                    click2 = True
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

    pygame.display.update()

    fpsClock.tick(FPS)
