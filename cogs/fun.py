from email import message
import discord
import os
import asyncio
import random

from config import BLUE, EMBED_THUMBNAIL, PREFIX, RED, GREEN
from discord.ext import commands

command_attrs = {'hidden': False}

class Fun(commands.Cog, name='Fun Commands'):
    def __init__(self, client):
        self.client = client
    
    
    @commands.command(name='guess', description='A simple guessing game.\n\n**Example**: {}guess'.format(PREFIX), command_attrs=command_attrs)
    @commands.has_guild_permissions(send_messages=True)
    @commands.cooldown(1, 10, commands.BucketType.user)
    async def _guess(self, ctx):
        if ctx.author.id == self.client.user.id:
            return
        
        e = discord.Embed(color=BLUE)
        e.add_field(name='Socket Guessing Game', value='Guess a number between **1** and **10**', inline=False)
        e.set_thumbnail(url='{}'.format(EMBED_THUMBNAIL))
        await ctx.send(embed=e)
        
        def is_correct(m):
            return m.author == ctx.author and m.content.isdigit()

        answer = random.randint(1, 10)

        try:
            guess = await self.client.wait_for("message", check=is_correct, timeout=10.0)
        except asyncio.TimeoutError:
            e = discord.Embed(color=RED)
            e.add_field(name='Socket Guessing Game', value='```diff\n- Sorry, you took too long. It was: {}\n```'.format(answer), inline=False)
            e.set_thumbnail(url='{}'.format(EMBED_THUMBNAIL))
            return await ctx.send(embed=e)


        if int(guess.content) == answer:
            e = discord.Embed(color=GREEN)
            e.add_field(name='Socket Guessing Game', value='```diff\n+ You are right!\n```', inline=False)
            e.set_thumbnail(url='{}'.format(EMBED_THUMBNAIL))
            await ctx.send(embed=e)
        else:
            e = discord.Embed(color=RED)
            e.add_field(name='Socket Guessing Game', value='```diff\n- Oops! It is actually: {}\n```'.format(answer), inline=False)
            e.set_thumbnail(url='{}'.format(EMBED_THUMBNAIL))
            await ctx.send(embed=e)
                
def setup(client):
    client.add_cog(Fun(client))