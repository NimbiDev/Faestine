import discord
from discord.ext import commands

GUILD = '899130986242113586'
TWITCH = 'Discord'
GITHUB = 'github.com/DevCorner-Github/Faestine'
ERROR_CHANNEL = '899741317318455346'
WELCOME_CHANNEL = '911521226038587412'
WELCOME_IMAGE = 'https://gifimage.net/wp-content/uploads/2017/09/anime-welcome-gif.gif'

RED = discord.colour.Colour.dark_red()
GREEN = discord.colour.Colour.dark_green()
GOLD = discord.colour.Colour.dark_gold()
BLUE = discord.colour.Colour.dark_blue()


class Owner(commands.Cog):
    def __init__(self, client):
        self.client = client
        

    @commands.command(aliases=['l'], description='Load a specified cog.')
    @commands.is_owner()
    async def load(self, ctx, extension):
        """
        :param ctx:
        :param extension:
        :return:
        """
        if ctx.invoked_subcommand is None:
            await ctx.send(':x: Invalid sub command.', delete_after=20)
        self.client.load_extension('cogs.{}'.format(extension))
        print('Loaded cogs.{}'.format(extension))
        await ctx.send('Successfully loaded the {} cog.'.format(extension))

    @commands.command(aliases=['ul', 'uload'], description='Unload a specified cog.')
    @commands.is_owner()
    async def unload(self, ctx, extension):
        """
        :param ctx:
        :param extension:
        :return:
        """
        if ctx.invoked_subcommand is None:
            await ctx.send(':x: Invalid sub command.', delete_after=20)
        self.client.unload_extension('cogs.{}'.format(extension))
        print('Unloaded cogs.{}'.format(extension))
        await ctx.send('Successfully unloaded the {} cog.'.format(extension))

    @commands.command(aliases=['rl', 'rload'], description='Unload and then reload a specified cog.')
    @commands.is_owner()
    async def reload(self, ctx, extension):
        """
        :param ctx:
        :param extension:
        :return:
        """
        if ctx.invoked_subcommand is None:
            await ctx.send(':x: Invalid sub command.', delete_after=20)
        self.client.unload_extension('cogs.{}'.format(extension))
        self.client.load_extension('cogs.{}'.format(extension))
        print('Reloaded cogs.{}'.format(extension))
        await ctx.send('Successfully reloaded the {} cog.'.format(extension))

    @commands.command(aliases=['t'], description='Enable or Disable a specified command')
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
            await ctx.send(':ballot_box_with_check: Successfully {} the command {}'.format(ternary, command.qualified_name))


def setup(client):
    client.add_cog(Owner(client))
