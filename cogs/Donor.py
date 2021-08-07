import asyncio
from discord.ext import commands
import discord
from discord import Color as c
import datetime

class Donor(commands.Cog):
  def __init__(self,bot):
    self.bot = bot
    self._donate_message = None

  @commands.group(name="req")
  async def req(self, ctx,clan: str, troops: str, spells: str, siege: str):
    await ctx.message.delete()
    embed =(discord.Embed(title = "Donation", description = "", color = c.blue()))
    embed.add_field(name='Requests', value= 'For: **{}** | Troops: {} | Spells: {} | Siege: {}'.format (clan, troops, spells, siege, inline=False))
    embed.set_footer(text="Command invoked by {}".format(ctx.message.author.name))
    embed.timestamp=datetime.datetime.utcnow()
    message = await ctx.send(embed=embed)
    
    while True:
      try:
        reaction, user = await self.bot.wait_for("reaction_add")
        if str(reaction.emoji) == "✅" and message.id==reaction.message.id:
          await message.delete()
      except asyncio.TimeoutError:
        await ctx.send("Timed Out")
        break

def setup(bot):
    bot.add_cog(Donor(bot))

