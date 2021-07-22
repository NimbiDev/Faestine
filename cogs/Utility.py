import discord
import time
import os
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
PREFIX = os.getenv('COMMAND_PREFIX')
TWITCH_API_TOKEN = os.getenv('TWITCH_TOKEN')
TWITCH_API_SECRET = os.getenv('TWITCH_SECRET')
WOLFRAM_API_ID = os.getenv('WOLFRAM_ID')


class Utility(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(aliases=['echo', 'beep'], description='Responds with the bot\'s current ping.', usage=f'Usage: {PREFIX}ping\nExample: {PREFIX}ping')
    @commands.has_guild_permissions(send_messages=True)
    async def ping(self, ctx):
        """
        :param ctx:
        :return:
        """
        await ctx.send(f'My current ping is {round (self.client.latency * 1000)}ms')

    @commands.command(aliases=['inv', 'i'], description='Get the public server invite.', usage=f'Usage: {PREFIX}invite\nExample: {PREFIX}invite')
    @commands.has_guild_permissions(send_messages=True, embed_links=True)
    async def invite(self, ctx):
        """
        :param ctx:
        :return:
        """
        await ctx.send('https://discord.me/BDG')

    @commands.command(aliases=['av', 'pfp'], description='Display a member\'s avatar', usage=f'Usage: {PREFIX}avatar [member]\nExample: {PREFIX}avatar @JohnDoe')
    @commands.has_guild_permissions(send_messages=True, embed_links=True)
    async def avatar(self, ctx, member: discord.Member = None):
        if member is None:
            member = ctx.author
        emb = discord.Embed(color=discord.Color.dark_red())
        emb.set_image(url=member.avatar_url)
        await ctx.send(embed=emb)


def setup(client):
    client.add_cog(Utility(client))
