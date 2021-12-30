import discord
import asyncio
from discord.ext import commands

class Social(commands.Cog, description='Twitter, Reddit, and RSS commands.'):
    def __init__(self, client):
        self.client = client

        # Insert Code Here

def setup(client):
    client.add_cog(Social(client))