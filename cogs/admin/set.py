import discord
import asyncio
from discord.ext import commands

class Set(commands.Cog):
    def __init__(self, client):
        self.client = client

        # Insert Code Here

def setup(client):
    client.add_cog.admin(Set(client))