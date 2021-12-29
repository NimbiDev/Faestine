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
client.load_extension('./admin/ban')
client.load_extension('./admin/massban')
client.load_extension('./admin/softban')
client.load_extension('./admin/banlist')
client.load_extension('./admin/role')
client.load_extension('./admin/set')
client.load_extension('./admin/kick')
client.load_extension('./admin/purge')
client.load_extension('./admin/channel')
client.load_extension('./admin/slowmode')
client.load_extension('./admin/thread')
client.load_extension('./admin/role')

# Load all Mod Cogs
client.load_extension('./mod/mute')
client.load_extension('./mod/tempmute')
client.load_extension('./mod/warn')
client.load_extension('./mod/prune')

# Load all Util Cogs
client.load_extension('./util/help')
client.load_extension('./util/avatar')
client.load_extension('./util/guild')
client.load_extension('./util/user')
client.load_extension('./util/search')
client.load_extension('./util/tag')

# Load all Social Cogs
client.load_extension('./social/twitter')
client.load_extension('./social/reddit')
client.load_extension('./social/rss')

# Load all Image Cogs
client.load_extension('./image/imgur')
client.load_extension('./image/tenor')
client.load_extension('./image/giphy')
client.load_extension('./image/rule34')

# Load all Events Cogs
# client.load_extension('./events/memberjoin')
# client.load_extension('./events/memberleave')
# client.load_extension('./events/guildcreate')
# client.load_extension('./events/guilddelete')
# client.load_extension('./events/error')
client.load_extension('./events/ready')
client.load_extension('./events/messege')

# Load all Owner Cogs
# client.load_extension('owner.load')
# client.load_extension('owner.unload')
# client.load_extension('owner.reload')
# client.load_extension('owner.toggle')
# client.load_extension('owner.debug')
# client.load_extension('owner.execute')

client.run(TOKEN)
