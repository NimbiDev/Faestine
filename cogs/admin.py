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


def setup(client):
    client.add_cog(Admin(client))
