import os
import sys
import time
import asyncio

from discord.ext import commands
from typing import List
import discord

from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('CLIENT_TOKEN')
PREFIX = os.getenv('CLIENT_PREFIX')


client = commands.Bot(
    command_prefix=commands.when_mentioned_or('{}'.format(PREFIX)),
    description='Discord client',
)


class Help(commands.Cog):
    def __init__(self, client):
        self.client = client


class CustomHelp(commands.MinimalHelpCommand):
    async def send_pages(self):
        destination = self.get_destination()
        embed = discord.Embed(color=discord.Color.blurple(), description='')
        for page in self.paginator.pages:
            embed.description += page
            await destination.send(embed=embed)


client.help_command = CustomHelp()

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')
        print(f'Loaded cogs.{filename[:-3]}')
    else:
        print(f'Unable to load cogs.{filename[:-3]}')


client.run('{}'.format(TOKEN))
