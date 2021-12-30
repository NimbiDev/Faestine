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
    description='Discord Bot',
)


class Help(commands.Cog):
    def __init__(self, client):
        self.client = client


class CustomHelp(commands.MinimalHelpCommand):
    async def send_pages(self):
        destination = self.get_destination()
        e = discord.Embed(color=discord.Color.blurple(), description='')
        for page in self.paginator.pages:
            e.description += page
            await destination.send(embed=e)


client.help_command = CustomHelp()


extensions = [
    'cogs.admin',
    'cogs.mod',
    'cogs.image',
    'cogs.events',
    'cogs.utility',
    'cogs.social'
]

for extension in extensions:
    try:
        client.load_extension(extension)
        print('{} extension loaded.'.format(extension))
    except Exception as error:
        print('{} can not be loaded. [{}]'.format(extension, error))

if __name__ == '__main__':
    client.run('{}'.format(TOKEN))
