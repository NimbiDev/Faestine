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


class Role(commands.Cog):
    def __init__(self, client):
        self.client = client
        

    @commands.command(aliases=['rank', 'r'], description='Add or remove roles from a member.')
    @commands.has_guild_permissions(manage_roles=True)
    async def role(self, ctx, member: discord.Member, *, role: discord.Role):
        
        if role.position > ctx.author.top_role.position:
            embed = discord.Embed(description=':x: The role {} is above your top role'.format(role.name),
                                  color=RED)
            embed.set_footer(text='{} | {}'.format(
                self.client.user.name, GITHUB), icon_url=self.client.user.avatar)
            return await ctx.send(embed=embed)
        if role in member.roles:
            await member.remove_roles(role)
            embed = discord.Embed(description='Role {} removed from {}'.format(role.name, member.display_name),
                                  color=discord.colour.Colour.dark_blue())
            embed.set_footer(text='{} | {}'.format(
                self.client.user.name, GITHUB), icon_url=self.client.user.avatar)
            await ctx.send(embed=embed)
        else:
            await member.add_roles(role)
            embed = discord.Embed(description='Added role {} to {}'.format(role.name, member.display_name),
                                  color=discord.colour.Colour.dark_blue())
            embed.set_footer(text='{} | {}'.format(
                self.client.user.name, GITHUB), icon_url=self.client.user.avatar)
            await ctx.send(embed=embed)


def setup(client):
    client.add_cog(Role(client))
