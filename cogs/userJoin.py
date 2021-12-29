import discord
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
YELLOW = discord.colour.Colour.dark_yellow()


class UserJoin(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_member_join(self, member):
        client = self.client
        channel = self.client.get_channel(WELCOME_CHANNEL)
        embed = discord.Embed(color=BLUE)
        embed.add_field(name="Welcome", value='{} has joined {}'.format(
            member.name, member.guild.name), inline=False)
        embed.set_image(url=WELCOME_IMAGE)
        embed.set_footer(text='{} | {}'.format(
            client.user.name, GITHUB), icon_url=client.user.avatar)
        await channel.send(embed=embed)


def setup(client):
    client.add_cog(UserJoin(client))
