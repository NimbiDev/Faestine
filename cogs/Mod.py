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
        authors = {}
        async for message in ctx.channel.history(limit=amount):
            if message.author not in authors:
                authors[message.author] = 1
            else:
                authors[message.author] += 1
            message.delete()

        msg = "\n".join([f"{author}:{amount}" for author, amount in authors.items()])

        await ctx.channel.purge(limit=amount + 1)
        await ctx.channel.send(msg, delete_after=20)


def setup(client):
    client.add_cog(Mod(client))
