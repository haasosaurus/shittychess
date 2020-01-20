# coding=utf-8


import sys
import pygame

from shittychess_settings import ShittySettings
from shittychess_layout import ShittyLayout


class ShittyEventMonitor:
    """
    manages all the pygame events for the game
    should be renamed to something better since
    it does more than monitor
    """

    def __init__(self, screen: pygame.Surface, settings: ShittySettings, layout: ShittyLayout) -> None:
        """
        initialize an instance of the class
        """

        self.screen = screen
        self.settings = settings
        self.layout = layout


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
