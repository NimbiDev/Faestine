import os

import discord
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
PREFIX = os.getenv('COMMAND_PREFIX')


class HELP(commands.HelpCommand):
    def __init__(self):
        super().__init__()

    async def send_bot_help(self, mapping):
        for cog in mapping:
            await self.get_destination().send(
                f'**{cog.qualified_name}**: `{[command.name for command in mapping[cog]]}`')

    async def send_cog_help(self, cog):
        await self.get_destination().send(
            f'**{cog.qualified_name}**: `{[command.name for command in cog.get_commands()]}`')

    async def send_group_help(self, group):
        await self.get_destination().send(
            f'**{group.name}**: `{[command.name for index, command in enumerate(group.commands)]}`')

    async def send_command_help(self, command):
        await self.get_destination().send(
            f'**{command.name}**: `{command.description}`\n```yaml\nAliases: {command.aliases}\n```\n```yaml\n{command.usage}\n```')


client = commands.Bot(command_prefix=PREFIX, help_command=HELP())

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')
        print(f'Loaded cogs.{filename[:-3]}')

client.run(TOKEN)
