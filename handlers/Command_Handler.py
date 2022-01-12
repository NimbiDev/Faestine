import discord
from discord.ext import commands


class Help(commands.Cog):
    def __init__(self, client):
        self.client = client


class CustomHelp(commands.MinimalHelpCommand):
    async def send_pages(self):
        destination = self.get_destination()
        embed = discord.Embed(color=discord.Color.blurple(), description='')
        for page in self.paginator.pages:
            embed.description += page
            await destination.send(embed=embed)

        client = self.client

        client.help_command = CustomHelp()

        for filename in os.listdir('./cogs'):
            if filename.endswith('.py'):
                client.load_extension(f'cogs.{filename[:-3]}')
                print(f'Loaded cogs.{filename[:-3]}')
            else:
                print(f'Unable to load cogs.{filename[:-3]}')