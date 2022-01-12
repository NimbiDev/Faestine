import os
from discord.ext import commands


import discord
from dotenv import load_dotenv

load_dotenv()

PREFIX = os.getenv('CLIENT_PREFIX')


class Ready(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        client = self.client
        print(f'Logged in as {self.client.user} (ID: {self.client.user.id})')
        print('------')

def setup(client):
    client.add_cog(Ready(client))