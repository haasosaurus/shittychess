# coding=utf-8

from typing import NoReturn

import pathlib

import pygame


class ShittyMovementPatterns:
    """class to save a piece's movement patterns"""

    def __init__(self):
        self.horizontal = 0
        self.vertical = 0
        self.diagonal = 0
        self.pattern_list = []


class ShittyPiece(pygame.sprite.Sprite):
    """base sprite class for pieces"""

    def __init__(self, screen: pygame.Surface, black: bool, rect: pygame.Rect, coords: str) -> NoReturn:
        pygame.sprite.Sprite.__init__(self)
        self.black = black
        self.screen = screen
        self.rect = rect
        self.coords = coords
        self.movement_patterns = ShittyMovementPatterns()
        self.image = None
        self.initial_position = True

        self.local_debug = False

    # this needs to be fixed for sure
    def __bool__(self) -> bool:
        if self.local_debug:
            print(type(self).__name__)
            print(type(self).__name__ != 'ShittyPiece')
        return type(self).__name__ != 'ShittyPiece'

    def set_rect(self, rect: pygame.Rect) -> NoReturn:
        """
        sets the piece's rect with another pygame.Rect
        used for resizing and such not moving a piece
        """

        self.rect.left = rect.left
        self.rect.top = rect.top
        self.rect.width = rect.width
        self.rect.height = rect.height

    def move(self, rect: pygame.Rect) -> NoReturn:
        """
        moves the piece during gameplay
        """

        if self.rect != rect:
            self.set_rect(rect)
            self.initial_position = False

    def move_patterns(self) -> ShittyMovementPatterns:
        return self.movement_patterns

    def update(self) -> NoReturn:
        pass


class ShittyPawn(ShittyPiece):
    """pawn sprite class"""

    def __init__(self, screen: pygame.Surface, black: bool, rect: pygame.Rect, coords: str) -> NoReturn:
        super().__init__(screen, black, rect, coords)

        # image stuff
        img_path = None
        if self.black:
            img_path = pathlib.Path('shitty_art/shittypawnblack.png')
        else:
            img_path = pathlib.Path('shitty_art/shittypawnwhite.png')
        self.image = pygame.image.load(str(img_path))

        # movement stuff
        self.black_move_patterns_initial = ShittyMovementPatterns()
        self.black_move_patterns_initial.pattern_list = [
            (0, 1), (0, 2),
            (1, 1), (-1, 1)
        ]
        self.black_move_patterns = ShittyMovementPatterns()
        self.black_move_patterns.pattern_list = [
            (0, 1),
            (1, 1), (-1, 1)
        ]
        self.white_move_patterns_initial = ShittyMovementPatterns()
        self.white_move_patterns_initial.pattern_list = [
            (0, -1), (0, -2),
            (1, -1), (-1, -1)
        ]
        self.white_move_patterns = ShittyMovementPatterns()
        self.white_move_patterns.pattern_list = [
            (0, -1),
            (1, -1), (-1, -1)
        ]

    def move_patterns(self) -> ShittyMovementPatterns:
        if self.black:
            if self.initial_position:
                return self.black_move_patterns_initial
            else:
                return self.black_move_patterns
        else:
            if self.initial_position:
                return self.white_move_patterns_initial
            else:
                return self.white_move_patterns


class ShittyRook(ShittyPiece):
    """rook sprite class"""

    def __init__(self, screen: pygame.Surface, black: bool, rect: pygame.Rect, coords: str) -> NoReturn:
        super().__init__(screen, black, rect, coords)
        img_path = None
        if self.black:
            img_path = pathlib.Path('shitty_art/shittyrookblack.png')
        else:
            img_path = pathlib.Path('shitty_art/shittyrookwhite.png')
        self.image = pygame.image.load(str(img_path))
        self.movement_patterns.horizontal = 7
        self.movement_patterns.vertical = 7


class ShittyBishop(ShittyPiece):
    """bishop sprite class"""

    def __init__(self, screen: pygame.Surface, black: bool, rect: pygame.Rect, coords: str) -> NoReturn:
        super().__init__(screen, black, rect, coords)
        img_path = None
        if self.black:
            img_path = pathlib.Path('shitty_art/shittybishopblack.png')
        else:
            img_path = pathlib.Path('shitty_art/shittybishopwhite.png')
        self.image = pygame.image.load(str(img_path))
        self.movement_patterns.diagonal = 7


class ShittyKnight(ShittyPiece):
    """knight sprite class"""

    def __init__(self, screen: pygame.Surface, black: bool, rect: pygame.Rect, coords: str) -> NoReturn:
        super().__init__(screen, black, rect, coords)
        img_path = None
        if self.black:
            img_path = pathlib.Path('shitty_art/shittyknightblack.png')
        else:
            img_path = pathlib.Path('shitty_art/shittyknightwhite.png')
        self.image = pygame.image.load(str(img_path))
        self.movement_patterns.pattern_list = [
            (1, 2), (1, -2),
            (2, 1), (2, -1),
            (-2, 1), (-2, -1),
            (-1, 2), (-1, -2),
        ]


class ShittyQueen(ShittyPiece):
    """queen sprite class"""

    def __init__(self, screen: pygame.Surface, black: bool, rect: pygame.Rect, coords: str) -> NoReturn:
        super().__init__(screen, black, rect, coords)
        img_path = None
        if self.black:
            img_path = pathlib.Path('shitty_art/shittyqueenblack.png')
        else:
            img_path = pathlib.Path('shitty_art/shittyqueenwhite.png')
        self.image = pygame.image.load(str(img_path))
        self.movement_patterns.horizontal = 7
        self.movement_patterns.vertical = 7
        self.movement_patterns.diagonal = 7


class ShittyKing(ShittyPiece):
    """king sprite class"""

    def __init__(self, screen: pygame.Surface, black: bool, rect: pygame.Rect, coords: str) -> NoReturn:
        super().__init__(screen, black, rect, coords)
        img_path = None
        if self.black:
            img_path = pathlib.Path('shitty_art/shittykingblack.png')
        else:
            img_path = pathlib.Path('shitty_art/shittykingwhite.png')
        self.image = pygame.image.load(str(img_path))
        self.movement_patterns.horizontal = 1
        self.movement_patterns.vertical = 1
        self.movement_patterns.diagonal = 1
