import os
import aiohttp
import random
import TenGiphPy
import discord
import json

from env import PREFIX, GIPHY_API, TENOR_API
from discord.ext import commands
from discord.ext.commands import CommandNotFound


TOKENS = {'TENOR_API': TENOR_API}
TENOR = TenGiphPy.Tenor(token=TOKENS['TENOR_API'])

command_attrs = {'hidden': False}


class Images(commands.Cog, name='Image commands', description='Use Giphy or Tenor API to grab random gifs from the web.'):
    def __init__(self, client):
        self.client = client
        self.session = aiohttp.ClientSession()

    def cog_unload(self):
        self.client.loop.create_task(self.session.close())

    @commands.command(name='giphy', description='Return a random gif by tag from Giphy.', usage='Usage: {}giphy [query]\nExample: {}giphy dog'.format(PREFIX, PREFIX))
    @commands.has_guild_permissions(send_messages=True, embed_links=True)
    async def _giphy(self, ctx, *, search):
        session = self.session
        embed = discord.Embed(colour=discord.Color.dark_gold())

        if search == '':
            response = await session.get('https://api.giphy.com/v1/gifs/random?api_key={}'.format(GIPHY_API))
            data = json.loads(await response.text())
            embed = discord.Embed(colour=discord.Colour.random())
            embed.set_image(url=data['data']['images']['original']['url'])
        else:
            search.replace(' ', '+')
            response = await session.get('http://api.giphy.com/v1/gifs/search?q={}&api_key={}&limit=10'.format(search, GIPHY_API))
            data = json.loads(await response.text())
            gif_choice = random.randint(0, 9)
            embed = discord.Embed(colour=discord.Colour.random())
            embed.set_image(url=data['data'][gif_choice]
                            ['images']['original']['url'])
            await ctx.message.delete()
            await ctx.send(embed=embed, mention_author=False)
    
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
    client.add_cog(Images(client))