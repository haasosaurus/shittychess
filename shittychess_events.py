# coding=utf-8


import sys
import pygame


class ShittyEventMonitor:
    """
    manages all the pygame events for the game
    should be renamed to something better since
    it does more than monitor
    """

    def __init__(self) -> None:
        self.screen = None  # pygame.Surface
        self.settings = None  # ShittySettings
        self.layout = None  # ShittyLayout

    # def configure(self) -> None:
    #     """
    #     configure class's properties after they have been assigned externally
    #     """

    #     pass

    def process_events(self) -> None:
        """
        process pygame events
        """

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    sys.exit()
                if event.key == pygame.K_h:
                    self.settings.headers_enabled = not self.settings.headers_enabled
                    self.screen = pygame.display.set_mode((self.settings.screen_width(), self.settings.screen_height()))
                    self.layout.resize()
            elif event.type == pygame.QUIT:
                sys.exit()
