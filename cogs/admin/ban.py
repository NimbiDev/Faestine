from discord.ext import commands
from typing import List
import discord

class Ban(commands.Cog):
    def __init__(self, client):
        self.client = client

    # Insert Code Here

def setup(client):
    client.add_cog(Ban(client))
