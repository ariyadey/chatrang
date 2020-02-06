"""
Use this class to play with AI through Terminal
"""

from src.ChessGame import ChessGame
from src.HumanPlayer import HumanPlayer
from src.RandomAI import RandomAI

white_player = HumanPlayer
black_player = RandomAI

game = ChessGame(white_player, black_player)

while not game.board.is_game_over():
    print(game)
    game.make_move()
