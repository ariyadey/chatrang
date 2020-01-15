from ChessGame import ChessGame
from HumanPlayer import HumanPlayer
from RandomAI import RandomAI

player1 = HumanPlayer()
player2 = RandomAI()

game = ChessGame(player1, player2)

while not game.is_game_over():
    print(game)
    game.make_move()

# print(hash(str(game.board)))
