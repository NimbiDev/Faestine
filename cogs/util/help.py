import discord
import asyncio
from discord.ext import commands


class Help(commands.Cog):
    def __init__(self, client):
        self.client = client

    class CustomHelp(commands.MinimalHelpCommand):
        async def send_pages(self):
            destination = self.get_destination()
            e = discord.Embed(color=discord.Color.blurple(), description='')
            for page in self.paginator.pages:
                e.description += page
            await destination.send(embed=e)

    self.client.help_command = CustomHelp()


def setup(client):
    client.add_cog.util(Help(client))
