import random
import sys

import chess
import chess.svg
from PyQt5 import QtSvg
from PyQt5.QtCore import *
from PyQt5.QtWidgets import QApplication

from ChessGame import ChessGame
from RandomAI import RandomAI


class ChessGui:
    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2
        self.game = ChessGame(player1, player2)

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
        print("making move, white turn " + str(self.game.board.turn))
        self.game.make_move()
        self.display_board()


if __name__ == "__main__":
    random.seed(1)
    # todo: gui does not work well with HumanPlayer, due to input() use on stdin conflict with event loop.

    player1 = RandomAI()
    player2 = RandomAI()

    game = ChessGame(player1, player2)
    gui = ChessGui(player1, player2)

    gui.start()

    sys.exit(gui.app.exec_())
