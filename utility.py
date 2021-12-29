import discord
import asyncio
from discord.ext import commands


class Utility(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(name='ping', aliases=['echo', 'beep'], description='Simple Ping Pong command.')
    async def _ping(self, ctx):
        await ctx.send('Pong!')


def setup(client):
    client.add_cog(Utility(client))
