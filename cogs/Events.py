import discord
import traceback
import sys
import os
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
GUILD = os.getenv('GUILD_ID')
TWITCH_URL = os.getenv('TWITCH_CHANNEL')
ERROR_CHANNEL = os.getenv('ERROR_CHANNEL_ID')
WELCOME_CHANNEL = os.getenv('WELCOME_CHANNEL_ID')
WELCOME_IMAGE = os.getenv('WELCOME_IMAGE_URL')


class Events(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.clean_prefix = "fae "

    @commands.Cog.listener()
    async def on_ready(self):
        await self.bot.change_presence(status=discord.Status.online, activity=discord.Streaming(name='{}help'.format(self.clean_prefix), url=TWITCH_URL))
        print('{} is online!'.format(self.bot.user.name))

    @commands.Cog.listener()
    async def on_member_join(self, member):
        channel = self.bot.get_channel(int(WELCOME_CHANNEL))
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
            await ctx.send('The command: {} has been disabled.'.format(ctx.command))

        elif isinstance(error, commands.NoPrivateMessage):
            try:
                print('There was an exception in command {}:'.format(ctx.command), file=sys.stderr)
                traceback.print_exception(type(error), error, error.__traceback__, file=sys.stderr)
                await ctx.author.send('The command: {} can not be used in Private Messages.'.format(ctx.command))
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
                await ctx.send('I do not have permission to use the command: {}'.format(ctx.command))

        elif isinstance(error, commands.MissingPermissions):
            if ctx.command.qualified_name == ctx.command:
                print('There was an exception in command {}:'.format(ctx.command), file=sys.stderr)
                traceback.print_exception(type(error), error, error.__traceback__, file=sys.stderr)
                await ctx.send('You do not have permission to use the command: {}'.format(ctx.command))

        elif isinstance(error, commands.MissingRequiredArgument):
            if ctx.command.qualified_name == ctx.command:
                print('There was an exception in command {}:'.format(ctx.command), file=sys.stderr)
                traceback.print_exception(type(error), error, error.__traceback__, file=sys.stderr)
                await ctx.send('Please pass in all required argument(s)... Type {}help {} for help.'.format(PREFIX, ctx.command))

        elif isinstance(error, commands.ThreadNotFound):
            error_channel = self.bot.get_channel(ERROR_CHANNEL)
            print('I can not find the specified thread.', file=sys.stderr)
            traceback.print_exception(type(error), error, error.__traceback__, file=sys.stderr)
            await error_channel.send('An Error Has Occurred {}:'.format(error), file=sys.stderr)

        elif isinstance(error, commands.ChannelNotFound):
            error_channel = self.bot.get_channel(ERROR_CHANNEL)
            print('I can not find the specified channel.', file=sys.stderr)
            traceback.print_exception(type(error), error, error.__traceback__, file=sys.stderr)
            await error_channel.send('An Error Has Occurred {}:'.format(error), file=sys.stderr)

        elif isinstance(error, commands.UserNotFound):
            error_channel = self.bot.get_channel(ERROR_CHANNEL)
            print('I can not find the specified user.', file=sys.stderr)
            traceback.print_exception(type(error), error, error.__traceback__, file=sys.stderr)
            await error_channel.send('An Error Has Occurred {}:'.format(error), file=sys.stderr)

        else:
            print('Ignoring exception in command {}:'.format(ctx.command), file=sys.stderr)
            traceback.print_exception(type(error), error, error.__traceback__, file=sys.stderr)


def setup(bot):
    bot.add_cog(Events(bot))
