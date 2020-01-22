from typing import NoReturn

import pygame


class ShittyMousePointer(pygame.sprite.Sprite):
    def __init__(self, x, y) -> NoReturn:
        super(pygame.sprite.Sprite, self).__init__()
        self.rect = pygame.Rect(x, y, 1, 1)
