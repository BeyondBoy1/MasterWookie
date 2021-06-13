# bot.py
import os
import discord
import math
from discord import message
from discord.ext.commands import Bot
from discord.ext.commands.core import check
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

bot = Bot(command_prefix='?') 

@bot.event
async def on_ready():
    print(f'{bot.user} has connected to Discord! Yay!')

#define constants
HOURS_PER_DAY = 24

@bot.command()
async def hero(ctx, days: float, hours:float, potions: float):

    # Your calculations
    total_hours = days*HOURS_PER_DAY + hours
    total_potion_hours = potions*9 
    final_upgrade = (total_hours) - (total_potion_hours) 
    #print("final upgrade= ", final_upgrade)
    if final_upgrade >= 24:
        final_days = final_upgrade // 24
        #print("final days = ", final_days)
        final_hours = (final_upgrade) - final_days*24
        #print("final hours= ", final_hours)
    else:
        final_days = 0
        final_hours = final_upgrade

    await ctx.send(f"Total hours for Hero Upgrades is {final_days} d, {final_hours} hr" )

#Hero conversion
while True:
    try:
        #days=int(input("Enter number of days for hero upgrade: "))
        #print("Number of days: ", days)
        #hours=int(input("Enter number of hours for hero upgrade: "))
        #print("Number of hours: ", hours)
        break;
    except ValueError:
        print("Invalid Input")

#total_hours = total_hours + hours
#print("Total hours for Hero Upgrades ", total_hours)

#Potion conversion
while True:
    try:
        #potions = int(input("How many builder potions do you want to use?"))
        #print("Number of potions: ", potions)
        break;
    except ValueError:
        print("Invalid Input")

#total_potion_hours = potions * 10 - potions
#print("total potion hours = ",total_potion_hours)

#Final calculation
#final_upgrade = total_hours - total_potion_hours
    #print("final upgrade= ", final_upgrade)
#if final_upgrade >= 24:
    #final_days = final_upgrade // 24
    #print("final days = ", final_days)
    #final_hours = final_upgrade - final_days*24
    #print("final hours= ", final_hours)
#print("Amount of time your hero upgrades will take: %sd %sh"% (final_days, final_hours))

bot.run(TOKEN)
