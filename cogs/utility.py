import discord
import asyncio

from discord.ext import commands
from discord.ext.commands import CommandNotFound
from env import BLUE, PREFIX

command_attrs = {'hidden': False}

class Utility(commands.Cog, name='🔧 Utility Commands'):
    def __init__(self, client):
        self.client = client

    @commands.command(name='ping', aliases=['echo', 'beep'], description='Returns the bot\'s latency.', command_attrs=command_attrs)
    @commands.has_guild_permissions(send_messages=True)
    async def _ping(self, ctx):
        client = self.client
        if round(client.latency * 1000) <= 50:
            embed = discord.Embed(
                title="PING",
                description=f":ping_pong: The ping is **{round(client.latency *1000)}** milliseconds!",
                color=0x44ff44
            )
        elif round(client.latency * 1000) <= 100:
            embed = discord.Embed(
                title="PING",
                description=f":ping_pong: The ping is **{round(client.latency *1000)}** milliseconds!",
                color=0xffd000
            )
        elif round(client.latency * 1000) <= 200:
            embed = discord.Embed(
                title="PING",
                description=f":ping_pong: The ping is **{round(client.latency *1000)}** milliseconds!",
                color=0xff6600
            )
        else:
            embed = discord.Embed(
                title="PING",
                description=f":ping_pong: The ping is **{round(client.latency *1000)}** milliseconds!",
                color=0x990000
            )
        await ctx.message.delete()
        await ctx.send(embed=embed, mention_author=False, delete_after=5)

    @commands.command(name='avatar', aliases=['ava', 'pfp'], description='Return a user\'s avatar.', command_attrs=command_attrs)
    @commands.has_guild_permissions(send_messages=True)
    async def _avatar(self, ctx, *, member: discord.Member = None):
        if not member:
            member = ctx.message.author
        embed = discord.Embed(title=str(member), color=BLUE)
        embed.set_image(url=member.avatar_url)
        await ctx.message.delete()
        await ctx.reply(embed=embed, mention_author=False)
        


def setup(client):
    client.add_cog(Utility(client))
