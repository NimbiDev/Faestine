import discord
import time
import traceback
import sys
import os
from discord.ext import commands

GUILD = '899130986242113586'
TWITCH = 'Discord'
GITHUB = 'github.com/DevCorner-Github/Faestine'
ERROR_CHANNEL = '899741317318455346'
WELCOME_CHANNEL = '911521226038587412'
WELCOME_IMAGE = 'https://gifimage.net/wp-content/uploads/2017/09/anime-welcome-gif.gif'

RED = discord.colour.Colour.dark_red()
GREEN = discord.colour.Colour.dark_green()
GOLD = discord.colour.Colour.dark_gold()
BLUE = discord.colour.Colour.dark_blue()



class Avatar(commands.Cog):
    def __init__(self, client):
        self.client = client
        

    @commands.command(aliases=['ava', 'pfp'], description='Display a member\'s avatar')
    @commands.has_guild_permissions(send_messages=True, embed_links=True)
    async def avatar(self, ctx, member: discord.Member = None):
        
        if member is None:
            member = ctx.author
        embed = discord.Embed(description='**__{}\'s Avatar__**'.format(member.display_name), color=BLUE)
        embed.set_image(url=member.avatar)
        await ctx.send(embed=embed)


def setup(client):
    client.add_cog(Avatar(client))
