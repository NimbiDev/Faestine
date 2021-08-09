import os

import discord
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GITHUB = os.getenv('GITHUB_URL')

bot = commands.Bot(command_prefix='fae ')


class HelpEmbed(commands.HelpCommand):
    def __init__(self):
        super().__init__()
        self.bot = bot
        self.clean_prefix = self.bot.command_prefix

    def get_command_signature(self, command):
        return '%s%s %s' % (self.clean_prefix, command.qualified_name, command.signature)

    async def send_bot_help(self, mapping):
        url = GITHUB
        embed = discord.Embed(description='Here is a list of available commands.\n\n**__Note__**\nFields marked with `<>` are required.\nFields marked with `[]` are optional.')
        for cog, command in mapping.items():
            filtered = await self.filter_commands(command, sort=True)
            command_signatures = [self.get_command_signature(c) for c in filtered]
            if command_signatures:
                cog_name = getattr(cog, 'qualified_name', 'Other')
                sig = '\n'.join(command_signatures)
                embed.add_field(name='{} Commands'.format(cog_name), value='```xml\n{}```'.format(sig), inline=False)
                embed.set_image(url='https://www.autoitscript.com/forum/uploads/monthly_2020_03/tech.gif.7449db47191b0e32967887c117908b3c.gif')
                embed.set_footer(text='{} | {}'.format(self.bot.user.name, url), icon_url=self.bot.user.avatar)
        channel = self.get_destination()
        await channel.send(embed=embed)


bot.help_command = HelpEmbed()

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        bot.load_extension('cogs.{}'.format(filename[:-3]))
        print('Loaded cogs.{}'.format(filename[:-3]))

bot.run(TOKEN)
