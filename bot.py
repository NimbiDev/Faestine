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


@client.command(name='load', aliases=['l'], description='Load the specified cog.')
@commands.is_owner()
async def _load(ctx, extension):
    try:
        client.load_extension(extension)
    except Exception as error:
        ctx.send('{} can not be loaded. [{}]'.format(extension, error))
        print('{} can not be loaded. [{}]'.format(extension, error))


@client.command(name='unload', aliases=['ul'], description='Unload a specified cog.')
@commands.is_owner()
async def _unload(ctx, extension):
    try:
        client.unload_extension(extension)
        ctx.send('{} has been unloaded.'.format(extension))
    except Exception as error:
        ctx.send('{} can not be unloaded. [{}]'.format(extension, error))
        print('{} can not be unloaded. [{}]'.format(extension, error))


@client.command(name='reload', aliases=['rl'], description='Unload and immediately reload a specified cog.')
@commands.is_owner()
async def _reload(ctx, extension):
    try:
        client.unload_extension(extension)
        client.load_extension(extension)
        ctx.send('{} has been reloaded. [{}]'.format(extension))
    except Exception as error:
        ctx.send('{} can not be reloaded. [{}]'.format(extension, error))
        print('{} can not be reloaded. [{}]'.format(extension, error))


extensions = [
    'admin',
    'mod',
    'image',
    'events',
    'owner',
    'utility',
    'social'
]

for extension in extensions:
    try:
        client.load_extension(extension)
    except Exception as error:
        print('{} can not be loaded. [{}]'.format(extension, error))

if __name__ == '__main__':
    client.run('{}'.format(TOKEN))
