import os

import discord
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
PREFIX = os.getenv('COMMAND_PREFIX')


class HelpEmbed(commands.HelpCommand):
    async def send_command_help(self, command):
        embed = discord.Embed(title=self.get_command_signature(command))
        embed.add_field(name="Help", value=command.help)
        alias = command.aliases
        if alias:
            embed.add_field(name="Aliases", value=", ".join(alias), inline=False)

        channel = self.get_destination()
        await channel.send(embed=embed)


bot = commands.Bot(command_prefix=commands.when_mentioned_or(PREFIX), help_command=HelpEmbed())

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        bot.load_extension(f'cogs.{filename[:-3]}')
        print(f'Loaded cogs.{filename[:-3]}')

bot.run(TOKEN)
