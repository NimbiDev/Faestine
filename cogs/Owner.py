import discord
import os
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
PREFIX = os.getenv('COMMAND_PREFIX')

class Owner(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(aliases=['load'], description='Load a specified cog.', usage=f'Usage: {PREFIX}load [cog]\nExample: b!load_cog Admin')
    @commands.is_owner()
    async def load_cog(self, ctx, extension):
        """
        :param ctx:
        :param extension:
        :return:
        """
        self.client.load_extension(f'cogs.{extension}')
        print(f'Loaded cogs.{extension}')
        await ctx.send(f'Successfully loaded the {extension} cog.')

    @commands.command(aliases=['unload'], description='Unload a specified cog.', usage=f'Usage: {PREFIX}unload [cog]\nExample: b!unload_cog Admin')
    @commands.is_owner()
    async def unload_cog(self, ctx, extension):
        """
        :param ctx:
        :param extension:
        :return:
        """
        self.client.unload_extension(f'cogs.{extension}')
        print(f'Unloaded cogs.{extension}')
        await ctx.send(f'Successfully unloaded the {extension} cog.')

    @commands.command(aliases=['reload'], description='Unload and then reload a specified cog.',
                    usage=f'Usage: {PREFIX}reload [cog]\nExample: b!reload_cog Admin')
    @commands.is_owner()
    async def reload_cog(self, ctx, extension):
        """
        :param ctx:
        :param extension:
        :return:
        """
        self.client.unload_extension(f'cogs.{extension}')
        self.client.load_extension(f'cogs.{extension}')
        print(f'Reloaded cogs.{extension}')
        await ctx.send(f'Successfully reloaded the {extension} cog.')


def setup(client):
    client.add_cog(Owner(client))