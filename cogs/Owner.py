import discord
from discord.ext import commands


class Owner(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=['load'], description='Load a specified cog.')
    @commands.is_owner()
    async def load_cog(self, ctx, extension):
        """
        :param ctx:
        :param extension:
        :return:
        """
        self.bot.load_extension('cogs.{}'.format(extension))
        print('Loaded cogs.{}'.format(extension))
        await ctx.send('Successfully loaded the {} cog.'.format(extension))

    @commands.command(aliases=['unload'], description='Unload a specified cog.')
    @commands.is_owner()
    async def unload_cog(self, ctx, extension):
        """
        :param ctx:
        :param extension:
        :return:
        """
        self.bot.unload_extension('cogs.{}'.format(extension))
        print('Unloaded cogs.{}'.format(extension))
        await ctx.send('Successfully unloaded the {} cog.'.format(extension))

    @commands.command(aliases=['reload'], description='Unload and then reload a specified cog.')
    @commands.is_owner()
    async def reload_cog(self, ctx, extension):
        """
        :param ctx:
        :param extension:
        :return:
        """
        self.bot.unload_extension(f'cogs.{extension}')
        self.bot.load_extension(f'cogs.{extension}')
        print(f'Reloaded cogs.{extension}')
        await ctx.send(f'Successfully reloaded the {extension} cog.')


def setup(bot):
    bot.add_cog(Owner(bot))
