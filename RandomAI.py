import random
from time import sleep


class RandomAI():
    def __init__(self):
        pass

    def choose_move(self, board):
        sleep(1)
        move = random.choice(board.legal_moves)
        print("Random AI recommends move " + str(move))
        return move
