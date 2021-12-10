def addobj(verts1:str, faces2:str):
    new_faces='f'
    line_count=0
    for i in verts1:
        if i.count('v')>0:
            line_count+=1
    split=faces2.replace('\n', ' \n')
    split=split.replace('f ', '')
    split=split.split(' ')
    for i in split:
        try:
            if i=='\\':
                new_faces+='\n'
                new_faces+='f'
            elif i=='n':
                pass
            else:
                new_faces+=' '
                new_faces+=str(int(i)+line_count)
        except:
            print('ohno')
    return new_faces