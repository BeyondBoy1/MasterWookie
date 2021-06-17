from discord.ext import commands
import math
import discord
import os


class HeroTime(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.group(name="herotime")
    async def herotime(self, ctx, days: float, hours: float, potions: float):

        #define constants
        HOURS_PER_DAY = 24
        MINUTES_PER_HOUR = 60
        #Your Calculations
        total_hours = days * HOURS_PER_DAY + hours
        total_potion_hours = potions * 9
        #if check for potion hours > upgrade
        if potions * 10 > total_hours:
            leftover_potion = (potions * 10 - total_hours) / 10
            leftover_days = leftover_potion // 24
            leftover_hours = math.floor(leftover_potion % 24)
            leftover_minutes = (leftover_potion - leftover_days * 24 -
                                leftover_hours) * MINUTES_PER_HOUR
            upgrade_time = total_hours / 10

        #amount of time in hours that hero upgrades will take after applying potions
        else:
            upgrade_time = (total_hours) - (total_potion_hours)
            leftover_potion = 0
            leftover_days = leftover_potion // 24
            leftover_hours = math.floor(leftover_potion % 24)
            leftover_minutes = (leftover_potion - leftover_days * 24 -
                                leftover_hours) * MINUTES_PER_HOUR

        #convert from hours to days, hours, minutes
        final_days = upgrade_time // 24
        final_hours = math.floor(upgrade_time % 24)
        final_minutes = (upgrade_time - final_days * 24 -
                         final_hours) * MINUTES_PER_HOUR

        embed = (discord.Embed(
            title="HeroTime upgrade and Remaining Builder Pot",
            description=""))
        embed.add_field(name='Time Remaining for your Heroes to be up',
                        value='{}d {}h {}m'.format(final_days,
                                                   final_hours,
                                                   final_minutes,
                                                   inline=True))
        embed.add_field(name='Amount of time left on Builder potions',
                        value='{}d {}h {}m'.format(leftover_days,
                                                   leftover_hours,
                                                   leftover_minutes,
                                                   inline=True))

        await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(HeroTime(bot))
