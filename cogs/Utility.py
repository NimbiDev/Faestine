import discord
import time
import os
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
TWITCH_API_TOKEN = os.getenv('TWITCH_TOKEN')
TWITCH_API_SECRET = os.getenv('TWITCH_SECRET')
WOLFRAM_API_ID = os.getenv('WOLFRAM_ID')


class Utility(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=['echo', 'beep'], description='Responds with the bot\'s current ping.')
    @commands.has_guild_permissions(send_messages=True)
    async def ping(self, ctx):
        """
        :param ctx:
        :return:
        """
        await ctx.send(f'My current ping is {round (self.bot.latency * 1000)}ms')

    @commands.command(aliases=['av', 'pfp'], description='Display a member\'s avatar')
    @commands.has_guild_permissions(send_messages=True, embed_links=True)
    async def avatar(self, ctx, member: discord.Member = None):
        if member is None:
            member = ctx.author
        emb = discord.Embed(color=discord.Color.random())
        emb.set_image(url=member.avatar_url)
        await ctx.send(embed=emb)


def setup(bot):
    bot.add_cog(Utility(bot))
