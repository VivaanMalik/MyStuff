import random
from turtle import width
import pygame
pygame.init()


run = True
screenratio = 8/5 # 16/9
W_height = pygame.display.Info().current_h
W_width = round(W_height*screenratio)
tilesize = round(W_height/10)
screen = pygame.display.set_mode((W_width, W_height), pygame.FULLSCREEN|pygame.SCALED)
pygame.display.set_caption("This is a window =)")
clock = pygame.time.Clock()
rotconst = 90

Water = pygame.image.load(".\\imgs\\Water.png")
Water = pygame.transform.scale(Water, (tilesize, tilesize))
Grass = pygame.image.load(".\\imgs\\Grass.png")
Grass = pygame.transform.scale(Grass, (tilesize, tilesize))
PeninsulaGrassW = pygame.image.load(".\\imgs\\GrassWater1Side.png")
PeninsulaGrassW = pygame.transform.scale(PeninsulaGrassW, (tilesize, tilesize))
PeninsulaGrassA = pygame.transform.rotate(PeninsulaGrassW, rotconst)
PeninsulaGrassS = pygame.transform.rotate(PeninsulaGrassA, rotconst)
PeninsulaGrassD = pygame.transform.rotate(PeninsulaGrassS, rotconst)
grassWithCornerWaterAS = pygame.image.load(".\\imgs\\GrassWaterCorner.png")
grassWithCornerWaterAS = pygame.transform.scale(grassWithCornerWaterAS, (tilesize, tilesize))
grassWithCornerWaterSD = pygame.transform.rotate(grassWithCornerWaterAS, rotconst)
grassWithCornerWaterDW = pygame.transform.rotate(grassWithCornerWaterSD, rotconst)
grassWithCornerWaterWA = pygame.transform.rotate(grassWithCornerWaterDW, rotconst)
CornerGrassAS = pygame.image.load(".\\imgs\\GrassWaterCornerInverse.png")
CornerGrassAS = pygame.transform.scale(CornerGrassAS, (tilesize, tilesize))
CornerGrassSD = pygame.transform.rotate(CornerGrassAS, rotconst)
CornerGrassDW = pygame.transform.rotate(CornerGrassSD, rotconst)
CornerGrassWA = pygame.transform.rotate(CornerGrassDW, rotconst)
GrassSideS = pygame.image.load(".\\imgs\\GrassWaterSide.png")
GrassSideS = pygame.transform.scale(GrassSideS, (tilesize, tilesize))
GrassSideD = pygame.transform.rotate(GrassSideS, rotconst)
GrassSideW = pygame.transform.rotate(GrassSideD, rotconst)
GrassSideA = pygame.transform.rotate(GrassSideW, rotconst)

## 2
Water2 = pygame.image.load(".\\newimgs\\Water.png")
Water2 = pygame.transform.scale(Water2, (tilesize, tilesize))
Grass2 = pygame.image.load(".\\newimgs\\Grass.png")
Grass2 = pygame.transform.scale(Grass2, (tilesize, tilesize))
WaterCornerSD2 = pygame.image.load(".\\newimgs\\WaterCorner.png")
WaterCornerSD2 = pygame.transform.scale(WaterCornerSD2, (tilesize, tilesize))
WaterCornerDW2 = pygame.transform.rotate(WaterCornerSD2, rotconst)
WaterCornerWA2 = pygame.transform.rotate(WaterCornerDW2, rotconst)
WaterCornerAS2 = pygame.transform.rotate(WaterCornerWA2, rotconst)
WaterSideS2 = pygame.image.load(".\\newimgs\\WaterSide.png")
WaterSideS2 = pygame.transform.scale(WaterSideS2, (tilesize, tilesize))
WaterSideD2 = pygame.transform.rotate(WaterSideS2, rotconst)
WaterSideW2 = pygame.transform.rotate(WaterSideD2, rotconst)
WaterSideA2 = pygame.transform.rotate(WaterSideW2, rotconst)

WaterBottom = [None, Water2, WaterSideW2]
GrassBottom = [None, Grass2, WaterCornerSD2, WaterCornerAS2, WaterSideS2]
GWWBottom = [None, WaterCornerWA2, WaterSideA2]
WWGBottom = [None, WaterCornerDW2, WaterSideD2]
WaterTop = [None, Water2, WaterSideS2]
GrassTop = [None, Grass2, WaterCornerDW2, WaterCornerWA2, WaterSideW2]
GWWTop = [None, WaterCornerSD2, WaterSideD2]
WWGTop = [None, WaterCornerAS2, WaterSideA2]
WaterLeft = [None, Water2, WaterSideD2]
GrassLeft = [None, Grass2, WaterCornerWA2, WaterCornerAS2, WaterSideA2]
GWWLeft = [None, WaterCornerDW2, WaterSideW2]
WWGLeft = [None, WaterCornerSD2, WaterSideS2]
WaterRight = [None, Water2, WaterSideA2]
GrassRight = [None, Grass2, WaterCornerSD2, WaterCornerDW2, WaterSideD2]
GWWRight = [None, WaterCornerAS2, WaterSideS2]
WWGRight = [None, WaterCornerWA2, WaterSideW2]


def ReGraphics1():
    global screen
    screen.fill((0, 0, 0))
    screen.blit(Water, (0, 0))
    screen.blit(Grass, (tilesize, 0))
    screen.blit(PeninsulaGrassW, (tilesize*2, 0))
    screen.blit(PeninsulaGrassA, (tilesize*3, 0))
    screen.blit(PeninsulaGrassS, (tilesize*4, 0))
    screen.blit(PeninsulaGrassD, (tilesize*5, 0))
    screen.blit(grassWithCornerWaterAS, (tilesize*6, 0))
    screen.blit(grassWithCornerWaterSD, (tilesize*7, 0))
    screen.blit(grassWithCornerWaterDW, (tilesize*8, 0))
    screen.blit(grassWithCornerWaterWA, (tilesize*9, 0))
    screen.blit(CornerGrassAS, (tilesize*10, 0))
    screen.blit(CornerGrassSD, (tilesize*11, 0))
    screen.blit(CornerGrassDW, (tilesize*12, 0))
    screen.blit(CornerGrassWA, (tilesize*13, 0))
    screen.blit(GrassSideS, (tilesize*14, 0))
    screen.blit(GrassSideD, (0, tilesize*15))
    screen.blit(GrassSideW, (0, tilesize))
    screen.blit(GrassSideA, (tilesize, tilesize))
    pygame.display.update()

def ReGraphics2():
    global screen
    screen.blit(Water2, (0, 0))
    screen.blit(Grass2, (tilesize, 0))
    screen.blit(WaterCornerSD2, (tilesize*2, 0))
    screen.blit(WaterCornerDW2, (tilesize*3, 0))
    screen.blit(WaterCornerWA2, (tilesize*4, 0))
    screen.blit(WaterCornerAS2, (tilesize*5, 0))
    screen.blit(WaterSideS2, (tilesize*6, 0))
    screen.blit(WaterSideD2, (tilesize*7, 0))
    screen.blit(WaterSideW2, (tilesize*8, 0))
    screen.blit(WaterSideA2, (tilesize*9, 0))
    pygame.display.update()


def findintersections(a, b:list):
    retrunlist = []
    for i in a:
        if i in b:
            retrunlist.append(i)
    return retrunlist

def GetTile(topimg = None, bottomimg = None, leftimg = None, rightimg = None):
    possible = [Water2, Grass2, WaterCornerAS2, WaterCornerDW2, WaterCornerSD2, WaterCornerWA2, WaterSideA2, WaterSideD2, WaterSideS2, WaterSideW2]
    if topimg!=None:
        possible=[]
        if topimg in WaterBottom:
            possible.extend(WaterTop)
        elif topimg in GrassBottom:
            possible.extend(GrassTop)
        elif topimg in GWWBottom:
            possible.extend(WWGTop)
        elif topimg in WWGBottom:
            possible.extend(GWWTop)

    if bottomimg!=None:
        if bottomimg in WaterTop:
            possible = findintersections(possible, WaterBottom)
        elif bottomimg in GrassTop:
            possible = findintersections(possible, GrassBottom)
        elif bottomimg in GWWTop:
            possible = findintersections(possible, WWGBottom)
        elif bottomimg in WWGTop:
            possible = findintersections(possible, GWWBottom)

    if leftimg!=None:
        if leftimg in WaterRight:
            possible = findintersections(possible, WaterLeft)
        elif leftimg in GrassRight:
            possible = findintersections(possible, GrassLeft)
        elif leftimg in GWWRight:
            possible = findintersections(possible, WWGLeft)
        elif leftimg in WWGRight:
            possible = findintersections(possible, GWWLeft)
    
    if rightimg!=None:
        if rightimg in WaterLeft:
            possible = findintersections(possible, WaterRight)
        elif rightimg in GrassLeft:
            possible = findintersections(possible, GrassRight)
        elif rightimg in GWWLeft:
            possible = findintersections(possible, WWGRight)
        elif rightimg in WWGLeft:
            possible = findintersections(possible, GWWRight)

    i = 0
    while i < len(possible):
        if possible[i] == None:
            possible.pop(i)
        i+=1
    if len(possible)==0:
        return None, 0
    finalimg = possible[random.randrange(0, len(possible))]
    return finalimg, len(possible)


background = []
backgroundpossibletiles = []
for i in range(round(W_height/tilesize)):
    line = []
    secondline = []
    for j in range(round(W_width/tilesize)):
        line.append(None)
        secondline.append(10)
    background.append(line)
    backgroundpossibletiles.append(secondline)
        
x = 0
y = 0
full = False
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        keyypress = pygame.key.get_pressed()
        if keyypress[pygame.K_SPACE] and not full:
            for Y in range (len(background)):
                for X in range (len(background[0])):
                    if Y == 0:
                        top = None
                    else:
                        top = background[Y-1][X]
                    if Y==len(background)-1:
                        bottom = None
                    else:
                        bottom = background[Y+1][X]
                    if X == 0:
                        left = None
                    else:
                        left = background[Y][X-1]
                    if X==len(background[Y])-1:
                        right = None
                    else:
                        right = background[Y][X+1]
                    tile, possibilities = GetTile(top, bottom, left, right)
                    backgroundpossibletiles[Y][X] = possibilities
            
            tmpnum = 10000
            for Y in range(len(backgroundpossibletiles)):
                for X in range(len(backgroundpossibletiles[Y])):
                    if tmpnum>backgroundpossibletiles[Y][X] and background[Y][X]==None:
                        x = X
                        y = Y

            if background[y][x] == None:
                # ReGraphics2()
                screen.fill((0, 0, 0))
                if y == 0:
                    top = None
                else:
                    top = background[y-1][x]
                if y==len(background)-1:
                    bottom = None
                else:
                    bottom = background[y+1][x]
                if x == 0:
                    left = None
                else:
                    left = background[y][x-1]
                if x==len(background[y])-1:
                    right = None
                else:
                    right = background[y][x+1]
                tile, possibilities = GetTile(top, bottom, left, right)
                background[y][x] = tile
                backgroundpossibletiles[y][x] = possibilities
            if background[y][x]==None:
                topy = y-1
                bottomy = y+1
                leftx = x-1
                rightx = x+1

                # if topy>=0:
                #     background[topy][x] = None
                # if bottomy<len(background):
                #     background[bottomy][x] = None
                # if leftx>=0:
                #     background[y][leftx] = None
                # if rightx<len(background[0]):
                #     background[y][rightx] = None


                if 0<=topy:
                    if topy <= 0:
                        top = None
                    else:
                        top = background[topy-1][x]
                    if topy>=len(background)-1:
                        bottom = None
                    else:
                        bottom = background[topy+1][x]
                    if x <= 0:
                        left = None
                    else:
                        left = background[topy][x-1]
                    if x>=len(background[topy])-1:
                        right = None
                    else:
                        right = background[topy][x+1]
                    tile, possibilities = GetTile(top, bottom, left, right)
                    background[topy][x] = tile
                    backgroundpossibletiles[topy][x] = possibilities

                if len(background)>bottomy:
                    if bottomy <= 0:
                        top = None
                    else:
                        top = background[bottomy-1][x]
                    if bottomy>=len(background)-1:
                        bottom = None
                    else:
                        bottom = background[bottomy+1][x]
                    if x <= 0:
                        left = None
                    else:
                        left = background[bottomy][x-1]
                    if x>=len(background[bottomy])-1:
                        right = None
                    else:
                        right = background[bottomy][x+1]
                    tile, possibilities = GetTile(top, bottom, left, right)
                    background[bottomy][x] = tile
                    backgroundpossibletiles[bottomy][x] = possibilities
                
                if 0<=rightx:
                    if y <= 0:
                        top = None
                    else:
                        top = background[y-1][leftx]
                    if y>=len(background)-1:
                        bottom = None
                    else:
                        bottom = background[y+1][leftx]
                    if leftx <= 0:
                        left = None
                    else:
                        left = background[y][leftx-1]
                    if leftx>=len(background[y])-1:
                        right = None
                    else:
                        right = background[y][leftx+1]
                    tile, possibilities = GetTile(top, bottom, left, right)
                    background[y][leftx] = tile
                    backgroundpossibletiles[y][leftx] = possibilities
                
                if len(background[0])>rightx:
                    if y <= 0:
                        top = None
                    else:
                        top = background[y-1][rightx]
                    if y>=len(background)-1:
                        bottom = None
                    else:
                        bottom = background[y+1][rightx]
                    if rightx <= 0:
                        left = None
                    else:
                        left = background[y][rightx-1]
                    if rightx>=len(background[y])-1:
                        right = None
                    else:
                        right = background[y][rightx+1]
                    tile, possibilities = GetTile(top, bottom, left, right)
                    background[y][rightx] = tile
                    backgroundpossibletiles[y][rightx] = possibilities

            screen.fill((0, 0, 0))
            width = 2
            for Y in range(len(background)):
                for X in range(len(background[y])):
                    if background[Y][X]!=None:
                        screen.blit(background[Y][X], (X*tilesize, Y*tilesize))
            pygame.draw.rect(screen, (255, 0, 0), [(x*tilesize)-width, (y*tilesize)-width, tilesize+(2*width), tilesize+(2*width)])
            if background[y][x]!=None:
                screen.blit(background[y][x], (x*tilesize, y*tilesize))
            else:
                pygame.draw.rect(screen, (0, 0, 0), [x*tilesize, y*tilesize, tilesize, tilesize]) 
            pygame.display.update()

            if x+1==len(background[y]):
                if y+1==len(background):
                    x = 0
                    y = 0
                else:
                    y+=1
                x = 0
            else:
                x+=1

        NoneCount = 0
        for i in background:
            for j in i:
                if j == None:
                    NoneCount+=1
        if NoneCount == 0:
            full = True
            screen.fill((0, 0, 0))
            for Y in range(len(background)):
                for X in range(len(background[y])):
                    if background[Y][X]!=None:
                        screen.blit(background[Y][X], (X*tilesize, Y*tilesize))
            pygame.display.update()

        if keyypress[pygame.K_DELETE]:
            for Y in range(len(background)):
                for X in range(len(background[Y])):
                    background[Y][X]=None
                    screen.fill((0, 0, 0))
                    pygame.display.update()
                    x =0
                    y =0
            full = False

        clock.tick(60)

pygame.quit()
quit()