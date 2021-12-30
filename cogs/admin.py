import discord
import asyncio
from discord.ext import commands
from discord.ext.commands import CommandNotFound


class Admin(commands.Cog, description='Administration commands to help manage your server.'):
    def __init__(self, client):
        self.client = client

    @commands.command(name="purge", aliases=['fprune', 'fclean', 'fdelete'], description='Delete a specified number of messeges from the channel.')
    @commands.has_permissions(administrator=True, manage_messages=True)
    async def purge(self, ctx, amount: int):
        await ctx.message.delete()
        deleted = await ctx.channel.purge(limit=amount)
        embed = discord.Embed(
            description=f'Successfully deleted {len(deleted)} messeges.', color=discord.Color.green())
        await ctx.send(embed=embed, mention_author=False, delete_after=5)

    @commands.command(name='banlist', aliases=['blist'], description='Get a list of banned users in the guild.')
    @commands.has_permissions(administrator=True, ban_members=True)
    async def banlist(self, ctx):
        client = self.client
        message = ctx.message
        orange = discord.Color.orange()

        bans = await client.get_bans(message.guild.id)
        for ban in bans:
            user = ban['user']
            reason = ban['reason']

        embed = discord.Embed(
            description='**{}**: {}'.format(user, reason), color=orange)
        await ctx.send(embed=embed, mention_author=False)


def setup(client):
    client.add_cog(Admin(client))
