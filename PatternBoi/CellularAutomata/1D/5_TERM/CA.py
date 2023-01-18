import time
size=int(input('Size: '))
gen=''
for i in range(size):
    if i==round(size/2):
        gen+='1'
    else:
        gen+='0'
Rule='111111111111111111111111111111111'
while int(Rule, 2)<0 or int(Rule, 2)>4294967295:
    Rule=str(bin(int(input('Rule[0-4294967295]: ')))[2:])
while len(Rule)!=32:
    Rule='0'+Rule
def FindNewGen(rule, oldgen:str):
    newgen=''
    rep=0
    for i in oldgen:
        if rep==0:
            pattern='00'+i+oldgen[rep+1]+oldgen[rep+2]
        if rep==1:
            pattern='0'+oldgen[rep-1]+i+oldgen[rep+1]+oldgen[rep+2]
        elif rep==len(oldgen)-2:
            pattern=oldgen[rep-2]+oldgen[rep-1]+i+oldgen[rep+1]+'0'
        elif rep==len(oldgen)-1:
            pattern=oldgen[rep-2]+oldgen[rep-1]+i+'00'
        else:
            pattern=oldgen[rep-2]+oldgen[rep-1]+i+oldgen[rep+1]+oldgen[rep+2]
        patterns=['00000', '00001', '00010', '00011', '00100', '00101', '00110', '00111', '01000', '01001', '01010', '01011', '01100', '01101', '01110', '01111', '10000', '10001', '10010', '10011', '10100', '10101', '10110', '10111', '11000', '11001', '11010', '11011', '11100', '11101', '11110', '11111']
        num=-1
        num=patterns.index(pattern)
        if num==-1:
            input('FALUIRE')
        newgen+=rule[num]
        rep+=1
    return(newgen)

while True:
    if (gen[0]=="1"):
        gen="0"+gen[1:]
    gen=FindNewGen(Rule, gen)
    print(gen.replace('1', '█').replace('0', ' ')[1:-1])
    i+=1
    time.sleep(0.25)