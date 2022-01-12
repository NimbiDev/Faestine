import discord
import asyncio
from discord.ext import commands
from discord.ext.commands import CommandNotFound



class Reload(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(name="reload", aliases=['rl', 'rload'], description='Unload and then immediately reload a specified cog.')
    @commands.is_owner()
    async def _reload(self, ctx, extension):

        client = self.client
        await client.unload_extension(f'cogs.{extension}')
        await client.load_extension(f'cogs.{extension}')
        await ctx.send('The {} cog has been successfully reloaded.'.format(extension))


def setup(client):
    client.add_cog(Reload(client))