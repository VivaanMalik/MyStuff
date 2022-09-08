import speech_recognition as sr
import vlc
import os
import pyttsx3
from dotenv import load_dotenv
import spotipy
import re
import pafy
import requests
import urllib.parse
import urllib.request
import time
from spotipy.oauth2 import SpotifyClientCredentials
from threading import Thread

TYPE=True

playurl=''
loop = False
Instance = vlc.Instance()
player = Instance.media_player_new()

load_dotenv()
client = os.getenv('CLIENT')
secret = os.getenv('SECRET')
client_credentials_manager = SpotifyClientCredentials(client_id=client, client_secret=secret)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

run=True
recogboii = sr.Recognizer()
speakboi = pyttsx3.init()
voices = speakboi.getProperty('voices')
speakboi.setProperty('voice', voices[1].id)    

def sayy(text):
    if TYPE:
        print(text)
    else:
        speakboi.say(text)
        speakboi.runAndWait()

def LISTEN():
    if TYPE:
        x=input('Command: ')
        return x
    else:
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("JARVIS: Listening...")
            r.adjust_for_ambient_noise(source, duration=1)
            r.pause_threshold = 1
            audio=r.listen(source)
            try:    
                query = r.recognize_google(audio)
                return query.lower()
            except:
                print("Try Again")
                return None

def loopy():
    global player
    global loop
    global playurl
    while True:
        if loop==True:
            if player.get_state()!=vlc.State.Playing and player.get_state()!=vlc.State.Paused:
                Instance = vlc.Instance()
                player = Instance.media_player_new()
                Media = Instance.media_new(playurl)
                Media.get_mrl()
                player.set_media(Media)
                player.play()
                time.sleep(5)

Thread(target = loopy).start

def jarvis():
    global loop
    global player
    global playurl
    request=LISTEN()
    if request!=None:
        try:
            request=request[request.index('jarvis'):]
            print(request)
        except ValueError:
            return
        if 'play' in request[6:12]:
            request=request.replace('jarvis ', '')
            try:
                loop=False
                player.stop()
                request=request.replace('jarvis ', '')
                query=request.replace('yeet', '')
                searchUrl = urllib.request.urlopen("https://www.youtube.com/results?search_query=" + query.replace(' ', '+'))
                results = re.findall(r"watch\?v=(\S{11})", searchUrl.read().decode())
                vid=requests.get("https://www.youtube.com/watch?v=" + "{}".format(results[0]))
                url = "https://www.youtube.com/watch?v=" + "{}".format(results[0])
                video = pafy.new(url)
                yt_title = video.title
                best = video.getbestaudio()
                playurl = best.url
                Instance = vlc.Instance()
                player = Instance.media_player_new()
                Media = Instance.media_new(playurl)
                Media.get_mrl()
                player.set_media(Media)
                player.play()
                #pywhatkit.playonyt(request.replace('play', ''))
                sayy('playing '+str(yt_title))
            except ValueError:
                sayy('Slow Internet!')
        elif 'stop' in request[6:12]:
            try:
                loop=False
                player.stop()
            except:
                pass
        elif 'pause' in request[6:13]:
            try:
                player.pause()
            except:
                pass
        elif 'repeat' in request:
            loop=True
            player.pause()
            sayy('Song is now looping')
            player.play()
        elif 'volume' in request[6:14]:
            vol=int(input('volume: '))
            player.audio_set_volume(vol)
while(1):
    jarvis()
