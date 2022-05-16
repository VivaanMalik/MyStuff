import window
from classes import *
import math
import numpy as np
import json

class ObjectCube():
    def __init__(self):
        self.object=json.load(open("mainobjects.json"))
        self.object=self.object["Cube"]
        self.verts=np.array(self.object["vertices"])
        self.edges=np.array(self.object["edges"])
        self.faces=np.array(self.object["faces"])

class ExternalObject():
    def __init__(self, name):
        self.object=json.load(open("Jsons\\"+name+".json"))
        self.verts=np.array(self.object["vertices"])
        self.edges=np.array(self.object["edges"])
        self.faces=np.array(self.object["faces"])

def render(verts, focallength=0.1, skew=0, Cpos=Vector3(0, 0, 10), Crot=Vector3(0, 0, 0), imgres=Vector2(500, 500), sensorsize=Vector2(0.05, 0.05), offset=None):
    if offset==None:
        offset=np.array(
            [[1, 0, 0, 0],
            [0, 1, 0, 0],
            [0, 0, 1, 0],
            [0, 0, 0, 1]]
        )
    result=[]
    Crot=Vector3(math.radians(Crot.x), math.radians(Crot.y), math.radians(Crot.z))
    RotateX=np.array(
        [[1, 0, 0, 0],
        [0, math.cos(Crot.x), -math.sin(Crot.x), 0],
        [0, math.sin(Crot.x), math.cos(Crot.x), 0],
        [0, 0, 0, 1]]
    )
    RotateY=np.array(
        [[math.cos(Crot.y), 0, math.sin(Crot.y), 0],
        [0, 1, 0, 0],
        [-math.sin(Crot.y), 0, math.cos(Crot.y), 0],
        [0, 0, 0, 1]]
    )
    RotateZ=np.array(
        [[math.cos(Crot.z), -math.sin(Crot.z), 0, 0],
        [math.sin(Crot.z), math.cos(Crot.z), 0, 0],
        [0, 0, 1, 0],
        [0, 0, 0, 1]]
    )
    CameraPos=np.array(
        [[1, 0, 0, -Cpos.x],
        [0, 1, 0, -Cpos.y],
        [0, 0, 1, -Cpos.z],
        [0, 0, 0, 1]]
    )
    Weirdassshit=np.array(
        [[(focallength*imgres.x)/(2*sensorsize.x), skew, 0, 0],
        [0, (focallength*imgres.y)/(2*sensorsize.y), 0, 0],
        [0, 0, -1, 0],
        [0, 0, 0, 1]]
    )
    for index, vertices in enumerate(verts):
        result.append(np.dot(RotateZ, vertices))
        result[index]=np.dot(RotateY, result[index])
        result[index]=np.dot(RotateX, result[index])
        result[index]=np.dot(CameraPos, result[index])
        result[index]=np.dot(Weirdassshit, result[index])
        Img = np.array(
                [[ 1/result[index][2], 0, 0, 0 ],
                [ 0, 1/result[index][2], 0, 0 ],
                [ 0, 0, 1, 0 ],
                [ 0, 0, 0, 1 ]], dtype=object
        )
        result[index]=np.dot(Img, result[index])
        result[index]=np.dot(offset, result[index])
        # for index, val in enumerate(result):
        #     result[index]=val.tolist()
        #     for indx in range(len(result[index])): 
        #         for index2, val2 in enumerate(result[index][indx]):
        #             result[index][indx][index2]=val2.tolist()
    return result

class LightSource():
    def __init__(self, power, Pos, imgres, depth) -> None:
        self.power=power
        Pos.x+=round(imgres.x)
        Pos.y+=round(imgres.y)
        Pos.z+=round(depth/2)
        self.pos=Pos
    def lineinmesh(self):
        pass
    def calculatemultiplier(self, dists, xy, detail):
        ogxys=[]
        semxys=[]
        for i in range(len(dists)):
            inog=False
            for j in ogxys:
                if round(xy[i].x/detail)*detail == j[0].x and round(xy[i].y/detail)*detail == j[0].y:
                    semxys.append([])
                    semxys[i].append(i)
                    inog=True
            if not inog:
                semxys.append([i])
                ogxys.append([xy[i], dists[i], i])
        finalmultipliers=[]
        for i in range(len(dists)):
            finalmultipliers.append(0.15)
        for index1, i in enumerate(semxys):
            if len(i)!=0:
                big=0
                for index2, j in enumerate(i):
                    if j>i[big]:
                        big=index2
                for index2, j in enumerate(i):
                    if big==index2:
                        finalmultipliers[j]=(self.power/(1/dists[j]))/100000
        return finalmultipliers

def sigmoid(x):
    return 1/(1+np.exp(-x))
