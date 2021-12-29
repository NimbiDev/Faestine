import discord
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



class Purge(commands.Cog):
    def __init__(self, client):
        self.client = client
        

    @commands.command(aliases=['clear', 'prune', 'delete'], description='Delete a specified number of messages.')
    @commands.has_guild_permissions(manage_messages=True)
    async def purge(self, ctx, amount: int):

        
        embed = discord.Embed(color=BLUE)
        authors = {}

        async for message in ctx.channel.history(limit=amount):
            if message.author not in authors:
                authors[message.author] = 1
            else:
                authors[message.author] += 1
            await message.delete()

        response = '\n'.join(['{}: {}'.format(author.name, amount)
                             for author, amount in authors.items()])

        embed.add_field(name='Messages Deleted',
                        value='```yml\n{}```'.format(response))
        embed.set_thumbnail(url=self.client.user.avatar)
        embed.set_footer(text='{} | {}'.format(
            self.client.user.name, GITHUB), icon_url=self.client.user.avatar)

        await ctx.channel.purge(limit=amount + 1)
        await ctx.channel.send(embed=embed, delete_after=20)


def setup(client):
    client.add_cog(Purge(client))
