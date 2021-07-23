import discord
import os
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
PREFIX = os.getenv('COMMAND_PREFIX')


class Mod(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(aliases=['clear', 'prune', 'delete'],
                      description='Delete a specified number of messages.',
                      usage=f'Usage: {PREFIX}purge [amount]\nExample: {PREFIX}purge 99')
    @commands.has_guild_permissions(manage_messages=True)
    async def purge(self, ctx, amount: int):
        await ctx.channel.purge(limit=amount + 1)
        await ctx.send(f'Successfully deleted {amount} messages.', delete_after=20)


def setup(client):
    client.add_cog(Mod(client))
