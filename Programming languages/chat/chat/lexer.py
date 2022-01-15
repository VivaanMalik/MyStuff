operatorz=["ad", "mainuz", "thicc ad", "thicc mainuz", "reemendur", "paawar ston", "me haz", "no look", "ignorz", "unignorz", "vich b", "du shit", "stap shit", "?"] #             + - * / % ^ [var assigning] # [Start comment line] [End comment line] = [start loop] [end loop] :
determainerz=["smol", "bigg", "iz", "naat", "olso", "orrr..."] #               < > == ! and or
specialcharz=[",", "(", ")"]
func=['iph']
bool=["nyoo", "yass"]
def lexofy(codelist):
    totaltokenlistthing=[]
    for i in codelist:
        i=i.replace("\n", '').replace("(", " ( ").replace(")", " ) ") # optimize i
        if (len(i.replace(' ', ''))!=0 and len(i.split(' '))!=0):
            i_tokenlist=[]
            i=i.split(' ')
            while "" in i:
                i.remove("")
            j=0
            while j<len(i):
                toadd=type(i[j])
                if toadd==None: # chek if itz 2 vurdz
                    if j!=len(i)-1:
                        toadd=type(i[j]+" "+i[j+1])
                    j+=1
                if toadd==None: # now call it a var
                    j-=1
                    i_tokenlist.append(["id", i[j]])
                else:
                    i_tokenlist.append(toadd)
                j+=1
            totaltokenlistthing.append(i_tokenlist)
    return totaltokenlistthing

def type(vurdz):
    try:
        x=float(vurdz)
        return ["num", float(vurdz)]
    except:
        if vurdz[0]=="'" and vurdz[-1]=="'" or vurdz[0]=='"' and vurdz[-1]=='"':
            return ["str", vurdz[1:-2]]
        elif vurdz in bool:
            return ["bool", bool.index(vurdz)]
        elif vurdz in func:
            return ["func", vurdz]
        elif vurdz[-1] == '(':
            return ["func", vurdz.replace('(', '').replace(' ', '')],["spchr", vurdz[-1]]
        elif vurdz in specialcharz:
            return ["spchr", vurdz]
        elif vurdz in operatorz:
            return ["op", vurdz]
        elif vurdz in determainerz:
            return ["deter", vurdz]
        else:
            return None
        
