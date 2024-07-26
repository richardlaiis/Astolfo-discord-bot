import discord
from discord.ext import commands
from core.classes import cogExtensions
import random
import json

with open('./setting.json', 'r', encoding='utf8') as jsonFile:
    info = json.load(jsonFile)

class React(cogExtensions):
    @commands.command()
    async def pic(self, ctx):
        random_pic = random.choice(info["IMG"])
        pic = discord.File(random_pic)
        await ctx.send(file = pic)
        await ctx.send(ans)
async def setup(bot):
    await bot.add_cog(React(bot))