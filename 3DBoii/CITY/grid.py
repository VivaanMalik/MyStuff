# alternate - + of da house coords per distance thing for less path wdth
# change the coords from to points |oo| to 4 |88|
import math
import matplotlib.pyplot as plt
import random
def HouseGrid(Grid, detail, size, dia):
    offsetdist=5
    vertices=round((dia*2.5)*detail)
    angle=0
    for distance in range(1, round(size/15)):
        Grid[2].append([])
    ang_count=0
    while int(round(angle))<=360:
        if (ang_count)%2==1:
            angle+=360/(vertices*2)
            off=90
        else:
            angle+=360/vertices
            off=-90
        index=0
        for distance in range(2, round(size/20)):
            dist=distance*20
            # if (ang_count)%2==1:
            #     coord=(dist*math.cos(math.radians(angle)), dist*math.sin(math.radians(angle)))
            # else:
            #     coord=(dist*math.cos(math.radians(angle)), dist*math.sin(math.radians(angle)))
            coord=(dist*math.cos(math.radians(angle)), dist*math.sin(math.radians(angle)))
            #coord=(coord[0]+(offsetdist*math.cos(math.radians(angle+off))), coord[1]+(offsetdist*math.sin(math.radians(angle+off))))
            Grid[2][index].append(coord)
            index+=1
        ang_count+=1
    grid=Grid
    return grid
def wavy(a:tuple, b:tuple, detail):
    path=[]
    distance=math.sqrt(((a[0]-b[0])**2)+((a[1]-b[1])**2))
    points=int(round(math.floor(distance/random.randrange(6, 8))*detail))
    range_dist=3
    i=0
    x_val=a[0]
    y_val=a[1]
    while i<points:
        i+=1
        x_val-=(a[0]-b[0])/points
        x_val+=random.randrange(-range_dist, range_dist+1)
        y_val-=(a[1]-b[1])/points
        y_val+=random.randrange(-range_dist, range_dist+1)
        path.append((x_val, y_val))
    return path
def deletenodes(circle:list, wavy, outer:bool=False, list:list=[]):
    for i in wavy:
        for j in i:
            for k in circle:
                if math.sqrt(((j[0]-k[0])**2)+((j[1]-k[1])**2))<=10:
                    if outer:
                        list.append(k)
                    circle.pop(circle.index(k))
    return circle, list
def circle_gen(cir:tuple, diameter):
    circle_points=[[], [], [], [], [], [], []] #outer circle -> inner circle -> connected sectors -> layers (123)
    vertices=diameter
    angle=360/vertices
    L1=False
    L2=False
    L3=False
    for i in range(vertices):
        l1=random.randrange(0, round(vertices/2))
        l2=random.randrange(0, round(vertices/2))
        l3=random.randrange(0, round(vertices/2))
        if l1==0:
            if L1:
                L1=False
            else:
                L1=True
        if L1:
            circle_points[3].append((((diameter/10)*8)*math.cos(math.radians(angle)), ((diameter/10)*8)*math.sin(math.radians(angle))))
        if l2==0:
            if L2:
                L2=False
            else:
                L2=True
        if L2:
            circle_points[4].append((((diameter/10)*6)*math.cos(math.radians(angle)), ((diameter/10)*6)*math.sin(math.radians(angle))))
        if l3==0:
            if L3:
                L3=False
            else:
                L3=True
        if L3:
            circle_points[5].append((((diameter/10)*4)*math.cos(math.radians(angle)), ((diameter/10)*4)*math.sin(math.radians(angle))))
        circle_points[0].append((diameter*math.cos(math.radians(angle)), diameter*math.sin(math.radians(angle))))
        circle_points[1].append((10*math.cos(math.radians(angle)), 10*math.sin(math.radians(angle))))
        angle+=360/vertices
        point=random.randrange(0, round(vertices/5))
        if point==0:
            circle_points[2].append((((diameter/2)+10)*math.cos(math.radians(angle)), ((diameter/2)+10)*math.sin(math.radians(angle))))
    if len(circle_points[2])==0:
        angle=(360/vertices)*(random.randrange(0, vertices))
        circle_points[2].append((((diameter/2)+10)*math.cos(math.radians(angle)), ((diameter/2)+10)*math.sin(math.radians(angle))))
    for i in circle_points:
        for j in i:
            list(j)[0]+=list(cir)[0]
            list(j)[1]+=list(cir)[1]
    return circle_points
def gengrid(size:tuple, cir:tuple=(0,0), detail:float=0.5, view=False):
    diameter=random.randrange(round((size[0]+size[1])/16), round((size[0]+size[1])/10))
    dia_multiplier=round((size[0]+size[1])/2)/diameter
    Grid=[circle_gen(cir, diameter),  [], []] # 0 iz circle point there v add xtra shit... 1 iz list of points of lines... 2 iz da list of houses/buildings areas
    for i in Grid[0][2]:
        Grid[1].append(wavy(i, tuple(((((size[0]+size[1])/2)*math.cos(math.atan2(i[1], i[0])), ((size[0]+size[1])/2)*math.sin(math.atan2(i[1], i[0]))))), detail))
    HouseGrid(Grid, detail, round((size[0]+size[1])/2), diameter)
    Grid[0][3], Grid[0][6]=deletenodes(Grid[0][3], Grid[1])
    Grid[0][4], Grid[0][6]=deletenodes(Grid[0][4], Grid[1])
    Grid[0][5], Grid[0][6]=deletenodes(Grid[0][5], Grid[1])
    Grid[0][0], Grid[0][6]=deletenodes(Grid[0][0], Grid[1], True, Grid[0][6])
    for i in Grid[2]:
        i, Grid[0][6]=deletenodes(i, Grid[1])
    if view==False:
        return Grid
    print(Grid)
    for i in Grid:
        for j in i:
            if len(j)!=0:
                plt.scatter(*zip(*j))
    plt.show()
    return Grid