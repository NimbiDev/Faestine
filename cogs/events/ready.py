from discord.ext import commands


class Ready(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready():
        print(f"Logged in as {self.client.user} (ID: {self.client.user.id})")
        print("------")


def setup(client):
    client.add_cog.events(Ready(client))
