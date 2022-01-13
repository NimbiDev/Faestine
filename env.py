
import discord
import os

from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('CLIENT_TOKEN')
PREFIX = os.getenv("CLIENT_PREFIX")
GIPHY_API = os.getenv("GIPHY_TOKEN")
TENOR_API = os.getenv('TENOR_TOKEN')
TWITCH = os.getenv('TWITCH_CHANNEL')
OID = os.getenv('OWNER_ID')
ONAME = os.getenv('OWNER_NAME')
DEV_TEAM = os.getenv('DEVELOPMENT_TEAM_NAME')
GHUB_REPO = os.getenv('GITHUB_REPO')
VERSION = os.getenv('CLIENT_VERSION')
EMBED_THUMBNAIL = os.getenv('EMBED_THUMBNAIL_URL')
EMBED_IMAGE = os.getenv('EMBED_IMAGE_URL')
BLUE = discord.Color.blue()