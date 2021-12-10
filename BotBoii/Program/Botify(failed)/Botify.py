import os
import requests
import asyncio
from discord import FFmpegPCMAudio
from youtube_dl import YoutubeDL
from dotenv import load_dotenv
import discord
from discord.utils import get
from discord.ext import commands
from discord.voice_client import VoiceClient
import nacl
load_dotenv()
TOKEN=os.getenv('TOKEN')
bot = commands.Bot(command_prefix="-")
Mus_players={}


@bot.command()
async def say(msg, *args):
	response = ""
	for arg in args:
		response = response + " " + arg
	await msg.channel.send(response)

@bot.command()
async def hi(msg):
    await msg.channel.send('Hey...')

@bot.command()
async def yt(msg, arg):
    try:
        if os.path.isfile("song/song.mp3"):
            os.remove("song/song.mp3")
    except PermissionError:
        await msg.send('Permission error')

    
    #FFMPEG_OPTIONS = {'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5', 'options': '-vn'}
    if str(arg).startswith('https://www.youtube.com/watch?v='):
        pass
    elif str(arg).startswith('www.youtube.com/watch?v='):
        arg='https://'+arg
    else:
        await msg.channel.send('Bruh, at least send a YT link')
        return
    r = requests.get(arg)
    if "Video unavailable" in r.text:
        await msg.channel.send('Bruh, at least send a valid YT link')
        return

@bot.command()
async def leave(msg):
    if (msg.message.guild.voice_client): # If the bot is in a voice channel 
        await msg.message.guild.voice_client.disconnect() # Leave the channel

@bot.command()
async def join(msg):
    member = msg.author # Get the member by ID
    try:
        print(str(member))
        channel = member.voice.channel
        if channel: # If user is in a channel
            await channel.connect() # Connect
            await msg.send("User is connected to a channel, joining...")
        else:
            #await msg.send("I am already connected to a channel.") # If the bot is already connected
            pass
    except AttributeError:
        return await msg.send("User is not in a channel, can't connect.") # Error message

bot.run(TOKEN)