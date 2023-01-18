import time
size=int(input('Size: '))
gen=''
for i in range(size):
    if i==round(size/2):
        gen+='1'
    else:
        gen+='0'
Rule=str(bin(int(input('Rule[0-255]: ')))[2:])
while len(Rule)!=8:
    Rule='0'+Rule
def FindNewGen(rule, oldgen:str):
    newgen=''
    rep=0
    for i in oldgen:
        if rep==0:
            pattern='0'+i+oldgen[rep+1]
        elif rep==len(oldgen)-1:
            pattern=oldgen[rep-1]+i+'0'
        else:
            pattern=oldgen[rep-1]+i+oldgen[rep+1]
        patterns=['111', '110', '101', '100', '011', '010', '001', '000']
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
    time.sleep(0.05)