import discord
import os

from env import PREFIX, THUMBNAIL, IMAGE, BLUE
from discord.ext import commands
from discord.ext.commands import CommandNotFound


class Help(commands.Cog):
    def __init__(self, client):
        self.client = client
    
    @commands.command(name='help', aliases=['h'], )
    @commands.has_permissions(add_reactions=True,embed_links=True)
    async def help(self,ctx,*cog):
        
        """Gets all cogs and commands of mine."""
        
        try:
            
            if not cog:
                
                halp=discord.Embed(title='Cog Listing and Uncatergorized Commands', description='Use `!help *cog*` to find out more about them!\n(BTW, the Cog Name Must Be in Title Case, Just Like this Sentence.)')
                cogs_desc = ''
                for x in self.client.cogs:
                    cogs_desc += ('{} - {}'.format(x,self.client.cogs[x].__doc__)+'\n')
                    halp.add_field(name='Cogs',value=cogs_desc[0:len(cogs_desc)-1],inline=False)
                    cmds_desc = ''
                    for y in self.client.walk_commands():
                        if not y.cog_name and not y.hidden:
                            cmds_desc += ('{} - {}'.format(y.name,y.help)+'\n')
                            halp.add_field(name='Uncatergorized Commands',value=cmds_desc[0:len(cmds_desc)-1],inline=False)
                            await ctx.message.add_reaction(emoji='✉')
                            await ctx.message.author.send('',embed=halp)
                else:
                    if len(cog) > 1:
                        halp = discord.Embed(title='Error!',description='That is way too many cogs!',color=discord.Color.red())
                        await ctx.message.author.send('',embed=halp)
                    else:
                        found = False
                for x in self.client.cogs:
                    for y in cog:
                        if x == y:
                            halp=discord.Embed(title=cog[0]+' Command Listing',description=self.client.cogs[cog[0]].__doc__)
                            for c in self.client.get_cog(y).get_commands():
                                if not c.hidden:
                                    halp.add_field(name=c.name,value=c.help,inline=False)
                            found = True
                if not found:
                    halp = discord.Embed(title='Error!',description='How do you even use "'+cog[0]+'"?',color=discord.Color.red())
                else:
                    await ctx.message.add_reaction(emoji='✉')
                await ctx.message.author.send('',embed=halp)
        except:
            pass

def setup(client):
    client.add_cog(Help(client))