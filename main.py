import discord
import os
from flask import Flask
#import keep_alive
from discord.ext.commands import Bot
from threading import Thread
from dotenv import load_dotenv


bot = Bot(command_prefix='?') 

load_dotenv()

TOKEN = os.getenv("DISCORD_TOKEN")

#define constants
MINUTES_PER_HOUR = 60
HOURS_PER_DAY = 24

@bot.event
async def on_ready():
  print(f'{bot.user} has connected to Discord!')
  await bot.change_presence(activity = discord.Game("Clash of Clans"))
  
    #final return (always round up) 

extensions = ['cogs.CommandEvents','cogs.BuilderPots','cogs.HelpInfo','cogs.HeroTime','cogs.Interview']

if __name__ == '__main__':
    for ext in extensions:
        bot.load_extension(ext)

#keep_alive.keep_alive()
bot.run(TOKEN)
