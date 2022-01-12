import discord

from env import PREFIX, OID, ONAME, DEV_TEAM, GHUB_REPO, VERSION
from discord.ext import commands
from discord.ext.commands import CommandNotFound
from discord.errors import Forbidden

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
        

    @commands.command(name='help', aliases=['h', 'cmds', 'commands', 'cmdhelp'], description='Display a full list of all of my available commands.', help='help')
    @commands.bot_has_permissions(add_reactions=True,embed_links=True)
    async def _help(self, ctx, *input):
        
        owner_id = OID
        	     
        if not input:
            try:
                owner = ctx.guild.get_member(owner_id).mention

            except AttributeError as e:
                owner = ONAME
                team = DEV_TEAM
                repo = GHUB_REPO
                prefix = PREFIX
                version = VERSION

            emb = discord.Embed(title='Commands and modules', color=discord.Color.blue(),
                                description='Use `{}help <module>` to gain more information about that module :smiley:\n'.format(prefix))

            cogs_desc = ''
            for cog in self.client.cogs:
                cogs_desc += '`{}` {}\n'.format(cog, self.client.cogs[cog].__doc__)

            emb.add_field(name='Modules', value=cogs_desc, inline=False)

            commands_desc = ''
            for command in self.client.walk_commands():
                
                if not command.cog_name and not command.hidden:
                    commands_desc += '{} - {}\n'.format(command.name, command.help)

            if commands_desc:
                emb.add_field(name='Not belonging to a module', value=commands_desc, inline=False)

            emb.add_field(name='About', value='This bot is developed by {}, based on discord.py.\n\
                                    This version of it is maintained by {}\n\
                                    Please visit {} to submit ideas or bugs.'.format(owner, team, repo))
            emb.set_footer(text='{} - Version: {}'.format(self.client.user.name, version))

        elif len(input) == 1:

            for cog in self.client.cogs:
                if cog.lower() == input[0].lower():

                    emb = discord.Embed(title=f'{cog} - Commands', description=self.client.cogs[cog].__doc__,
                                        color=discord.Color.green())

                    for command in self.client.get_cog(cog).get_commands():
                        if not command.hidden:
                            emb.add_field(name='`{}{}`'.format(PREFIX, command.name), value=command.help, inline=False)
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
            owner = ONAME
            repo = GHUB_REPO
                        
            emb = discord.Embed(title='It\'s a magical place.',
                                description='I don\'t know how you got here. But I didn\'t see this coming at all.\n'
                                            'Would you please be so kind to report that issue to me on github?\n'
                                            '{}\n'
                                            'Thank you! ~{}'.format(repo, owner),
                                color=discord.Color.red())

        await send_embed(ctx, emb)


def setup(client):
    client.add_cog(Help(client))