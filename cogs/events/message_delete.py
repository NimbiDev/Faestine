import os
from discord.ext import commands


import discord
from dotenv import load_dotenv

load_dotenv()

PREFIX = os.getenv('CLIENT_PREFIX')


class Message_Delete(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_messege_delete(self, ctx, messege):
        # Code here
        return
    
    
def setup(client):
    client.add_cog(Message_Delete(client))