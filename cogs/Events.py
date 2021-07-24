import discord
import traceback
import sys
import os
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
PREFIX = os.getenv('COMMAND_PREFIX')
GUILD = os.getenv('GUILD_ID')
TWITCH_URL = os.getenv('TWITCH_CHANNEL')
WELCOME_CHANNEL = os.getenv('WELCOME_CHANNEL')
WELCOME_IMAGE = os.getenv('WELCOME_IMAGE_URL')


class Events(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        await self.client.change_presence(status=discord.Status.online,
                                          activity=discord.Streaming(name='{}help'.format(PREFIX), url=TWITCH_URL))
        print('{} is online!'.format(self.client.user.name))

    @commands.Cog.listener()
    async def on_member_join(self, member):
        channel = self.client.get_channel(int(WELCOME_CHANNEL))
        _emb = discord.Embed(color=discord.colour.Color.random())
        _emb.add_field(name="Welcome", value='{} has joined {}'.format(member.name, member.guild.name), inline=False)
        _emb.set_image(url=WELCOME_IMAGE)
        await channel.send(embed=_emb)

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        """The event triggered when an error is raised while invoking a command.
        Parameters
        ------------
        ctx: commands.Context
            The context used for command invocation.
        error: commands.CommandError
            The Exception raised.
        """
        if hasattr(ctx.command, 'on_error'):
            return

        cog = ctx.cog
        if cog:
            if cog._get_overridden_method(cog.cog_command_error) is not None:
                return

        ignored = (commands.CommandNotFound,)
        error = getattr(error, 'original', error)

        if isinstance(error, ignored):
            return

        if isinstance(error, commands.DisabledCommand):
            print('There was an exception in command {}:'.format(ctx.command), file=sys.stderr)
            traceback.print_exception(type(error), error, error.__traceback__, file=sys.stderr)
            await ctx.send(f'{ctx.command} has been disabled.')

        elif isinstance(error, commands.NoPrivateMessage):
            try:
                print('There was an exception in command {}:'.format(ctx.command), file=sys.stderr)
                traceback.print_exception(type(error), error, error.__traceback__, file=sys.stderr)
                await ctx.author.send(f'{ctx.command} can not be used in Private Messages.')
            except discord.HTTPException:
                pass

        elif isinstance(error, commands.CommandError):
            if ctx.command.qualified_name == ctx.command:
                print('There was an exception in command {}:'.format(ctx.command), file=sys.stderr)
                traceback.print_exception(type(error), error, error.__traceback__, file=sys.stderr)
                await ctx.send('There was a problem with that command...')

        elif isinstance(error, commands.BotMissingPermissions):
            if ctx.command.qualified_name == ctx.command:
                print('There was an exception in command {}:'.format(ctx.command), file=sys.stderr)
                traceback.print_exception(type(error), error, error.__traceback__, file=sys.stderr)
                await ctx.send('I do not have permission to do that!')

        elif isinstance(error, commands.MissingPermissions):
            if ctx.command.qualified_name == ctx.command:
                print('There was an exception in command {}:'.format(ctx.command), file=sys.stderr)
                traceback.print_exception(type(error), error, error.__traceback__, file=sys.stderr)
                await ctx.send('You do not have permission to do that!')

            elif isinstance(error, commands.NotOwner):
                if ctx.command.qualified_name == ctx.command:
                    print('There was an exception in command {}:'.format(ctx.command), file=sys.stderr)
                    traceback.print_exception(type(error), error, error.__traceback__, file=sys.stderr)
                    await ctx.send('This command is locked to the Bot Owner')

            elif isinstance(error, commands.MissingRequiredArgument):
                if ctx.command.qualified_name == ctx.command:
                    print('There was an exception in command {}:'.format(ctx.command), file=sys.stderr)
                    traceback.print_exception(type(error), error, error.__traceback__, file=sys.stderr)
                    await ctx.send(
                        'Please pass in all required argument(s)... Type {}help {} for help.'.format(PREFIX, ctx.command))

        else:
            print('Ignoring exception in command {}:'.format(ctx.command), file=sys.stderr)
            traceback.print_exception(type(error), error, error.__traceback__, file=sys.stderr)


def setup(client):
    client.add_cog(Events(client))
