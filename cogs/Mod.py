import discord
import os
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
GITHUB = os.getenv('GITHUB_URL')


class Mod(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.clean_prefix = self.bot.command_prefix

    @commands.command(aliases=['res_thread', 'rt', 'tr', 'thread_res'], description='Restore a specified archived thread')
    @commands.has_guild_permissions(manage_threads=True)
    async def restore_thread(self, ctx, thread: discord.Thread):
        if not thread.archived:
            await ctx.send('{} is already open.'.format(thread.name), delete_after=20)
        else:
            await thread.send('{} has been restored by {}.'.format(thread.name, ctx.author.name), delete_after=20)
            await ctx.send(':white_check_mark: Successfully restored thread {}'.format(thread.name), delete_after=20)

    @commands.command(aliases=['del_thread', 'dt', 'td', 'thread_del'], description='Delete a specified thread')
    @commands.has_guild_permissions(manage_threads=True)
    async def delete_thread(self, ctx, thread: discord.Thread):
        if not thread:
            await ctx.send(':x: You must specify a thread for me to delete', delete_after=20)
        else:
            name = thread.name
            await thread.delete()
            await ctx.send(':white_check_mark: Successfully deleted thread: {}'.format(name), delete_after=20)

    @commands.command(aliases=['clear', 'prune', 'delete'], description='Delete a specified number of messages.')
    @commands.has_guild_permissions(manage_messages=True)
    async def purge(self, ctx, amount: int):

        url = GITHUB
        embed = discord.Embed(color=discord.colour.Color.blue())
        authors = {}

        async for message in ctx.channel.history(limit=amount):
            if message.author not in authors:
                authors[message.author] = 1
            else:
                authors[message.author] += 1
            await message.delete()

        response = '\n'.join(['{}: {}'.format(author.name, amount) for author, amount in authors.items()])

        embed.add_field(name='Messages Deleted', value='```yml\n{}```'.format(response))
        embed.set_thumbnail(url=self.bot.user.avatar)
        embed.set_footer(text='{} | {}'.format(self.bot.user.name, url), icon_url=self.bot.user.avatar)

        await ctx.channel.purge(limit=amount + 1)
        await ctx.channel.send(embed=embed, delete_after=20)


def setup(bot):
    bot.add_cog(Mod(bot))
