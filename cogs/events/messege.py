from discord.ext import commands


class Messege(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_message(self, message):
        print(message)


def setup(client):
    client.add_cog.events(Messege(client))