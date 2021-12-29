import discord
import traceback
import sys
import os
from discord.ext import commands

GUILD = '899130986242113586'
TWITCH = 'Discord'
GITHUB = 'github.com/DevCorner-Github/Faestine'
ERROR_CHANNEL = '899741317318455346'
WELCOME_CHANNEL = '911521226038587412'
WELCOME_IMAGE = 'https://gifimage.net/wp-content/uploads/2017/09/anime-welcome-gif.gif'

RED = discord.colour.Colour.dark_red()
GREEN = discord.colour.Colour.dark_green()
GOLD = discord.colour.Colour.dark_gold()
BLUE = discord.colour.Colour.dark_blue()
YELLOW = discord.colour.Colour.dark_yellow()


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