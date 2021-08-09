import os

import discord
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

bot = commands.Bot(command_prefix="fae ")


class HelpEmbed(commands.HelpCommand):
    def __init__(self):
        super().__init__()
        self.clean_prefix = "fae "

    def get_command_signature(self, command):
        return '%s%s %s' % (self.clean_prefix, command.qualified_name, command.signature)

    async def send_bot_help(self, mapping):
        emb = discord.Embed(title='Help')
        for cog, command in mapping.items():
            filtered = await self.filter_commands(command, sort=True)
            command_signatures = [self.get_command_signature(c) for c in filtered]
            if command_signatures:
                cog_name = getattr(cog, 'qualified_name', 'Other')
                emb.add_field(name=cog_name, value='\n```yaml'.join(command_signatures) + '```', inline=False)

        channel = self.get_destination()
        await channel.send(embed=emb)


bot.help_command = HelpEmbed()

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        bot.load_extension(f'cogs.{filename[:-3]}')
        print(f'Loaded cogs.{filename[:-3]}')

bot.run(TOKEN)
