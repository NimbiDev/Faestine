import discord
import aiohttp
import TenGiphPy

import random
import json

from env import BLUE, GIPHY_API, TENOR_API
from discord.ext import commands


TOKENS = {'TENOR_API': TENOR_API}
TENOR = TenGiphPy.Tenor(token=TOKENS['TENOR_API'])

command_attrs = {'hidden': False}


class Images(commands.Cog, name='Image commands', description='Use Giphy or Tenor API to grab random gifs from the web.'):
    def __init__(self, client):
        self.client = client
        self.session = aiohttp.ClientSession()

    def cog_unload(self):
        self.client.loop.create_task(self.session.close())

    @commands.command(name='giphy', description='Return a random gif by tag from Giphy.')
    @commands.has_guild_permissions(send_messages=True)
    async def _giphy(self, ctx, *, search):
        session = self.session

        if search == '':
            response = await session.get('https://api.giphy.com/v1/gifs/random?api_key={}'.format(GIPHY_API))
            data = json.loads(await response.text())
            embed = discord.Embed(color=BLUE)
            embed.set_image(url=data['data']['images']['original']['url'])
        else:
            search.replace(' ', '+')
            response = await session.get('http://api.giphy.com/v1/gifs/search?q={}&api_key={}&limit=10'.format(search, GIPHY_API))
            data = json.loads(await response.text())
            gif_choice = random.randint(0, 9)
            embed = discord.Embed(color=BLUE)
            embed.set_image(url=data['data'][gif_choice]
                            ['images']['original']['url'])
            await ctx.message.delete()
            await ctx.send(embed=embed, mention_author=False)
    
    @commands.command(aliases=['t'], description='Return a random gif by tag from tenor.')
    @commands.has_guild_permissions(send_messages=True)
    async def tenor(self, ctx, *, _text):

        tenorUrl = await TENOR.arandom(str(_text))

        embed = discord.Embed(colour=BLUE)
        embed.set_image(url=tenorUrl)
        await ctx.message.delete()
        await ctx.send(embed=embed, mention_author=False)

def setup(client):
    client.add_cog(Images(client))