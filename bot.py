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


for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')
    else:
        print(f'Unable to load {filename[:-3]}')

        
client.run(TOKEN)
