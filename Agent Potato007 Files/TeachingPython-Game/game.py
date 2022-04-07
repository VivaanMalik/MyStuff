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
midtilesize = round(tilesize*0.75)

roomdata = []
screen = pygame.display.set_mode((W_width, W_height), pygame.FULLSCREEN|pygame.SCALED)
pygame.display.set_caption("This is a window =)")
clock = pygame.time.Clock()

playeranimationindex=0

HORIZONTALWALL = pygame.image.load("IMAJIZ\\HORIZONTALWALL.png")
VERTICALWALL = pygame.image.load("IMAJIZ\\VERTICALWALL.png")
PLAYER_WALK_RIGHT = [pygame.image.load("IMAJIZ\\CHAR_WALK_01.png"),pygame.image.load("IMAJIZ\\CHAR_WALK_02.png"), pygame.image.load("IMAJIZ\\CHAR_WALK_03.png"), pygame.image.load("IMAJIZ\\CHAR_WALK_04.png"), pygame.image.load("IMAJIZ\\CHAR_WALK_05.png"), pygame.image.load("IMAJIZ\\CHAR_WALK_06.png")]
PLAYER_WALK_LEFT = [pygame.image.load("IMAJIZ\\CHAR_WALK_07.png"),pygame.image.load("IMAJIZ\\CHAR_WALK_08.png"), pygame.image.load("IMAJIZ\\CHAR_WALK_09.png"), pygame.image.load("IMAJIZ\\CHAR_WALK_10.png"), pygame.image.load("IMAJIZ\\CHAR_WALK_11.png"), pygame.image.load("IMAJIZ\\CHAR_WALK_12.png")]
PLAYER_WALK_FRONT = [pygame.image.load("IMAJIZ\\CHAR_WALK_13.png"),pygame.image.load("IMAJIZ\\CHAR_WALK_14.png"), pygame.image.load("IMAJIZ\\CHAR_WALK_15.png"), pygame.image.load("IMAJIZ\\CHAR_WALK_16.png")]
PLAYER_WALK_BACK = [pygame.image.load("IMAJIZ\\CHAR_WALK_17.png"),pygame.image.load("IMAJIZ\\CHAR_WALK_18.png"), pygame.image.load("IMAJIZ\\CHAR_WALK_19.png"), pygame.image.load("IMAJIZ\\CHAR_WALK_20.png")]
PLAYER_IDLE=[pygame.image.load("IMAJIZ\\CHAR_IDLE_01.png"), pygame.image.load("IMAJIZ\\CHAR_IDLE_02.png"), pygame.image.load("IMAJIZ\\CHAR_IDLE_03.png"), pygame.image.load("IMAJIZ\\CHAR_IDLE_04.png")]
NS_TILES=[pygame.image.load("IMAJIZ\\TILE_NS_01.png"), pygame.image.load("IMAJIZ\\TILE_NS_02.png"), pygame.image.load("IMAJIZ\\TILE_NS_03.png")]
SN_TILES=[pygame.image.load("IMAJIZ\\TILE_SN_01.png"), pygame.image.load("IMAJIZ\\TILE_SN_02.png"), pygame.image.load("IMAJIZ\\TILE_SN_03.png")]
SS_TILES=[pygame.image.load("IMAJIZ\\TILE_SS_01.png"), pygame.image.load("IMAJIZ\\TILE_SS_02.png"), pygame.image.load("IMAJIZ\\TILE_SS_03.png")]
NN_TILES=[pygame.image.load("IMAJIZ\\TILE_NN_01.png"), pygame.image.load("IMAJIZ\\TILE_NN_02.png"), pygame.image.load("IMAJIZ\\TILE_NN_03.png")]

def drawGraphics(rooms, roomindex, PlayerX, PlayerY, PlayerAnim):
    global roomdata
    global playeranimationindex
    
    if len(roomdata)==0:
        for i in range(len(rooms)):
            roomdata.append([])

    # drawroomz
    screen.fill((0, 173, 124))
    if len(roomdata[roomindex])==0:
        for i in range(170):
            if i in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]:
                roomdata[roomindex].append(random.choice(NS_TILES))
            elif i == 0:
                roomdata[roomindex].append(random.choice(SS_TILES))
            elif i in [16, 32, 48, 64, 80, 96, 112, 128, 144]:
                roomdata[roomindex].append(random.choice(SN_TILES))
            else:
                roomdata[roomindex].append(random.choice(NN_TILES))
    else:
        for i in range(len(roomdata[roomindex])):
            xpos=i%16
            ypos=math.floor(i/16)
            image = roomdata[roomindex][i]
            smoltilesie = math.ceil(tilesize/2)
            image = pygame.transform.scale(image, (smoltilesie, smoltilesie))
            screen.blit(image, (xpos*smoltilesie+round(smoltilesie/2), ypos*smoltilesie+round(midtilesize*1.1)))
        for i in range(11):
            wall = HORIZONTALWALL
            wall =  pygame.transform.scale(wall, (midtilesize, round(midtilesize*1.1)))
            screen.blit(wall, (i*midtilesize, 0))
        for i in range(8):
            wall1 = VERTICALWALL
            wall2 = VERTICALWALL
            wall1 = pygame.transform.scale(wall1, ((midtilesize*1.1), midtilesize))
            wall2 = pygame.transform.scale(wall2, (midtilesize, midtilesize))
            wall2 = pygame.transform.flip(wall2, True, False)
            screen.blit(wall1, (0, (i*midtilesize)))
            screen.blit(wall2, (screen.get_width()-wall2.get_width(), (i*midtilesize)))

    # draw player
    if PlayerAnim=="IDLE":
        playeranimationindex+=2
        if (playeranimationindex>=60):
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
    elif PlayerAnim=="RIGHT":
        playeranimationindex+=2
        if (playeranimationindex>=30):
            playeranimationindex=0
        playersprite=PLAYER_IDLE[0]
        if playeranimationindex<5:
            playersprite = PLAYER_WALK_RIGHT[0]
        elif playeranimationindex<10:
            playersprite = PLAYER_WALK_RIGHT[1]
        elif playeranimationindex<15:
            playersprite = PLAYER_WALK_RIGHT[2]
        elif playeranimationindex<20:
            playersprite = PLAYER_WALK_RIGHT[3]
        elif playeranimationindex<25:
            playersprite = PLAYER_WALK_RIGHT[4]
        elif playeranimationindex<30:
            playersprite = PLAYER_WALK_RIGHT[5]
    elif PlayerAnim=="LEFT":
        playeranimationindex+=2
        if (playeranimationindex>=30):
            playeranimationindex=0
        playersprite=PLAYER_IDLE[0]
        if playeranimationindex<5:
            playersprite = PLAYER_WALK_LEFT[0]
        elif playeranimationindex<10:
            playersprite = PLAYER_WALK_LEFT[1]
        elif playeranimationindex<15:
            playersprite = PLAYER_WALK_LEFT[2]
        elif playeranimationindex<20:
            playersprite = PLAYER_WALK_LEFT[3]
        elif playeranimationindex<25:
            playersprite = PLAYER_WALK_LEFT[4]
        elif playeranimationindex<30:
            playersprite = PLAYER_WALK_LEFT[5]
    elif PlayerAnim=="DOWN":
        playeranimationindex+=2
        if (playeranimationindex>=20):
            playeranimationindex=0
        playersprite=PLAYER_IDLE[0]
        if playeranimationindex<5:
            playersprite = PLAYER_WALK_FRONT[0]
        elif playeranimationindex<10:
            playersprite = PLAYER_WALK_FRONT[1]
        elif playeranimationindex<15:
            playersprite = PLAYER_WALK_FRONT[2]
        elif playeranimationindex<20:
            playersprite = PLAYER_WALK_FRONT[3]
    elif PlayerAnim=="UP":
        playeranimationindex+=2
        if (playeranimationindex>=20):
            playeranimationindex=0
        playersprite=PLAYER_IDLE[0]
        if playeranimationindex<5:
            playersprite = PLAYER_WALK_BACK[0]
        elif playeranimationindex<10:
            playersprite = PLAYER_WALK_BACK[1]
        elif playeranimationindex<15:
            playersprite = PLAYER_WALK_BACK[2]
        elif playeranimationindex<20:
            playersprite = PLAYER_WALK_BACK[3]

    playersprite=pygame.transform.scale(playersprite, (midtilesize, midtilesize))
    screen.blit(playersprite, (PlayerX, PlayerY))
    
    pygame.display.update()

def main():
    global run
    PlayerX = round((W_width/2)-midtilesize)
    PlayerY = round((W_height/2)-(midtilesize/2))
    PLAYERANIM="IDLE"
    rooms = RoomGenerator.GetRooms()
    CurrentRoom = rooms.index(1)
    speed=12
    PlayerXspeed=0
    PlayerYspeed=0

    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            # elif event.type == pygame.KEYUP:
            #     pressed = event.key
            #     if pressed==pygame.K_w and PLAYERANIM == "UP":
            #         PLAYERANIM = "IDLE"
            #     if pressed==pygame.K_a and PLAYERANIM == "LEFT":
            #         PLAYERANIM = "IDLE"
            #     if pressed==pygame.K_s and PLAYERANIM == "DOWN":
            #         PLAYERANIM = "IDLE"
            #     if pressed==pygame.K_d and PLAYERANIM == "RIGHT":
            #         PLAYERANIM = "IDLE"
            # elif event.type == pygame.KEYDOWN:
            #     pressed = event.key
            #     if pressed==pygame.K_w:
            #         PLAYERANIM = "UP"
            #     if pressed==pygame.K_a:
            #         PLAYERANIM = "LEFT"
            #     if pressed==pygame.K_s:
            #         PLAYERANIM = "DOWN"
            #     if pressed==pygame.K_d:
            #         PLAYERANIM = "RIGHT"

            PLAYERANIM = "IDLE"
            keyypress = pygame.key.get_pressed()
            if keyypress[pygame.K_w]:
                PLAYERANIM = "UP"
            if keyypress[pygame.K_a]:
                PLAYERANIM = "LEFT"
            if keyypress[pygame.K_s]:
                PLAYERANIM = "DOWN"
            if keyypress[pygame.K_d]:
                PLAYERANIM = "RIGHT"
                
            if PLAYERANIM == "RIGHT":
                PlayerXspeed=speed
                PlayerYspeed=0
            elif PLAYERANIM == "DOWN":
                PlayerYspeed=round(speed*0.85)
                PlayerXspeed=0
            elif PLAYERANIM == "LEFT":
                PlayerXspeed=-speed
                PlayerYspeed=0
            elif PLAYERANIM == "UP":
                PlayerYspeed=round(-speed*0.85)
                PlayerXspeed=0

            if PlayerX+midtilesize+PlayerXspeed<=W_width and PLAYERANIM=="RIGHT":
                PlayerX+=PlayerXspeed
            if PlayerY+midtilesize+PlayerYspeed<=W_height and PLAYERANIM=="DOWN":
                PlayerY+=PlayerYspeed
            if PlayerY+PlayerYspeed>=0 and PLAYERANIM=="UP":
                PlayerY+=PlayerYspeed
            if PlayerX+PlayerXspeed>=0 and PLAYERANIM=="LEFT":
                PlayerX+=PlayerXspeed

        drawGraphics(rooms, CurrentRoom, PlayerX, PlayerY, PLAYERANIM)
        clock.tick(30)
    pygame.quit()

main()