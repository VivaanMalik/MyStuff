import math
import random
import RoomGenerator
import pygame

pygame.init()

run = True
screenratio = 8/5 # 16/9
W_height = pygame.display.Info().current_h
W_width = round(W_height*screenratio)
tilesize = round(W_height/5)

roomdata = []
screen = pygame.display.set_mode((W_width, W_height), pygame.FULLSCREEN|pygame.SCALED)
pygame.display.set_caption("This is a window =)")
clock = pygame.time.Clock()

playeranimationindex=0

PLAYER_IDLE=[pygame.image.load("IMAJIZ\\CHAR_IDLE_01.png"), pygame.image.load("IMAJIZ\\CHAR_IDLE_02.png"), pygame.image.load("IMAJIZ\\CHAR_IDLE_03.png"), pygame.image.load("IMAJIZ\\CHAR_IDLE_04.png")]
NS_TILES=[pygame.image.load("IMAJIZ\\TILE_NS_01.png"), pygame.image.load("IMAJIZ\\TILE_NS_02.png"), pygame.image.load("IMAJIZ\\TILE_NS_03.png"), pygame.image.load("IMAJIZ\\TILE_NS_04.png")]
SN_TILES=[pygame.image.load("IMAJIZ\\TILE_SN_01.png"), pygame.image.load("IMAJIZ\\TILE_SN_02.png"), pygame.image.load("IMAJIZ\\TILE_SN_03.png"), pygame.image.load("IMAJIZ\\TILE_SN_04.png")]
SS_TILES=[pygame.image.load("IMAJIZ\\TILE_SS_01.png"), pygame.image.load("IMAJIZ\\TILE_SS_02.png"), pygame.image.load("IMAJIZ\\TILE_SS_03.png"), pygame.image.load("IMAJIZ\\TILE_SS_04.png")]
NN_TILES=[pygame.image.load("IMAJIZ\\TILE_NN_01.png"), pygame.image.load("IMAJIZ\\TILE_NN_02.png"), pygame.image.load("IMAJIZ\\TILE_NN_03.png"), pygame.image.load("IMAJIZ\\TILE_NN_04.png")]

def drawGraphics(rooms, roomindex, PlayerX, PlayerY):
    global roomdata
    global playeranimationindex
    
    if len(roomdata)==0:
        for i in range(len(rooms)):
            roomdata.append([])

    # drawroomz
    screen.fill((0, 173, 124))
    if len(roomdata[roomindex])==0:
        for i in range(40):
            if i in [1, 2, 3, 4, 5, 6, 7]:
                roomdata[roomindex].append(random.choice(NS_TILES))
            elif i == 0:
                roomdata[roomindex].append(random.choice(SS_TILES))
            elif i in [8, 16, 24, 32]:
                roomdata[roomindex].append(random.choice(SN_TILES))
            else:
                roomdata[roomindex].append(random.choice(NN_TILES))
    else:
        for i in range(len(roomdata[roomindex])):
            xpos=i%8
            ypos=math.floor(i/8)
            image = roomdata[roomindex][i]
            image = pygame.transform.scale(image, (tilesize, tilesize))
            screen.blit(image, (xpos*tilesize, ypos*tilesize))

    # draw player
    playeranimationindex+=1
    if (playeranimationindex==60):
        playeranimationindex=0
    
    playersprite=PLAYER_IDLE[0]
    if playeranimationindex<24:
        playersprite = PLAYER_IDLE[0]
    elif playeranimationindex<30:
        playersprite = PLAYER_IDLE[1]
    elif playeranimationindex<54:
        playersprite = PLAYER_IDLE[2]
    elif playeranimationindex<60:
        playersprite = PLAYER_IDLE[3]
    playersprite=pygame.transform.scale(playersprite, (tilesize, tilesize))
    screen.blit(playersprite, (PlayerX, PlayerY))
    
    pygame.display.update()

def main():
    global run
    PlayerX = round((W_width/2)-tilesize)
    PlayerY = round((W_height/2)-(tilesize/2))

    rooms = RoomGenerator.GetRooms()
    CurrentRoom = rooms.index(1)

    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            
        drawGraphics(rooms, CurrentRoom, PlayerX, PlayerY)
        clock.tick(120)
    pygame.quit()

main()