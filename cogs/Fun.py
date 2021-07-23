import discord
    import os
    import aiohttp
    import random
    import json
    from discord.ext import commands
    from dotenv import load_dotenv

    load_dotenv()
    PREFIX = os.getenv('COMMAND_PREFIX')
    TENOR_API_TOKEN = os.getenv('TENOR_TOKEN')


    class Fun(commands.Cog):
        def __init__(self, client):
            self.client = client

        @commands.command(aliases=['g'], description='Get a random gif from tenor via tag', usage=f'Usage: {PREFIX}gif [tag]\nExample: {PREFIX}gif dog')
        @commands.has_guild_permissions(send_messages=True, embed_links=True)
        async def gif(self, ctx, query):
            async with aiohttp.ClientSession() as session:
                embed = discord.Embed(
                    colour=discord.Colour.dark_red())
                response = await session.get(
                    f'https://api.tenor.com/v1/search?q={query}&key={TENOR_API_TOKEN}&limit=30&media_filter=basic')
                data = json.loads(await response.text())
                gif_choice = random.randint(0, 29)

                for result in data['results']:
                    print('- result -')
                    # print(result)

                    for media in result['media']:
                        print('- media -')
                        # print(media)
                        # print(media['gif'])
                        print('url:', media['gif']['url'])

                        embed.set_image(url=data['results'][0][gif_choice]['gif']['url'])

            await session.close()
            await ctx.send(embed=embed)
