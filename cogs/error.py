import discord
import traceback
import sys
import os
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
GUILD = os.getenv('GUILD_ID')
TWITCH = os.getenv('TWITCH_CHANNEL')
GITHUB = os.getenv('GITHUB_URL')
ERROR_CHANNEL = os.getenv('ERROR_CHANNEL_ID')
WELCOME_CHANNEL = os.getenv('WELCOME_CHANNEL_ID')
WELCOME_IMAGE = os.getenv('WELCOME_IMAGE_URL')


class Error(commands.Cog):
    def __init__(self, client):
        self.client = client

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
            print('There was an exception in command {}:'.format(
                ctx.command), file=sys.stderr)
            traceback.print_exception(
                type(error), error, error.__traceback__, file=sys.stderr)
            await ctx.reply('The command {} is disabled.'.format(ctx.command))

        elif isinstance(error, commands.NoPrivateMessage):
            try:
                print('There was an exception in command {}:'.format(
                    ctx.command), file=sys.stderr)
                traceback.print_exception(
                    type(error), error, error.__traceback__, file=sys.stderr)
                await ctx.author.send('The command {} can not be used in Private Messages.'.format(ctx.command))
            except discord.HTTPException:
                pass

        elif isinstance(error, commands.CommandError):
            if ctx.command.qualified_name == ctx.command:
                print('There was an exception in command {}:'.format(
                    ctx.command), file=sys.stderr)
                traceback.print_exception(
                    type(error), error, error.__traceback__, file=sys.stderr)
                await ctx.reply('There was a problem with that command...')

        elif isinstance(error, commands.BotMissingPermissions):
            if ctx.command.qualified_name == ctx.command:
                print('There was an exception in command {}:'.format(
                    ctx.command), file=sys.stderr)
                traceback.print_exception(
                    type(error), error, error.__traceback__, file=sys.stderr)
                await ctx.reply('I do not have permission to use the command: {}'.format(ctx.command))

        elif isinstance(error, commands.MissingPermissions):
            if ctx.command.qualified_name == ctx.command:
                print('There was an exception in command {}:'.format(
                    ctx.command), file=sys.stderr)
                traceback.print_exception(
                    type(error), error, error.__traceback__, file=sys.stderr)
                await ctx.reply('You do not have permission to use the command {}'.format(ctx.command))

        elif isinstance(error, commands.MissingRequiredArgument):
            if ctx.command.qualified_name == ctx.command:
                print('There was an exception in command {}:'.format(
                    ctx.command), file=sys.stderr)
                await ctx.reply('Please pass in all required argument(s)... Type {}help {} for help.'.format(self.clean_prefix, ctx.command))
                traceback.print_exception(
                    type(error), error, error.__traceback__, file=sys.stderr)

        elif isinstance(error, commands.ThreadNotFound):
            error_channel = self.client.get_channel(ERROR_CHANNEL)
            print('I can not find the specified thread.', file=sys.stderr)
            traceback.print_exception(
                type(error), error, error.__traceback__, file=sys.stderr)
            await error_channel.send('An Error Has Occurred {}:'.format(error), file=sys.stderr)

        elif isinstance(error, commands.ChannelNotFound):
            error_channel = self.client.get_channel(ERROR_CHANNEL)
            print('I can not find the specified channel.', file=sys.stderr)
            traceback.print_exception(
                type(error), error, error.__traceback__, file=sys.stderr)
            await error_channel.send('An Error Has Occurred {}:'.format(error), file=sys.stderr)

        elif isinstance(error, commands.UserNotFound):
            error_channel = self.client.get_channel(ERROR_CHANNEL)
            print('I can not find the specified user.', file=sys.stderr)
            traceback.print_exception(
                type(error), error, error.__traceback__, file=sys.stderr)
            await error_channel.send('An Error Has Occurred {}:'.format(error), file=sys.stderr)

        else:
            print('Ignoring exception in command {}:'.format(
                ctx.command), file=sys.stderr)
            traceback.print_exception(
                type(error), error, error.__traceback__, file=sys.stderr)


def setup(client):
    client.add_cog(Error(client))