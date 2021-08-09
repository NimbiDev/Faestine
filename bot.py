import os

import discord
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

bot = commands.Bot(command_prefix='fae ')


class HelpEmbed(commands.HelpCommand):
    def __init__(self):
        super().__init__()
        self.bot = bot
        self.clean_prefix = self.bot.command_prefix

    def get_command_signature(self, command):
        return '%s%s %s' % (self.clean_prefix, command.qualified_name, command.signature)

    async def send_bot_help(self, mapping):
        for cog, command in mapping.items():
            filtered = await self.filter_commands(command, sort=True)
            command_signatures = [self.get_command_signature(c) for c in filtered]
            if command_signatures:
                cog_name = getattr(cog, 'qualified_name', 'Other')
                sig = '\n'.join(command_signatures)
                channel = self.get_destination()
                emb = discord.Embed(description='**__{} Commands__**\n```xml\n{}```'.format(cog_name, sig))
                emb.colour(discord.Colour.blue())
                emb.timestamp()
                emb.set_footer(text=self.bot.user.name, icon_url=self.bot.user.avatar)
                await channel.send(embed=emb)


bot.help_command = HelpEmbed()

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        bot.load_extension('cogs.{}'.format(filename[:-3]))
        print('Loaded cogs.{}'.format(filename[:-3]))

bot.run(TOKEN)
