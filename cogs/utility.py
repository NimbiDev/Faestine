import discord
import asyncio
from discord.ext import commands


class Utility(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(name='ping', aliases=['echo', 'beep'], description='Returns the bot\'s latency.')
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
        await ctx.send(embed=embed, mention_author=False, delete_after=20)

    @commands.command(name='avatar', aliases=['ava', 'pfp'], description='Return a user\'s avatar.')
    async def avatar(self, ctx, *, member: discord.Member = None):
        if not member:
            member = ctx.message.author
        e = discord.Embed(title=str(member), color=0xAE0808)
        e.set_image(url=member.avatar_url)
        await ctx.message.delete()
        await ctx.reply(embed=e, mention_author=False)


def setup(client):
    client.add_cog(Utility(client))
