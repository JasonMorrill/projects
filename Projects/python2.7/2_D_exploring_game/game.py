import pygame, sys, random
from pygame.locals import *
pygame.init()
FPS = 10
game_font = pygame.font.SysFont("default", 50)
game_font2 = pygame.font.SysFont("default", 25)
game_font3 = pygame.font.SysFont("Stencil", 100)
fpsClock = pygame.time.Clock()
Display_Surface = pygame.display.set_mode((1000, 800))
pygame.display.set_caption('Survival Game')
health = 10
Time = "Day"
def Draw(xcord,ycord,image):
    Display_Surface.blit(image, (xcord, ycord))

def move(xvalue,yvalue,direction,grid):
    if direction == 'right' and xvalue <980:
                   
                    if grid[xvalue/20+1][yvalue/20 ] != "S" and grid[xvalue/20+1][yvalue/20 -1] == "S" and grid[xvalue/20+1][yvalue/20 -2 ] == "S" and grid[xvalue/20+1][yvalue/20 -3 ] == "S" and xvalue <1000:
                            xvalue = xvalue + 20
                            yvalue = yvalue - 20
                    elif grid[xvalue/20+1][yvalue/20 ] == "S" and grid[xvalue/20+1][yvalue/20 -1] == "S" and grid[xvalue/20+1][yvalue/20 -2 ] == "S"  and xvalue <1000:
                           xvalue = xvalue + 20
                    
                       
    elif direction == 'left':
                   
                    if grid[xvalue/20-1][playery/20 ] == "S" and grid[xvalue/20-1][yvalue/20 -1] == "S" and grid[xvalue/20-1][yvalue/20 -2 ] == "S" and xvalue >0:
                       xvalue = xvalue- 20

                    elif grid[xvalue/20-1][yvalue/20 ]!= "S" and grid[xvalue/20-1][yvalue/20 -1] == "S" and grid[xvalue/20-1][yvalue/20 -2 ] == "S" and grid[xvalue/20-1][yvalue/20 -3 ] == "S" and xvalue >0:

                        xvalue = xvalue - 20
                        yvalue =yvalue - 20
    return xvalue,yvalue



White = (255, 255, 255)
Red = (255,0,0)
Black = ( 0, 0, 0)
Dark = ( 25,25, 25)
Yellow = (255,255,0)
Leaves = pygame.image.load('Leaves.png')

Grass = pygame.image.load('Grass.png')

Blue = (153,255,255)
Blue2 = (0,0,255)
DarkBlue = (0,0,153)
Grey = (153,153,153)
Dirt = pygame.image.load('Dirt.png')
Heart = pygame.image.load('Heart.png')
Wood = pygame.image.load('Wood.png')
Bar = pygame.image.load('Bar.png')
Stone = pygame.image.load('Stone.png')
Bedrock = pygame.image.load('Bedrock.png')
Gold = pygame.image.load('Gold.png')
Iron = pygame.image.load('Iron.png')
Coal = pygame.image.load('Coal.png')
Moon = pygame.image.load('Moon.png')
Sun = pygame.image.load('Sun.png')
Body = pygame.image.load('Body.png')
Legs = pygame.image.load('Legs.png')
Face_Left = pygame.image.load('Face_Left.png')
Face_Right = pygame.image.load('Face_Right.png')
znum = 0
zx = []
zy = []
menu =True


menustart = True

while True:
    if menu:
        
            if menustart ==True:
                menustart = False
                click = False
                click2 = False
                mov = False
                count = 0
                count2 = 0
                ystart = 13
                Bar_pos = 1
                Inv_bar = [["E" for rows in range(1)]for lines in range(9)]
                dire = 'right'
                grid = [["S" for rows in range(40)]for lines in range(50)]
                playerx = 0
                playery = 240
                inv_pos =0
                pause = False
                

                control = False
                control_start = True
                gen =False
                save = False
                for x in range(0,50):
                    for y in range(0,40):
                        x1 = x *20
                        y1 = y * 20
                        Draw(x1,y1,Dirt)
                pygame.draw.rect(Display_Surface, Grey, (265,300,200,50), 0)
                pygame.draw.rect(Display_Surface, Grey, (550,300,200,50), 0)
                pygame.draw.rect(Display_Surface, Grey, (415,400,200,50), 0)
                new = game_font.render(str("New Game"), True, White)
                Display_Surface.blit(new,(275, 310))
                load = game_font.render(str("Load Game"), True, White)
                Display_Surface.blit(load,(560, 310))
                cont = game_font.render(str("Controls"), True, White)
                Display_Surface.blit(cont,(440, 410))
                Title = game_font3.render(str("Welcome"), True, White)
                Display_Surface.blit(Title,(225,150))
                health = 10
            if click:
                click = False
                if 265< mx < 465 and 300<my < 350:
                    gen = True
                    
                    menu = False
                    
                elif 550 < mx < 750 and 300 < my < 350:
                    
                    save = True
                    menu = False
                    
                elif 415 < mx < 615 and 400 < my < 450:
                    menu = False
                    control = True
                    control_start = True
                    
    if control:
        if control_start:
            control_start = False
            for x in range(0,50):
                        for y in range(0,40):
                            x1 = x *20
                            y1 = y * 20
                            Draw(x1,y1,Dirt)
            pygame.draw.rect(Display_Surface,Grey , (400,700,200,50), 0)
            back = game_font.render(str("Main Menu"), True, White)
            Display_Surface.blit(back,(410, 710))
            text = game_font.render(str("Left Mouse Button = Destroy Block"), True, White)
            Display_Surface.blit(text,(225, 50))
            text = game_font.render(str("Right Mouse Button = Place Block"), True, White)
            Display_Surface.blit(text,(225, 100))
            text = game_font.render(str("Esc = Pause / Unpause"), True, White)
            Display_Surface.blit(text,(355, 150))
            text = game_font.render(str("D = Move Right"), True, White)
            Display_Surface.blit(text,(375, 200))
            text = game_font.render(str("A = Move Left"), True, White)
            Display_Surface.blit(text,(375, 250))
            text = game_font.render(str("1 - 9 = Switch Blocks"), True, White)
            Display_Surface.blit(text,(325, 300))
        if click:
            click = False
            if 400 < mx < 600 and 700 < my < 750:
                    
                menustart = True
                menu =True
        
        pass
    if gen:
        
        gen = False
        for x in range(0,50):
        
        
                for y in range(ystart,40):
                            
                            if y ==ystart:
                                grid[x][y] = "G"
                                td =  random.randint(1,25)
                                if td == 1:
                                    try:
                                        grid[x][y-1] = "W"
                                        grid[x][y-2] = "W"
                                        grid[x][y-3] = "W"
                                        grid[x][y-4] = "L"
                                        grid[x-1][y-4] = "L"
                                        grid[x][y-5] = "L"
                                        grid[x+2][y-4] = "L"
                                        grid[x+1][y-5] = "L"
                                        grid[x][y-6] = "L"
                                        grid[x+1][y-4] = "L"
                                        grid[x-1][y-5] = "L"
                                        grid[x-2][y-4] = "L"
                                        
                                        
                                        
                                        
                                    except:
                                        pass
                            else:
                                grid[x][y] = "D"
                for y2 in range(ystart + 10,40):
                    
                   
                    grid[x][y2] = "R"
                    os =  random.randint(1,100)
                    
                    if os == 1:
                            try:
                                    grid[x][y2] = "A"
                                    grid[x-1][y2] = "A"
                                    grid[x-2][y2] = "A"
                                    grid[x-1][y2-1] = "A"
                                    grid[x-1][y2+1] = "A"
                                    
                                    
                            except:
                                pass
                    elif os == 2:
                            try:
                                    grid[x][y2] = "I"
                                    grid[x-1][y2] = "I"
                                    grid[x-2][y2] = "I"
                                    grid[x-1][y2-1] = "I"
                                    grid[x-1][y2+1] = "I"

                            except:
                                pass
                                    
                    elif os == 3:
                            try:
                                    grid[x][y2] = "C"
                                    grid[x-1][y2] = "C"
                                    grid[x-2][y2] = "C"
                                    grid[x-1][y2-1] = "C"
                                    grid[x-1][y2+1] = "C"
                                    
                                    
                            except:
                                pass
                
                z = random.randint(1,3)
                if z == 1:
                    ystart = ystart + 1
                elif z == 2:
                    ystart = ystart
                else:
                    ystart = ystart - 1
        for x in range(0,50):
            grid[x][39] = "B"
    elif save:
        
        save = False
        inFile = open("save.txt","r")
        
        for x in range(0,50):
            for y in range(0,40):
                val = inFile.readline().rstrip("\n")
                grid[x][y] = val
        for x in range(0,9):
            val = inFile.readline().rstrip("\n")
            Inv_bar[x][0] = val


            
    elif menu == False and pause == False and control == False:
        
            
        count +=1
        if count <=1020:
            Display_Surface.fill(Blue)
            Draw(count,40,Sun)
            Time = "Day"
        else:
            Display_Surface.fill(Black)
            Draw(count2,40,Moon)
            Time = "Night"
            if znum <=5:
                zsp = random.randint(0,100)
                if zsp == 0:
                    znum = znum + 1
                    zx2 = random.randint(0,50)
                    for abc in range(0,40):
                        if grid[zx][abc] == "G":
                            zx.append(zx)
                
        if count>1020:
            count2 +=2
        if count2>1020:
            count = 0
            count2 = 0
        
        for x in range(0,50):
            for y in range(0,40):
                x1 = x *20
                y1 = y * 20
                
                if grid[x][y] == "D":
                    
                    Draw(x1,y1,Dirt)
                    
                elif grid[x][y] == "R":
                    
                    Draw(x1,y1,Stone)
                elif grid[x][y] == "A":
                    Draw(x1,y1,Gold)
                elif grid[x][y] == "I":
                   Draw(x1,y1,Iron)
                elif grid[x][y] == "B":
                    
                    Draw(x1,y1,Bedrock)   
                
                elif grid[x][y] == "W":
                    
                    Draw(x1,y1,Wood)
                elif grid[x][y] == "G":
                    
                    Draw(x1,y1,Grass)
                elif grid[x][y] == "L":
                    Draw(x1,y1,Leaves)
                elif grid[x][y] == "C":
                   Draw(x1,y1,Coal)
                
        
        mx,my = pygame.mouse.get_pos()
        if mx < playerx -60:
                mx = playerx - 60
        elif mx > playerx +80:
                mx = playerx + 80
        if my < playery- 60:
                my = playery - 60
        elif my > playery + 60:
                my = playery + 60
        pygame.draw.rect(Display_Surface,Dark , (mx - 1,my -5,2,10), 0)
        pygame.draw.rect(Display_Surface, Dark, (mx - 5,my -1,10,2), 0)
        
        if click:
            click = False
            if grid[mx//20][my//20]  != "S" and grid[mx//20][my//20]  != "B":
                for x in range(0,9):
                    
                    if str(Inv_bar[x][0])[0] == grid[mx//20][my//20]:
                                num = int(str(Inv_bar[x][0])[1:])
                                num = num + 1
                                Inv_bar[x][0] = grid[mx//20][my//20]+ str(num)
                                break
                    elif Inv_bar[x][0] == "E":
                        Inv_bar[x][0] = str(grid[mx//20][my//20]) + "1"
                        
                        break
                grid[mx//20][my//20] = "S"
        if click2:
            click2 = False
            if grid[mx//20][my//20] == "S":
                    if str(Inv_bar[inv_pos][0][0]) != "E":
                        num = int(Inv_bar[inv_pos][0][1:])
                        num = num -1
                        grid[mx//20][my//20] = str(Inv_bar[inv_pos][0][0])
                        if num <= 0:
                            Inv_bar[inv_pos][0] = "E"
                        else:
                            Inv_bar[inv_pos][0] = Inv_bar[inv_pos][0][0] + str(num)
                            
                        
        if grid[playerx/20][playery/20 +1 ] == "S":
                            playery = playery + 20
 
        if mov:
            playerx,playery = move(playerx,playery,dire,grid)
                
                
        if dire == 'right':
            playery2 = playery -40
            Draw(playerx,playery2, Face_Right)
           
        else:
            playery2 = playery -40
            Draw(playerx,playery2, Face_Left)
        playery2 = playery -20
        Draw(playerx,playery2, Body)
        Draw(playerx,playery, Legs)

        Draw(350,0,Bar)
        for x in range(0,9):
            if Inv_bar[x][0] != "E":
                num = int(str(Inv_bar[x][0])[1:])
                item = str(Inv_bar[x][0])[0]
                x2 = 358 + 33 * x
                
                x3 = 352 + 33* inv_pos
                if item == "D":
                        
                        Draw(x2,5,Dirt)
                        
                elif item  == "R":
                        
                        Draw(x2,5,Stone)
                elif item  == "A":
                        Draw(x2,5,Gold)
                elif item == "I":
                       Draw(x2,5,Iron)
                    
                    
                elif item  == "W":
                        
                        Draw(x2,5,Wood)
                elif item  == "G":
                        
                        Draw(x2,5,Grass)
                elif item == "L":
                        Draw(x2,5,Leaves)
                elif item  == "C":
                       Draw(x2,5,Coal)
                nums = game_font2.render(str(num), True, White)
                Display_Surface.blit(nums,(x2, 10))
                pygame.draw.rect(Display_Surface,Yellow , (x3,1 ,30,28), 1)
        for x in range(0,health):
            x2 = x * 10 + 50
            Draw(x2,5,Heart)
    elif pause:
          
          pygame.draw.rect(Display_Surface,Grey , (400,200,200,50), 0)
          back = game_font.render(str("Main Menu"), True, White)
          Display_Surface.blit(back,(410, 210))
          pygame.draw.rect(Display_Surface,Grey , (400,400,200,50), 0)
          save_game = game_font.render(str("Save Game"), True, White)
          Display_Surface.blit(save_game,(405, 410))
          if click:
            if 400 < mx < 600 and 200 < my < 250:
                
                menustart = True
                menu =True
            elif 400 < mx < 600 and 400 < my < 450:
                outFile = open("save.txt","w")
                for x in range(0,50):
                    for y in range(0,40):
                       outFile.write(grid[x][y] + "\n")

                for x in range(0,9):
                    outFile.write(Inv_bar[x][0] + "\n")
                    
                outFile.close()


              
    for event in pygame.event.get():
            if event.type == KEYDOWN:
                
                    if event.key == K_1:
                        inv_pos = 0
                    elif event.key == K_2:
                        inv_pos =1
                    elif event.key == K_3:
                        inv_pos = 2
                    elif event.key == K_4:
                        inv_pos = 3
                    elif event.key == K_5:
                        inv_pos = 4
                    elif event.key == K_6:
                        inv_pos =5
                    elif event.key == K_7:
                        inv_pos = 6
                    elif event.key == K_8:
                        inv_pos = 7
                    elif event.key == K_9:
                        inv_pos = 8
                    if event.key == K_d:
                        mov = True
                        dire = 'right'
                    elif event.key == K_a:
                        dire = 'left'
                        mov = True
                    if event.key == K_ESCAPE:
                        if menu == False:
                            if pause == False:
                                pause = True
                            else:
                                pause = False
                    
            if event.type == KEYUP:
                    if event.key == K_d:
                        mov = False
                    
                    elif event.key == K_a:
                    
                        mov = False
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click  = True
                if event.button == 3:
                    click2  = True
                mx,my = pygame.mouse.get_pos()

            if event.type == QUIT:
                pygame.quit()
                sys.exit()
    pygame.display.update()

    fpsClock.tick(FPS)

