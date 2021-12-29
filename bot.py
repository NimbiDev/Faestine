import os
import discord
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('CLIENT_TOKEN')
GITHUB = os.getenv('GITHUB_URL')
PREFIX = os.getenv('CLIENT_PREFIX')

client = commands.Bot(command_prefix=f'{PREFIX}')

for filename in os.listdir('./cogs/'):
    if filename.endswith('.py'):
        client.load_extension('cogs.{}'.format(filename[:-3]))
        print('Loaded cogs.{}'.format(filename[:-3]))

client.run(TOKEN)