import discord
import asyncio

from env import PREFIX
from discord.ext import commands
from discord.ext.commands import CommandNotFound


class Clean(commands.Cog):
    def __init__(self, client):
        self.client = client

        # Insert Code Here

def setup(client):
    client.add_cog(Clean(client))