import discord
import asyncio
from discord.ext import commands


class Admin(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(name="purge", aliases=['fprune', 'fclean', 'fdelete'], description='Delete a specified number of messeges from the channel.')
    @commands.has_permissions(administrator=True, manage_messages=True)
    async def purge(self, ctx, amount: int):
        await ctx.message.delete()
        deleted = await ctx.channel.purge(limit=amount)
        embed = discord.Embed(title='Purge', description=f'Successfully deleted {len(deleted)} messeges.', color=discord.Color.green())
        await ctx.send(embed=embed, mention_author=False, delete_after=20)


def setup(client):
    client.add_cog(Admin(client))
