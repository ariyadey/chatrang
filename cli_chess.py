"""
Use this class to play with AI through Terminal
"""

from ChessGame import ChessGame
from HumanPlayer import HumanPlayer
from RandomAI import RandomAI

white_player = HumanPlayer
black_player = RandomAI

game = ChessGame(white_player, black_player)

while not game.board.is_game_over():
    print(game)
    game.make_move()
