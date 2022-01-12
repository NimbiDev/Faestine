import discord
import asyncio

from env import PREFIX
from discord.ext import commands
from discord.ext.commands import CommandNotFound



class Avatar(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(name='avatar', aliases=['ava', 'pfp'], description='Return a user\'s avatar.', usage='Usage: {}avatar [query]\nExample:avatar {} @Nimbi'.format(PREFIX, PREFIX))
    async def avatar(self, ctx, *, member: discord.Member = None):
        if not member:
            member = ctx.message.author
        e = discord.Embed(title=str(member), color=0xAE0808)
        e.set_image(url=member.avatar_url)
        await ctx.message.delete()
        await ctx.reply(embed=e, mention_author=False)

def setup(client):
    client.add_cog(Avatar(client))