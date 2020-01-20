# coding=utf-8


import pygame

from shittychess_settings import ShittySettings
from shittychess_events import ShittyEventMonitor
from shittychess_board import ShittyBoard
from shittychess_logic import ShittyLogic
from shittychess_layout import ShittyLayout


class ShittyChess:
    """base class for the game"""

    def __init__(self) -> None:
        # setup pygame
        pygame.init()
        pygame.display.set_caption("Shitty Chess")

        # initialize our property classes
        self.settings = ShittySettings()
        self.screen = pygame.display.set_mode((self.settings.screen_width(), self.settings.screen_height()))
        self.logic = ShittyLogic()
        self.board = ShittyBoard()
        self.layout = ShittyLayout()
        self.event_monitor = ShittyEventMonitor()

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
        self.event_monitor.screen = self.screen
        self.event_monitor.settings = self.settings
        self.event_monitor.layout = self.layout

        # configure our property classes
        self.logic.configure()
        self.board.configure()
        self.layout.configure()
        # self.event_monitor.configure()

        # assorted properties
        self.exiting = False
        self.local_debug = False


    def run_game(self) -> None:
        """This is the main function of the program which runs the code."""

        self.main_loop()


    def main_loop(self) -> None:
        """main loop of the program"""

        while not self.exiting:
            self.event_monitor.process_events()
            if self.settings.headers_enabled:
                self.screen.fill(self.settings.header_background_color)

            # just testing to see if my ShittyPiece __bool__ method works, and attempting to highlight a piece's
            # available moves by coords
            if self.settings.debug:
                if self.layout.sprite_exists_all('b1'):
                    if self.local_debug:
                        print('sprite is a valid game piece, calling self.board.draw(sprite)')
                    self.board.draw('b1')
                else:
                    if self.local_debug:
                        print('sprite is not a valid chess piece, calling self.board.draw()')
                    self.board.draw()
            else:
                self.board.draw()

            self.layout.draw()
            pygame.display.flip()


if __name__ == '__main__':
    chess = ShittyChess()
    chess.run_game()
