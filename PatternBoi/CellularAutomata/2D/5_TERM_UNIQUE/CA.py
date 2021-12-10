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
Rule='111111111111111111111111111111111'
while int(Rule, 2)<0 or int(Rule, 2)>4294967295:
    Rule=str(bin(int(input('Rule[0-4294967295]: ')))[2:])
while len(Rule)!=32:
    Rule='0'+Rule
replacement=['00000', '00001', '00010', '00011', '00100', '00101', '00110', '00111', '01000', '01001', '01010', '01011', '01100', '01101', '01110', '01111', '10000', '10001', '10010', '10011', '10100', '10101', '10110', '10111', '11000', '11001', '11010', '11011', '11100', '11101', '11110', '11111'] # up down left right center
def FindGen(rule, gen):
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
            pattern=''
            if yadd==0 :                #UP
                pattern+='0'
            else: 
                pattern+=gen[yadd-1][xadd]
            if yadd==len(gen)-1 :                #DOWN
                pattern+='0'
            else: 
                pattern+=gen[yadd+1][xadd]
            if xadd==0 :                #LEFT
                pattern+='0'
            else: 
                pattern+=gen[yadd][xadd-1]
            if xadd==len(gen)-1 :                #RIGHT
                pattern+='0'
            else: 
                pattern+=gen[yadd][xadd+1]
            pattern+=gen[yadd][xadd]
            new_gen_line+=rule[replacement.index(pattern)]
        xadd=-1
        newgen.append(new_gen_line)
    return newgen
while True:
    for i in gen:
        sys.stdout.write(i.replace('1', '█').replace('0', ' ')+'\n')
    gen=FindGen(Rule, gen)
    sys.stdout.flush()
    time.sleep(1)