import discord
import os
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
GITHUB = os.getenv('GITHUB_URL')


class Thread(commands.Cog):
    def __init__(self, client):
        self.client = client
        self.clean_prefix = self.client.command_prefix

    @commands.group(name='thread', aliases=['t'], description='Close, or restore a thread')
    @commands.has_guild_permissions(manage_threads=True)
    async def thread(self, ctx, thread: discord.Thread):
        if ctx.invoked_subcommand is None:
            await ctx.send(':x: Invalid sub command.', delete_after=20)

    @commands.command(aliases=['delthread'], description='Close a specified thread.')
    @commands.has_guild_permissions(manage_threads=True)
    async def close(self, ctx, thread: discord.Thread):
        if ctx.invoked_subcommand is None:
            await ctx.send(':x: Invalid sub command.', delete_after=20)
        if not thread:
            await ctx.send(':x: You must specify a thread for me to delete', delete_after=20)
        else:
            name = thread.name
            await thread.delete()
            await ctx.send(':ballot_box_with_check: Successfully deleted thread: {}'.format(name), delete_after=20)

    @commands.command(aliases=['resthread'], description='Restore a specified archived thread')
    @commands.has_guild_permissions(manage_threads=True)
    async def restore(self, ctx, thread: discord.Thread):
        if ctx.invoked_subcommand is None:
            await ctx.send(':x: Invalid sub command.', delete_after=20)
        if not thread.archived:
            await ctx.send(':confused: {} is already open.'.format(thread.name), delete_after=20)
        else:
            await thread.send('{} has been restored by {}.'.format(thread.name, ctx.author.name), delete_after=20)
            await ctx.send(':ballot_box_with_check: Successfully restored thread {}'.format(thread.name), delete_after=20)


def setup(client):
    client.add_cog(Thread(client))
