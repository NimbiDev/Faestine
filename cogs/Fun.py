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

tokens = {'tenor': TENOR_API_TOKEN}

t = TenGiphPy.Tenor(token=tokens['tenor'])


class Fun(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(aliases=['gif'], description='Return a random tenor gif by tag.', usage=f'Usage: {PREFIX}tenor [query]\nExample: {PREFIX}tenor dog')
    async def tenor(self, ctx, *, giftag):
        """
        :param ctx:
        :param giftag:
        :return:
        """
        getgifurl = await t.arandom(str(giftag))
        await ctx.send(f'{getgifurl}')










def setup(client):
    client.add_cog(Fun(client))
