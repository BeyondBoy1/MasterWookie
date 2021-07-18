from discord.ext import commands
import asyncio
import discord
from discord import Color as c

class ClanInfo(commands.Cog):
    def __init__(self,bot):
        self.bot= bot
    
    @commands.command(name = "claninfo")
    async def claninfo(self, ctx):
        embed = discord.Embed(title = "Main Clans")
        embed.add_field(name="Mini Matter (#2PJYCQYV9)",value= "[Clan Link]( https://link.clashofclans.com/en?action=OpenClanProfile&tag=2PJYCQYV9)", inline=False )
        embed.add_field(name="Legendary Monks (#PCCUPG9R)",value= "[Clan Link]( https://link.clashofclans.com/en?action=OpenClanProfile&tag=PCCUPG9R)", inline=False )
        embed.add_field(name="Golden Clan (#C2QPR82Q)",value= "[Clan Link]( https://link.clashofclans.com/en?action=OpenClanProfile&tag=C2QPR82Q)", inline=False )
        embed.add_field(name="Dark Matter (#Q2VYY8C8)",value= "[Clan Link]( https://link.clashofclans.com/en?action=OpenClanProfile&tag=Q2VYY8C8)", inline=False )
        embed.add_field(name=" Sheer Force (#VUCVG2J0)",value= "[Clan Link]( https://link.clashofclans.com/en?action=OpenClanProfile&tag=VUCVG2J0)", inline=False)
        

        await ctx.send(embed=embed)

    @commands.command(name = "cwlclans")
    async def cwlclans(self, ctx):
        embed = discord.Embed(title = "CWL Clans")
        embed.add_field(name="ReqnReceiveWar (#J2PVJ2GU)",value= "[Clan Link]( https://link.clashofclans.com/en?action=OpenClanProfile&tag=J2PVJ2GU)", inline=False )
        embed.add_field(name="Petarung Sejati (#PCP02V8C)",value= "[Clan Link]( https://link.clashofclans.com/en?action=OpenClanProfile&tag=PCP02V8C)", inline=False )
        embed.add_field(name="Killer_Black_Wf (#8VQYR2LR)",value= "[Clan Link]( https://link.clashofclans.com/en?action=OpenClanProfile&tag=2PJYCQYV9)", inline=False )
        embed.add_field(name="Dark Matter (#Q2VYY8C8)",value= "[Clan Link]( https://link.clashofclans.com/en?action=OpenClanProfile&tag=Q2VYY8C8)", inline=False )
        embed.add_field(name=" Sheer Force (#VUCVG2J0)",value= "[Clan Link]( https://link.clashofclans.com/en?action=OpenClanProfile&tag=VUCVG2J0)", inline=False)
        embed.add_field(name=" Endor (#2YLL8UVPY)",value= "[Clan Link]( https://link.clashofclans.com/en?action=OpenClanProfile&tag=2YLL8UVPY)", inline=False)
        embed.add_field(name="Legendary Monks (#PCCUPG9R)",value= "[Clan Link]( https://link.clashofclans.com/en?action=OpenClanProfile&tag=PCCUPG9R)", inline=False)

        await ctx.send(embed=embed)

def setup(bot):
      bot.add_cog(ClanInfo(bot))
