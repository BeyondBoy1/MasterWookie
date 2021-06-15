from discord.ext import commands
import asyncio
import discord

class HelpInfo(commands.Cog):
    def __init__(self,bot):
        self.bot= bot
    
    @commands.command(name = "herotimehelp")
    async def herotimehelp(self, ctx):
        embed = discord.Embed(title = " ?herotime help",description = "Bot Command = ?herotime ")
        embed.set_image(url="https://wallpapercave.com/wp/wp2424065.jpg")

        embed.add_field(name='1st parameter', value = ' Days on hero upgrade', inline=True )
        embed.add_field(name='2nd parameter', value = ' Hours on hero upgrade', inline=True )
        embed.add_field(name='3rd parameter', value = 'Intended # of potions to use', inline=True )
        embed.add_field(name='Syntax', value = '?herotime  2 12 3 ', inline=False )

        await ctx.send(embed=embed)

    
    @commands.command(name = "builderpotshelp")
    async def builderpotshelp(self,ctx):
        embed = discord.Embed(title = " ?builderpots help",
                                description = "Bot Command = ?builderpots "
                                )
        embed.set_image(url="https://miro.medium.com/max/386/1*at7aSnsL1mNIDTWPnxMQCg.png")

        embed.add_field(name='1st parameter', value = ' Time Remaining in 1st War', inline=True )
        embed.add_field(name='2nd parameter', value = ' Days on hero upgrade', inline=True )
        embed.add_field(name='3rd parameter', value = 'Hours on hero upgrade', inline=True )
        embed.add_field(name='Syntax', value = '?builderpots 2 2 12 ', inline=False )

        await ctx.send(embed=embed)

def setup(bot):
      bot.add_cog(HelpInfo(bot))