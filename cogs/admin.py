import discord
import asyncio
from discord.ext import commands
from discord.ext.commands import CommandNotFound

command_attrs = {'hidden': False}

class Admin(commands.Cog, name='🛡️ Administrator Commands 🛡️'):
    def __init__(self, client):
        self.client = client

    @commands.command(name="purge", aliases=['fprune', 'fclean', 'fdelete'], description='Delete a specified number of messeges from the channel.', command_attrs=command_attrs)
    @commands.has_permissions(administrator=True, manage_messages=True)
    async def purge(self, ctx, amount: int):
        await ctx.message.delete()
        deleted = await ctx.channel.purge(limit=amount)
        embed = discord.Embed(
            description=f'Successfully deleted {len(deleted)} messeges.', color=discord.Color.green())
        await ctx.send(embed=embed, mention_author=False, delete_after=5)


def setup(client):
    client.add_cog(Admin(client))
