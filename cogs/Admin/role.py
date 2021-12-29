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


class Role(commands.Cog):
    def __init__(self, client):
        self.client = client
        

    @commands.command(aliases=['rank', 'r'], description='Add or remove roles from a member.')
    @commands.has_guild_permissions(manage_roles=True)
    async def role(self, ctx, member: discord.Member, *, role: discord.Role):
        github_url = GITHUB
        if role.position > ctx.author.top_role.position:
            embed = discord.Embed(description=':x: The role {} is above your top role'.format(role.name),
                                  color=discord.colour.Colour.dark_red())
            embed.set_footer(text='{} | {}'.format(
                self.client.user.name, github_url), icon_url=self.client.user.avatar)
            return await ctx.send(embed=embed)
        if role in member.roles:
            await member.remove_roles(role)
            embed = discord.Embed(description='Role {} removed from {}'.format(role.name, member.display_name),
                                  color=discord.colour.Colour.dark_blue())
            embed.set_footer(text='{} | {}'.format(
                self.client.user.name, github_url), icon_url=self.client.user.avatar)
            await ctx.send(embed=embed)
        else:
            await member.add_roles(role)
            embed = discord.Embed(description='Added role {} to {}'.format(role.name, member.display_name),
                                  color=discord.colour.Colour.dark_blue())
            embed.set_footer(text='{} | {}'.format(
                self.client.user.name, github_url), icon_url=self.client.user.avatar)
            await ctx.send(embed=embed)


def setup(client):
    client.add_cog(Role(client))
