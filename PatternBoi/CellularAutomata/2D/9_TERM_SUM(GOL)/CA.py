import time
import sys
import random
size=0
while size<1 or size>200:
    size=int(input('Size: '))
gen=[]
add_str=''
for i in range(size):
    add_str+='0'
for i in range(size):
    gen.append(add_str)
random_1=[]
for i in range(round(size*size/5)):
    random_1.append([random.randrange(0, size-1), random.randrange(0, size-1)])
for i in random_1:
    gen[i[0]]=gen[i[0]][0:i[1]]+'1'+gen[i[0]][i[1]+1:] #sets gen [x] to gen x with replace char at y pos
def FindGen(gen):
    newgen=[]
    global replacement
    yadd=-1
    xadd=-1
    for y in gen:
        yadd+=1
        new_gen_line=''
        for x in y:
            xadd+=1
            #print('({0}, {1})'.format(xadd, yadd))
            pattern=['', '', '',
                     '', '0', '',
                     '', '', '']
            if yadd==0:
                pattern[0]='0'
                pattern[1]='0'
                pattern[2]='0'
            if yadd==len(gen)-1:
                pattern[6]='0'
                pattern[7]='0'
                pattern[8]='0'
            if xadd==0:
                pattern[0]='0'
                pattern[3]='0'
                pattern[6]='0'
            if xadd==len(gen[yadd])-1:
                pattern[2]='0'
                pattern[5]='0'
                pattern[8]='0'

            if pattern[0]=='':
                pattern[0]=gen[yadd-1][xadd-1]
            if pattern[1]=='':
                pattern[1]=gen[yadd-1][xadd]
            if pattern[2]=='':
                pattern[2]=gen[yadd-1][xadd+1]
            if pattern[3]=='':
                pattern[3]=gen[yadd][xadd-1]
            if pattern[5]=='':
                pattern[5]=gen[yadd][xadd+1]
            if pattern[6]=='':
                pattern[6]=gen[yadd+1][xadd-1]
            if pattern[7]=='':
                pattern[7]=gen[yadd+1][xadd]
            if pattern[8]=='':
                pattern[8]=gen[yadd+1][xadd+1]
            patternsum=0
            for i in pattern:
                if i == '1':
                    patternsum+=1
            if gen[yadd][xadd]=='1':
                if patternsum==2 or patternsum==3:
                    new_gen_line+='1'
                else:
                    new_gen_line+='0'
            elif gen[yadd][xadd]=='0':
                if patternsum==3:
                    new_gen_line+='1'
                else:
                    new_gen_line+='0'                
        xadd=-1
        newgen.append(new_gen_line)
    return newgen
while True:
    for i in gen:
        sys.stdout.write(i.replace('1', '█').replace('0', ' ')+'\n')
    gen=FindGen(gen)
    sys.stdout.flush()
    time.sleep(1)