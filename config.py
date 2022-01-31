# Imports
import discord
import os

from dotenv import load_dotenv

load_dotenv()
# Env Variables
TOKEN = os.getenv('CLIENT_TOKEN')
PREFIX = os.getenv("CLIENT_PREFIX")
GIPHY_API = os.getenv("GIPHY_TOKEN")
TENOR_API = os.getenv('TENOR_TOKEN')
DEV_ONE = os.getenv('ROLE_ID_ONE')
DEV_TWO  = os.getenv('ROLE_ID_TWO')
TWITCH = os.getenv('TWITCH_CHANNEL')
OWNER_ID = os.getenv('OWNER_ID')
OWNER_NAME = os.getenv('OWNER_NAME')
DEV_TEAM = os.getenv('DEVELOPMENT_TEAM_NAME')
DEV_ID = os.getenv('DEV_ID')
DEV_NAME = os.getenv('DEV_NAME')
GITHUB_REPO = os.getenv('GITHUB_REPO')
EMBED_THUMBNAIL = os.getenv('EMBED_THUMBNAIL_URL')
EMBED_IMAGE = os.getenv('EMBED_IMAGE_URL')
CLIENT_VERSION = os.getenv('VERSION')

# Color Variables
RANDOM = discord.Color.random()
BLUE = discord.Color.blue()
BLURPLE = discord.Color.blurple()
GOLD = discord.Color.gold()
RED = discord.Color.red()
GREEN = discord.Color.green()
DARKRED = discord.Color.dark_red()
DARKBLUE = discord.Color.dark_blue()
DARKGOLD = discord.Color.dark_gold()