#!/usr/bin/env python
# coding=utf-8


import pygame

from shittychess_settings import ShittySettings
from shittychess_events import ShittyEventMonitor
from shittychess_board import ShittyBoard
from shittychess_logic import ShittyLogic
from shittychess_layout import ShittyLayout


class ShittyChess:

    def __init__(self):
        pygame.init()
        pygame.display.set_caption("Shitty Chess")
        self.settings = ShittySettings()
        self.screen = pygame.display.set_mode((self.settings.screen_width(), self.settings.screen_height()))
        self.board = ShittyBoard(self.screen, self.settings)
        self.logic = ShittyLogic(self.settings)
        self.layout = ShittyLayout(self.screen, self.logic)
        self.event_monitor = ShittyEventMonitor(self.screen, self.settings, self.layout)
        self.exiting = False


    def run_game(self):
        """This is the main function of the program which runs the code."""

        self.main_loop()


    def main_loop(self):


        while not self.exiting:
            self.event_monitor.process_events()
            if self.settings.headers:
                self.screen.fill(self.settings.header_background_color)
            self.board.draw()
            self.layout.draw()
            pygame.display.flip()


if __name__ == '__main__':
    chess = ShittyChess()
    chess.run_game()
