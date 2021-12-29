import discord
import asyncio
from discord.ext import commands


class User(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(description="Display information about a specified member.")
    async def user(self, ctx, member):
        msg = f'{member} joined on {member.joined_at} and has {len(member.roles)} roles.'
        await ctx.send(msg)

    @user.error
    async def user_error(self, ctx, error):
        if isinstance(error, commands.BadArgument):
            await ctx.send('I could not find that member...')


def setup(client):
    client.add_cog(User(client))
