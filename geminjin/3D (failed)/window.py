from pickletools import pybytes
from classes import *
import math
import pygame
import numpy as np

pygame.init()

clock=pygame.time.Clock()


def sigmoid(x):
    return 1/(1+np.exp(-x))

def distance(pos1, pos2):
    return math.sqrt((pos2.x-pos1.x)**2+(pos2.y-pos1.y)**2+(pos2.z-pos1.z)**2)

def MeanPoint(points):
    xavg=0
    yavg=0
    zavg=0
    for i in points:
        xavg+=i[0]
        yavg+=i[1]
        zavg+=i[2]
    xavg/=len(points)
    yavg/=len(points)
    zavg/=len(points)
    return Vector3(xavg, yavg, zavg)


BG=pygame.Color(25, 25, 25)
Cubecolor=pygame.Color(128, 0, 255)
gren=pygame.Color(0, 250, 0)
cyan=pygame.Color(0, 250, 250)


w=0
h=0
tick=0
screen=None

def readyup(tickin, win, hin, nem):
    global w, h, tick, screen
    tick=tickin
    w=win
    h=hin
    screen = pygame.display.set_mode((w, h))
    pygame.display.set_caption(nem)
    screen.fill(BG)
    pygame.display.flip()

def drawpoint(x, y, z, i=0):
    global screen
    
    d=z
    #pygame.draw.rect(screen, gren, pygame.Rect(x-(round(d/2)), y-(round(d/2)), d, d))
    if i >=4:
        pygame.draw.circle(screen, gren, (x, y), d)
    else:
        pygame.draw.circle(screen, cyan, (x, y), d)

def diff(x, y):
    return abs(x-y)

def type(x, y, txt, offset=0, size=32, color=cyan):
    global screen
    global w, h

    if x>round(w/2):
        x+=offset*(diff(round(w/2), x)/round(w/4))
    elif x<round(w/2):
        x-=offset*(diff(round(w/2), x)/round(w/4))
    if y>round(h/2):
        y+=offset*(diff(round(h/2), y)/round(h/4))
    elif y<round(h/2):
        y-=offset*(diff(round(h/2), y)/round(h/4))

    font = pygame.font.Font('freesansbold.ttf', size)
    text = font.render(txt, True, color, None)
    tectrekt=text.get_rect()
    tectrekt.center=(x, y)
    screen.blit(text, tectrekt)

def checkquit():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    pygame.display.flip()
    clock.tick(tick)

def Dotz(verts):
    global screen   
    global w, h

    screen.fill(BG)
    xylist=[]
    for index, i in enumerate(verts):
        x=round(i[0].tolist()[0][0])
        y=round(i[1].tolist()[0][0])    
        x+=round(w/2)
        y+=round(h/2)
        z=i[2].tolist()[0][0]
        dia=6/sigmoid(round(i[2].tolist()[0][0]))

        #drawpoint(x, y, dia)

        xylist.append((x, y, z, index+1))
    return xylist

def Linez(data, edges):
    global screen
    for i in edges:
        point1=i[0][0]
        point2=i[1][0]
        point1=(data[point1][0], data[point1][1])
        point2=(data[point2][0], data[point2][1])
        pygame.draw.line(screen, gren, point1, point2, 2)

def rotatey(coords, rot):
    rot=math.radians(rot)
    RotateY=np.array(
            [[math.cos(rot), 0, math.sin(rot), 0],
            [0, 1, 0, 0],
            [-math.sin(rot), 0, math.cos(rot), 0],
            [0, 0, 0, 1]]
        )
    return np.dot(coords, RotateY)

def Ngonz(data, faces, lightsource):
    global screen
    facestorender=[]
    meanpoints=[]
    pointsformean=[]
    dists=[]
    xys=[]
    
    for i in faces:
        for j in i:
            pointsformean.append(data[j[0]-1])
        meanpoint=MeanPoint(pointsformean)
        meanpoints.append(meanpoint)
        dists.append(distance(lightsource.pos, meanpoint))
        # xy=rotatey([meanpoint.x, meanpoint.y, meanpoint.z, 1], 90)
        xy=Vector2(meanpoint.x, meanpoint.z)
        xys.append(xy)

    multipliers=lightsource.calculatemultiplier(dists, xys, 0.1)

    for indexi, i in enumerate(faces):
        points=[]
        pointsformean=[]
        for j in i:
            points.append(data[j[0]-1][:2])
            pointsformean.append(data[j[0]-1])
        color=Cubecolor

        meanpoint=MeanPoint(pointsformean)
        multiplier=multipliers[indexi]


        multiplier = distance(lightsource.pos, meanpoint)/500
        r=round(color.r*multiplier)
        g=round(color.g*multiplier)
        b=round(color.b*multiplier)
        color=pygame.Color(r, g, b)
        # for index in

        facestorender.append([meanpoint.z, color, points, (meanpoint.x, meanpoint.y)])
    facestorender=sorted(facestorender, key=lambda x: x[0])
    facestorender.reverse()
    for i in facestorender:
        pygame.draw.polygon(screen, i[1], i[2], 0)
        #pygame.draw.circle(screen, (0, 0, 255), i[3], 10)
        #type(i[3][0], i[3][1], str(round(i[0]*100)/100), offset=15, size=20, color=pygame.Color(255, 0, 0))
    for i in data:
        #type(i[0], i[1], str(i[3]), offset=10)
        pass
    pygame.draw.circle(screen, pygame.Color(255, 0, 100), (lightsource.pos.x, lightsource.pos.y), 10)