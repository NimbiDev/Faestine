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



class DurationConverter(commands.Converter):
    async def convert(self, ctx, argument):
        amount = argument[:-1]
        unit = argument[-1]

        if amount.isdigit() and unit in ['m', 's']:
            return int(amount), unit

        raise commands.BadArgument(message=':x: Invalid duration...')


class UnBan(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(aliases=['u'], description='Unban a member from the guild.')
    @commands.has_guild_permissions(ban_members=True)
    async def unban(self, ctx, member: commands.MemberConverter):
        """
        :param ctx:
        :param member:
        :return:
        """
        client = self.client
        await ctx.guild.unban(member)
        embed = discord.Embed(
            description='**__User Unbanned__**', color=GREEN)
        embed.add_field(name='User', value='{}'.format(member), inline=False)
        embed.set_footer(text='{} | {}'.format(
            client.user.name, GITHUB), icon_url=client.user.avatar)
        await ctx.send(embed=embed)


def setup(client):
    client.add_cog(UnBan(client))
