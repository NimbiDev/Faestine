import os
import sys
import time
import asyncio
import discord
import logging

from discord.ext import commands
from discord.ext.commands import CommandNotFound
from typing import List
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('CLIENT_TOKEN')
PREFIX = os.getenv('CLIENT_PREFIX')
TWITCH = os.getenv('TWITCH_CHANNEL')
ERR_FILE = os.getenv('ERROR_FILE')
DBUG_FILE = os.getenv('DEBUG_FILE')


activity = discord.Streaming(name='with cogs | {}help'.format(
    PREFIX), url='https://twitch.tv/{}'.format(TWITCH))


client = commands.Bot(
    command_prefix=commands.when_mentioned_or('{}'.format(PREFIX)),
    description='Discord client',
    activity=activity,
    status=discord.Status.online
)

client.remove_command('help')

# class Help(commands.Cog):
#     def __init__(self, client):
#         self.client = client


# class CustomHelp(commands.MinimalHelpCommand):
#     async def send_pages(self):
#         destination = self.get_destination()
#         embed = discord.Embed(color=discord.Color.blurple(), description='')
#         for page in self.paginator.pages:
#             embed.description += page
#             await destination.send(embed=embed)


# client.help_command = CustomHelp()

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension('cogs.{}'.format(filename[:-3]))
        print('Loaded cogs.{}'.format(filename[:-3]))
    else:
        print('Unable to load cogs.{}'.format(filename[:-3]))
        
# for filename in os.listdir('./cogs/admin'):
#     if filename.endswith('.py'):
#         client.load_extension('cogs.{}'.format(filename[:-3]))
#         print('Loaded cogs.{}'.format(filename[:-3]))
#     else:
#         print('Unable to load cogs.{}'.format(filename[:-3]))
        
# for filename in os.listdir('./cogs/mod'):
#     if filename.endswith('.py'):
#         client.load_extension('cogs.{}'.format(filename[:-3]))
#         print('Loaded cogs.{}'.format(filename[:-3]))
#     else:
#         print('Unable to load cogs.{}'.format(filename[:-3]))

# for filename in os.listdir('./cogs/events'):
#     if filename.endswith('.py'):
#         client.load_extension('cogs.{}'.format(filename[:-3]))
#         print('Loaded cogs.{}'.format(filename[:-3]))
#     else:
#         print('Unable to load cogs.{}'.format(filename[:-3]))

# for filename in os.listdir('./cogs/images'):
#     if filename.endswith('.py'):
#         client.load_extension('cogs.{}'.format(filename[:-3]))
#         print('Loaded cogs.{}'.format(filename[:-3]))
#     else:
#         print('Unable to load cogs.{}'.format(filename[:-3]))

# for filename in os.listdir('./cogs/owner'):
#     if filename.endswith('.py'):
#         client.load_extension('cogs.{}'.format(filename[:-3]))
#         print('Loaded cogs.{}'.format(filename[:-3]))
#     else:
#         print('Unable to load cogs.{}'.format(filename[:-3]))

# for filename in os.listdir('./cogs/social'):
#     if filename.endswith('.py'):
#         client.load_extension('cogs.{}'.format(filename[:-3]))
#         print('Loaded cogs.{}'.format(filename[:-3]))
#     else:
#         print('Unable to load cogs.{}'.format(filename[:-3]))

# for filename in os.listdir('./cogs/util'):
#     if filename.endswith('.py'):
#         client.load_extension('cogs.{}'.format(filename[:-3]))
#         print('Loaded cogs.{}'.format(filename[:-3]))
#     else:
#         print('Unable to load cogs.{}'.format(filename[:-3]))

error_logger = logging.getLogger('discord')
debug_logger = logging.getLogger('discord')
debug_logger.setLevel(logging.DEBUG)
error_logger.setLevel(logging.ERROR)
debug_handler = logging.FileHandler(filename=DBUG_FILE, encoding='utf-8', mode='w')
error_handler = logging.FileHandler(filename=ERR_FILE, encoding='utf-8', mode='w')
debug_handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
error_handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
debug_logger.addHandler(debug_handler)
error_logger.addHandler(error_handler)

client.run('{}'.format(TOKEN))
