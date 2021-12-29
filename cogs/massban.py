import discord
import asyncio
import typing
import os
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
YELLOW = discord.colour.Colour.dark_yellow()


class DurationConverter(commands.Converter):
    async def convert(self, ctx, argument):
        amount = argument[:-1]
        unit = argument[-1]

        if amount.isdigit() and unit in ['m', 's']:
            return int(amount), unit

        raise commands.BadArgument(message=':x: Invalid duration...')


class MassBan(commands.Cog):
    def __init__(self, client):
        self.client = client
        

    @commands.command(aliases=['mb'], description='Ban multiple users for a specified reason')
    @commands.has_guild_permissions(ban_members=True)
    async def massban(self, ctx, members: commands.Greedy[discord.Member],
                       delete_days: typing.Optional[int] = 0, *,
                       reason: str):
        """Mass bans members with an optional delete_days parameter"""
        embed = discord.Embed(description='**__Users Banned__**', color=discord.colour.Colour.dark_red())
        for member in members:
            await member.ban(delete_message_days=delete_days, reason=reason)
            embed.add_field(name='Users',
                            value='{}: {}#{}, '.format(member.display_name, member.name, member.discriminator),
                            inline=False)
            embed.add_field(name='Reason', value='{}'.format(reason), inline=False)
            await ctx.send(embed=embed)

   

def setup(client):
    client.add_cog(MassBan(client))
