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


class Images(commands.Cog, name='Image Commands'):
    def __init__(self, client):
        self.client = client
        self.session = aiohttp.ClientSession()

    def cog_unload(self):
        self.client.loop.create_task(self.session.close())

    @commands.command(name='giphy', description='Return a random gif by tag from Giphy.', command_attrs=command_attrs)
    @commands.has_guild_permissions(send_messages=True, embed_links=True)
    async def _giphy(self, ctx, *, search):
        session = self.session
        embed = discord.Embed(colour=BLUE)

        if search == '':
            response = await session.get(f'https://api.giphy.com/v1/gifs/random?api_key={GIPHY_API}')
            data = json.loads(await response.text())
            embed.set_image(url=data['data']['images']['original']['url'])
        else:
            search.replace(' ', '+')
            response = await session.get(f'http://api.giphy.com/v1/gifs/search?q={search}&api_key={GIPHY_API}&limit=10')
            data = json.loads(await response.text())
            gif_choice = random.randint(0, 9)
            embed.set_image(url=data['data'][gif_choice]['images']['original']['url'])
            await ctx.send(embed=embed)
    
    @commands.command(aliases=['t'], description='Return a random gif by tag from tenor.', command_attrs=command_attrs)
    @commands.has_guild_permissions(send_messages=True, embed_links=True)
    async def tenor(self, ctx, *, _text):
        
        tenorUrl = await TENOR.arandom(str(_text))

        embed = discord.Embed(colour=BLUE)
        embed.set_image(url=tenorUrl)
        await ctx.message.delete()
        await ctx.send(embed=embed, mention_author=False)

def setup(client):
    client.add_cog(Images(client))