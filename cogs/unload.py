import discord
import asyncio

from env import PREFIX
from discord.ext import commands
from discord.ext.commands import CommandNotFound



class Unload(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(name="unload", aliases=['ul', 'uload'], description='Unload a specified cog.')
    @commands.is_owner()
    async def _unload(self, ctx, extension):

        client = self.client
        await client.unload_extension(f'cogs.{extension}')
        await ctx.send('The {} cog has been successfully unloaded.'.format(extension))

def setup(client):
    client.add_cog(Unload(client))