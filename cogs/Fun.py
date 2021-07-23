import discord
import os
import TenGiphPy
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()

PREFIX = os.getenv('COMMAND_PREFIX')
OSU_API_TOKEN = os.getenv('OSU_TOKEN')
GW2_API_TOKEN = os.getenv('GW2_TOKEN')
TENOR_API_TOKEN = os.getenv('TENOR_TOKEN')
GIPHY_API_TOKEN = os.getenv('GIPHY_TOKEN')

tokens = {'tenor': f'{TENOR_API_TOKEN}',
          'giphy': f'{GIPHY_API_TOKEN}'}

t = TenGiphPy.Tenor(token=tokens['tenor'])
g = TenGiphPy.Giphy(token=tokens['giphy'])


class Fun(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(aliases=['t'], description='Return a random gif by tag from tenor.', usage=f'Usage: {PREFIX}tenor [query]\nExample: {PREFIX}tenor dog')
    @commands.has_guild_permissions(send_messages=True, embed_links=True)
    async def tenor(self, ctx, *, giftag):
        getgifurl = await t.arandom(str(giftag))
        await ctx.send(f'{getgifurl}')

    @tenor.error
    async def tenor_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send(':x: Gif tag cant be None. Please give a valid tag to search.')
        else:
            raise error

    @commands.command(aliases=['g'], description='Return a random gif by tag from giphy.', usage=f'Usage: {PREFIX}giphy [query]\nExample: {PREFIX}giphy dog')
    @commands.has_guild_permissions(send_messages=True, embed_links=True)
    async def giphy(self, ctx, *, giftag):
        getgifurl = await g.arandom(str(giftag))
        await ctx.send(f'{getgifurl}')

    @giphy.error
    async def giphy_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send(':x: Gif tag cant be None. Please give a valid tag to search.')
        else:
            raise error


def setup(client):
    client.add_cog(Fun(client))
