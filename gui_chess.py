import random
import sys

import chess
import chess.svg
from PyQt5 import QtSvg
from PyQt5.QtCore import *
from PyQt5.QtWidgets import QApplication

from AlphaBetaAI import AlphaBetaAI
from ChessGame import ChessGame
from RandomAI import RandomAI


class ChessGui:
    def __init__(self, white_player, black_player):
        self.player1 = white_player
        self.player2 = black_player
        self.game = ChessGame(white_player, black_player)

        self.app = QApplication(sys.argv)
        self.svgWidget = QtSvg.QSvgWidget()
        self.svgWidget.setGeometry(50, 50, 400, 400)
        self.svgWidget.show()

    def start(self):
        self.timer = QTimer()

        self.timer.timeout.connect(self.make_move)

        self.timer.start(10)
        self.display_board()

    def display_board(self):
        svg_board = chess.svg.board(self.game.board)
        svg_bytes = QByteArray()
        svg_bytes.append(svg_board)
        self.svgWidget.load(svg_bytes)

    def make_move(self):
        if not self.game.board.is_game_over():
            print("making move, white turn " + str(self.game.board.turn))
            self.game.make_move()
        else:
            print("################## GAME OVER ##################")
            self.timer.stop()

        self.display_board()


if __name__ == "__main__":
    random.seed(3)
    # todo: gui does not work well with HumanPlayer, due to input() use on stdin conflict with event loop.

    white_player = RandomAI
    black_player = AlphaBetaAI(is_ai_white=False, depth=4)

    gui = ChessGui(white_player, black_player)

    gui.start()

    sys.exit(gui.app.exec_())
