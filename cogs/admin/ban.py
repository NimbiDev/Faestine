from discord.ext import commands
from typing import List
import discord

class BanFlags(commands.FlagConverter):
        members: List[discord.Member] = commands.flag(name='member')
        reason: str
        days: int = 1

class Ban(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(name="ban")
    @commands.has_permissions(ban_members=True)
    async def ban(ctx, *, flags: BanFlags):
        for member in flags.members:
            await member.ban(reason=flags.reason, delete_message_days=flags.days)
            members= ', '.join(str(member) for member in flags.members)
            plural= f'{flags.days} days' if flags.days != 1 else f'{flags.days} day'
            await ctx.send(f'Banned {members} for {flags.reason!r} (deleted {plural} worth of messages)')

def setup(client):
    client.add_cog(Ban(client))
