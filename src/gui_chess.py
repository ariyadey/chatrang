"""
Use this file to watch to AI playing with each other through GUI
"""

import random
import sys

import chess
import chess.svg
from PyQt5 import QtSvg
from PyQt5.QtCore import *
from PyQt5.QtWidgets import QApplication

from src.AlphaBetaAI import AlphaBetaAI
from src.ChessGame import ChessGame
from src.RandomAI import RandomAI


class ChessGui:
    def __init__(self, white_player, black_player):
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
            turn = "White" if self.game.board.turn else "Black"
            print("making move, " + turn + " turn...")
            self.game.make_move()
        else:
            print("################## GAME OVER ##################")
            self.timer.stop()

        self.display_board()


if __name__ == "__main__":
    random.seed(3)  # Change this value to get different random movements

    # gui does not work well with HumanPlayer,
    # due to input() use on stdin conflict with event loop.

    # Choose the type of AI for players below:
    white_player = RandomAI
    black_player = AlphaBetaAI(is_ai_white=False, depth=4)

    gui = ChessGui(white_player, black_player)
    gui.start()
    sys.exit(gui.app.exec_())
