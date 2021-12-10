import utils
import os
def findpoint(xy1:tuple, xy2:tuple, k:float):
    # Formula for point in line iz =   (x, y) = (x1 + k(x2 - x1), y1 + k(y2 - y1)
    return (xy1[0] + (k*(xy2[0] - xy1[0])), xy1[1] + (k*(xy2[1] - xy1[1])))
def find_3d_point(xyz1:tuple, xyz2:tuple, xyz3:tuple, k:float): #xyz1 iz clozest point, xyz2 iz flat point on sem level height az xyz1, xyz3 is vertically on xyz1
    x=findpoint((xyz1[0], xyz1[2]), (xyz2[0], xyz2[2]), k)[0]
    z=findpoint((xyz1[0], xyz1[2]), (xyz2[0], xyz2[2]), k)[1]
    y=findpoint((xyz1[0], xyz1[1]), (xyz3[0], xyz3[1]), k)[1]
    return (x, y, z)
def genwall(faces:list, verts:str, debug):
    #gen verts, add faces with utils return both
    newverts=[]
    verts=verts.split('\n')
    verts.pop(len(verts)-1)
    for i in faces:
        newverts.append(verts[i-1].split(' '))
    for i in range(0, len(newverts)):
        lenverts=len(newverts[i])
        j=0
        while j<lenverts:
            if newverts[i][j].find('v')!=-1:
                newverts[i].pop(j)
                lenverts-=1
            newverts[i][j]=float(newverts[i][j])
            j+=1
        newverts[i]=tuple(newverts[i])
    oldverts=newverts
    newverts=[find_3d_point(oldverts[0], oldverts[1], oldverts[3], .25), 
            find_3d_point(oldverts[1], oldverts[0], oldverts[2], .25), 
            find_3d_point(oldverts[3], oldverts[2], oldverts[0], .25),
            find_3d_point(oldverts[2], oldverts[3], oldverts[1], .25)]
    glassface=utils.addobj(verts, 'f 1 2 4 3\n')
    tmpglassface_seperated=glassface.replace('f ', '').replace('\n', '').split(' ')
    vert=''
    for i in newverts:
        vert+='v {0} {1} {2}\n'.format(i[0], i[1], i[2])
    face='f {0} {1} {2} {3}\nf {4} {5} {6} {7}\nf {8} {9} {10} {11}\nf {12} {13} {14} {15}\n'.format(
        faces[0], faces[1], tmpglassface_seperated[1], tmpglassface_seperated[0],
        faces[2], faces[3], tmpglassface_seperated[3], tmpglassface_seperated[2],
        faces[0], faces[3], tmpglassface_seperated[3], tmpglassface_seperated[0],
        faces[2], faces[1], tmpglassface_seperated[1], tmpglassface_seperated[2]
    )
    return vert, face, glassface
def gen(shape:list, h, theme, detail):
    # shape haz da marked pozitions
    # h menz da height 
    # theme repreezent da... well theme (bricks, stone... bleh bleh bleh)
    floor=1
    objfaces='usemtl {0}\n'.format(theme[0])
    objvertices=''
    for i in range(round(h/floor)+1):
        for j in shape:
            objvertices+= 'v {0} {1} {2}\n'.format(str(j[0]), str((i*floor)), str(j[1]))
    glassfaces=''
    floorno=0    
    for i in range(len(shape)):
        for j in range(round(h/floor)):
            item_no=(i*round(h/floor))+j+1
            groundfloor= 0#Change to 0
            if item_no%len(shape)!=0:
                if floorno!=groundfloor:
                    vert, face, glassface=genwall([item_no, item_no+1, item_no+len(shape)+1, item_no+len(shape)], objvertices, 1)
                    objfaces+=face
                    objvertices+=vert
                    glassfaces+=glassface
                else:
                    objfaces+='f {0} {1} {2} {3}\n'.format(item_no, item_no+1, item_no+len(shape)+1, item_no+len(shape))
            else:
                if floorno!=groundfloor:
                    vert, face, glassface=genwall([item_no, item_no-len(shape)+1, item_no+1, item_no+len(shape)], objvertices, 0)
                    objvertices+=vert
                    objfaces+=face
                    glassfaces+=glassface
                else:
                    objfaces+='f {0} {1} {2} {3}\n'.format(item_no, item_no-len(shape)+1, item_no+1, item_no+len(shape))
                floorno+=1
    objfaces+='f '
    for i in range(len(shape)):
        objfaces+=str((len(shape)*h)+1+i)+' '
    objfaces+='\nusemtl {0}\n'.format(theme[1])
    objfaces+=glassfaces
    with open('tmp.obj', 'w+') as f:
        f.write('mtllib mtl.mtl\no tst\n')
        f.write(objvertices)
        f.write(objfaces)
    os.system('start .\\tmp.obj')
    return objvertices, objfaces

#   gen([(10, 10), (10, 20), (15, 25), (20, 20), (20, 10)], 1000, ['brick', 'glass'], 0.5)
