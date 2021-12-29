import discord
import asyncio
from discord.ext import commands


class Utility(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(name='user-info', aliases=['user'], description='Display information about a specified member.')
    async def _userinfo(self, ctx, member):
        msg = f'{member} joined on {member.joined_at} and has {len(member.roles)} roles.'
        await ctx.send(msg)

    @commands.command(name='ping', aliases=['echo', 'beep'], description='Simple Ping Pong command.')
    async def _ping(self, ctx):
        await ctx.send('Pong!')


def setup(client):
    client.add_cog(Utility(client))
