#!/usr/bin/env python
# coding=utf-8


import pygame

class ShittyBoard:
    """This class represents a board."""

    def __init__(self, screen, settings):
        """Initialize the board's attributes."""

        self.screen = screen
        self.settings = settings

        # Get the image, its rect and set it on the screen.
        tile_image = 'shitty_art/shittychess_tile.png'
        self.image = pygame.image.load(tile_image)
        self.rect = pygame.Rect(0, 0, 0, 0)
        self.screen_rect = self.screen.get_rect()

        # Set image rect equal to the screen rect.
        #self.rect = self.screen_rect


    def draw(self):
        for i in range(0, self.settings.tile_h * 4, self.settings.tile_h):
            for j in range(0, self.settings.tile_w * 4, self.settings.tile_w):
                self.rect.x = i
                self.rect.y = j
                self.screen.blit(self.image, self.rect)
