import discord
import traceback
import sys
import os
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
TWITCH_API_TOKEN = os.getenv('TWITCH_TOKEN')
TWITCH_API_SECRET = os.getenv('TWITCH_SECRET')
GUILD = os.getenv('GUILD_ID')
TWITCH = os.getenv('TWITCH_CHANNEL')
GITHUB = os.getenv('GITHUB_URL')
ERROR_CHANNEL = os.getenv('ERROR_CHANNEL_ID')
WELCOME_CHANNEL = os.getenv('WELCOME_CHANNEL_ID')
WELCOME_IMAGE = os.getenv('WELCOME_IMAGE_URL')


class Ready(commands.Cog):
    def __init__(self, client):
        self.client = client
        

    @commands.Cog.listener()
    async def on_ready(self):
        client = self.client
        
        await client.change_presence(status=discord.Status.online, activity=discord.Streaming(name='{} help'.format(client.command_prefix), url=TWITCH))
        print('{} is online!'.format(client.user.name))

def setup(client):
    client.add_cog(Ready(client))