import discord
import os

from env import PREFIX, THUMBNAIL, IMAGE, BLUE
from discord.ext import commands
from discord.ext.commands import CommandNotFound

class Help(commands.Cog):
    def __init__(self, client):
        self.client = client
    
    @commands.command(name='help', aliases=['h'])
    @commands.group(invoke_without_command = True)
    @commands.has_guild_permissions(send_messages=True)
    async def _help(self, ctx):
        embed = discord.Embed(title='Command Help', description='Categories: Administration, Moderation, Images, Social, Utility', color=BLUE)
        embed.set_thumbnail(url=THUMBNAIL)
        embed.set_image(url=IMAGE)
        await ctx.send(embed=embed)
        
    @help.command(name='administration', aliases=['admin'])
    @commands.has_guild_permissions(administrator=True)
    async def _Administration(self, ctx):
        embed = discord.Embed(title='Administrator Commands', description='```css\n' + 'Kick: Kick a member for a specified reason.\nExample: {}kick @JohnDoe Harrassment\n\nBan: Ban a user for a specified reason.\nExample: {}ban @JohnDoe Harrassment\n\nPurge: Delete a specified number of messages from the channel.\nExample: {}purge 50'.format(PREFIX, PREFIX, PREFIX) + '\n```', color=BLUE)
        embed.set_thumbnail(url=THUMBNAIL)
        embed.set_image(url=IMAGE)
        await ctx.send(embed=embed)

    @help.command(name='moderation', aliases=['mod'])
    @commands.has_guild_permissions(manage_server=True)
    async def _Moderation(self, ctx):
        embed = discord.Embed(title='Moderator Commands', description='```css\n' + 'mute: Mute a member for a specified reason..\nExample: {}mute @JohnDoe Spamming\n\ntempmute: Temporarily mute a member for a specified reason.\nExample: {}tempmute @JohnDoe 10m Spamming\n\nUnmute: Unmute e member.\nExample: {}unmute @JohnDoe'.format(PREFIX, PREFIX, PREFIX) + '\n```', color=BLUE)
        embed.set_thumbnail(url=THUMBNAIL)
        embed.set_image(url=IMAGE)
        await ctx.send(embed=embed)

    @help.command(name='images', aliases=['img'])
    @commands.has_guild_permissions(send_messages=True)
    async def _Images(self, ctx):
        embed = discord.Embed(title='Image Commands', description='```css\n' + 'giphy: Display a random gif by tag via Giphy API.\nExample: {}giphy dog\n\ntenor: Displayb a random gif by tag via Tenor API.\nExample: {}tenor dog'.format(PREFIX, PREFIX) + '\n```', color=BLUE)
        embed.set_thumbnail(url=THUMBNAIL)
        embed.set_image(url=IMAGE)
        await ctx.send(embed=embed)
        
    @help.command(name='social', aliases=['soc'])
    @commands.has_guild_permissions(send_messages=True)
    async def _Social(self, ctx):
        embed = discord.Embed(title='Social Commands', description='```css\n' + 'twitter: Display the 10 most recent post(s) from a specified Twitter.\nExample: {}twitter @GuildWars2\n\nreddit: Display the 10 most recent post(s) from a specified subreddit.\nExample: {}reddit r/funny' + '\n```', color=BLUE)
        embed.set_thumbnail(url=THUMBNAIL)
        embed.set_image(url=IMAGE)
        await ctx.send(embed=embed)
        
    @help.command(name='utility', aliases=['util'])
    @commands.has_guild_permissions(send_messages=True)
    async def _Utility(self, ctx):
        embed = discord.Embed(title='Utility Commands', description='```css\n' + '' + '\n```', color=BLUE)
        embed.set_thumbnail(url=THUMBNAIL)
        embed.set_image(url=IMAGE)
        await ctx.send(embed=embed)

def setup(client):
    client.add_cog(Help(client))