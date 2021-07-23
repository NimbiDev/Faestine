import discord
import os
import TenGiphPy
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()

PREFIX = os.getenv('COMMAND_PREFIX')
OSU_API_TOKEN = os.getenv('OSU_TOKEN')
GW2_API_TOKEN = os.getenv('GW2_TOKEN')
TENOR_API_TOKEN = os.getenv('TENOR_TOKEN')

TOKENS = {'TENOR_API': TENOR_API_TOKEN}

TENOR = TenGiphPy.Tenor(token=TOKENS['TENOR_API'])


class TicTacToeButton(discord.ui.Button['TicTacToe']):
    def __init__(self, x: int, y: int):
        super().__init__(style=discord.ButtonStyle.secondary, label='\u200b', row=y)
        self.x = x
        self.y = y

    async def callback(self, interaction: discord.Interaction):
        assert self.view is not None
        view: TicTacToe = self.view
        state = view.board[self.y][self.x]
        if state in (view.X, view.O):
            return

        if view.current_player == view.X:
            self.style = discord.ButtonStyle.danger
            self.label = 'X'
            self.disabled = True
            view.board[self.y][self.x] = view.X
            view.current_player = view.O
            content = "It is now O's turn"
        else:
            self.style = discord.ButtonStyle.success
            self.label = 'O'
            self.disabled = True
            view.board[self.y][self.x] = view.O
            view.current_player = view.X
            content = "It is now X's turn"

        winner = view.check_board_winner()
        if winner is not None:
            if winner == view.X:
                content = 'X won!'
            elif winner == view.O:
                content = 'O won!'
            else:
                content = "It's a tie!"

            for child in view.children:
                assert isinstance(child, discord.ui.Button)
                child.disabled = True

            view.stop()

        await interaction.response.edit_message(content=content, view=view)


class TicTacToe(discord.ui.View):
    X = -1
    O = 1
    Tie = 2

    def __init__(self):
        super().__init__()
        self.current_player = self.X
        self.board = [
            [0, 0, 0],
            [0, 0, 0],
            [0, 0, 0],
        ]

        for x in range(3):
            for y in range(3):
                self.add_item(TicTacToeButton(x, y))

    def check_board_winner(self):
        for across in self.board:
            value = sum(across)
            if value == 3:
                return self.O
            elif value == -3:
                return self.X

        for line in range(3):
            value = self.board[0][line] + self.board[1][line] + self.board[2][line]
            if value == 3:
                return self.O
            elif value == -3:
                return self.X

        diag = self.board[0][2] + self.board[1][1] + self.board[2][0]
        if diag == 3:
            return self.O
        elif diag == -3:
            return self.X

        diag = self.board[0][0] + self.board[1][1] + self.board[2][2]
        if diag == 3:
            return self.O
        elif diag == -3:
            return self.X

        if all(i != 0 for row in self.board for i in row):
            return self.Tie

        return None


class Fun(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(name='gif', aliases=['tenor'], description='Return a random gif by tag', usage=f'Usage: {PREFIX}gif [query]\nExample: {PREFIX}gif dog')
    @commands.has_guild_permissions(send_messages=True, embed_links=True)
    async def _gif(self, ctx, *, _text):

        _url = await TENOR.arandom(str(_text))

        _emb = discord.Embed(colour=discord.Colour.random())
        _emb.set_image(url=_url)
        await ctx.send(embed=_emb)

    @_gif.error
    async def _gif_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send(':x: Tag cant be None. Please give a valid tag to search.')
        else:
            raise error


    @commands.command(name='tictactoe', aliases=['ttt'], description='Play Tic Tac Toe', usage=f'Usage: {PREFIX}tic\nExample: {PREFIX}tic')
    async def tic_tac_toe(self, ctx: commands.Context):
        await ctx.send('Tic Tac Toe: X goes first', view=TicTacToe())


def setup(client):
    client.add_cog(Fun(client))
