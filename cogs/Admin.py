import discord
import asyncio
from discord.ext import commands


class DurationConverter(commands.Converter):
    async def convert(self, ctx, argument):
        amount = argument[:-1]
        unit = argument[-1]

        if amount.isdigit() and unit in ['m', 's']:
            return int(amount), unit

        raise commands.BadArgument(message=':x: Invalid duration...')


class Admin(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.clean_prefix = 'fae '

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

    @commands.command(aliases=['b'], description='Ban a member from the guild.')
    @commands.has_guild_permissions(ban_members=True)
    async def ban(self, ctx, member: commands.MemberConverter, reason=None):
        """
        :param ctx:
        :param member:
        :param reason:
        :return:
        """
        await ctx.guild.ban(reason=reason)
        await ctx.send('Successfully banned {} for {}.'.format(member, reason))

    @commands.command(aliases=['tb'], description='Temporarily ban a member from the guild.', usage='fae temp_ban <member> [duration]')
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
        await ctx.send('Temporarily banned {} for {}{}.'.format(member, amount, unit))
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
        await ctx.send('Successfully unbanned {}.'.format(member))

    @commands.command(aliases=['rank', 'r'], description='Add or remove roles from a member.')
    @commands.has_guild_permissions(manage_roles=True)
    async def role(self, ctx, member: discord.Member, *, role: discord.Role):
        if role.position > ctx.author.top_role.position:
            return await ctx.send(':x: The role {} is above your top role.'.format(role.name))
        if role in member.roles:
            await member.remove_roles(role)
            await ctx.send('Removed {} from {}'.format(role.name, member.display_name))
        else:
            await member.add_roles(role)
            await ctx.send('Added {} to {}'.format(role.name, member.display_name))


def setup(bot):
    bot.add_cog(Admin(bot))
