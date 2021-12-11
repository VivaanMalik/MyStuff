import keyboard
from pynput.keyboard import Key, Controller
import unicodedata
import random
import pyperclip
import subprocess
from ahk import AHK
ahk = AHK()
kb=Controller()
ordthing=0
char_limit=50
valid_keys=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '2', '3', '4', '5', '6', '7', '8', '9', '~', '!', '^', '&', '*', '(', ')', '-', '_', '=', '+', '{', '}', '\\', ':', ';', "'", '<', '>', ',', '.', '?', '/']
TOCOPY=''
Pause=False
def Press(key):
    global TOCOPY
    global Pause
    if key.name=='esc':
        Pause=True
    if keyboard.is_pressed('ctrl'):
        return
    if keyboard.is_pressed('shift'):
        if key.name=='esc':
            Pause=False
            return
    if Pause:
        return
    code_key=key.name
    if key.name=='space':
        kb.press(Key.backspace)
        kb.release(Key.backspace)
        keyboard.write('  ')
        return
    if code_key in valid_keys:
        pass
    else:
        return
    try:
        ordthing=ord(code_key)
    except:
        try:
            ordthing=ord(unicodedata.lookup(code_key))
        except:
            return
    unicode=hex(ordthing)
    unicode='00'+str(unicode)[2:]
    unicode=unicode.upper()
    with open('confooz.txt', encoding='utf-8') as f:
        lines=f.readlines()
        lolsaid=False
        OPLINES=[]
        for i in lines:
            #if i[8:12]==unicode or i[9:13]==unicode:
            if unicode+' ;' in i[6:17]:
                OPLINES.append(lines.index(i))
                lolsaid=True
        if not lolsaid:
            print(ordthing)
            print(unicode)
        LETTERUNICODELINE=lines[OPLINES[random.randrange(0, len(OPLINES))]]
        LETTERUNICODE=u''
        for i in LETTERUNICODELINE:
            if i ==';':
                break
            LETTERUNICODE+=i
        LETTERUNICODE=LETTERUNICODE[:-1]
        kb.press(Key.backspace)
        kb.release(Key.backspace)
        TOCOPY=chr(int('0x'+LETTERUNICODE, 0))
        keyboard.write(TOCOPY)
keyboard.on_release(callback=Press)
keyboard.wait()

