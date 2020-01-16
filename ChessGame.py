"""
This class manages the implementation of chess
It handles how to communicate with AI algorithms
It's an interface between AI algorithms and the user
"""

import chess


class ChessGame:
    def __init__(self, player1, player2):
        self.board = chess.Board()
        self.players = [player1, player2]

    def __str__(self):
        column_labels = "\n_______________" \
                        "\na b c d e f g h\n"
        board_str = str(self.board) + column_labels
        move_str = "White to move" if self.board.turn else "Black to move"
        return board_str + "\n" + move_str + "\n"

    def make_move(self):
        player = self.players[1 - int(self.board.turn)]  # Switch the turn
        move = player.choose_move(self.board)  # Call AI functions or get user movement
        if move:
            self.board.push(move)  # Make the movement


# Evaluation functions:

def evaluate(board):
    overall_value = 0
    for i in range(63):  # Iterate aver all the squares of the board
        piece = board.piece_at(i)
        if piece is not None:  # Is square empty?
            value = get_piece_value(piece)
            if piece.color:  # Am I white or black?
                overall_value += value
            else:
                overall_value -= value
    return overall_value


def get_piece_value(piece):  # todo: piece to piece type
    piece_name = str(piece)
    if piece_name == "P" or piece_name == "p":
        return 100
    if piece_name == "N" or piece_name == "n":
        return 320
    if piece_name == "B" or piece_name == "b":
        return 330
    if piece_name == "R" or piece_name == "r":
        return 500
    if piece_name == "Q" or piece_name == "q":
        return 900
    if piece_name == 'K' or piece_name == 'k':
        return 20000
