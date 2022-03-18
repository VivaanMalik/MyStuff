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
    def __init__(self, power, Pos) -> None:
        self.power=power
        self.pos=Pos
        


def sigmoid(x):
    return 1/(1+np.exp(-x))
