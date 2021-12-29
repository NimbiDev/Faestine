import discord
import time
import traceback
import sys
import os
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
TWITCH_API_TOKEN = os.getenv('TWITCH_TOKEN')
TWITCH_API_SECRET = os.getenv('TWITCH_SECRET')
GITHUB = os.getenv('GITHUB_URL')


class Utility(commands.Cog):
    def __init__(self, client):
        self.client = client
        

    @commands.command(aliases=['echo', 'beep'], description='Responds with the bot\'s current ping.')
    @commands.has_guild_permissions(send_messages=True)
    async def ping(self, ctx):
        """
        :param ctx:
        :return:
        """
        github_url = GITHUB
        embed = discord.Embed(description='**__Ping__**\n```yml\nLatency: {}ms```'.format(round(self.client.latency * 1000)), color=discord.colour.Colour.dark_blue())
        embed.set_image(url=self.client.user.avatar)
        embed.set_footer(text='{} | {}'.format(self.client.user.name, github_url))
        await ctx.send(embed=embed)

    @commands.command(aliases=['av', 'pfp'], description='Display a member\'s avatar')
    @commands.has_guild_permissions(send_messages=True, embed_links=True)
    async def avatar(self, ctx, member: discord.Member = None):
        github_url = GITHUB
        if member is None:
            member = ctx.author
        embed = discord.Embed(description='**__{}\'s Avatar__**'.format(member.display_name), color=discord.colour.Color.dark_blue())
        embed.set_image(url=member.avatar)
        embed.set_footer(text='{} | {}'.format(self.client.user.name, github_url), icon_url=self.client.user.avatar)
        await ctx.send(embed=embed)


def setup(client):
    client.add_cog(Utility(client))
