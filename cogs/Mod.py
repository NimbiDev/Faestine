import discord
import os
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
PREFIX = os.getenv('COMMAND_PREFIX')


class Mod(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=['restore', 'tr'], description='Restore a specified archived thread')
    @commands.has_guild_permissions(manage_threads=True)
    async def restore_thread(self, ctx, thread: discord.Thread):
        if not thread.archived:
            await ctx.reply('{} is already open.'.format(thread.name), delete_after=20)
        else:
            await thread.send('The thread has been restored.', delete_after=20)
            await ctx.reply('Restoring thread: {}'.format(thread.name), delete_after=20)

    @commands.command(aliases=['clear', 'prune', 'delete'], description='Delete a specified number of messages.')
    @commands.has_guild_permissions(manage_messages=True)
    async def purge(self, ctx, amount: int):
        authors = {}
        async for message in ctx.channel.history(limit=amount):
            if message.author not in authors:
                authors[message.author] = 1
            else:
                authors[message.author] += 1
            await message.delete()

        msg = "\n".join([f'{author}: {amount}' for author, amount in authors.items()])

        await ctx.channel.purge(limit=amount + 1)
        await ctx.channel.send(f'**__Messages Purged__**\n```yaml\n{msg}\n```', delete_after=20)


def setup(bot):
    bot.add_cog(Mod(bot))
