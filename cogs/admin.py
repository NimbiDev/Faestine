from config import GREEN, PREFIX, RED
import discord
import asyncio
from discord.ext import commands

command_attrs = {'hidden': False}

class Admin(commands.Cog, name='Administrator Commands'):
    def __init__(self, client):
        self.client = client

    @commands.command(name="purge", aliases=['prune', 'clean', 'delete'], description='Delete a specified number of messeges from the channel.\n\n**Example**: `{}purge 25`'.format(PREFIX), command_attrs=command_attrs)
    @commands.has_permissions(manage_messages=True)
    @commands.cooldown(1, 10, commands.BucketType.user)
    async def purge(self, ctx, amount: int):
        await ctx.message.delete()
        deleted = await ctx.channel.purge(limit=amount)
        e = discord.Embed(
            description=f'\✅ Successfully deleted {len(deleted)} messeges.',
            color=GREEN
            )
        await ctx.send(embed=e, mention_author=False, delete_after=5)
        
    @commands.command(name="ban", description='Ban a member form the guild for a specified reason.\n\n**Example**: {}ban @JohnDoe Harrassment'.format(PREFIX), command_attrs=command_attrs)
    @commands.has_permissions(ban_members=True)
    @commands.cooldown(1, 10, commands.BucketType.user)
    async def _ban (self, ctx, member:discord.User=None, reason =None):
        if member == None or member == ctx.author:
            await ctx.send("\⛔ You cannot ban yourself")
            return
        if reason == None:
            reason = "No reason provided"
        await member.ban(reason = reason)
        e = discord.Embed(description='User Ban Issued', color=RED)
        e.add_field(name='Member', value=member, inline=False)
        e.add_filed(name='Reason', value=reason, inline=False)
        await ctx.send(embed=e, mention_author=False)
        
    @commands.command(name='unban', description='Unban a member from the guild.\n\n**Example**: {}unban JohnDoe#0000'.format(PREFIX), command_attrs=command_attrs)
    @commands.has_permissions(ban_members=True)
    @commands.cooldown(1, 10, commands.BucketType.user)
    async def _unban(self, ctx, *, member):
        banned_users = await ctx.guild.bans()
        member_name, member_discriminator = member.split("#")

        for ban_entry in banned_users:
            user = ban_entry.user

            if (user.name, user.discriminator) == (member_name, member_discriminator):
                await ctx.guild.unban(user)
                e = discord.Embed(description='User Ban Revoked', color=GREEN)
                e.add_field(name='Member', value=user.mention, inline=False)
                await ctx.send(embed=e, mention_author=False)
                return

def setup(client):
    client.add_cog(Admin(client))
