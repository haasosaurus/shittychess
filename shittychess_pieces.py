# coding=utf-8


import pathlib

import pygame


class ShittyPiece(pygame.sprite.Sprite):
    """base sprite class for pieces"""

    def __init__(self, screen: pygame.Surface, black: bool, rect: pygame.Rect, coords: str) -> None:
        pygame.sprite.Sprite.__init__(self)
        self.black = black
        self.screen = screen
        self.rect = rect
        self.coords = coords
        self.image = None

    def move(self, x: int, y: int) -> None:
        """
        changes the piece's rect coordinates
        """

        self.rect.left = x
        self.rect.top = y

    def set_size(self, width: int, height: int) -> None:
        """
        changes the piece's rect size
        """

        self.rect.width = width
        self.rect.height = height

    def update(self) -> None:
        pass


class ShittyPawn(ShittyPiece):
    """pawn sprite class"""

    def __init__(self, screen: pygame.Surface, black: bool, rect: pygame.Rect, coords: str) -> None:
        super().__init__(screen, black, rect, coords)
        img_path = None
        if self.black:
            img_path = pathlib.Path('shitty_art/shittypawnblack.png')
        else:
            img_path = pathlib.Path('shitty_art/shittypawnwhite.png')
        self.image = pygame.image.load(str(img_path))
        self.initial_position = True


class ShittyRook(ShittyPiece):
    """rook sprite class"""

    def __init__(self, screen: pygame.Surface, black: bool, rect: pygame.Rect, coords: str) -> None:
        super().__init__(screen, black, rect, coords)
        img_path = None
        if self.black:
            img_path = pathlib.Path('shitty_art/shittyrookblack.png')
        else:
            img_path = pathlib.Path('shitty_art/shittyrookwhite.png')
        self.image = pygame.image.load(str(img_path))
        self.initial_position = True


class ShittyBishop(ShittyPiece):
    """bishop sprite class"""

    def __init__(self, screen: pygame.Surface, black: bool, rect: pygame.Rect, coords: str) -> None:
        super().__init__(screen, black, rect, coords)
        img_path = None
        if self.black:
            img_path = pathlib.Path('shitty_art/shittybishopblack.png')
        else:
            img_path = pathlib.Path('shitty_art/shittybishopwhite.png')
        self.image = pygame.image.load(str(img_path))


class ShittyKnight(ShittyPiece):
    """knight sprite class"""

    def __init__(self, screen: pygame.Surface, black: bool, rect: pygame.Rect, coords: str) -> None:
        super().__init__(screen, black, rect, coords)
        img_path = None
        if self.black:
            img_path = pathlib.Path('shitty_art/shittyknightblack.png')
        else:
            img_path = pathlib.Path('shitty_art/shittyknightwhite.png')
        self.image = pygame.image.load(str(img_path))


class ShittyQueen(ShittyPiece):
    """queen sprite class"""

    def __init__(self, screen: pygame.Surface, black: bool, rect: pygame.Rect, coords: str) -> None:
        super().__init__(screen, black, rect, coords)
        img_path = None
        if self.black:
            img_path = pathlib.Path('shitty_art/shittyqueenblack.png')
        else:
            img_path = pathlib.Path('shitty_art/shittyqueenwhite.png')
        self.image = pygame.image.load(str(img_path))


class ShittyKing(ShittyPiece):
    """king sprite class"""

    def __init__(self, screen: pygame.Surface, black: bool, rect: pygame.Rect, coords: str) -> None:
        super().__init__(screen, black, rect, coords)
        img_path = None
        if self.black:
            img_path = pathlib.Path('shitty_art/shittykingblack.png')
        else:
            img_path = pathlib.Path('shitty_art/shittykingwhite.png')
        self.image = pygame.image.load(str(img_path))
        self.initial_position = True
