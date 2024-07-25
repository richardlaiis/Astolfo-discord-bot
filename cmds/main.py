import discord
from discord.ext import commands
from core.classes import cogExtensions

class Main(cogExtensions):
    @commands.command()
    async def ping(self, ctx):
        await ctx.send(f'{self.bot.latency} (s)')

async def setup(bot):
    await bot.add_cog(Main(bot))