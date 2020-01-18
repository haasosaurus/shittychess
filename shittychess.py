#!/usr/bin/env python
# coding=utf-8


import pygame

from shittychess_settings import ShittySettings
from shittychess_events import ShittyEventMonitor
from shittychess_board import ShittyBoard
from shittychess_pieces import ShittyPawn


class ShittyChess:

    def __init__(self):
        self.settings = ShittySettings()
        self.event_monitor = ShittyEventMonitor()
        pygame.init()
        self.screen = pygame.display.set_mode((self.settings.screen_width,
                                               self.settings.screen_height))
        self.board = ShittyBoard(self.screen, self.settings)


    def run_game(self):
        """This is the main function of the program which runs the code."""

        pygame.display.set_caption("Shitty Chess")
        self.main_loop()


    def main_loop(self):
        pawn = ShittyPawn(self.screen)
        # Starts the main loop for the game.
        while True:
            self.event_monitor.process_events()
            # Refresh the screen with the newest info.
            self.board.blitme()
            pawn.blitme()
            pygame.display.flip()


if __name__ == '__main__':
    chess = ShittyChess()
    chess.run_game()
