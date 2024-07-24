import discord
from discord.ext import commands
import json

with open('./setting.json', 'r', encoding='utf8') as jsonFile:
    info = json.load(jsonFile)

intents = discord.Intents.all()
bot = commands.Bot(command_prefix='.', intents = intents)

@bot.event
async def on_ready():
    print('Bot is online.')

@bot.command()
async def ping(ctx):
    await ctx.send(f'{bot.latency} (s)')

bot.run(info['TOKEN'])