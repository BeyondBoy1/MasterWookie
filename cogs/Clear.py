from discord.ext import commands
import asyncio
import discord

class Clear(commands.Cog):
    def __init__(self,bot):
        self.bot= bot
    
    @commands.command(name = "clear")
    @commands.has_role('Elder')
    async def clear(self, ctx, amount:int):
      await ctx.channel.purge(limit=amount)
       

def setup(bot):
      bot.add_cog(Clear(bot))