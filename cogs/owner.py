import discord
import asyncio

from env import PREFIX
from discord.ext import commands
from discord.ext.commands import CommandNotFound


class Owner(commands.Cog, description='Debugging commands for use by the bot owner.'):
    def __init__(self, client):
        self.client = client

    @commands.command(name="load", aliases=['l'], description='Load a specified cog.')
    @commands.is_owner()
    async def _load(self, ctx, extension):    

        client = self.client
        await client.load_extension(f'cogs.{extension}')
        await ctx.send('The {} cog has been successfully loaded.'.format(extension))

    @commands.command(name="unload", aliases=['ul', 'uload'], description='Unload a specified cog.')
    @commands.is_owner()
    async def _unload(self, ctx, extension):

        client = self.client
        await client.unload_extension(f'cogs.{extension}')
        await ctx.send('The {} cog has been successfully unloaded.'.format(extension))

    @commands.command(name="reload", aliases=['rl', 'rload'], description='Unload and then immediately reload a specified cog.')
    @commands.is_owner()
    async def _reload(self, ctx, extension):

        client = self.client
        await client.unload_extension(f'cogs.{extension}')
        await client.load_extension(f'cogs.{extension}')
        await ctx.send('The {} cog has been successfully reloaded.'.format(extension))


def setup(client):
    client.add_cog(Owner(client))
