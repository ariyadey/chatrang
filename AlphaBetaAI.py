import sys

import chess

from ChessGame import evaluate


# It's just as smart as Minimax, but it thinks faster and ignores nonsense nodes (moves)
class AlphaBetaAI:
    def __init__(self, is_ai_white: bool, depth=3):
        self.depth = depth
        self.is_white = is_ai_white

    def choose_move(self, board: chess.Board()):
        best_move = None
        best_move_value = -sys.maxsize

        alpha = -sys.maxsize
        beta = sys.maxsize

        # Iterate over all the legal moves and choose the best one
        for movement in board.legal_moves:

            # Evaluate them one be one recursively
            board.push(movement)
            movement_value = max(best_move_value, self.minimax(
                self.depth - 1, board, alpha, beta, is_maximizing=False))
            board.pop()

            # Choose the best one
            if movement_value > best_move_value:
                best_move_value = movement_value
                best_move = movement

        print("AlphaBeta AI recommends move " + str(best_move) + "\n")
        return best_move

    def minimax(self, depth, board, alpha, beta, is_maximizing):

        # It's enough! Let's evaluate the board.
        if depth == 0:
            value = evaluate(board)
            return value if self.is_white else -value

        legal_moves = board.legal_moves

        # Go deeper recursively
        if is_maximizing:
            best_move = -sys.maxsize
            for movement in legal_moves:
                board.push(movement)
                best_move = max(best_move, self.minimax(
                    depth - 1, board, alpha, beta, not is_maximizing))
                board.pop()
                # Ignore nonsense nodes and branches
                alpha = max(alpha, best_move)
                if beta <= alpha:
                    break
                ##########
            return best_move
        else:
            best_move = sys.maxsize
            for movement in legal_moves:
                board.push(movement)
                best_move = min(best_move, self.minimax(
                    depth - 1, board, alpha, beta, not is_maximizing))
                board.pop()
                # Ignore nonsense nodes and branches
                beta = min(beta, best_move)
                if beta <= alpha:
                    break
                ##########
            return best_move
