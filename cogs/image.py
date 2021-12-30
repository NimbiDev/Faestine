import os
import aiohttp
import random
import discord
import json
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()

prefix = os.getenv("CLIENT_PREFIX")
giphy_api = os.getenv("GIPHY_API_KEY")

command_attrs = {'hidden': False}


class Images(commands.Cog):
    def __init__(self, client):
        self.client = client
        self.session = aiohttp.ClientSession()

    def cog_unload(self):
        self.client.loop.create_task(self.session.close())

    @commands.command(name='gif')
    async def _gif(self, ctx, *, search):
        session = self.session
        embed = discord.Embed(colour=discord.Color.dark_gold())

        if search == '':
            response = await session.get('https://api.giphy.com/v1/gifs/random?api_key={}'.format(giphy_api))
            data = json.loads(await response.text())
            embed.set_image(url=data['data']['images']['original']['url'])
        else:
            search.replace(' ', '+')
            response = await session.get('http://api.giphy.com/v1/gifs/search?q={}&api_key={}&limit=10'.format(search, giphy_api))
            data = json.loads(await response.text())
            gif_choice = random.randint(0, 9)
            embed.set_image(url=data['data'][gif_choice]
                            ['images']['original']['url'])
            await ctx.send(embed=embed)


def setup(client):
    client.add_cog(Images(client))
