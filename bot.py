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
    command_prefix=commands.when_mentioned_or("."),
    description="Discord Bot",
)


for filename in os.listdir('./cogs/admin'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.admin.{filename[:-3]}')
    else:
        print(f'Unable to load {filename[:-3]}')

for filename in os.listdir('./cogs/mod'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.mod.{filename[:-3]}')
    else:
        print(f'Unable to load {filename[:-3]}')

for filename in os.listdir('./cogs/util'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.utl.{filename[:-3]}')
    else:
        print(f'Unable to load {filename[:-3]}')

for filename in os.listdir('./cogs/events'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.events.{filename[:-3]}')
    else:
        print(f'Unable to load {filename[:-3]}')
for filename in os.listdir('./cogs/social'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.social.{filename[:-3]}')
    else:
        print(f'Unable to load {filename[:-3]}')
for filename in os.listdir('./cogs/image'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.image.{filename[:-3]}')
    else:
        print(f'Unable to load {filename[:-3]}')
for filename in os.listdir('./cogs/owner'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.owner.{filename[:-3]}')
    else:
        print(f'Unable to load {filename[:-3]}')

client.run(TOKEN)
