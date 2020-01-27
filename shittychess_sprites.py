# coding=utf-8


from os import PathLike
from typing import List
from typing import NoReturn
from typing import Tuple
from typing import Union

import pygame


class ShittyColor:
    def __init__(self, color: str) -> NoReturn:

        if not isinstance(color, str):
            raise TypeError('color must be a string, either \'black\' or \'white\'')
        if color not in ['black', 'white']:
            raise ValueError('color must be either \'black\' or \'white\'')
        self._black = True if color == 'black' else False

    def is_black(self):
        return self._black

    def is_white(self):
        return not self._black

    def __eq__(self, other):
        if isinstance(other, ShittyColor):
            return self.is_black() == other.is_black()
        elif isinstance(other, str):
            if other in ['black', 'whtie']:
                return other == str(self)
            else:
                raise NotImplementedError('Can only test equality against strings \'black\' and \'white\'')
        else:
            raise NotImplementedError('Can only test equality with other ShittyColor objects, or \'black\' and \'white\'')

    def __str__(self):
        if self._black:
            return 'black'
        return 'white'

    def __repr__(self):
        return f'ShittyColor(\'{str(self)}\')'


class ShittyMousePointer(pygame.sprite.Sprite):
    def __init__(self, x, y) -> NoReturn:
        """constructor"""

        pygame.sprite.Sprite.__init__(self)
        self.rect = pygame.Rect(x, y, 1, 1)


class ShittySprite(pygame.sprite.Sprite):
    """base sprite class for pieces and spaces"""

    def __init__(
            self,
            color: Union[ShittyColor, str],
            rect: pygame.Rect,
            coords: Tuple[int, int],
            img_path: Union[PathLike, str]
    ) -> NoReturn:
        """constructor"""

        pygame.sprite.Sprite.__init__(self)
        self.rect = rect
        self.color = ShittyColor(color) if isinstance(color, str) else color
        self.image: Union[pygame.image, None] = None
        self.coords = coords
        self.load_image(img_path)

    def load_image(self, img_path: Union[PathLike, str]) -> NoReturn:
        self.image = pygame.image.load(
            img_path if isinstance(img_path, str) else str(img_path)
        )
        width = 75
        height = 75
        rect = self.image.get_rect()
        if rect.width != width or rect.height != height:
            self.image = pygame.transform.smoothscale(self.image, (width, height))

    def move_to_front(self) -> bool:
        for group in self.groups():
            try:
                group.move_to_front(self)
                return True
            except AttributeError as e:
                print(f'{e}\ncontinuing...')
                continue
        return False


class ShittyMovementPatterns:
    """class to save a piece's movement patterns"""

    def __init__(
            self,
            horizontal: int = 0,
            vertical: int = 0,
            diagonal: int = 0,
    ) -> NoReturn:
        """constructor"""

        self.horizontal = horizontal
        self.vertical = vertical
        self.diagonal = diagonal


class ShittyPiece(ShittySprite):
    """base sprite class for pieces"""

    def __init__(
            self,
            color: Union[ShittyColor, str],
            rect: pygame.Rect,
            coords: Tuple[int, int],
            img_path: Union[PathLike, str]
    ) -> NoReturn:
        """constructor"""

        super().__init__(color, rect, coords, img_path)
        self.initial_position = True
        self.movements = []

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

    def move_patterns(self) -> List[ShittyMovementPatterns]:  # change to tuple
        """returns move patterns for this piece"""

        return self.movements

    def update(self) -> NoReturn:
        """pygame sprite group helper method"""

        # placeholder since it's giving me a warning using pass
        print(f'{self.__class__.__name__} updated')


class ShittyPawn(ShittyPiece):
    """pawn sprite class"""

    name = 'pawn'

    def __init__(
            self,
            color: Union[ShittyColor, str],
            rect: pygame.Rect,
            coords: Tuple[int, int],
            img_path: Union[PathLike, str]
    ) -> NoReturn:
        """constructor"""

        super().__init__(color, rect, coords, img_path)
        self.movements.append(ShittyMovementPatterns(
            vertical=1,
            diagonal=1
        ))
        self.movements.append(ShittyMovementPatterns(
            vertical=2,
            diagonal=1
        ))

    def move(self, rect: pygame.Rect) -> NoReturn:
        """moves the piece during game play"""

        if self.rect != rect:
            self.set_rect(rect)
            if self.initial_position:
                self.initial_position = False
                indexes = []
                for index, movement in enumerate(self.movements):
                    if movement.vertical > 1:
                        indexes.append(index)
                for index in reversed(sorted(indexes)):
                    del self.movements[index]


class ShittyRook(ShittyPiece):
    """rook sprite class"""

    name = 'rook'

    def __init__(
            self,
            color: Union[ShittyColor, str],
            rect: pygame.Rect,
            coords: Tuple[int, int],
            img_path: Union[PathLike, str]
    ) -> NoReturn:
        """constructor"""

        super().__init__(color, rect, coords, img_path)
        self.movements.append(ShittyMovementPatterns(
            horizontal=7,
            vertical=7,
        ))


class ShittyBishop(ShittyPiece):
    """bishop sprite class"""

    name = 'bishop'

    def __init__(
            self,
            color: Union[ShittyColor, str],
            rect: pygame.Rect,
            coords: Tuple[int, int],
            img_path: Union[PathLike, str]
    ) -> NoReturn:
        """constructor"""

        super().__init__(color, rect, coords, img_path)
        self.movements.append(ShittyMovementPatterns(
            diagonal=7
        ))


class ShittyKnight(ShittyPiece):
    """knight sprite class"""

    name = 'knight'

    def __init__(
            self,
            color: Union[ShittyColor, str],
            rect: pygame.Rect,
            coords: Tuple[int, int],
            img_path: Union[PathLike, str]
    ) -> NoReturn:
        """constructor"""

        super().__init__(color, rect, coords, img_path)
        self.movements.append(ShittyMovementPatterns(
            horizontal=2,
            vertical=1,
        ))
        self.movements.append(ShittyMovementPatterns(
            horizontal=1,
            vertical=2,
        ))


class ShittyQueen(ShittyPiece):
    """queen sprite class"""

    name = 'queen'

    def __init__(
            self,
            color: Union[ShittyColor, str],
            rect: pygame.Rect,
            coords: Tuple[int, int],
            img_path: Union[PathLike, str]
    ) -> NoReturn:
        """constructor"""

        super().__init__(color, rect, coords, img_path)
        self.movements.append(ShittyMovementPatterns(
            horizontal=7,
            vertical=7,
            diagonal=7,
        ))


class ShittyKing(ShittyPiece):
    """king sprite class"""

    name = 'king'

    def __init__(
            self,
            color: Union[ShittyColor, str],
            rect: pygame.Rect,
            coords: Tuple[int, int],
            img_path: Union[PathLike, str]
    ) -> NoReturn:
        """constructor"""

        super().__init__(color, rect, coords, img_path)
        self.movements.append(ShittyMovementPatterns(
            horizontal=1,
            vertical=1,
            diagonal=1,
        ))
