import discord
import asyncio

from env import PREFIX
from discord.ext import commands
from discord.ext.commands import CommandNotFound



class Ping(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(name='ping', aliases=['echo', 'beep'], description='Returns the bot\'s latency.', help='Usage: {}ping\nExample: {}ping'.format(PREFIX, PREFIX))
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

def setup(client):
    client.add_cog(Ping(client))