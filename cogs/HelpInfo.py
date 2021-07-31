from discord.ext import commands
import asyncio
import discord
from discord import Color as c
import datetime

class HelpCommands(commands.Cog):
    def __init__(self,bot):
        self.bot= bot
    
    @commands.command(name = "herotimehelp", description="Tells you the time it will take to upgrade your hero if you use 'X' amount of builderpots")
    async def herotimehelp(self, ctx):
        await ctx.message.delete()
        embed = discord.Embed(title = " ?herotime help",description = "Bot Command = ?herotime ")
        embed.set_image(url="https://wallpapercave.com/wp/wp2424065.jpg")

        embed.add_field(name='1st parameter', value = ' Days on hero upgrade', inline=True )
        embed.add_field(name='2nd parameter', value = ' Hours on hero upgrade', inline=True )
        embed.add_field(name='3rd parameter', value = 'Intended # of potions to use', inline=True )
        embed.add_field(name='Syntax', value = '?herotime  2 12 3 ', inline=False )
        embed.set_footer(text="Command invoked by {}".format(ctx.message.author.name))
        embed.timestamp=datetime.datetime.utcnow()

        await ctx.send(embed=embed)

    
    @commands.command(name = "builderpotshelp", description=" Tells you the number of builder potions you need to use between NOW and 4 hours before the end of the next war")
    async def builderpotshelp(self,ctx):
        await ctx.message.delete()
        embed = discord.Embed(title = " ?builderpots help",
                                description = "Bot Command = ?builderpots "
                                )
        embed.set_image(url="https://miro.medium.com/max/386/1*at7aSnsL1mNIDTWPnxMQCg.png")

        embed.add_field(name='1st parameter', value = ' Time Remaining in 1st War', inline=True )
        embed.add_field(name='2nd parameter', value = ' Days on hero upgrade', inline=True )
        embed.add_field(name='3rd parameter', value = 'Hours on hero upgrade', inline=True )
        embed.add_field(name='Syntax', value = '?builderpots 2 2 12 ', inline=False )
        embed.set_footer(text="Command invoked by {}".format(ctx.message.author.name))
        embed.timestamp=datetime.datetime.utcnow()

        await ctx.send(embed=embed)
    
    @commands.command(name = "eahelp",description="Calculates amount of troops needed for Eagle Artillery to activate")
    async def eahelp(self, ctx):
        await ctx.message.delete()
        embed = discord.Embed(title = " ?ea help",description = "Bot Command = ?ea ")
        embed.set_image(url="https://i.pinimg.com/originals/2c/19/40/2c194096ace7833189bb0a460054c767.jpg")

        embed.add_field(name='1st parameter', value = ' Eagle Artillery Level', inline=True )
        embed.add_field(name='2nd parameter', value = ' Troop space', inline=True )
        embed.add_field(name='3rd parameter', value = ' # of Spells', inline=True )
        embed.add_field(name='4th parameter', value = '# of Heroes deployed', inline=True )
        embed.add_field(name='5th parameter', value = '# of Siege Machine used', inline=True )
        embed.add_field(name='Syntax', value = '?ea  1 220 4 1 0 ', inline=False )

        await ctx.send(embed=embed)

    @commands.command(name="help")
    async def help(self,ctx):
      author = ctx.message.author
      embed =(discord.Embed(color = c.gold()))
      embed.add_field(name='Hero Time', value = 'Tells you the time it will take to upgrade your hero if you use X amount of builderpots',inline=False)
      embed.add_field(name='Builder Pots', value = 'Tells you the number of builder potions you need to use between NOW and 4 hours before the end of the next war',inline=False)
      embed.add_field(name='Eagle Artillery', value = 'Calculates amount of troops needed for Eagle Artillery to activate',inline=False)
      embed.set_footer(text="Command invoked by {}".format(ctx.message.author.name))
      embed.timestamp=datetime.datetime.utcnow()

      await ctx.send(embed=embed)

def setup(bot):
      bot.add_cog(HelpCommands(bot))