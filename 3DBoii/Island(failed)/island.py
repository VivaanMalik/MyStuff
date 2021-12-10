from generativepy.drawing import make_image, setup
from generativepy.geometry import Circle, Polygon
from generativepy.color import Color
from scipy.misc.common import face
from scipy.spatial import Voronoi, voronoi_plot_2d
import random
import json
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
from perlin_noise import PerlinNoise
import sys
import math

def progress(count, total, status=''):
    total-=1
    bar_len = 69
    filled_len = int(round(bar_len * count / float(total)))

    percents = round(100.0 * count / float(total), 1)
    bar = 'e' * filled_len + '' * (bar_len - filled_len)

    sys.stdout.write('y%st %s%s | %s out of %s |%s\r' % (bar, percents, '%', str(count), str(total), status))
    sys.stdout.flush()

test=(input('TEST NUMBER:\n'))

siiize=input('Custom size (or random)? [c/r]:\n')
if siiize=='c':
    SIZE=int(input('Size:\n'))
elif siiize=='r':
    SIZE=random.randrange(1000, 10000)
print('SIZE: '+str(SIZE))

pooints=input('Custom points/same as size/random? [c/s/r]:\n')
if pooints=='c':
    POINTS=int(input('Points:\n'))
elif pooints=='s':
    POINTS=SIZE
elif pooints=='r':
    POINTS=random.randrange(1000, 10000)
print('POINTS: '+str(POINTS))

seedd=input('Custom seed (or random)? [c/r]:\n')
if seedd=='c':
    SEED=int(input('Seed:\n'))
elif seedd=='r':
    SEED=random.randrange(1, 1000000)
print('SEED: '+str(SEED))

noise = PerlinNoise(octaves=1, seed=SEED)
xpix, ypix = round(SIZE/2), round(SIZE/2)
pic = [[noise([i/xpix, j/ypix]) for j in range(xpix)] for i in range(ypix)]

# Create a list of random points
random.seed(SEED)
points = [[random.randrange(0,SIZE), random.randrange(0,SIZE)]
          for i in range(POINTS)]
points.append((0, 0))
points.append((0, SIZE-1))
points.append((SIZE-1, 0))
points.append((SIZE-1, SIZE-1))
dump=[]

def drawVoronoi(ctx, pixel_width, pixel_height, frame_no, frame_count):
    global dump
    global SIZE
    setup(ctx, pixel_width, pixel_height, background=Color(1))
    voronoi = Voronoi(points, False, False, 'Qbb Qc Qz')
    voronoi_vertices = voronoi.vertices
    dump=voronoi_vertices.tolist()
    finadump=[]
    for vpair in voronoi.ridge_vertices:
        if vpair[0] >= 0 and vpair[1] >= 0:
            v0 = voronoi.vertices[vpair[0]]
            v1 = voronoi.vertices[vpair[1]]
            if v0[0]>=0 and v0[1]>=0 and v1[0]>=0 and v1[1]>=0:
                if v0[0]<=SIZE*2 and v0[1]<=SIZE*2 and v1[0]<=SIZE*2 and v1[1]<=SIZE*2:
                    finadump.append([v0.tolist(), v1.tolist()])
    with open('voronoi tsts/coordinates/'+test+'_VORONOI_CORD.json', 'w+') as f:
        json.dump(finadump, f, indent=4)
    with open('voronoi tsts/face_data/'+test+'_VORONOI_CORD.json', 'w+') as f:
        json.dump(voronoi.regions, f, indent=4)
    shaps=[]
    for region in voronoi.regions:
       if -1 not in region:
           polygon = [voronoi_vertices[p] for p in region]
           shaps.append(polygon)
           Polygon(ctx).of_points(polygon).stroke(line_width=2)
    

make_image('./voronoi tsts/imgs/'+test+'_VORONOI_IMG', drawVoronoi, SIZE, SIZE)
pic = np.asarray(pic)
pic=(((pic - pic.min()) / (pic.max() - pic.min())) * 255).astype(np.uint8)
noisepic=Image.fromarray(pic)
noisepic=noisepic.save('./perlin tsts/imgs/'+test+'_PERLIN_IMG.jpg')
noisepic=Image.open('./perlin tsts/imgs/'+test+'_PERLIN_IMG.jpg')


width, height = noisepic.size
noisepic=noisepic.resize((width*4, height*4))

coords=list(json.load(open('voronoi tsts/coordinates/'+test+'_VORONOI_CORD.json', 'r')))

with open('Models/'+test+'_MTL.mtl', 'w+') as f:
    f.write('''newmtl ghass\n
Ka 1.000000 1.000000 1.000000\n
Kd 0.640000 0.640000 0.640000\n
Ks 0.500000 0.500000 0.500000\n
Ns 96.078431\n
Ni 1.000000\n
d 1.000000\n
illum 0\n
map_Kd .\ghass.jpg''')

method=2

with open('Models/'+test+'_MODEL.obj', 'w+') as f:
    f.write('mtllib '+test+'_MTL.mtl\n')
    f.write('o island_num_'+test+'\n')
    v_cords=[]
    for j in coords:
        progress(coords.index(j), len(coords), 'Calculating vertices')
        for i in j:
            try:
                if i in v_cords:
                    pass
                else:
                    v_cords.append(i)
                    tmp=noisepic.getpixel((round(i[0]), round(i[1])))
                    f.write('v '+str(i[0])+' '+str(round(tmp))+' '+str(i[1])+'\n')
            except:
                print(i)
                input('FaLiUrE!')
    print('\n', end='')
    f.close
with open('Models/'+test+'_MODEL.obj', 'r') as fr:
    linez=fr.readlines()
with open('Models/'+test+'_MODEL.obj', 'a') as f:
    if method==0:
        while i+2<=len(coords):
            f.write('f '+str(i)+' '+str(i+1)+' '+str(i+2)+'\n')
            i+=1
            progress((i+2), len(coords), 'Calculating faces')
    elif method==1:
        f.write('f ')
        for i in range(len(coords)):
            f.write(str(i)+' ')
    elif method==2:
        faces=list(json.load(open('voronoi tsts/face_data/'+test+'_VORONOI_CORD.json', 'r')))
        for i in faces:
            progress(faces.index(i), len(faces), 'Calculating faces')
            if len(i)>2:
                fnums='f'
                faceperlist=[]
                Take=True
                for j in i:
                    if j==-1:
                        Take=False
                    else:
                        faceperlist.append(j)
                if Take==True:
                    tmpface=faceperlist
                    faceperlist=[]
                    for j in tmpface:
                        lookup='v '+str(dump[j][0])
                        append=None
                        for line in linez:
                            if lookup in line:
                                append=linez.index(line)+1
                                break
                        if append!=None:
                            faceperlist.append(append)
                        
                    for j in faceperlist:
                        if len(faceperlist)>=3:
                            fnums+=' '+str(j)
                            fnums+=' '+str(faceperlist[faceperlist.index(j)+1])
                            fnums+=' '+str(faceperlist[faceperlist.index(j)+2])
                            if faceperlist.index(j)<=len(faceperlist)-3:
                                break
                            fnums+='\nf'
                    fnums+='\n'
                    if len(fnums)>5:
                        f.write(fnums)
                    Take=False
        print('\n', end='')