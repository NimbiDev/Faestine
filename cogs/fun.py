import discord
import os
import asyncio
import random

from env import PREFIX
from discord.ext import commands
from discord.ext.commands import CommandNotFound

command_attrs = {'hidden': False}

class Fun(commands.Cog, name='🎮 Fun Commands 🎮'):
    def __init__(self, client):
        self.client = client
    
    
    @commands.command(name='guess', aliases=['g'], description='A simple guessing game.', command_attrs=command_attrs)
    @commands.has_guild_permissions(send_messages=True)    
    async def _guess(self, ctx, message):
        if message.author.id == self.user.id:
            return

        await message.channel.send("Guess a number between 1 and 10.")

        def is_correct(m):
            return m.author == message.author and m.content.isdigit()

        answer = random.randint(1, 10)

        try:
            guess = await self.wait_for("message", check=is_correct, timeout=5.0)
        except asyncio.TimeoutError:
            return await message.channel.send(
                "Sorry, you took too long it was {}.".format(answer)
            )

        if int(guess.content) == answer:
            await message.channel.send("You are right!")
        else:
            await message.channel.send("Oops. It is actually {}.".format(answer))
                
def setup(client):
    client.add_cog(Fun(client))