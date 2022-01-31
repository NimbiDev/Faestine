import discord
import os
import sys
import time
import asyncio
import logging
import chalk

from config import EMBED_THUMBNAIL, PREFIX, TOKEN, TWITCH, BLUE, GITHUB_REPO, CLIENT_VERSION
from discord.ext import commands

from typing import List

activity = discord.Streaming(name='with cogs | {}help'.format(PREFIX), url='https://twitch.tv/{}'.format(TWITCH))

client = commands.Bot(
    command_prefix=('{}'.format(PREFIX)),
    description='Multi-purpose Discord bot ready to skill up and boost your server.\n\n**Version**: {}\n**Repo**: [DevCorner-Github/Faestine]({})'.format(CLIENT_VERSION, GITHUB_REPO),
    activity=activity,
    status=discord.Status.online
)

  
class Help(commands.Cog):
    def __init__(self, client):
        self.client = client

class CustomHelp(commands.MinimalHelpCommand):
    async def send_pages(self):
        destination = self.get_destination()
        embed = discord.Embed(color=BLUE, description='')
        embed.set_thumbnail(url='{}'.format(EMBED_THUMBNAIL))
        for page in self.paginator.pages:
            embed.description += page
            await destination.send(embed=embed)

client.help_command = CustomHelp()

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension('cogs.{}'.format(filename[:-3]))
        print(chalk.cyan('>>| Loaded cogs.{}'.format(filename[:-3])))
    else:
        print(chalk.yellow('>>| Unable to load cogs.{}'.format(filename[:-3])))
                
debug_logger = logging.getLogger('discord')
debug_logger.setLevel(logging.DEBUG)
debug_handler = logging.FileHandler(filename='debug.log', encoding='utf-8', mode='w')
debug_handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
debug_logger.addHandler(debug_handler)
        
client.run('{}'.format(TOKEN))
