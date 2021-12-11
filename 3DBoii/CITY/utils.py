def addobj(verts1:str, faces2:str):
    new_faces='f'
    line_count=0
    for i in verts1:
        if i.count('v')>0:
            line_count+=1
    split=faces2.replace('\n', ' \n')
    split=split.replace('f ', '')
    split=split.split(' ')
    for i in range(len(split)):
        item=split[i]
        try:
            if item=='\n':
                new_faces+='\n'
                if i!=len(split)-1:
                    new_faces+='f'
            else:
                new_faces+=' '
                new_faces+=str(int(item)+line_count)
        except:
            print('ohno')
    return new_faces

def formatface(face:str, facesnum):
    face=face.replace('f ', '').replace('\n', '').split(' ') #get numbers
    finafaces=''
    repeatnum=facesnum-2
    for i in range(len(face)-(facesnum-1)):
        if face[i+(facesnum-1)]=='':
            finafaces+='f'
            for j in range(facesnum-1):
                finafaces+=' {0}'.format(face[i+j])
            finafaces+=' '+str(face[0])
            finafaces+='\n'
            break
        else:
            finafaces+='f'
            for j in range(facesnum):
                finafaces+=' {0}'.format(face[i+j])
            finafaces+='\n'
            #finafaces+='f {0} {1} {2}\n'.format(face[i], face[i+1], face[i+2])
    face=face[:-1]
    x=len(face)-(facesnum-2)
    for i in range(repeatnum):
        finafaces+='f'
        if x+j+i>=len(face):
            x-=len(face)
        for j in range(facesnum):
            finafaces+=' {0}'.format(face[x+j+i])
        finafaces+='\n'
    return finafaces