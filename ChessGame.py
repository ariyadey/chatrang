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
        self.board.push(move)

    def is_game_over(self):
        return self.board.is_game_over()
