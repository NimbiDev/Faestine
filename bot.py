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

activity = discord.Streaming(name='with cogs | {}help'.format(
    PREFIX), url='https://twitch.tv/{}'.format(TWITCH))

client = commands.Bot(
    command_prefix=commands.when_mentioned_or(PREFIX),
    description='Multi-purpose discord bot built in discord.py',
    activity=activity,
    status=discord.Status.online
)

  
class Help(commands.Cog):
    def __init__(self, client):
        self.client = client

class CustomHelp(commands.HelpCommand):
    async def send_bot_help(self, mapping):
        embed = discord.Embed(title="Command help")
        for cog, cmds in mapping.items():
            embed.set_thumbnail(url='https://raw.githubusercontent.com/DevCorner-Github/Faestine/main/assets/logo.png')
            embed.add_field(name = cog.qualified_name, value = f"{len(cmds) commands}")
            
        channel = self.get_destination()
        await channel.send(embed=embed)

client.help_command = CustomHelp()

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')
        print(f'Loaded cogs.{filename[:-3]}')
    else:
        print(f'Unable to load cogs.{filename[:-3]}')
        
client.run(TOKEN)
