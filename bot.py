#memeBot
import os
import discord
from dotenv import load_dotenv
from discord.ext import commands
from discord.utils import get
load_dotenv()
token = os.getenv('DISCORD_TOKEN')
bot = commands.Bot(command_prefix= '?')
songFileName = 0
sounds = ["ohnono","etu","bruh","omgwow","tbc","jesus"]

@bot.command(name ='play', help = '?play [sound name] to play sounds from the list')
async def Play(ctx,*args):
    songFileName = "0"
    commandInput = str(args[0])
    print(commandInput)
    voice = get(bot.voice_clients,guild= ctx.guild)
    #if already connected it will not join again
    if voice and voice.is_connected():
        print("Bot already connected")
    else:
        if ctx.author.voice and ctx.author.voice.channel:
            channel = ctx.author.voice.channel
            voice = await channel.connect()
        else:
            await ctx.send("sadKek. You are not connected to a voice channel")
            return


    for index,sound in enumerate(sounds):
        if sound == commandInput or str(index + 1) == commandInput:
            songFileName = sounds[index] + ".mp3"

    print(songFileName)
    songFileExist = os.path.exists("sounds/"+songFileName)
    print(songFileExist)
    if songFileExist:
        await ctx.send(f"playing {songFileName}")
        finishPlayMessage = songFileName + " has finished playing!"
        voice.play(discord.FFmpegPCMAudio("sounds/"+songFileName)
        ,after= lambda e:print(finishPlayMessage))
    else:
        print("Got unknown error, file not found")

@bot.command(name = 'list',help = 'list the sound commands')
async def List(ctx):
    ListStr = ""
    for index,sound in enumerate(sounds):
        ListStr += str(index+1) + " - " + sound +"\n"
    await ctx.send(ListStr)

@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')
    
@bot.event
async def on_disconnect():
    print("disconnected from discord")

bot.run(token)