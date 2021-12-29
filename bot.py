import os

import discord
from discord.ext import commands

from dotenv import load_dotenv


load_dotenv()
TOKEN = os.getenv('CLIENT_TOKEN')
GITHUB = os.getenv('GITHUB_URL')
PREFIX = os.getenv('CLIENT_PREFIX')

client = commands.Bot(command_prefix=PREFIX)


class HelpEmbed(commands.HelpCommand):
    def __init__(self):
        super().__init__()
        self.client = client
        self.clean_prefix = self.client.command_prefix

    def get_command_signature(self, command):
        return '%s%s %s' % (self.clean_prefix, command.qualified_name, command.signature)

    async def send_bot_help(self, mapping):
        url = GITHUB
        embed = discord.Embed(
            description='Here is a list of available commands.\n\n**__Note__**\nFields marked with `<>` are required.\nFields marked with `[]` are optional.', color=discord.colour.Color.dark_blue())
        for cog, command in mapping.items():
            filtered = await self.filter_commands(command, sort=True)
            command_signatures = [
                self.get_command_signature(c) for c in filtered]
            if command_signatures:
                cog_name = getattr(cog, 'qualified_name', 'Other')
                sig = '\n'.join(command_signatures)
                embed.add_field(name='{} Commands'.format(
                    cog_name), value='```xml\n{}```'.format(sig), inline=False)
                embed.set_image(url=self.client.user.avatar)
                embed.set_footer(text='{} | {}'.format(
                    self.client.user.name, url), icon_url=self.client.user.avatar)
        channel = self.get_destination()
        await channel.send(embed=embed)


client.help_command = HelpEmbed()

# for filename in os.listdir('./cogs'):
#     if filename.endswith('.py'):
#         client.load_extension('cogs.{}'.format(filename[:-3]))
#         print('Loaded cogs.{}'.format(filename[:-3]))

for filename in os.listdir(f"{filename}/*"):
    for filename in os.listdir(f"{filename}/*"):
        if filename.endswith('.py'):
            filename = filename[5:-3]
            print(f"Loaded " + filename.replace('\\', '.'))
            client.load_extension("cogs." + filename.replace('\\', '.'))

client.run(TOKEN)