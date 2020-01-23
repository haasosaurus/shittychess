# coding=utf-8


from typing import NoReturn

import pygame

from shittychess_settings import ShittySettings
from shittychess_events import ShittyEventHandler
from shittychess_board import ShittyBoard
from shittychess_logic import ShittyLogic
from shittychess_layout import ShittyLayout


class ShittyChess:
    """base class for the game"""

    def __init__(self) -> NoReturn:
        """constructor"""

        # setup pygame
        pygame.init()
        pygame.display.set_caption("Shitty Chess")
        self.clock = pygame.time.Clock()

        # initialize our property classes
        self.settings = ShittySettings()
        self.screen = pygame.display.set_mode((
            self.settings.screen_width(),
            self.settings.screen_height()
        ))
        self.logic = ShittyLogic()
        self.board = ShittyBoard()
        self.layout = ShittyLayout()
        self.event_handler = ShittyEventHandler()

        # make assignments to our property classes
        self.board.screen = self.screen
        self.board.settings = self.settings
        self.board.logic = self.logic
        self.board.layout = self.layout
        self.logic.settings = self.settings
        self.logic.board = self.board
        self.logic.layout = self.layout
        self.layout.screen = self.screen
        self.layout.settings = self.settings
        self.layout.logic = self.logic
        self.event_handler.screen = self.screen
        self.event_handler.settings = self.settings
        self.event_handler.layout = self.layout
        self.event_handler.logic = self.logic
        self.event_handler.board = self.board

        # configure our property classes
        self.board.configure()  # this should come before logic
        self.logic.configure()
        self.layout.configure()
        # self.event_handler.configure()

        # more pygame configuration
        pygame.display.set_icon(pygame.image.load(self.settings.app_icon_path))

        # assorted properties
        self.local_debug = False

    def __del__(self):
        """destructor"""

        pygame.quit()  # i don't trust pygame

    def run_game(self) -> NoReturn:
        """This is the main function of the program which runs the code."""

        self.main_loop()

    def main_loop(self) -> NoReturn:
        """main loop of the program"""

        while not self.settings.exiting:
            self.event_handler.process_events()
            if self.settings.headers_enabled:
                self.screen.fill(self.settings.header_background_color)
            self.board.draw()
            self.layout.draw()
            pygame.display.flip()
            self.clock.tick(60)


if __name__ == '__main__':
    chess = ShittyChess()
    chess.run_game()
