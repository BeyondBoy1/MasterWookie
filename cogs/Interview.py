from discord.ext import commands
import asyncio
import math
import discord
import os

class Interview(commands.Cog):
    def __init__(self,bot):
        self.bot= bot

  #Sends Welcome and War Rules Images
    @commands.group(name = "interview")
    async def interview(self,ctx):
      embed = discord.Embed(title = "General Rules",description = "React with a :thumbsup: if you've understood this")
      embed.set_image(url="https://media.discordapp.net/attachments/849131570618040360/854989465118441482/General_Rules.png")
      await ctx.send(embed=embed)

      embed = discord.Embed(title = "War Rules",description = "React with a :thumbsup: if you've understood this")
      embed.set_image(url="https://media.discordapp.net/attachments/849131570618040360/854989415809810462/image0.png")
      await ctx.send(embed=embed)

def setup(bot):
      bot.add_cog(Interview(bot))