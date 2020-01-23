# coding=utf-8

from os import PathLike
from typing import Union
from typing import Tuple
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

    def __init__(
            self,
            black: bool,
            rect: pygame.Rect,
            coords: Tuple[int, int],
            img_path: Union[PathLike, str],
            **kwargs
    ) -> NoReturn:
        """constructor"""

        super().__init__(black, rect, coords, img_path)
        self.initial_position = True
        self.movement_patterns = ShittyMovementPatterns()

    def set_rect(self, rect: pygame.Rect) -> NoReturn:
        """
        sets the piece's rect with another pygame.Rect
        used for resizing and such not moving a piece
        """

        self.rect = pygame.Rect.copy(rect)

    def move(self, rect: pygame.Rect) -> NoReturn:
        """moves the piece during game play"""

        if self.rect != rect:
            self.set_rect(rect)
            if self.initial_position:
                self.initial_position = False

    def move_patterns(self) -> ShittyMovementPatterns:
        """returns move patterns for this piece"""

        return self.movement_patterns

    def update(self) -> NoReturn:
        """pygame sprite group helper method"""

        # placeholder since it's giving me a warning using pass
        print(f'{self.__class__.__name__} updated')


class ShittyPawn(ShittyPiece):
    """pawn sprite class"""

    def __init__(
            self,
            black: bool,
            rect: pygame.Rect,
            coords: Tuple[int, int],
            img_path: Union[PathLike, str]
    ) -> NoReturn:
        """constructor"""

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
        """returns specific move patterns for the pawn's current state"""

        if self.black:
            if self.initial_position:
                return self.black_move_patterns_initial
            return self.black_move_patterns
        else:
            if self.initial_position:
                return self.white_move_patterns_initial
            return self.white_move_patterns


class ShittyRook(ShittyPiece):
    """rook sprite class"""

    def __init__(
            self,
            black: bool,
            rect: pygame.Rect,
            coords: Tuple[int, int],
            img_path: Union[PathLike, str]
    ) -> NoReturn:
        """constructor"""

        super().__init__(black, rect, coords, img_path)

        # movement stuff
        self.movement_patterns.horizontal = 7
        self.movement_patterns.vertical = 7


class ShittyBishop(ShittyPiece):
    """bishop sprite class"""

    def __init__(
            self,
            black: bool,
            rect: pygame.Rect,
            coords: Tuple[int, int],
            img_path: Union[PathLike, str]
    ) -> NoReturn:
        """constructor"""

        super().__init__(black, rect, coords, img_path)

        # movement stuff
        self.movement_patterns.diagonal = 7


class ShittyKnight(ShittyPiece):
    """knight sprite class"""

    def __init__(
            self,
            black: bool,
            rect: pygame.Rect,
            coords: Tuple[int, int],
            img_path: Union[PathLike, str]
    ) -> NoReturn:
        """constructor"""

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

    def __init__(
            self,
            black: bool,
            rect: pygame.Rect,
            coords: Tuple[int, int],
            img_path: Union[PathLike, str]
    ) -> NoReturn:
        """constructor"""

        super().__init__(black, rect, coords, img_path)

        # movement stuff
        self.movement_patterns.horizontal = 7
        self.movement_patterns.vertical = 7
        self.movement_patterns.diagonal = 7


class ShittyKing(ShittyPiece):
    """king sprite class"""

    def __init__(
            self,
            black: bool,
            rect: pygame.Rect,
            coords: Tuple[int, int],
            img_path: Union[PathLike, str]
    ) -> NoReturn:
        """constructor"""

        super().__init__(black, rect, coords, img_path)

        # movement stuff
        self.movement_patterns.horizontal = 1
        self.movement_patterns.vertical = 1
        self.movement_patterns.diagonal = 1
