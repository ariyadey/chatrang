from ChessGame import ChessGame
from HumanPlayer import HumanPlayer
from RandomAI import RandomAI

white_player = HumanPlayer()
black_player = RandomAI()

game = ChessGame(white_player, black_player)

while not game.is_game_over():
    print(game)
    game.make_move()

# todo: check legal moves emptiness for all the classes
# todo: extract common methods from classes to a seperate file
