import discord
import asyncio
import typing
import os
from discord.ext import commands

GITHUB = 'github.com/DevCorner-Github/Faestine'

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


class TempBan(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(aliases=['tb'], description='Temporarily ban a member from the guild.', usage='<member> [duration]')
    @commands.has_guild_permissions(ban_members=True)
    async def tempban(self, ctx, member: commands.MemberConverter, duration=DurationConverter):
        """
        :param ctx:
        :param member:
        :param duration:
        :return:
        """
        client = self.client

        multiplier = {'s': 1, 'm': 60}
        amount, unit = duration

        await ctx.guild.ban(member)

        embed = discord.Embed(
            description='**__User Temporarily Banned__**', color=RED)
        embed.add_field(name='User', value='{}'.format(member), inline=False)
        embed.add_field(name='Duration', value='{}{}'.format(amount, unit))
        embed.set_footer(text='{} | {}'.format(
            client.user.name, GITHUB), icon_url=client.user.avatar)

        await ctx.send(embed=embed)
        await asyncio.sleep(amount * multiplier[unit])
        await ctx.guild.unban(member)


def setup(client):
    client.add_cog(TempBan(client))
