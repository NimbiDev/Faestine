import discord
import asyncio
from discord.ext import commands

class Thread(commands.Cog):
    def __init__(self, client):
        self.client = client

        # Insert Code Here

def setup(client):
    client.add_cog(Thread(client))