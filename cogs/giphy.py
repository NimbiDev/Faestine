import os
import aiohttp
import random
import discord
import json

from env import PREFIX, GIPHY_API

from discord.ext import commands
from discord.ext.commands import CommandNotFound

command_attrs = {'hidden': False}


class Giphy(commands.Cog):
    def __init__(self, client):
        self.client = client
        self.session = aiohttp.ClientSession()

    def cog_unload(self):
        self.client.loop.create_task(self.session.close())

    @commands.command(name='giphy', description='Returna  random gif by tag from Giphy.', usage='Usage: {}giphy [query]\nExample: {}giphy dog'.format(PREFIX, PREFIX))
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


def setup(client):
    client.add_cog(Giphy(client))