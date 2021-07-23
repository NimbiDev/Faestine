import discord
import os
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
PREFIX = os.getenv('COMMAND_PREFIX')
GUILD = os.getenv('GUILD_ID')
TWITCH_URL = os.getenv('TWITCH_CHANNEL')
WELCOME_CHANNEL = os.getenv('WELCOME_CHANNEL_NAME')
WELCOME_IMAGE = os.getenv('WELCOME_IMAGE_URL')


class Events(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        """
        :return:
        """

        await self.client.change_presence(status=discord.Status.online, activity=discord.Streaming(name=f'{PREFIX}help', url=TWITCH_URL))
        print(f'{self.client.user.name} is online!')

    @commands.Cog.listener()
    async def on_member_join(self, member):
        for channel in member.guild.channels:
            if not str(channel) != WELCOME_CHANNEL:
                print('Invalid Welcome Channel Name')
            else:
                embed = discord.Embed(color=discord.colour.Color.random())
                embed.add_field(name="Welcome", value=f"{member.name} has joined {member.guild.name}", inline=False)
                embed.set_image(
                    url=WELCOME_IMAGE)
                await channel.send(embed=embed)

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        """
        :param ctx:
        :param error:
        :return:
        """
        if isinstance(error, commands.MissingRequiredArgument):
            print(f'===============================\n[ERROR] MissingRequiredArguments\n===============================\n{error}\n')
            await ctx.send(f'**Missing Required Arguments**\n```css\n{error}\n```')
        elif isinstance(error, commands.MissingPermissions):
            print(f'===============================\n[ERROR] MissingRequiredPermissions\n===============================\n{error}\n')
            await ctx.send(f'**Missing Required Permissions**\n```css\n{error}\n```')
        elif isinstance(error, commands.UserNotFound):
            print(f'===============================\n[ERROR] UserNotFound\n===============================\n{error}\n')
            await ctx.send(f'**User Not Found**\n```css\n{error}\n```')
        elif isinstance(error, commands.ChannelNotFound):
            print(f'===============================\n[ERROR] ChannelNotFound\n===============================\n{error}\n')
            await ctx.send(f'**Channel Not Found**\n```css\n{error}\n```')
        elif isinstance(error, commands.BotMissingPermissions):
            print(f'===============================\n[ERROR] BotMissingPermissions\n===============================\n{error}\n')
            await ctx.send(f'**Bot Missing Required Permissions**\n```css\n{error}\n```')
        elif isinstance(error, commands.RoleNotFound):
            print(f'===============================\n[ERROR] RoleNotFound\n===============================\n{error}\n')
            await ctx.send(f'**Role Not Found**\n```css\n{error}\n```')
        elif isinstance(error, commands.CommandError):
            print(f'===============================\n[ERROR] CommandError\n===============================\n{error}\n')
        elif isinstance(error, commands.CommandNotFound):
            print(f'===============================\n[ERROR] CommandNotFound\n===============================\n{error}\n')
        elif isinstance(error, commands.BadArgument):
            print(f'===============================\n[ERROR] BadArgument\n===============================\n{error}\n')
        elif isinstance(error, commands.UserInputError):
            print(f'===============================\n[ERROR] UserInputError\n===============================\n{error}\n')
        elif isinstance(error, commands.TooManyArguments):
            print(f'===============================\n[ERROR] TooManyArguments\n===============================\n{error}\n')
        elif isinstance(error, commands.UnexpectedQuoteError):
            print(f'===============================\n[ERROR] UnexpectedQuoteError\n===============================\n{error}\n')
        elif isinstance(error, commands.BadBoolArgument):
            print(f'===============================\n[ERROR] BadBoolArgument\n===============================\n{error}\n')
        elif isinstance(error, commands.NotOwner):
            print(f'===============================\n[ERROR] NotOwner\n===============================\n{error}\n')
        elif isinstance(error, commands.ArgumentParsingError):
            print(f'===============================\n[ERROR] ArgumentParsingError\n===============================\n{error}\n')
        elif isinstance(error, commands.BadColourArgument):
            print(f'===============================\n[ERROR] BadColourArgument\n===============================\n{error}\n')
        elif isinstance(error, commands.BadInviteArgument):
            print(f'===============================\n[ERROR] BadInviteArgument\n===============================\n{error}\n')
        elif isinstance(error, commands.BadUnionArgument):
            print(f'===============================\n[ERROR] BadUnionArgument\n===============================\n{error}\n')
        elif isinstance(error, commands.ChannelNotReadable):
            print(f'===============================\n[ERROR] ChannelNotReadable\n===============================\n{error}\n')
        elif isinstance(error, commands.BotMissingAnyRole):
            print(f'===============================\n[ERROR] BotMissingAnyRole\n===============================\n{error}\n')
        elif isinstance(error, commands.BotMissingRole):
            print(f'===============================\n[ERROR] BotMissingRole\n===============================\n{error}\n')
        elif isinstance(error, commands.CheckFailure):
            print(f'===============================\n[ERROR] CheckFailure\n===============================\n{error}\n')
        elif isinstance(error, commands.CheckAnyFailure):
            print(f'===============================\n[ERROR] CheckAnyFailure\n===============================\n{error}\n')
        elif isinstance(error, commands.ExtensionError):
            print(f'===============================\n[ERROR] ExtensionError\n===============================\n{error}\n')
        elif isinstance(error, commands.ExtensionFailed):
            print(f'===============================\n[ERROR] ExtensionFailed\n===============================\n{error}\n')
        elif isinstance(error, commands.ExpectedClosingQuoteError):
            print(f'===============================\n[ERROR] ExpectedClosingQuoteError\n===============================\n{error}\n')


def setup(client):
    client.add_cog(Events(client))