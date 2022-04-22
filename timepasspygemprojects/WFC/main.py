import random
from tkinter import W
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
    possible = []
    if topimg in WaterBottom:
        possible.append(x for x in WaterTop)
    elif topimg in GrassBottom:
        possible.append(x for x in GrassTop)
    elif topimg in GWWBottom:
        possible.append(x for x in WWGTop)
    elif topimg in WWGBottom:
        possible.append(x for x in GWWTop)

    if bottomimg in WaterTop:
        possible.append(findintersections(possible, WaterBottom))
    elif bottomimg in GrassTop:
        possible.append(findintersections(possible, GrassBottom))
    elif bottomimg in GWWTop:
        possible.append(findintersections(possible, WWGBottom))
    elif bottomimg in WWGTop:
        possible.append(findintersections(possible, GWWBottom))

    for i in range(possible):
        if possible[i] == None:
            possible.pop(i)

    return possible[random.randrange(0, possible.count())]

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        # ReGraphics2()
        screen.fill((0, 0, 0))
        # screen.blit() add source to new function
        pygame.display.update()

        clock.tick(60)

pygame.quit()
quit()