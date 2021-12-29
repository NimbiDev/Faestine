import os

import discord
from discord.ext import commands

from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('CLIENT_TOKEN')
GITHUB = os.getenv('GITHUB_URL')
PREFIX = os.getenv('CLIENT_PREFIX')

client = commands.Bot(command_prefix=f'{PREFIX}')


class HelpEmbed(commands.HelpCommand):
    def __init__(self):
        super().__init__()
        self.client = client


# for filename in os.listdir('./cogs'):
#     if filename.endswith('.py'):
#         client.load_extension('cogs.{}'.format(filename[:-3]))
#         print('Loaded cogs.{}'.format(filename[:-3]))

for filename in os.listdir(f"./cogs/*"):
    if filename.endswith('.py'):
        filename = filename[5:-3]
        client.load_extension("cogs.{}".format(filename[:-3].replace('\\', '.')))
        print(f"Loaded cog.{}".format(filename[:-3].replace('\\', '.')))


client.run(TOKEN)
