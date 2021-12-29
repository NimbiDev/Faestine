import discord
import asyncio
import typing
import os
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
GITHUB = os.getenv('GITHUB_URL')


class DurationConverter(commands.Converter):
    async def convert(self, ctx, argument):
        amount = argument[:-1]
        unit = argument[-1]

        if amount.isdigit() and unit in ['m', 's']:
            return int(amount), unit

        raise commands.BadArgument(message=':x: Invalid duration...')


class Ban(commands.Cog):
    def __init__(self, client):
        self.client = client
        

    @commands.command(aliases=['b'], description='Ban a member from the guild.')
    @commands.has_guild_permissions(ban_members=True)
    async def ban(self, ctx, member: commands.MemberConverter, reason=None):
        """
        :param ctx:
        :param member:
        :param reason:
        :return:
        """
        github_url = GITHUB
        embed = discord.Embed(description='**__User Banned__**', color=discord.colour.Colour.dark_red())
        await ctx.guild.ban(reason=reason)
        embed.add_field(name='User', value='{}'.format(member), inline=False)
        embed.add_field(name='Reason', value='{}'.format(reason), inline=False)
        embed.set_footer(text='{} | {}'.format(self.client.user.name, github_url), icon_url=self.client.user.avatar)
        await ctx.send(embed=embed)

def setup(client):
    client.add_cog(Ban(client))
