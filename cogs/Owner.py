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

    @commands.command(aliases=[''], description='Enable or Disable a specified command')
    @commands.is_owner()
    async def toggle(self, ctx, *, command):
        command = self.bot.get_command(command)

        if command is None:
            await ctx.reply(':x: I can not find a command with that name!')

        elif ctx.command == command:
            await ctx.reply(':x: You can not disable this command!')

        else:
            command.enabled = not command.enabled
            ternary = 'enabled' if command.enabled else 'disabled'
            await ctx.reply('\\:white_check_mark: Successfully {} the command {}'.format(ternary, command.qualified_name))


def setup(bot):
    bot.add_cog(Owner(bot))
