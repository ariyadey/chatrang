import random
from time import sleep


class RandomAI():
    def __init__(self):
        pass

    def choose_move(self, board):
        move = random.choice(board.legal_moves)
        sleep(1)  # I'm thinking so hard.
        print("Random AI recommends move " + str(move))
        return move
