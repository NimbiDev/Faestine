import discord
import asyncio
from discord.ext import commands
from discord.ext.commands import CommandNotFound


class Tempmute(commands.Cog):
    def __init__(self, client):
        self.client = client

        # Insert Code Here

def setup(client):
    client.add_cog(Tempmute(client))