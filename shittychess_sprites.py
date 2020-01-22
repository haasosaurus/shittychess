from os import PathLike
from typing import Union
from typing import NoReturn

import pygame


class ShittyMousePointer(pygame.sprite.Sprite):
    def __init__(self, x, y) -> NoReturn:
        super(pygame.sprite.Sprite, self).__init__()
        self.rect = pygame.Rect(x, y, 1, 1)


class ShittySprite(pygame.sprite.Sprite):
    """base sprite class for pieces and spaces"""

    def __init__(self, black: bool, rect: pygame.Rect, coords: str, img_path: Union[PathLike, str], **kwargs) -> NoReturn:
        super().__init__(**kwargs)
        self.rect = rect
        self.black = black
        self.image = None  # pygame.image
        self.coords = coords
        self.load_image(img_path)

    def load_image(self, img_path: Union[PathLike, str]) -> NoReturn:
        self.image = pygame.image.load(img_path if isinstance(img_path, str) else str(img_path))


class ShittySpace(ShittySprite):
    """
    sprite class for board spaces
    """

    def __init__(self, black: bool, rect: pygame.Rect, coords: str, img_path: Union[PathLike, str], **kwargs) -> NoReturn:
        super().__init__(black, rect, coords, img_path, **kwargs)
        self.indexes = None  # Tuple[int, int]
