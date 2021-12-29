import os
import sys
import time
import asyncio

from discord.ext import commands
from typing import List
import discord

from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('CLIENT_TOKEN')
PREFIX = os.getenv('CLIENT_PREFIX')


client = commands.Bot(
    command_prefix=commands.when_mentioned_or("."),
    description="Discord Bot",
)


# Load all Admin Commands
client.load_extension('./admin/ban.py')
client.load_extension('./admin/massban.py')
client.load_extension('./admin/softban.py')
client.load_extension('./admin/banlist.py')
client.load_extension('./admin/role.py')
client.load_extension('./admin/set.py')
client.load_extension('./admin/kick.py')
client.load_extension('./admin/purge.py')
client.load_extension('./admin/channel.py')
client.load_extension('./admin/slowmode.py')
client.load_extension('./admin/thread.py')
client.load_extension('./admin/role.py')

# Load all Mod Cogs
client.load_extension('./mod/mute.py')
client.load_extension('./mod/tempmute.py')
client.load_extension('./mod/warn.py')
client.load_extension('./mod/prune.py')

# Load all Util Cogs
client.load_extension('./util/help.py')
client.load_extension('./util/avatar.py')
client.load_extension('./util/guild.py')
client.load_extension('./util/user.py')
client.load_extension('./util/search.py')
client.load_extension('./util/tag.py')

# Load all Social Cogs
client.load_extension('./social/twitter.py')
client.load_extension('./social/reddit.py')
client.load_extension('./social/rss.py')

# Load all Image Cogs
client.load_extension('./image/imgur.py')
client.load_extension('./image/tenor.py')
client.load_extension('./image/giphy.py')
client.load_extension('./image/rule34.py')

# Load all Events Cogs
# client.load_extension('./events/memberjoin.py')
# client.load_extension('./events/memberleave.py')
# client.load_extension('./events/guildcreate.py')
# client.load_extension('./events/guilddelete.py')
# client.load_extension('./events/error.py')
client.load_extension('./events/ready.py')
client.load_extension('./events/messege.py')

# Load all Owner Cogs
# client.load_extension('owner.load.py')
# client.load_extension('owner.unload.py')
# client.load_extension('owner.reload.py')
# client.load_extension('owner.toggle.py')
# client.load_extension('owner.debug.py')
# client.load_extension('owner.execute.py')

client.run(TOKEN)
