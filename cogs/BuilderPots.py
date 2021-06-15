from discord.ext import commands
import asyncio
import math
import discord
import os

class BuilderPots(commands.Cog):
    def __init__(self,bot):
        self.bot= bot


    @commands.group(name = "builderpots")
    async def builderpots(self, ctx, firstwar: float, days: float, hours: float):
    #Potions = ((length of hero upgrade) - (time remaining in 1st war after attacks) + (Time remaining in 2nd war before attacks) - 48)/9

    #define constants
        HOURS_PER_DAY = 24

    # Your calculations
        total_hours = days*HOURS_PER_DAY + hours
        potions = math.ceil(((total_hours) - (firstwar) + (4) - (48))/9)
        if potions <=0:
            potions = 0

        embed = discord.Embed(title = "Number of Potions needed for Hero Upgrades is", description = "{}".format(potions))

        await ctx.send(embed = embed)


def setup(bot):
      bot.add_cog(BuilderPots(bot))


