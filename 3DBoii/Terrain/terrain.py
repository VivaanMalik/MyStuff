import noise
import sys
def progress(count, total, status=''):
    total-=1
    bar_len = 69
    filled_len = int(round(bar_len * count / float(total)))

    percents = round(100.0 * count / float(total), 1)
    bar = 'e' * filled_len + ' ' * (bar_len - filled_len)

    sys.stdout.write('y%st %s%s | %s out of %s parts | %s\r' % (bar, percents, '%', str(count), str(total), status))
    sys.stdout.flush()
size=int(input('Size of terrain (m): '))
Suffix=input('Suffix: ')
x=0
y=0
perlin=[]
while x<=size:
    perlin_add=[]
    progress(x, size, 'Generating Perlin Noise...')
    while y<=size:
        perlin_add.append(str(-100*noise.pnoise2(x/100, y/100, octaves=6, persistence=0.5, lacunarity=2, repeatx=size, repeaty=size, base=0)))
        y+=1
    perlin.append(perlin_add)
    y=0
    x+=1
print('\n')
with open('Model/Terrain_'+Suffix+'_'+str(size)+'.obj', 'w+') as f:
    f.write('mtllib 0_MTL.mtl\no terrain_num_'+Suffix+'\n')
    x=0
    y=0
    vnum=0
    ice_v=[]
    while x<=size:
        progress(x, size, 'Generating Vertices...')
        while y<=size:
            vnum+=1
            if (float(perlin[x][y])>17):
                ice_v.append(vnum)
            f.write('v '+str(x)+' '+perlin[x][y]+' '+str(y)+'\n')
            #f.write('v '+str(x)+' 0 '+str(y)+'\n')
            y+=1
        y=0
        x+=1
    print('\n')
    x=0
    y=0
    f.write('v 0 -10 0\nv 0 -10 {0}\nv {0} -10 0\nv {0} -10 {0}\n'.format(size))
    f.write('o surface\nusemtl ghass\ns 1\n')
    startingnum=1
    ice_f=[]
    while x<size:
        progress(x, size, 'Generating Faces...')
        while y<=size:
            if startingnum%(size+1)==0:
                f.write('#f {0} {1} {2} {3}\n'.format(startingnum, startingnum+1, startingnum+size+2, startingnum+size+1))
            else:
                if startingnum in ice_v or (startingnum+1) in ice_v or (startingnum+size+2) in ice_v or (startingnum+size+1) in ice_v:
                    ice_f.append('f {0} {1} {2} {3}\n'.format(startingnum, startingnum+1, startingnum+size+2, startingnum+size+1))
                else:
                    f.write('f {0} {1} {2} {3}\n'.format(startingnum, startingnum+1, startingnum+size+2, startingnum+size+1))
            startingnum+=1
            y+=1
        y=0
        x+=1
    print('\n')
    if len(ice_f)>0:
        f.write('usemtl snow\ns 2\n')
        for i in ice_f:
            f.write(i)
            progress(ice_f.index(i), len(ice_f)-1, 'Generating snow...')
    print('\n')
    f.write('o water\nusemtl water\ns 3\n')
    f.write('f -1 -2 -4 -3')
    print("DONE")