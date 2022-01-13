import discord
import os
import sys
import time
import asyncio
import logging

from env import PREFIX, TOKEN, TWITCH, BLUE
from discord.ext import commands
from discord.ext.commands import CommandNotFound

from typing import List

activity = discord.Streaming(name=f'with cogs | {PREFIX}help', url=f'https://twitch.tv/{TWITCH}')

client = commands.Bot(
    command_prefix=commands.when_mentioned_or(f'{PREFIX}'),
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
        embed = discord.Embed(color=BLUE, description=f'{commands.command}')
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
        
info_logger, error_logger, debug_logger = logging.getLogger('discord')

logger = [
    info_logger,
    debug_logger,
    error_logger
]

debug_logger.setLevel(logging.DEBUG)
debug_handler = logging.FileHandler(filename='debug-logger.log', encoding='utf-8', mode='w')
debug_handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))

logger.setLevel(logging.ERROR)
error_handler = logging.FileHandler(filename='error-logger.log', encoding='utf-8', mode='w')
error_handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))

info_logger.setLevel(logging.INFO)
info_handler = logging.FileHandler(filename='info-logger.log', encoding='utf-8', mode='w')
info_handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))

handlers = [
    info_handler,
    debug_handler,
    error_handler
]

logger.addHandler(handlers)
        
client.run(f'{TOKEN}')
