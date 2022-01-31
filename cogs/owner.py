import discord
import asyncio

from config import GREEN, PREFIX, DEV_ONE, DEV_TWO
from discord.ext import commands

command_attrs = {'hidden': True}

class Owner(commands.Cog, name='Owner Commands'):
    def __init__(self, client):
        self.client = client

    @commands.command(name="load", description='Load a specified cog.\n\n**Example**: `{}load Fun`'.format(PREFIX), command_attrs=command_attrs)
    @commands.is_owner()
    @commands.cooldown(1, 10, commands.BucketType.user)
    async def _load(self, ctx, *, extension):    
        self.client.load_extension('cogs.{}'.format(extension))
        e = discord.Embed(description='\✅ The {} cog has been successfully loaded.'.format(extension), color=GREEN)
        await ctx.send(embed=e, mention_author=False)

    @commands.command(name="unload", description='Unload a specified cog.\n\n**Example**: `{}unload Fun`'.format(PREFIX), command_attrs=command_attrs)
    @commands.is_owner()
    @commands.cooldown(1, 10, commands.BucketType.user)
    async def _unload(self, ctx, *, extension):
        self.client.unload_extension('cogs.{}'.format(extension))
        e = discord.Embed(description='\✅ The {} cog has been successfully unloaded.'.format(extension), color=GREEN)
        await ctx.send(embed=e, mention_author=False)

    @commands.command(name="reload", description='Unload and then immediately reload a specified cog.\n\n**Example**: `{}reload Fun`'.format(PREFIX), command_attrs=command_attrs)
    @commands.is_owner()
    @commands.cooldown(1, 10, commands.BucketType.user)
    async def _reload(self, ctx, *, extension):
        self.client.reload_extension('cogs.{}'.format(extension))
        e = discord.Embed(description='\✅ The {} cog has been successfully reloaded.'.format(extension), color=GREEN)
        await ctx.send(embed=e, mention_author=False)


def setup(client):
    client.add_cog(Owner(client))
