import discord
import os
import sys
import time
import asyncio
import logging

from env import PREFIX, TOKEN, TWITCH
from discord.ext import commands
from discord.ext.commands import CommandNotFound

from typing import List

activity = discord.Streaming(name='with cogs | {}help'.format(
    PREFIX), url='https://twitch.tv/{}'.format(TWITCH))

client = commands.Bot(
    command_prefix=commands.when_mentioned_or(PREFIX),
    name='Faestine',
    title='Faestine',
    description='Multi-purpose discord bot built in discord.py',
    activity=activity,
    status=discord.Status.online
)

  
class Help(commands.Cog):
    def __init__(self, client):
        self.client = client

class CustomHelp(commands.MinimalHelpCommand):
    async def send_pages(self):
        destination = self.get_destination()
        embed = discord.Embed(color=discord.Color.blue(), description=f'{commands.command}')
        embed.set_thumbnail(url='https://raw.githubusercontent.com/DevCorner-Github/Faestine/main/assets/logo.png')
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
