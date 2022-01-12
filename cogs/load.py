import discord
import asyncio

from env import PREFIX
from discord.ext import commands
from discord.ext.commands import CommandNotFound



class Load(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(name="load", aliases=['l'], description='Load a specified cog.', usage='Usage: {}load [query]\nExample: {}load purge'.format(PREFIX, PREFIX))
    @commands.is_owner()
    async def _load(self, ctx, extension):    

        client = self.client
        await client.load_extension(f'cogs.{extension}')
        await ctx.send('The {} cog has been successfully loaded.'.format(extension))
        
def setup(client):
    client.add_cog(Load(client))