import os

import discord
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
PREFIX = os.getenv('COMMAND_PREFIX')


class HelpEmbed(commands.MinimalHelpCommand):
    async def send_pages(self):
        destination = self.get_destination()
        for page in self.paginator.pages:
            help_embed = discord.Embed(description=page)
            await destination.send(embed=help_embed)


bot = commands.Bot(command_prefix=commands.when_mentioned_or(PREFIX), help_command=HelpEmbed())

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        bot.load_extension(f'cogs.{filename[:-3]}')
        print(f'Loaded cogs.{filename[:-3]}')

bot.run(TOKEN)
