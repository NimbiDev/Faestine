import discord
import os
import TenGiphPy

from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()

PREFIX = os.getenv('CLIENT_PREFIX')
TENOR_API_TOKEN = os.getenv('TENOR_TOKEN')

TOKENS = {'TENOR_API': TENOR_API_TOKEN}

TENOR = TenGiphPy.Tenor(token=TOKENS['TENOR_API'])


class Tenor(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(aliases=['t'], description='Return a random gif by tag from tenor.', usage='Usage: {}tenor [query]\nExample: {}tenor dog'.format(PREFIX, PREFIX))
    @commands.has_guild_permissions(send_messages=True, embed_links=True)
    async def tenor(self, ctx, *, _text):

        _url = await TENOR.arandom(str(_text))

        embed = discord.Embed(colour=discord.Colour.random())
        embed.set_image(url=_url)
        await ctx.send(embed=embed)

    @tenor.error
    async def tenor_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send(':x: Tag cant be None. Please give a valid tag to search.')
        else:
            raise error


def setup(client):
    client.add_cog(Tenor(client))
    