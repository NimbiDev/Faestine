import discord
import asyncio
from discord.ext import commands

class Owner(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(name='load', aliases=['l'], description='Load a specified cog.')
    @commands.is_owner()
    async def _load(self, ctx, extension):
        try:
            self.client.load_extension(extension)
        except Exception as error:
            ctx.send('{} can not be loaded.'.format(extension, error))  
            print('{} can not be loaded.'.format(extension, error))

    @commands.command(name='unload', aliases=['ul'], description='Unload a specified cog.')
    @commands.is_owner()
    async def _unload(self, ctx, extension):
        try:
            await self.client.unload_extension(extension)
            ctx.send('{} has been unloaded.'.format(extension))
        except Exception as error:
            ctx.send('{} can not be unloaded.'.format(extension, error))  
            print('{} can not be unloaded.'.format(extension, error))  

    @commands.command(name='reload', aliases=['rl'], description='Unload and immediately reload a specified cog.')
    @commands.is_owner()
    async def _reload(self, ctx, extension):
        try:
            await self.client.unload_extension(extension)
            self.client.load_extension(extension)
            ctx.send('{} has been reloaded.'.format(extension))
        except Exception as error:
            ctx.send('{} can not be reloaded.'.format(extension, error))  
            print('{} can not be reloaded.'.format(extension, error))      

def setup(client):
    client.add_cog(Owner(client))