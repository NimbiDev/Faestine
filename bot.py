import traceback
import sys
import time
import os
import discord
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('CLIENT_TOKEN')
GITHUB = os.getenv('GITHUB_URL')

client = commands.Bot(command_prefix='fae ')

class CustomHelp(commands.MinimalHelpCommand):
    async def send_pages(self):
        destination = self.get_destination()
        for page in self.paginator.pages:
            embed = discord.Embed(description=page)
            await destination.send(embed=embed)


client.help_command = CustomHelp()

for filename in os.listdir('./cogs/'):
    if filename.endswith('.py'):
        client.load_extension('cogs.{}'.format(filename[:-3]))
        print('Loaded cogs.{}'.format(filename[:-3]))

client.run(TOKEN)
