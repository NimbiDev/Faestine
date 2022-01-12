import os
import sys
import time
import asyncio
import discord
import logging

from discord.ext import commands
from discord.ext.commands import CommandNotFound
from typing import List
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('CLIENT_TOKEN')
PREFIX = os.getenv('CLIENT_PREFIX')
TWITCH = os.getenv('TWITCH_CHANNEL')
ERR_FILE = os.getenv('ERROR_FILE')
DBUG_FILE = os.getenv('DEBUG_FILE')


activity = discord.Streaming(name='with cogs | {}help'.format(
    PREFIX), url='https://twitch.tv/{}'.format(TWITCH))


client = commands.Bot(
    command_prefix=commands.when_mentioned_or('{}'.format(PREFIX)),
    description='Discord client',
    activity=activity,
    status=discord.Status.online
)

client.remove_command('help')
initial_extensions = [
        'cogs.help',
            ]  

class Help(commands.Cog):
    """
    Sends this help message
    """

    def __init__(self, client):
        self.client = client
        

    @commands.command()
    # @commands.bot_has_permissions(add_reactions=True,embed_links=True)
    async def help(self, ctx, *input):
        
        """Shows all modules of that bot"""
        
        prefix = PREFIX
        version = VERSION
        owner = OID
        owner_name = ONAME
        	     
        if not input:
            try:
                owner = ctx.guild.get_member(owner).mention

            except AttributeError as e:
                owner = owner

            emb = discord.Embed(title='Commands and modules', color=discord.Color.blue(),
                                description=f'Use `{prefix}help <module>` to gain more information about that module '
                                            f':smiley:\n')

            cogs_desc = ''
            for cog in self.client.cogs:
                cogs_desc += f'`{cog}` {self.client.cogs[cog].__doc__}\n'

            emb.add_field(name='Modules', value=cogs_desc, inline=False)

            commands_desc = ''
            for command in self.client.walk_commands():
                
                if not command.cog_name and not command.hidden:
                    commands_desc += f'{command.name} - {command.help}\n'

            if commands_desc:
                emb.add_field(name='Not belonging to a module', value=commands_desc, inline=False)

            emb.add_field(name="About", value=f"The Bots is developed by Chriѕ#0001, based on discord.py.\n\
                                    This version of it is maintained by {owner}\n\
                                    Please visit https://github.com/nonchris/discord-fury to submit ideas or bugs.")
            emb.set_footer(text=f"Bot is running {version}")

        elif len(input) == 1:

            for cog in self.client.cogs:
                if cog.lower() == input[0].lower():

                    emb = discord.Embed(title=f'{cog} - Commands', description=self.client.cogs[cog].__doc__,
                                        color=discord.Color.green())

                    for command in self.client.get_cog(cog).get_commands():
                        if not command.hidden:
                            emb.add_field(name=f"`{prefix}{command.name}`", value=command.help, inline=False)
                    break

            else:
                emb = discord.Embed(title="What's that?!",
                                    description=f"I've never heard from a module called `{input[0]}` before :scream:",
                                    color=discord.Color.orange())

        elif len(input) > 1:
            emb = discord.Embed(title="That's too much.",
                                description="Please request only one module at once :sweat_smile:",
                                color=discord.Color.orange())

        else:
            emb = discord.Embed(title="It's a magical place.",
                                description="I don't know how you got here. But I didn't see this coming at all.\n"
                                            "Would you please be so kind to report that issue to me on github?\n"
                                            "https://github.com/nonchris/discord-fury/issues\n"
                                            "Thank you! ~Chris",
                                color=discord.Color.red())

        await send_embed(ctx, emb)
        
# class Help(commands.Cog):
#     def __init__(self, client):
#         self.client = client


# class CustomHelp(commands.MinimalHelpCommand):
#     async def send_pages(self):
#         destination = self.get_destination()
#         embed = discord.Embed(color=discord.Color.blurple(), description='')
#         for page in self.paginator.pages:
#             embed.description += page
#             await destination.send(embed=embed)


# client.help_command = CustomHelp()

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension('cogs.{}'.format(filename[:-3]))
        print(f'Loaded cogs.{filename[:-3]}')
    else:
        print(f'Unable to load cogs.{filename[:-3]}')
        
# for filename in os.listdir('./cogs/admin'):
#     if filename.endswith('.py'):
#         client.load_extension('cogs.{}'.format(filename[:-3]))
#         print('Loaded cogs.{}'.format(filename[:-3]))
#     else:
#         print('Unable to load cogs.{}'.format(filename[:-3]))
        
# for filename in os.listdir('./cogs/mod'):
#     if filename.endswith('.py'):
#         client.load_extension('cogs.{}'.format(filename[:-3]))
#         print('Loaded cogs.{}'.format(filename[:-3]))
#     else:
#         print('Unable to load cogs.{}'.format(filename[:-3]))

# for filename in os.listdir('./cogs/events'):
#     if filename.endswith('.py'):
#         client.load_extension('cogs.{}'.format(filename[:-3]))
#         print('Loaded cogs.{}'.format(filename[:-3]))
#     else:
#         print('Unable to load cogs.{}'.format(filename[:-3]))

# for filename in os.listdir('./cogs/images'):
#     if filename.endswith('.py'):
#         client.load_extension('cogs.{}'.format(filename[:-3]))
#         print('Loaded cogs.{}'.format(filename[:-3]))
#     else:
#         print('Unable to load cogs.{}'.format(filename[:-3]))

# for filename in os.listdir('./cogs/owner'):
#     if filename.endswith('.py'):
#         client.load_extension('cogs.{}'.format(filename[:-3]))
#         print('Loaded cogs.{}'.format(filename[:-3]))
#     else:
#         print('Unable to load cogs.{}'.format(filename[:-3]))

# for filename in os.listdir('./cogs/social'):
#     if filename.endswith('.py'):
#         client.load_extension('cogs.{}'.format(filename[:-3]))
#         print('Loaded cogs.{}'.format(filename[:-3]))
#     else:
#         print('Unable to load cogs.{}'.format(filename[:-3]))

# for filename in os.listdir('./cogs/util'):
#     if filename.endswith('.py'):
#         client.load_extension('cogs.{}'.format(filename[:-3]))
#         print('Loaded cogs.{}'.format(filename[:-3]))
#     else:
#         print('Unable to load cogs.{}'.format(filename[:-3]))

error_logger = logging.getLogger('discord')
debug_logger = logging.getLogger('discord')
debug_logger.setLevel(logging.DEBUG)
error_logger.setLevel(logging.ERROR)
debug_handler = logging.FileHandler(filename=DBUG_FILE, encoding='utf-8', mode='w')
error_handler = logging.FileHandler(filename=ERR_FILE, encoding='utf-8', mode='w')
debug_handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
error_handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
debug_logger.addHandler(debug_handler)
error_logger.addHandler(error_handler)

client.run('{}'.format(TOKEN))
