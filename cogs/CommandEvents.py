from discord.ext import commands
import asyncio

class CommandEvents(commands.Cog):
    def __init__(self,bot):
        self.bot= bot


    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
      print(ctx.command.name + "was invoked incorrectly.")
      print(error)

    @commands.Cog.listener()
    async def on_command_completion(self, ctx):
      print(ctx.command.name + "was invoked successfully.")

def setup(bot):
      bot.add_cog(CommandEvents(bot))














def setup(bot):
    bot.add_cog(CommandEvents(bot))

 