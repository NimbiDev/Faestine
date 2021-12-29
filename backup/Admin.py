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



class DurationConverter(commands.Converter):
    async def convert(self, ctx, argument):
        amount = argument[:-1]
        unit = argument[-1]

        if amount.isdigit() and unit in ['m', 's']:
            return int(amount), unit

        raise commands.BadArgument(message=':x: Invalid duration...')


class Admin(commands.Cog):
    def __init__(self, client):
        self.client = client
        

    @commands.command(aliases=['k'], description='Kick a member from the guild.')
    @commands.has_guild_permissions(kick_members=True)
    async def kick(self, ctx, member: commands.MemberConverter, reason=None):
        """
        :param ctx:
        :param member:
        :param reason:
        :return:
        """
        await ctx.guild.kick(reason=reason)
        await ctx.send('Successfully kicked {} for {}.'.format(member, reason))

    @commands.command(aliases=['mb'], description='Ban multiple users for a specified reason')
    @commands.has_guild_permissions(ban_members=True)
    async def mass_ban(self, ctx, members: commands.Greedy[discord.Member],
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

    @commands.command(aliases=['b'], description='Ban a member from the guild.')
    @commands.has_guild_permissions(ban_members=True)
    async def ban(self, ctx, member: commands.MemberConverter, reason=None):
        """
        :param ctx:
        :param member:
        :param reason:
        :return:
        """
        
        embed = discord.Embed(description='**__User Banned__**', color=discord.colour.Colour.dark_red())
        await ctx.guild.ban(reason=reason)
        embed.add_field(name='User', value='{}'.format(member), inline=False)
        embed.add_field(name='Reason', value='{}'.format(reason), inline=False)
        embed.set_footer(text='{} | {}'.format(self.client.user.name, GITHUB), icon_url=self.client.user.avatar)
        await ctx.send(embed=embed)

    @commands.command(aliases=['tb'], description='Temporarily ban a member from the guild.', usage='<member> [duration]')
    @commands.has_guild_permissions(ban_members=True)
    async def temp_ban(self, ctx, member: commands.MemberConverter, duration=DurationConverter):
        """
        :param ctx:
        :param member:
        :param duration:
        :return:
        """
        
        multiplier = {'s': 1, 'm': 60}
        amount, unit = duration

        await ctx.guild.ban(member)

        embed = discord.Embed(description='**__User Temporarily Banned__**', color=discord.colour.Colour.dark_red())
        embed.add_field(name='User', value='{}'.format(member), inline=False)
        embed.add_field(name='Duration', value='{}{}'.format(amount, unit))
        embed.set_footer(text='{} | {}'.format(self.client.user.name, GITHUB), icon_url=self.client.user.avatar)

        await ctx.send(embed=embed)
        await asyncio.sleep(amount * multiplier[unit])
        await ctx.guild.unban(member)

    @commands.command(aliases=['u'], description='Unban a member from the guild.')
    @commands.has_guild_permissions(ban_members=True)
    async def unban(self, ctx, member: commands.MemberConverter):
        """
        :param ctx:
        :param member:
        :return:
        """
        
        await ctx.guild.unban(member)
        embed = discord.Embed(description='**__User Unbanned__**', color=discord.colour.Colour.dark_green())
        embed.add_field(name='User', value='{}'.format(member), inline=False)
        embed.set_footer(text='{} | {}'.format(self.client.user.name, GITHUB), icon_url=self.client.user.avatar)
        await ctx.send(embed=embed)

    @commands.command(aliases=['rank', 'r'], description='Add or remove roles from a member.')
    @commands.has_guild_permissions(manage_roles=True)
    async def role(self, ctx, member: discord.Member, *, role: discord.Role):
        
        if role.position > ctx.author.top_role.position:
            embed = discord.Embed(description=':x: The role {} is above your top role'.format(role.name),
                                  color=discord.colour.Colour.dark_red())
            embed.set_footer(text='{} | {}'.format(self.client.user.name, GITHUB), icon_url=self.client.user.avatar)
            return await ctx.send(embed=embed)
        if role in member.roles:
            await member.remove_roles(role)
            embed = discord.Embed(description='Role {} removed from {}'.format(role.name, member.display_name),
                                  color=discord.colour.Colour.dark_blue())
            embed.set_footer(text='{} | {}'.format(self.client.user.name, GITHUB), icon_url=self.client.user.avatar)
            await ctx.send(embed=embed)
        else:
            await member.add_roles(role)
            embed = discord.Embed(description='Added role {} to {}'.format(role.name, member.display_name),
                                  color=discord.colour.Colour.dark_blue())
            embed.set_footer(text='{} | {}'.format(self.client.user.name, GITHUB), icon_url=self.client.user.avatar)
            await ctx.send(embed=embed)


def setup(client):
    client.add_cog(Admin(client))
