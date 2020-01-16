import random
from time import sleep


class RandomAI:
    def __init__(self):
        pass

    @staticmethod
    def choose_move(board):
        sleep(1)
        legal_moves = list(board.legal_moves)
        if legal_moves:
            move = random.choice(legal_moves)  # todo: game is over.
            print("Random AI recommends move " + str(move))
            return move
