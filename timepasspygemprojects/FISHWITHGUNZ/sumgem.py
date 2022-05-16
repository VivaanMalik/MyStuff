import math
import random
import pygame
pygame.init()

run = True
screenratio = 8/5 # 16/9
W_height = pygame.display.Info().current_h
W_width = round(W_height*screenratio)
tilesize = round(W_height/7.5)
screen = pygame.display.set_mode((W_width, W_height), pygame.FULLSCREEN|pygame.SCALED)
pygame.display.set_caption("Fish With Guns")
clock = pygame.time.Clock()
fps = 60
# fish = pygame.image.load("FishWithGun.png")
fish = pygame.image.load("Chad - Fish with Guns.png")
fish = pygame.transform.scale(fish, (tilesize, tilesize))
gun = pygame.image.load("AK-47.png")
gun = pygame.transform.scale(gun, (round(tilesize/1.5), round(tilesize/1.5)))
fish.blit(gun, (round(tilesize/3), round(tilesize/3)))
bulletxsize = round(tilesize/4)
bulletysize = round(tilesize/4)
enemies = []
bullets= []
lose = False
x = round((W_width/2)-(tilesize/2))
y = round((W_height/2)-(tilesize/2))
xadd = 0
yadd =0
frem = 0
enemyspeed = 7
bulletspeed = 10
eps = math.ceil(fps/0.5)
epsaddfrem = 5*fps
speed=5
reduceepsspeed = 5
shootrate = round(fps/4)
shoot = False
shootfrem = shootrate
bulletdamage = 25

def render_enemy(x, y):
    # screen.blit()
    pygame.draw.rect(screen, (0, 0, 0), [x, y, tilesize, tilesize])

def render_bullet(x, y):
    # screen.blit()
    pygame.draw.rect(screen, (255, 0, 0), [x, y, bulletxsize, bulletysize])

def setVars():
    global lose, x, y, yadd, xadd, frem, enemyspeed, bulletspeed, eps, epsaddfrem, speed, reduceepsspeed, shoot, shootfrem, bulletdamage, shootrate, enemies, bullets, run
    lose = False
    x = round((W_width/2)-(tilesize/2))
    y = round((W_height/2)-(tilesize/2))
    xadd = 0
    yadd =0
    frem = 0
    enemyspeed = 7
    bulletspeed = 10
    eps = math.ceil(fps/0.5)
    epsaddfrem = 5*fps
    speed=5
    reduceepsspeed = 5
    shootrate = round(fps/4)
    shoot = False
    shootfrem = shootrate
    bulletdamage = 25
    enemies = []
    bullets= []
    run =True

setVars()

def mainloop():
    global run, W_height, W_width, tilesize, screen, clock, fps, fish, lose, x, y, yadd, xadd, frem, enemyspeed, bulletspeed, eps, epsaddfrem, speed, reduceepsspeed, shoot, shootfrem, bulletdamage, shootrate, enemies, bullets
    while run:
        frem+=1
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run=False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT or event.key == ord('a'):
                    xadd = -speed
                if event.key == pygame.K_RIGHT or event.key == ord('d'):
                    xadd = speed
                if event.key == pygame.K_UP or event.key == ord('w'):
                    yadd = -speed
                if event.key == pygame.K_DOWN or event.key == ord('s'):
                    yadd = speed
                if event.key == pygame.K_SPACE and shootfrem%shootrate==0:
                    shoot = True
                
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == ord('a') or event.key == pygame.K_RIGHT or event.key == ord('d'):
                    xadd = 0
                if event.key == pygame.K_UP or event.key == ord('w') or event.key == pygame.K_DOWN or event.key == ord('s'):
                    yadd = 0

        if x+xadd>=0 and x+xadd<=W_width-fish.get_width():
            x+=xadd
        if y+yadd>=0 and y+yadd<=W_height-fish.get_height():
            y+=yadd
        if y+1<=W_height-fish.get_height():
            y+=1
        shootfrem+=1
        if shootfrem>shootrate:
            shootfrem=shootrate
        screen.fill((0, 200, 255))
        if frem%eps==0:
            enemy = [W_width, random.randrange(0, W_height-tilesize), 50]
            enemies.append(enemy)
        if frem%epsaddfrem==0 and eps-reduceepsspeed>=10:
            eps-=reduceepsspeed
        topop = []
        for i in range(len(enemies)):
            enemies[i][0]-=enemyspeed
            if enemies[i][0]<=0-tilesize:
                topop.append(i)
        for i in topop:
            enemies.pop(i)
        if shoot:
            shootfrem=0
            shoot = False
            bullets.append([x+fish.get_width(), y+round(fish.get_height()/2)])
        topop = []
        for i in range(len(bullets)):
            bullets[i][0]+=bulletspeed
            if bullets[i][0]>W_width:
                topop.append(i)
            for e in range(len(enemies)):
                if bullets[i][0]+bulletxsize>=enemies[e][0] and abs((bullets[i][1]+round(bulletysize/2))-(enemies[e][1]+round(tilesize/2)))<tilesize:
                    enemies[e][2]-=bulletdamage
                    topop.append(i)
        for i in topop:
            bullets.pop(i)
        topop = []
        for i in range(len(enemies)):
            if enemies[i][2]<=0:
                topop.append(i)
        for i in topop:
            enemies.pop(i)
        for i in enemies:
            render_enemy(i[0], i[1])
            if i[0]<=x+fish.get_width()-1 and abs(y-i[1])<round(tilesize/2) and abs(x-i[0])<round(tilesize):
                run = False
                lose = True
        for i in bullets:
            render_bullet(i[0], i[1])
        screen.blit(fish, (x, y))
        pygame.display.update()
        clock.tick(fps)

mainloop()

while lose:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            lose=False
        elif event.type==pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                setVars()
                mainloop()
    screen.fill((0, 0, 0))
    pygame.display.update()
    clock.tick(60)

pygame.quit()
quit()