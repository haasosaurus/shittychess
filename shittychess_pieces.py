# coding=utf-8

from os import PathLike
from typing import Union
from typing import NoReturn

import pygame

from shittychess_sprites import ShittySprite


class ShittyMovementPatterns:
    """class to save a piece's movement patterns"""

    def __init__(self):
        self.horizontal = 0
        self.vertical = 0
        self.diagonal = 0
        self.pattern_list = []


class ShittyPiece(ShittySprite):
    """base sprite class for pieces"""

    def __init__(self, black: bool, rect: pygame.Rect, coords: str, img_path: Union[PathLike, str], **kwargs) -> NoReturn:
        super().__init__(black, rect, coords, img_path)
        self.initial_position = True
        self.movement_patterns = ShittyMovementPatterns()

        self.local_debug = True

    # this needs to be fixed for sure
    def __bool__(self) -> bool:
        # if self.local_debug:
        #     print(type(self).__name__)
        #     print(type(self).__name__ != 'ShittyPiece')
        return type(self).__name__ != 'ShittyPiece'

        # if self.local_debug:
        #     print(f'ShittyPiece.__bool__() isinstance(self, ShittyPiece)  != {isinstance(self, ShittyPiece)}')
        # return not isinstance(self, ShittyPiece)

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
            if self.initial_position:
                self.initial_position = False

    def move_patterns(self) -> ShittyMovementPatterns:
        return self.movement_patterns

    def update(self) -> NoReturn:
        pass


class ShittyPawn(ShittyPiece):
    """pawn sprite class"""

    def __init__(self, black: bool, rect: pygame.Rect, coords: str, img_path: Union[PathLike, str]) -> NoReturn:
        super().__init__(black, rect, coords, img_path)


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

    def __init__(self, black: bool, rect: pygame.Rect, coords: str, img_path: Union[PathLike, str]) -> NoReturn:
        super().__init__(black, rect, coords, img_path)

        # movement stuff
        self.movement_patterns.horizontal = 7
        self.movement_patterns.vertical = 7


class ShittyBishop(ShittyPiece):
    """bishop sprite class"""

    def __init__(self, black: bool, rect: pygame.Rect, coords: str, img_path: Union[PathLike, str]) -> NoReturn:
        super().__init__(black, rect, coords, img_path)

        # movement stuff
        self.movement_patterns.diagonal = 7


class ShittyKnight(ShittyPiece):
    """knight sprite class"""

    def __init__(self, black: bool, rect: pygame.Rect, coords: str, img_path: Union[PathLike, str]) -> NoReturn:
        super().__init__(black, rect, coords, img_path)

        # movement stuff
        self.movement_patterns.pattern_list = [
            (1, 2), (1, -2),
            (2, 1), (2, -1),
            (-2, 1), (-2, -1),
            (-1, 2), (-1, -2),
        ]


class ShittyQueen(ShittyPiece):
    """queen sprite class"""

    def __init__(self, black: bool, rect: pygame.Rect, coords: str, img_path: Union[PathLike, str]) -> NoReturn:
        super().__init__(black, rect, coords, img_path)

        # movement stuff
        self.movement_patterns.horizontal = 7
        self.movement_patterns.vertical = 7
        self.movement_patterns.diagonal = 7


class ShittyKing(ShittyPiece):
    """king sprite class"""

    def __init__(self, black: bool, rect: pygame.Rect, coords: str, img_path: Union[PathLike, str]) -> NoReturn:
        super().__init__(black, rect, coords, img_path)

        # movement stuff
        self.movement_patterns.horizontal = 1
        self.movement_patterns.vertical = 1
        self.movement_patterns.diagonal = 1
