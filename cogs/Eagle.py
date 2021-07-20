from discord.ext import commands
import asyncio
import math
import discord
import os
from discord import Color as c

class Eagle(commands.Cog):
    def __init__(self,bot):
        self.bot= bot

    @commands.group(name = "ea")
    async def ea(self, ctx, level: float, troops: float, spells:float, heroes: float, siege: float):
        await ctx.message.delete()
        #define constants
        HERO = 25
        SPELLS = 5
        SIEGE_MACHINE = 1
        #Your Calculations
        total_space = troops + spells*SPELLS + heroes*HERO
      #for eagle level and troop space
        if level <= 2 and total_space >= 180:
          embed =(discord.Embed(title = "Eagle Artillery"))
          embed.add_field(name='What happens?', value= ' Eagle Artillery Activated')
          embed.set_image(url=" https://static.wikia.nocookie.net/b83200ba-a6c1-4553-82a5-060c55db7381")
          embed.set_footer(text="Command invoked by {}".format(ctx.message.author.name))
          await ctx.send(embed=embed, delete_after=5.0)
            
        #for eagle level and troop space -> no activation
        else:
          embed =(discord.Embed(title = "Eagle Artillery"))
          embed.add_field(name='What happens?', value= ' Eagle Artillery Dormant')
          embed.set_image(url="https://scontent.fblr22-1.fna.fbcdn.net/v/t31.18172-0/s640x640/21543817_1805786122779036_4806587827551608126_o.jpg?_nc_cat=106&ccb=1-3&_nc_sid=730e14&_nc_ohc=E4Uhaao9rkAAX9W-KX6&_nc_ht=scontent.fblr22-1.fna&oh=8740b5808dd1f1f8a8efb05e35ba0aba&oe=60F18550")
          embed.set_footer(text="Command invoked by {}".format(ctx.message.author.name))
          await ctx.send(embed=embed, delete_after=5.0)
        
        
def setup(bot):
      bot.add_cog(Eagle(bot))
