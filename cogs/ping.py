import discord
import time
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


class Ping(commands.Cog):
    def __init__(self, client):
        self.client = client
        

    @commands.command(aliases=['echo', 'beep'], description='Responds with the bot\'s current ping.')
    @commands.has_guild_permissions(send_messages=True)
    async def ping(self, ctx):
        """
        :param ctx:
        :return:
        """
        client = self.client
        
        embed = discord.Embed(description='**__Ping__**\n```yml\nLatency: {}ms```'.format(round(client.latency * 1000)), color=discord.colour.Colour.dark_blue())
        embed.set_image(url=client.user.avatar)
        embed.set_footer(text='{} | {}'.format(client.user.name, GITHUB))
        await ctx.send(embed=embed)

def setup(client):
    client.add_cog(Ping(client))
