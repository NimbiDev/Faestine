import discord
import asyncio
import typing
import os
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
GITHUB = os.getenv('GITHUB_URL')


class Mod(commands.Cog):
    def __init__(self, client):
        self.client = client

        for filename in os.listdir('./mod/'):
            if filename.endswith('.py'):
                client.load_extension('cogs.{}'.format(filename[:-3]))
                print('Loaded cogs.{}'.format(filename[:-3]))


def setup(client):
    client.add_cog(Mod(client))