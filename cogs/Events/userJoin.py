import discord
import traceback
import sys
import os
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
GUILD = os.getenv('GUILD_ID')
TWITCH = os.getenv('TWITCH_CHANNEL')
GITHUB = os.getenv('GITHUB_URL')
ERROR_CHANNEL = os.getenv('ERROR_CHANNEL_ID')
WELCOME_CHANNEL = os.getenv('WELCOME_CHANNEL_ID')
WELCOME_IMAGE = os.getenv('WELCOME_IMAGE_URL')


class UserJoin(commands.Cog):
    def __init__(self, client):
        self.client = client
        self.clean_prefix = self.client.command_prefix

    @commands.Cog.listener()
    async def on_member_join(self, member):
        github_url = GITHUB
        channel = self.client.get_channel(WELCOME_CHANNEL)
        embed = discord.Embed(color=discord.colour.Color.dark_blue())
        embed.add_field(name="Welcome", value='{} has joined {}'.format(member.name, member.guild.name), inline=False)
        embed.set_image(url=WELCOME_IMAGE)
        embed.set_footer(text='{} | {}'.format(self.client.user.name, github_url), icon_url=self.client.user.avatar)
        await channel.send(embed=embed)


def setup(client):
    client.add_cog(UserJoin(client))