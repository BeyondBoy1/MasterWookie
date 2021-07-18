from discord.ext import commands
import asyncio
import math
import discord
import os
from discord import Color as c

class Interview(commands.Cog):
    def __init__(self,bot):
        self.bot= bot

  #Sends Welcome and War Rules Images
    @commands.group(name = "interview")
    @commands.has_role('Elder')
    async def interview(self,ctx):
      await ctx.message.delete()
      embed = discord.Embed(title = "General Rules",description = "If you accept the following rules, react with a 👍 ")
      embed.set_image(url="https://media.discordapp.net/attachments/849131570618040360/854989465118441482/General_Rules.png")
      msg1=await ctx.send(embed=embed)
      reaction = "👍"
      await msg1.add_reaction(emoji=reaction)

      embed = discord.Embed(title = "War Rules",description = "If you accept the following rules, react with a 👍")
      embed.set_image(url="https://media.discordapp.net/attachments/849131570618040360/854989415809810462/image0.png")
      msg2=await ctx.send(embed=embed)
      reaction = "👍"
      await msg2.add_reaction(emoji=reaction)

      while True:
          try:
            reaction1, user1=await self.bot.wait_for("reaction_add")
            if str(reaction1.emoji) == "👍" and msg1.id==reaction1.message.id:
                try:
                    reaction2, user2=await self.bot.wait_for("reaction_add")
                    if str(reaction2.emoji) == "👍" and msg2.id==reaction2.message.id and user2.id==user1.id:
                        Role = discord.utils.get(user2.guild.roles, name="Briefed")
                        await user2.add_roles(Role)
                except asyncio.TimeoutError:
                    await ctx.send("Member has not been Briefed")
                    break
          except asyncio.TimeoutError:
                await ctx.send("Member has not accepted the Wookie Force Guidelines")
                break
              
def setup(bot):      
  bot.add_cog(Interview(bot))
