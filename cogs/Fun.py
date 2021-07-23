import discord
import os
import aiohttp
import random
import json
import TenGiphPy
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()

PREFIX = os.getenv('COMMAND_PREFIX')
OSU_API_TOKEN = os.getenv('OSU_TOKEN')
GW2_API_TOKEN = os.getenv('GW2_TOKEN')
TENOR_API_TOKEN = os.getenv('TENOR_TOKEN')
GIPHY_API_TOKEN = os.getenv('GIPHY_TOKEN')

TOKENS = {'TENOR_API': TENOR_API_TOKEN, 'GIPHY_API': GIPHY_API_TOKEN}

TENOR = TenGiphPy.Tenor(token=TOKENS['TENOR_API'])
GIPHY = TenGiphPy.Giphy(token=TOKENS['GIPHY_API'])


class Fun(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(aliases=['t'], description='Return a random gif by tag from tenor.', usage=f'Usage: {PREFIX}tenor [query]\nExample: {PREFIX}tenor dog')
    @commands.has_guild_permissions(send_messages=True, embed_links=True)
    async def tenor(self, ctx, *, text):
        response = await TENOR.arandom(str(text))
        await ctx.send(f'{response}')

    @commands.command(aliases=['g'], description='Return a random gif by tag from giphy.', usage=f'Usage: {PREFIX}giphy [query]\nExample: {PREFIX}giphy dog')
    @commands.has_guild_permissions(send_messages=True, embed_links=True)
    async def giphy(self, ctx, *, text):
        response = await GIPHY.arandom(str(text))
        await ctx.send(f'{response}')


def setup(client):
    client.add_cog(Fun(client))
