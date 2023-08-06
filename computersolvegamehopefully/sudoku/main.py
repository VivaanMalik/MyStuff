from PIL import ImageGrab, Image, ImageFilter
import numpy as np
import pytesseract
import time
import copy
import pyautogui
import cv2
import imutils

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

time.sleep(0.5)

startx=303
starty=313
size=534
sizeoffset=5

pyautogui.hotkey('alt', 'tab')
time.sleep(1)
pic = ImageGrab.grab(bbox=(startx, starty, startx+size, startx+size))
pyautogui.hotkey('alt', 'tab')

boxes=[[0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0]]

boxes_raw=[[0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0]]

possible_values=[["", "", "", "", "", "", "", "", ""],
                 ["", "", "", "", "", "", "", "", ""],
                 ["", "", "", "", "", "", "", "", ""],
                 ["", "", "", "", "", "", "", "", ""],
                 ["", "", "", "", "", "", "", "", ""],
                 ["", "", "", "", "", "", "", "", ""],
                 ["", "", "", "", "", "", "", "", ""],
                 ["", "", "", "", "", "", "", "", ""],
                 ["", "", "", "", "", "", "", "", ""]]

def loadboxes(pic:Image):
    for y in range(9):
        for x in range(9):
            img = pic.crop((round(x/9*size), round(y/9*size), round(x/9*size) + round(size/9), round(y/9*size) + round(size/9)))
            img=img.crop((sizeoffset, sizeoffset, img.size[0]-sizeoffset, img.size[1]-sizeoffset))

            img=img.filter(ImageFilter.GaussianBlur(radius = 1))
            for _i in range(2):
                img=img.filter(ImageFilter.SHARPEN)
            img=img.resize((100, 100), Image.LANCZOS)
            img=img.filter(ImageFilter.MinFilter(size=3))
            img=img.convert("L")
            img=img.point(lambda p: 255 if p > 128 else 0)
            img=img.convert("1")
            img.save("Images\\"+str(x)+str(y)+".png")
        
        
            number =  pytesseract.image_to_string(np.array(img), config="--psm 10", lang='eng')

            boxes_raw[y][x]=number
            if number[0] in "123456789SaQgAG":
                boxes[y][x]="-"+number[0].replace("a", "0").replace("S", "3").replace("Q", "9").replace("g", "9").replace("A", "4").replace("G", "5")
                if boxes[y][x]=="-0":
                    boxes[y][x]=0
            else:
                boxes[y][x]=0
            possible_values[y][x]=str(boxes[y][x]).replace("-", "").replace("0", "")
    print("\n\npuzzle:")

def verify(boxes):
    for y in range(9):
        count=[0, 0, 0, 0, 0, 0, 0, 0, 0]
        for x in range(9):
            if boxes[y][x]!=0:
                count[abs(int(boxes[y][x]))-1]+=1
        for i in count:
            if i>1:
                print(count)
                return False
    
    for x in range(9):
        count=[0, 0, 0, 0, 0, 0, 0, 0, 0]
        for y in range(9):
            if boxes[y][x]!=0:
                count[abs(int(boxes[y][x]))-1]+=1
        for i in count:
            if i>1:
                print(count)
                return False

    for y in range(0, 9, 3):
        for x in range(0, 9, 3):
            count=[0, 0, 0, 0, 0, 0, 0, 0, 0]
            for _y in range(3):
                for _x in range(3):
                    if boxes[y+_y][x+_x]!=0:
                        count[abs(int(boxes[y+_y][x+_x]))-1]+=1
            for i in count:
                if i>1:
                    print(count)
                    return False
    return True

def prettyprintsudoku(boxes, highlightcell=None):
    suffix="\033[0m"
    grey="\033[30m"
    red="\033[31m"
    green="\033[32m"
    yellow="\033[33m"
    blue="\033[34m"
    purple="\033[35m"
    cyan="\033[36m"
    white="\033[37m"

    highlight_line=purple
    normal_line=grey
    prewritten_number=blue
    written_number=white
    highlighted_cell=green
    wrongcell=red

    isvalid = verify(boxes)

    linecount = 0
    while True:
        line=""
        if linecount%2==0:
            line="+---+---+---+---+---+---+---+---+---+"
            if linecount%6==0:
                line=highlight_line+line+suffix
            else:
                line=highlight_line+"+"+suffix+normal_line+"---+---+---"+highlight_line+"+"+suffix+normal_line+"---+---+---"+highlight_line+"+"+suffix+normal_line+"---+---+---"+highlight_line+"+"+suffix
        else:
            charcount=0
            while True:
                if charcount%2==1:
                    line+=" "
                elif charcount%12==0:
                    line+=highlight_line+"|"+suffix
                elif charcount%4==0:
                    line+=normal_line+"|"+suffix
                else:
                    c = int(boxes[int((linecount-1)/2)][int((charcount-2)/4)])
                    if c<0:
                        line+=prewritten_number+str(c).replace("-", "")+suffix
                    elif c==0:
                        line+=" "
                    else:
                        if highlightcell!=None:
                            if highlightcell[1]==int((linecount-1)/2) and highlightcell[0]==int((charcount-2)/4):
                                if isvalid:
                                    line+=highlighted_cell+str(c)+suffix 
                                else:
                                    line+=wrongcell+str(c)+suffix
                            else:                          
                                line+=written_number+str(c)+suffix
                        else:                          
                            line+=written_number+str(c)+suffix
                charcount+=1
                if charcount==37:
                    break
        print(line)
        linecount+=1
        if linecount==19:
            break
    if not isvalid:
        input("")

def fillpossibiltygrid(boxes):
    maxpossibilities=1

    #lone number
    for y in range(9):
        for x in range(9):
            if boxes[y][x]==0:
                possibilities="123456789"

                for _x in boxes[y]:
                    possibilities=possibilities.replace(str(_x).replace("-", ""), "")

                for _y in boxes:
                    possibilities=possibilities.replace(str(_y[x]).replace("-", ""), "")

                for _y in range((y//3)*3, (y//3)*3+3):
                    for _x in range((x//3)*3, (x//3)*3+3):
                        possibilities=possibilities.replace(str(boxes[_y][_x]).replace("-", ""), "")                    

                if len(possibilities)==1:
                    boxes[y][x]=possibilities
                    print("Only possible number")
                    prettyprintsudoku(boxes, (x, y))
                
                possible_values[y][x]=possibilities

    for y in range(9):
        count=[0, 0, 0, 0, 0, 0, 0, 0, 0]
        last=[0, 0, 0, 0, 0, 0, 0, 0, 0]

        obviouspairstuff=[]
        hiddenpairstuff=[]

        for x in range(9):
            #last remaining cell
            if boxes[y][x]==0:
                for i in possible_values[y][x]:
                    if count[int(i)-1]!=-1:
                        count[int(i)-1]+=1
                        last[int(i)-1]=x
            else:
                count[int(abs(int(boxes[y][x])))-1]=-1

            if x!=8:
                for x2 in range(x+1, 9):
                    #obvious pair
                    if len(possible_values[y][x])==2 and possible_values[y][x]==possible_values[y][x2]:
                        obviouspairstuff.append((possible_values[y][x], x, x2, y))

                    #hidden pair
                    else:
                        p=''.join(set(possible_values[y][x]).intersection(possible_values[y][x2]))
                        if len(p)!=2:
                            break
                        hiddenpair=True
                        for i in range(9):
                            if i!=x and i!=x2:
                                if len(''.join(set(p).intersection(possible_values[y][i])))!=0:
                                    hiddenpair=False
                        if hiddenpair:
                            hiddenpairstuff.append((x, x2, y))

        for i in range(9):
            if count[i]==1:
                boxes[y][last[i]]=str(i+1)
                possible_values[y][last[i]]=str(i+1)
                print(count)
                print(f"Only possible position in row")
                prettyprintsudoku(boxes, (last[i], y))
        
        for i in obviouspairstuff:
            for j in range(9):
                if j!=i[1] and j!=i[2]:
                    print(f"Obvious pairs in row {i[3]}: ({i[0][0]}, {i[0][1]})")
                    possible_values[i[3]][j].replace(i[0][0], "").replace(i[0][1], "")
                    prettyprintsudoku(boxes)
        
        for i in hiddenpairstuff:
            p = ''.join(set(possible_values[y][i[0]]).intersection(possible_values[y][i[1]]))
            print(f"Hidden pairs in row {i[2]}: ({p[0]}, {p[1]})")
            possible_values[i[2]][i[0]]=p
            possible_values[i[2]][i[1]]=p
            prettyprintsudoku(boxes)


    for x in range(9):
        count=[0, 0, 0, 0, 0, 0, 0, 0, 0]
        last=[0, 0, 0, 0, 0, 0, 0, 0, 0]

        obviouspairstuff=[]
        hiddenpairstuff=[]

        for y in range(9):
            #last remaining cell
            if boxes[y][x]==0:
                for i in possible_values[y][x]:
                    if count[int(i)-1]!=-1:
                        count[int(i)-1]+=1
                        last[int(i)-1]=y
            else:
                count[int(abs(int(boxes[y][x])))-1]=-1
        
            if y!=8:
                for y2 in range(y+1, 9):
                    #obvious pair
                    if len(possible_values[y][x])==2 and possible_values[y][x]==possible_values[y2][x]:
                        obviouspairstuff.append((possible_values[y][x], y, y2, x))

                    #hidden pair
                    else:
                        p=''.join(set(possible_values[y][x]).intersection(possible_values[y2][x]))
                        if len(p)!=2:
                            break
                        hiddenpair=True
                        for i in range(9):
                            if i!=y and i!=y2:
                                if len(''.join(set(p).intersection(possible_values[i][x])))!=0:
                                    hiddenpair=False
                        if hiddenpair:
                            hiddenpairstuff.append((y, y2, x))
                        
        for i in range(9):
            if count[i]==1:
                boxes[last[i]][x]=str(i+1)
                possible_values[last[i]][x]=str(i+1)
                print(count)
                for j in possible_values:
                    print(j)
                print(f"Only possible position in column")
                prettyprintsudoku(boxes, (x, last[i]))
        
        for i in obviouspairstuff:
            for j in range(9):
                if j!=i[1] and j!=i[2]:
                    print(f"Obvious pairs in column {i[3]}: ({i[0][0]}, {i[0][1]})")
                    possible_values[j][i[3]].replace(i[0][0], "").replace(i[0][1], "")
                    prettyprintsudoku(boxes)
        
        for i in hiddenpairstuff:
            p = ''.join(set(possible_values[i[0]][x]).intersection(possible_values[i[1]][x]))
            print(f"Hidden pairs in column {i[2]}: ({p[0]}, {p[1]})")
            possible_values[i[0]][i[2]]=p
            possible_values[i[1]][i[2]]=p
            prettyprintsudoku(boxes)


    for y in range(0, 9, 3):
        for x in range(0, 9, 3):
            count=[0, 0, 0, 0, 0, 0, 0, 0, 0]
            last=[0, 0, 0, 0, 0, 0, 0, 0, 0]

            obviouspairstuff=[]
            hiddenpairstuff=[]

            for _y in range(3):
                for _x in range(3):
                    #last remaining cell
                    if boxes[y+_y][x+_x]==0:
                        for i in possible_values[y+_y][x+_x]:
                            if count[int(i)-1]!=-1:
                                count[int(i)-1]+=1
                                last[int(i)-1]=_y*3+_x
                    else:
                        count[int(abs(int(boxes[y+_y][x+_x])))-1]=-1
                    
                    if not (_y==2 and _x==2):
                        for _y2 in range((_y if _x!=2 else _y+1), 3):
                            for _x2 in range(_x+1, 3):
                                #obvious pair
                                if len(possible_values[y+_y][x+_x])==2 and possible_values[y+_y][x+_x]==possible_values[y+_y2][x+_x2]:
                                    obviouspairstuff.append((possible_values[y+_y][x+_x], (x+_x, y+_y), (x+_x2, y+_y2), (x, y)))
                                
                                # #hidden pair
                                # else:
                                #     p=''.join(set(possible_values[y+_y][x+_x]).intersection(possible_values[y+_y2][x+_x2]))
                                #     print("p")
                                #     print(p)
                                #     if len(p)==2:
                                #         hiddenpair=True
                                #         for j in range(3):
                                #             for k in range(3):
                                #                 if j!=_y and j!=_y2 and k!=_x and k!=_x2:
                                #                     if len(''.join(set(p).intersection(possible_values[y+j][x+k])))!=0:
                                #                         hiddenpair=False
                                #         if hiddenpair:
                                #             print("hiddepair")
                                #             print(f'{x+_x}, {y+_y}')
                                #             print(f'{x+_x2}, {y+_y2}')
                                #             hiddenpairstuff.append((copy.deepcopy((_x, _y)), copy.deepcopy((_x2, _y2)) , p))

            for i in range(9):
                if count[i]==1:
                    boxes[y+(last[i]//3)][x+(last[i]%3)]=str(i+1)
                    possible_values[y+(last[i]//3)][x+(last[i]%3)]=str(i+1)
                    print(count)
                    print(f"Only possible position in block")
                    prettyprintsudoku(boxes, (x+(last[i]%3), y+(last[i]//3)))
            
            for i in obviouspairstuff:
                for j in range(3):
                    for k in range(3):
                        xval = i[3][0]+j
                        yval = i[3][1]+k
                        if xval!=i[1][0] and xval!=i[2][0] and yval!=i[1][1] and yval!=i[2][1]:
                            print(f"Obvious pairs in block ({i[3][0]}, {i[3][1]}): ({i[0][0]}, {i[0][1]})")
                            possible_values[i[3][0]][i[3][1]].replace(i[0][0], "").replace(i[0][1], "")
                            prettyprintsudoku(boxes)
            
            # for i in hiddenpairstuff:
            #     p = i[2]
            #     print(f"Hidden pairs in block ({x//3}, {y//3}): ({p[0]}, {p[1]})")
            #     possible_values[y+i[0][1]][x+i[0][0]]=p
            #     possible_values[y+i[1][1]][x+i[1][0]]=p
            #     prettyprintsudoku(boxes)

    for y in range(9):
        for x in range(9):
            maxpossibilities=max(maxpossibilities, len(possible_values[y][x]))

    return maxpossibilities

def solvesudoku(boxes):
    while True:
        old=copy.deepcopy(possible_values)
        maxpossibilities=fillpossibiltygrid(boxes)
        # print(maxpossibilities)
        if maxpossibilities==1:
            print("hopefully solved???")
            return
        if old==possible_values:
            print("too dumb")
            return
        old=copy.deepcopy(possible_values)

def typeitin(boxes):
    pyautogui.hotkey('alt', 'tab')
    time.sleep(0.01)
    for y in range(9):
        for x in reversed(range(9)) if y%2==1 else range(9):
            if str(boxes[y][x])[0]!="-":
                pyautogui.press(str(boxes[y][x]))
            if boxes[y][x]==0:
                pyautogui.press("shift")
                for i in possible_values[y][x]:
                    pyautogui.press(i)
                pyautogui.press("shift")
            if y%2==1:
                pyautogui.press("left")
            else:
                pyautogui.press("right")
        pyautogui.press("down")

loadboxes(pic)
prettyprintsudoku(boxes)
solvesudoku(boxes)
prettyprintsudoku(boxes)
typeitin(boxes)

print("\nboxes raw:")
for i in boxes_raw:
    print(i)
print("\nboxes:")
for i in boxes:
    print(i)
print("\npossible values:")
for i in possible_values:
    print(i)

# print("\n")
# for i in boxes:
#     print(i)

pic.show()