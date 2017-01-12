# This program simulates John Conway’s Game of Life using pygame.
#click to add / remove cells
import pygame, sys, random
from pygame.locals import *
pygame.init()
FPS = 100



game_font = pygame.font.SysFont("engraversmt", 50)
fpsClock = pygame.time.Clock()
Display_Surface = pygame.display.set_mode((600, 600))
pygame.display.set_caption('Game of Life')
White = (255, 255, 255)
Black = ( 0, 0, 0)
Blue = (0,0, 255)
Grey = ( 100, 100, 100)
start = True
gen1 = True
click = False
text1 = ""
turn = False
gen = 1
while True:
    Display_Surface.fill(Black)
    if start == True:
        if click == True:
            click = False
            if 5 < mx <55 and  400 < my < 440:
                text1 = text1 + "1"
            elif 65 < mx <115 and  400 < my < 440:
                text1 =  text1+ "2"
            elif 125 < mx <165 and  400 < my < 440:
                text1 = text1 + "3"
            elif 185 < mx <225 and  400 < my < 440:
                text1 = text1 + "4"
            elif 245 < mx <285 and  400 < my < 440:
                text1 = text1 + "5"
            elif 305 < mx <345 and  400 < my < 440:
                text1 = text1 + "6"
            elif 365 < mx <405 and  400 < my < 440:
                text1 = text1 + "7"
            elif 425 < mx <465 and  400 < my < 440:
                text1 = text1 + "8"
            elif 485 < mx <525 and  400 < my < 440:
                text1 = text1 + "9"
            elif 545 < mx <585 and  400 < my < 440:
                text1 = text1 + "0"
            elif 80 < mx <230 and  450 < my < 490:
                text1 = ""
            elif 320 < mx <470 and  450 < my < 490:
                start = False
                if text1 == "":
                    text1 = "0"
                
                cells = int(text1)
                if cells >400:
                    cells = 400
                
                
        text2 = "Number of live cells: "+ text1
        text = game_font.render(str(text2), True, White)
        Display_Surface.blit(text,(50, 200))
        pygame.draw.rect(Display_Surface, Grey, (5,400,50,40), 0)
        pygame.draw.rect(Display_Surface, Grey, (65,400,50,40), 0)
        pygame.draw.rect(Display_Surface, Grey, (125,400,50,40), 0)
        pygame.draw.rect(Display_Surface, Grey, (185,400,50,40), 0)
        pygame.draw.rect(Display_Surface, Grey, (245,400,50,40), 0)
        pygame.draw.rect(Display_Surface, Grey, (305,400,50,40), 0)
        pygame.draw.rect(Display_Surface, Grey, (365,400,50,40), 0)
        pygame.draw.rect(Display_Surface, Grey, (425,400,50,40), 0)
        pygame.draw.rect(Display_Surface, Grey, (485,400,50,40), 0)
        pygame.draw.rect(Display_Surface, Grey, (545,400,50,40), 0)
        pygame.draw.rect(Display_Surface, Grey, (80,450,150,40), 0)
        pygame.draw.rect(Display_Surface, Grey, (320,450,150,40), 0)
        dele = game_font.render(str("Delete"), True, White)
        Display_Surface.blit(dele,(100, 455))
        ent = game_font.render(str("Enter"), True, White)
        Display_Surface.blit(ent,(340, 455))
        n1 = game_font.render(str("1"), True, White)
        Display_Surface.blit(n1,(20, 405))
        n2 = game_font.render(str("2"), True, White)
        Display_Surface.blit(n2,(80, 405))
        n3 = game_font.render(str("3"), True, White)
        Display_Surface.blit(n3,(140, 405))
        n4 = game_font.render(str("4"), True, White)
        Display_Surface.blit(n4,(200, 405))
        n5 = game_font.render(str("5"), True, White)
        Display_Surface.blit(n5,(260, 405))
        n6 = game_font.render(str("6"), True, White)
        Display_Surface.blit(n6,(320, 405))
        n7 = game_font.render(str("7"), True, White)
        Display_Surface.blit(n7,(380, 405))
        n8 = game_font.render(str("8"), True, White)
        Display_Surface.blit(n8,(440, 405))
        n9 = game_font.render(str("9"), True, White)
        Display_Surface.blit(n9,(500, 405))
        n0 = game_font.render(str("0"), True, White)
        Display_Surface.blit(n0,(560, 405))
        
    elif gen1 == True:
        gen1 = False
        grid = [["-" for x in range(22)]for y in range(22)]
        
        for z in range(0,cells):
            x1 = random.randint(1,20)
            y1 = random.randint(1,20)
            check = False
            while check == False:
                
                
                if grid[x1][y1] == "X":
                    x1 = random.randint(1,20)
                    y1 = random.randint(1,20)
                else:
                    grid[x1][y1] = "X"
                    check = True
        
    elif turn == True:
        gen = gen + 1
        turn = False
        cells = 0
        grid2 = [["-" for x in range(22)]for y in range(22)]
        for x in range(1,21):
            for y in range(1,21):
                if grid[x][y] == "X":
                    numadj = 0
                    for x2 in range(-1,2):
                        for y2 in range(-1,2):
                            if x2 == 0 and y2 == 0:
                                numadj = numadj
                            else:
                                tile = grid[x+ x2][y + y2]
                                if tile == "X":
                                    numadj = numadj+1
                    if numadj == 2 or numadj == 3:
                        grid2[x][y] = "X"
                        cells = cells +1
                else:
                    numadj = 0
                    for x2 in range(-1,2):
                        for y2 in range(-1,2):
                            if x2 == 0 and y2 == 0:
                                numadj = numadj
                            else:
                                tile = grid[x+ x2][y + y2]
                                if tile == "X":
                                    numadj = numadj+1
                    if  numadj == 3:
                        grid2[x][y] = "X"
                        cells = cells +1
        grid = grid2
        
    else:
        pygame.draw.rect(Display_Surface, Grey, (150,480,280,40), 0)
        ent = game_font.render(str("Next Generation"), True, White)
        Display_Surface.blit(ent,(155, 485))
        text2 = "Number of live cells: " + str(cells)
        text22 = game_font.render(str(text2), True, White)
        Display_Surface.blit(text22,(130, 10))
        text3 = "Generation: " + str(gen)
        text33 = game_font.render(str(text3), True, White)
        Display_Surface.blit(text33,(180, 550))
        for x in range(1,21):
            for y in range(1,21):
                x1 = x *20 + 80
                y1 = y * 20 + 50
                if grid[x][y] == "X":
                    
                    pygame.draw.rect(Display_Surface, Blue, (x1,y1,20,20), 0)
                else:
                    
                    pygame.draw.rect(Display_Surface, White, (x1,y1,20,20), 0)
        if click == True:
            
            click = False
            if 80< mx < 500 and 50< my <470:
                x2 = mx - 80
                x2 = x2 // 20
                y2 = my - 50
                y2 = y2 // 20
                
                
                if grid[x2][y2] == "X":
                    grid[x2][y2] = "-"
                elif grid[x2][y2] == "-":
                    grid[x2][y2] = "X"
            if 150 < mx <430 and  480 < my < 520:
                turn = True
    for event in pygame.event.get():
            if event.type == MOUSEBUTTONDOWN:
                mx,my = pygame.mouse.get_pos()
                
                click = True
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

    pygame.display.update()

    fpsClock.tick(FPS)
