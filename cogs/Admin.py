import discord
import asyncio
from discord.ext import commands


class Admin(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    class DurationConverter(commands.Converter):
        async def convert(self, ctx, argument):
            amount = argument[:-1]
            unit = argument[-1]

            if amount.isdigit() and unit in ['m', 's']:
                return int(amount), unit

            raise commands.BadArgument(message=':x: Invalid duration...')

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
        await ctx.send(f'Successfully kicked {member} for {reason}.')

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
        await ctx.send(f'Successfully banned {member} for {reason}.')

    @commands.command(aliases=['tb'], description='Temporarily ban a member from the guild.')
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
        await ctx.send(f'Temporarily banned {member} for {amount}{unit}.')
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
        await ctx.send(f'Successfully unbanned {member}.')

    @commands.command(aliases=['rank', 'r'], description='Add or remove roles from a member.')
    @commands.has_guild_permissions(manage_roles=True)
    async def role(self, ctx, member: discord.Member, *, role: discord.Role):
        if role.position > ctx.author.top_role.position:
            return await ctx.send(':x: | That role is above your top role!')
        if role in member.roles:
            await member.remove_roles(role)
            await ctx.send(f"Removed {role.name} from {member.display_name}")
        else:
            await member.add_roles(role)
            await ctx.send(f"Added {role.name} to {member.display_name}")


def setup(bot):
    bot.add_cog(Admin(bot))
