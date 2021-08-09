import discord
import time
import os
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
TWITCH_API_TOKEN = os.getenv('TWITCH_TOKEN')
TWITCH_API_SECRET = os.getenv('TWITCH_SECRET')
GITHUB = os.getenv('GITHUB_URL')


class Utility(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.clean_prefix = self.bot.command_prefix

    @commands.command(aliases=['echo', 'beep'], description='Responds with the bot\'s current ping.')
    @commands.has_guild_permissions(send_messages=True)
    async def ping(self, ctx):
        """
        :param ctx:
        :return:
        """
        url = GITHUB
        embed = discord.Embed(description='```yml\nLatency: {}ms```'.format(round(self.bot.latency * 1000)), color=discord.colour.Colour.dark_blue())
        embed.set_footer(text='{} | {}'.format(self.bot.name, url))
        await ctx.send()

    @commands.command(aliases=['av', 'pfp'], description='Display a member\'s avatar')
    @commands.has_guild_permissions(send_messages=True, embed_links=True)
    async def avatar(self, ctx, member: discord.Member = None):
        if member is None:
            member = ctx.author
        embed = discord.Embed(color=discord.colour.Color.dark_blue())
        embed.set_image(url=member.avatar_url)
        await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(Utility(bot))
