import discord
import os
from flask import Flask
#import keep_alive
from discord.ext.commands import Bot
from threading import Thread
from dotenv import load_dotenv
from discord_components import *

bot = Bot(command_prefix='?') 

load_dotenv()

TOKEN = os.getenv("DISCORD_TOKEN")

#define constants
MINUTES_PER_HOUR = 60
HOURS_PER_DAY = 24

@bot.event
async def on_ready():
  print(f'{bot.user} has connected to Discord!')
  DiscordComponents(bot)
  await bot.change_presence(activity = discord.Game("Clash of Clans"))
  
    #final return (always round up) 

<<<<<<< HEAD
extensions = ['cogs.CommandEvents','cogs.BuilderPots','cogs.HelpInfo','cogs.HeroTime','cogs.Interview','cogs.Form']
=======
extensions = [
    'cogs.CommandEvents', 
    'cogs.HeroTime', 
    'cogs.HelpCommands',
    'cogs.BuilderPots', 
    'cogs.Interview',
     'cogs.ClanInfo', 
     'cogs.Clear',
    'cogs.Eagle']
>>>>>>> 41836e2b72f51842080a66a6950d186165b5b785

if __name__ == '__main__':
    for ext in extensions:
        bot.load_extension(ext)

#keep_alive.keep_alive()
bot.run(TOKEN)
