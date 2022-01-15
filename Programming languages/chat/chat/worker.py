import math
def workofy(listoftokenz, varlist): # varlist has var name and then same syntax as currentblock
    for i in range(len(listoftokenz)):
        j=0
        while j<len(listoftokenz[i]):
            currentblock=listoftokenz[i][j]
            if currentblock[0]=='id':
                if listoftokenz[i][j+1][1]!='vich b' or listoftokenz[i][j-1][1]!='me haz':
                    listoftokenz[i][j]=findvar(currentblock, varlist)
            j+=1
        print(listoftokenz)
        j=0
        while j < len(listoftokenz[i]):
            currentblock=listoftokenz[i][j]
            if currentblock[1]=='no look':
                break
            else:
                method=currentblock[1]
                onOperation(currentblock, listoftokenz[i], j, varlist)
            j+=1
    

def findvar(var, varlist):
    if var[0]=='id':
        finvar=[]
        finvar.append(varlist[var[1]][2])
        finvar.append(varlist[var[1]][3])
        return finvar
    else:
        return var

def changevar(var, val, varlist):
    varlist[var[1]][2]=val[0]
    varlist[var[1]][3]=val[1]

def addvar(var, varlist):
    var.append('str')
    varlist[var[1]]=var.append('')

def onOperation(currentblock, i, j, varlist):
    # op ignorz, unignorz, du shit, stap shit, ?
    # deter 
    # func iph
    if currentblock[1]=='ad':
        return sum(i[j-1], i[j+1])
    elif currentblock[1]=='mainuz':
        return sub(i[j-1], i[j+1])
    elif currentblock[1]=='thicc ad':
        return multiply(i[j-1], i[j+1])
    elif currentblock[1]=='thicc mainuz':
        return divide(i[j-1], i[j+1])
    elif currentblock[1]=='reemendur':
        return mod(i[j-1], i[j+1])
    elif currentblock[1]=='paawar ston':
        return pow(i[j-1], i[j+1])
    elif currentblock[1]=='me haz':
        addvar(i[j+1], varlist)
        return
    elif currentblock[1]=='vich b':
        changevar(i[j-1], i[j+1], varlist)
        return
    

def pow(a, b):
    return a**b

def mod(a, b):
    return a%b

def divide(a, b):
    return a/b

def multiply(a, b):
    if a[0]=='num' and b[0]!='num' or a[0]!='num' and b[0]=='num':
        finstr=''
        for i in range(math.floor(a[1])):
            finstr+=str(b[1])
        return finstr
    else:
        return a*b

def sum(a, b):
    if a[0] != 'num' or b[0] != 'num':
        return str(a)+str(b)
    else:
        return a+b

def sub(a, b):
    if a[0] != 'num' or b[0] != 'num':
        a=a[1]
        b=b[1]
        a=list(str(a))
        for i in list(str(b)):
            if i in a:
                a.remove(i)
        b=''
        for i in a:
            b+=i
        return b
    else:
        return a[1]-b[1]
