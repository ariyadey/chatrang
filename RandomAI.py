import random
from time import sleep


class RandomAI:
    def __init__(self):
        pass

    @staticmethod
    def choose_move(board):
        sleep(1)
        legal_moves = list(board.legal_moves)
        move = random.choice(legal_moves)
        print("Random AI recommends move " + str(move) + "\n")
        return move
