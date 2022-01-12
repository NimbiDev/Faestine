import os
from discord.ext import commands


import discord
from dotenv import load_dotenv

load_dotenv()

PREFIX = os.getenv('CLIENT_PREFIX')


class Error_Handler(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        invalid_argument_error = ':x: Invalid Argument.'
        missing_permissions_error = ':x: You do not have permission to use that command.'
        red = discord.Color.dark_red()

        from discord.ext.commands import CommandNotFound, MissingPermissions, BadArgument

        if isinstance(error, BadArgument):
            embed = discord.Embed(
                description=invalid_argument_error, color=red)
            await ctx.send(embed=embed, mention_author=False, delete_after=5)
        if isinstance(error, MissingPermissions):
            embed = discord.embed(
                description=missing_permissions_error, color=red)
            await ctx.send(embed=embed, mention_author=False, delete_after=5)
        if isinstance(error, CommandNotFound):
            return
        else:
            raise error


def setup(client):
    client.add_cog(Error_Handler(client))