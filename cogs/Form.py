from discord.ext import commands
import asyncio
import math
import discord
import os
from discord_components import *

class Form(commands.Cog):
    def __init__(self,bot):
        self.bot= bot
    @commands.group(name = "wow",description="new feature")
    async def wow(self, ctx):
        await ctx.send('This is new to discord',
                       components=[
                           Select(placeholder='Select something!',options=[SelectOption(label='Time',value='second')])
    ])

def setup(bot):
    bot.add_cog(Form(bot))
