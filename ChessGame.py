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
        player = self.players[1 - int(self.board.turn)]
        # todo: implementation
        move = player.choose_move(self.board)
        if move:
            self.board.push(move)

    def is_game_over(self):
        return self.board.is_game_over()


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


def evaluate(board):
    overall_value = 0
    for i in range(63):
        piece = board.piece_at(i)
        if piece is not None:  # todo: piece to piece type
            value = get_piece_value(piece)
            if piece.color:  # todo: I changed it from + to -
                overall_value += value
            else:
                overall_value -= value
    return overall_value
