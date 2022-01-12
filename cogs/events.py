import discord
import os

from env import PREFIX
from discord.ext import commands
from discord.ext.commands import CommandNotFound


class Events(commands.Cog, description='Events and triggeres that run in the background.'):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        client = self.client
        print(f'Logged in as {self.client.user} (ID: {self.client.user.id})')
        print('------')

    @commands.Cog.listener()
    async def on_messege_delete(self, ctx, messege):
        return

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):

        invalid_argument_error = ':x: Invalid Argument.'
        missing_permissions_error = ':x: You do not have permission to use that command.'
        red = discord.Color.dark_red()

        from commands import CommandNotFound, MissingPermissions, BadArgument

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
    client.add_cog(Events(client))
