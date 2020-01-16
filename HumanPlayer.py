import chess


class HumanPlayer:
    def __init__(self):
        print("Moves can be entered using four characters. \n"
              "For example, d2d4 moves the piece at d2 to d4.")
        pass

    @staticmethod
    def choose_move(board):
        uci_move = None
        while True:
            human_move = input("Please enter your move: ")
            try:
                uci_move = chess.Move.from_uci(human_move)
            except ValueError:
                print("Invalid move format; try again!")
                continue

            if uci_move not in board.legal_moves:
                print("An illegal move; try again!")

        return uci_move
