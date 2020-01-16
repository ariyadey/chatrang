import sys

import chess

from ChessGame import evaluate


class MinimaxAI:
    def __init__(self, is_ai_white: bool, depth=3):
        self.depth = depth
        self.is_white = is_ai_white

    def choose_move(self, board: chess.Board()):
        best_move = None
        best_move_value = -sys.maxsize
        for movement in board.legal_moves:
            board.push(movement)
            movement_value = max(best_move_value, self.minimax(self.depth - 1, board, is_maximizing=False))
            board.pop()
            if movement_value > best_move_value:
                best_move_value = movement_value
                best_move = movement
        print("Minimax AI recommends move " + str(best_move))
        return best_move

    def minimax(self, depth, board, is_maximizing):
        if depth == 0:
            value = evaluate(board)
            return value if self.is_white else -value

        legal_moves = board.legal_moves
        if is_maximizing:
            best_move = -sys.maxsize
            for movement in legal_moves:
                board.push(movement)
                best_move = max(best_move, self.minimax(depth - 1, board, not is_maximizing))
                board.pop()
            return best_move
        else:
            best_move = sys.maxsize
            for movement in legal_moves:
                board.push(movement)
                best_move = min(best_move, self.minimax(depth - 1, board, not is_maximizing))
                board.pop()
            return best_move
