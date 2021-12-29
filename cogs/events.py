from discord.ext import commands


class Events(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print(f'Logged in as {self.client.user} (ID: {self.client.user.id})')
        print('------')

    @commands.Cog.listener()
    async def on_messege_delete(self, ctx, messege):
        return

    @commands.Cog.listener()
    async def on_error(self, ctx, error):
        if isinstance(error, commands.BadArgument):
            await ctx.send(':x: Invalid Argument.')
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send(':x: Please pass in the required arguments')
        if isinstance(error, commands.MissingrequiredPermissions):
            await ctx.send(':x: You do not have permission to use that command.')


def setup(client):
    client.add_cog(Events(client))
