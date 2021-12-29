import discord
from discord.ext import commands


class Owner(commands.Cog):
    def __init__(self, client):
        self.client = client
        

    @commands.command(aliases=['load'], description='Load a specified cog.')
    @commands.is_owner()
    async def load_cog(self, ctx, extension):
        """
        :param ctx:
        :param extension:
        :return:
        """
        self.client.load_extension('cogs.{}'.format(extension))
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
        self.client.unload_extension('cogs.{}'.format(extension))
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
        self.client.unload_extension('cogs.{}'.format(extension))
        self.client.load_extension('cogs.{}'.format(extension))
        print('Reloaded cogs.{}'.format(extension))
        await ctx.send('Successfully reloaded the {} cog.'.format(extension))

    @commands.command(aliases=[''], description='Enable or Disable a specified command')
    @commands.is_owner()
    async def toggle(self, ctx, *, command):
        command = self.client.get_command(command)

        if command is None:
            await ctx.send(':x: I can not find a command with that name!')

        elif ctx.command == command:
            await ctx.send(':x: You can not disable this command!')

        else:
            command.enabled = not command.enabled
            ternary = 'enabled' if command.enabled else 'disabled'
            await ctx.send('Successfully {} the command {}'.format(ternary, command.qualified_name))


def setup(client):
    client.add_cog(Owner(client))
