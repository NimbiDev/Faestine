import discord
import os
import logging
import chalk

from config import DARKRED, PREFIX
from discord.ext import commands


class Events(commands.Cog, name='Events', description='Events and triggeres that run in the background.'):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        c = self.client
        print(chalk.white('-------------------------------------------------------------'))
        print(chalk.green('>>| Logged in as {} (ID: {})'.format(c.user, c.user.id)))
        print(chalk.white('-------------------------------------------------------------'))

    @commands.Cog.listener()
    async def on_messege_delete(self, ctx, messege):
        return

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        
        error_message = '\⛔ {}'.format(error)
        
        if isinstance(error, commands.CommandNotFound):
            return
        else:
            e = discord.Embed(
                description=error_message,
                color=DARKRED
            )
            await ctx.send(embed=e, mention_author=False)
            print(chalk.yellow(f'>>| {error}'))
            # Uncommit the below line when debugging
            # raise error
        
        
def setup(client):
    client.add_cog(Events(client))
