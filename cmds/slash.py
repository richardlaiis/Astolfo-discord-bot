import discord
from discord import app_commands
from core.classes import cogExtensions
# from typing import Optional
# import random
# import json

# with open('./setting.json', 'r', encoding='utf8') as jsonFile:
#     info = json.load(jsonFile)

class Slash(cogExtensions):
    @app_commands.command(name = "hello", description = "To test if Astolfo is dead.")
    async def hello(self, interaction: discord.Interaction) -> None:
        await interaction.response.send_message("Hello world!")

    @app_commands.command(name = "pow", description = "Computing the answer of a^b.")
    @app_commands.describe(a = "base", b = "exponent")
    async def pow(self, interaction: discord.Interaction, a: float, b: float) -> None:
        await interaction.response.send_message(f"{a}^{b}={a**b}")
    
    # @app_commands.command(name = "say", description = "Say what you want to say.")
    # @app_commands.describe(user = "name", content = "words")
    # async def say(self, interaction: discord.Interaction, user: str, content: Optional[str] = None):
    #     if content == None:
    #         content = "..."
    #     await interaction.response.send_message(f"{user} made me say: {content}")

async def setup(bot):
    await bot.add_cog(Slash(bot))