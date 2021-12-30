import discord
import asyncio
from discord.ext import commands
from discord.ext.commands import CommandNotFound


class Kick(commands.Cog, description='Commands for moderating your server.'):
    def __init__(self, client):
        self.client = client

        # Insert Code Here

def setup(client):
    client.add_cog(Kick(client))