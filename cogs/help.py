import discord
import os

from discord.ext import commands
from discord.errors import Forbidden
from dotenv import load_dotenv

load_dotenv()
PREFIX = os.getenv('CLIENT_PREFIX')
OID = os.getenv('OWNER_ID')
ONAME = os.getenv('OWNER_NAME')
DEV_TEAM = os.getenv('DEVELOPMENT_TEAM_NAME')
GHUB_REPO = os.getenv('GITHUB_REPO')
VERSION = os.getenv('CLIENT_VERSION')

async def send_embed(ctx, embed):
    try:
        await ctx.send(embed=embed)
    except Forbidden:
        try:
            await ctx.send('Hey, seems like I can\'t send embeds. Please check my permissions :)')
        except Forbidden:
            repo = GHUB_REPO
            await ctx.author.send(
                'Hey, seems like I can\'t send any message in {} on {}\nMay you inform the development team about this issue? :slight_smile: \n{}'.format(ctx.channel.name, ctx.guild.name, repo) , embed=embed)

class Help(commands.Cog):
    def __init__(self, client):
        self.client = client
        

    @commands.command(name='help', aliases=['h', 'cmds', 'commands', 'cmdhelp'], description='Display a full list of all of my available commands.')
    @commands.bot_has_permissions(add_reactions=True,embed_links=True)
    async def _help(self, ctx, *input):
        client_prefix = PREFIX
        version_number = VERSION
        owner_id = OID
        team_name = DEV_TEAM
        github_repo = GHUB_REPO
        owner_name = ONAME
        	     
        if not input:
            try:
                owner = ctx.guild.get_member(owner_id).mention

            except AttributeError as e:
                owner = owner_name
                team = team_name
                repo = github_repo
                prefix = client_prefix
                version = version_number

            emb = discord.Embed(title='Commands and modules', color=discord.Color.blue(),
                                description='Use `{}help <module>` to gain more information about that module :smiley:\n'.format(prefix))

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

            emb.add_field(name='About', value='This bot is developed by {}, based on discord.py.\n\
                                    This version of it is maintained by {}\n\
                                    Please visit {} to submit ideas or bugs.'.format(owner, team, repo))
            emb.set_footer(text=f'Bot is running {version}')

        elif len(input) == 1:

            for cog in self.client.cogs:
                if cog.lower() == input[0].lower():

                    emb = discord.Embed(title=f'{cog} - Commands', description=self.client.cogs[cog].__doc__,
                                        color=discord.Color.green())

                    for command in self.client.get_cog(cog).get_commands():
                        prefix = client_prefix
                        if not command.hidden:
                            emb.add_field(name='`{}{}`'.format(prefix, command.name), value=command.help, inline=False)
                    break

            else:
                emb = discord.Embed(title='What\'s that?!',
                                    description='I\'ve never heard from a module called `{}` before :scream:'.format(input[0]),
                                    color=discord.Color.orange())

        elif len(input) > 1:
            emb = discord.Embed(title='That\'s too much.',
                                description='Please request only one module at once :sweat_smile:',
                                color=discord.Color.orange())

        else:
            owner = owner_name
            repo = github_repo
                        
            emb = discord.Embed(title='It\'s a magical place.',
                                description='I don\'t know how you got here. But I didn\'t see this coming at all.\n'
                                            'Would you please be so kind to report that issue to me on github?\n'
                                            '{}\n'.format(repo)
                                            'Thank you! ~{}'.format(owner),
                                color=discord.Color.red())

        await send_embed(ctx, emb)


def setup(client):
    client.add_cog(Help(client))