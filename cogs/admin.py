import discord
import asyncio
from discord.ext import commands


class Admin(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(name="purge", aliases=['fprune', 'fclean', 'fdelete'], description='Delete a specified number of messeges from the channel.')
    @commands.has_permissions(manage_messeges=True)
    async def purge(self, ctx, amount: int):
        deleted = await ctx.channel.purge(limit=amount)
        e = discord.embed(
            title='Purge',
            description='Successfully deleted {} messeges.'.format(
                len(deleted)),
            color=discord.Color.green()
        )
        await ctx.send(embed=e, mention_auther=False)


def setup(client):
    client.add_cog(Admin(client))
