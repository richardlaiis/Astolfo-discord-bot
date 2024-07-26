import discord
from discord.ext import commands
import json
import os
import asyncio

with open('./setting.json', 'r', encoding='utf8') as jsonFile:
    info = json.load(jsonFile)

intents = discord.Intents.all()
bot = commands.Bot(command_prefix='.', intents = intents)

@bot.event
async def on_ready():
    print(f'{bot.user} is online.')
    slash = await bot.tree.sync()
    print(f"{len(slash)} slash commands loaded.")

@bot.command()
async def load(ctx, extension):
    await bot.load_extension(f'cmds.{extension}')
    await ctx.send(f'{extension} loaded')

@bot.command()
async def unload(ctx, extension):
    print('test')
    await bot.unload_extension(f'cmds.{extension}')
    await ctx.send(f'{extension} unloaded')

@bot.command()
async def reload(ctx, extension):
    await bot.reload_extension(f'cmds.{extension}')
    await ctx.send(f'{extension} reloaded')

async def load_extensions():
    for filename in os.listdir('./cmds'):
        if filename.endswith('.py'):
            await bot.load_extension(f'cmds.{filename[:-3]}')

async def main():
    async with bot:
        await load_extensions()
        await bot.start(info['TOKEN'])

if __name__ == '__main__':
    asyncio.run(main())