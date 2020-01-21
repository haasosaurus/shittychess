# coding=utf-8


from typing import List
from typing import Tuple
from typing import Union
from typing import NoReturn

import pygame

from shittychess_utils import ShittyMousePointer
from shittychess_pieces import ShittyPiece


class ShittySpace(pygame.sprite.Sprite):

    def __init__(self, rect: pygame.Rect, coords: str) -> NoReturn:
        pygame.sprite.Sprite.__init__(self)
        self.rect = rect
        self.coords = coords

class ShittyLogic:
    """
    game 'logic' class
    the shittiest logic
    """

    def __init__(self) -> NoReturn:
        self.settings = None  # ShittySettings
        self.board = None  # ShittyBoard
        self.layout = None # ShittyLayout
        self.__coords_to_rect = {}
        self.__rect_to_coords = {}
        self.__coords_to_indexes = {}
        self.__indexes_to_coords = {}
        self.__spaces_to_coords = {}
        self.__spaces_group = pygame.sprite.Group()

    def configure(self) -> NoReturn:
        """
        configure class's properties after they have been assigned externally
        this sets up all the dicts and their matching dicts that i thought we needed to
        make this 'logic' work
        """

        self.settings.coords_list = []
        for row, y in zip(self.settings.row_headers, range(0, self.settings.board_height(), self.settings.space_height())):
            for col, x in zip(self.settings.col_headers, range(0, self.settings.board_width(), self.settings.space_width())):
                pos_name = col + row
                tmp_rect = pygame.Rect(x, y, self.settings.space_width(), self.settings.space_height())
                self.__coords_to_rect.update({pos_name: tmp_rect})
                self.settings.coords_list.append(pos_name)
        for y, row_number in enumerate(self.settings.row_headers):
            for x, col_letter in enumerate(self.settings.col_headers):
                self.__coords_to_indexes.update({f'{col_letter}{row_number}': (x, y)})
        for coords, indexes in self.__coords_to_indexes.items():
            self.__indexes_to_coords.update({indexes: coords})
        for coords, rect in self.__coords_to_rect.items():
            self.__rect_to_coords.update({(rect.left, rect.top, rect.width, rect.height): coords})
            tmp_rect = pygame.Rect.copy(rect)
            tmp_rect.left += self.settings.board_start_x()
            tmp_rect.top += self.settings.board_start_y()
            self.__spaces_to_coords.update({ShittySpace(tmp_rect, coords): coords})
        for space in self.__spaces_to_coords:
            self.__spaces_group.add(space)

    def resize(self) -> NoReturn:
        for sprite, coords in self.__spaces_to_coords.items():
            sprite.rect = self.coords_to_rect(coords)

    def xy_to_coords(self, x: int, y: int) -> Union[str, None]:
        collisions = pygame.sprite.spritecollide(ShittyMousePointer(x, y), self.__spaces_group, False)
        if len(collisions) == 1:
            if collisions[0] in self.__spaces_to_coords:
                return self.__spaces_to_coords[collisions[0]]
        return None

    def coords_to_indexes(self, coords: str) -> Union[Tuple[int, int], None]:
        """
        takes chess coordinates
        returns the corresponding zero-indexed tuple with 2D list indexes for the board space,
        or None if not found
        0, 5 = ShittyLogic.coords_to_indexes('f4')
        """

        if coords in self.__coords_to_indexes:
            return self.__coords_to_indexes[coords]
        return None

    def coords_to_rect(self, coords: str) -> Union[pygame.Rect, None]:
        """
        takes chess coordinates
        returns a pygame.Rect object of the corresponding board space or None if not found
        pygame.Rect(0, 120, 60, 60) = ShittyLogic.coords_to_rect('f4')
        """

        if coords not in self.__coords_to_rect:
            return None
        tmp_rect = pygame.Rect(self.__coords_to_rect[coords])
        if self.settings.headers_enabled:
            tmp_rect.left += self.settings.row_header_width()
            tmp_rect.top += self.settings.col_header_height()
        return tmp_rect

    def indexes_to_coords(self, indexes: Tuple[int, int]) -> Union[str, None]:
        """
        takes a zero-indexed tuple with 2D list indexes
        returns the corresponding chess notation for a board space or None if not found
        'f4' = ShittyLogic.indexes_to_coords(0, 5)
        """

        if indexes in self.__indexes_to_coords:
            return self.__indexes_to_coords[indexes]
        return None

    def indexes_to_rect(self, indexes: Tuple[int, int]) -> Union[pygame.Rect, None]:
        """
        takes a zero-indexed tuple with 2D list indexes
        returns a pygame.Rect object of the corresponding board space or None if not found
        pygame.Rect(0, 120, 60, 60) = ShittyLogic.indexes_to_rect(0, 5)
        """

        return self.coords_to_rect(self.indexes_to_coords(indexes))

    def rect_to_coords(self, rect: pygame.Rect) -> Union[str, None]:
        """
        takes a pygame.Rect object
        returns the corresponding chess notation for a board space or None if not found
        'f4' = ShittyLogic.rect_to_coords(pygame.Rect(0, 120, 60, 60))
        """

        left = rect.left
        top = rect.top
        width = rect.width
        height = rect.height
        if self.settings.headers_enabled:
            left -= self.settings.row_header_width()
            top -= self.settings.col_header_height()
        tmp_tuple = (left, top, width, height)
        if tmp_tuple not in self.__rect_to_coords:
            return None
        return self.__rect_to_coords[(left, top, width, height)]

    def rect_to_indexes(self, rect: pygame.Rect) -> Union[Tuple[int, int], None]:
        """
        takes a pygame.Rect object
        returns the corresponding zero-indexed tuple with 2D list indexes for the board space,
        or None if not found
        0, 5 = ShittyLogic.rect_to_indexes(pygame.Rect(0, 120, 60, 60))
        """

        return self.coords_to_indexes(self.rect_to_coords(rect))

    def __valid_space_coords(self, piece: ShittyPiece) -> List[str]:
        """
        make a list of valid moves for a piece that are on the game board,
        no other error checking performed. return them as a list of chess
        coordinate strings
        """

        space_coords = []
        piece_indexes = self.coords_to_indexes(piece.coords)
        if piece.move_patterns().horizontal > 0:
            pass
        if piece.move_patterns().vertical > 0:
            pass
        if piece.move_patterns().diagonal > 0:
            pass
        for pattern in piece.move_patterns().pattern_list:
            x = piece_indexes[0] + pattern[0]
            if x >= self.settings.cols or x < 0:
                continue
            y = piece_indexes[1] + pattern[1]
            if self.settings.rows > y >= 0:
                space_coords.append(self.indexes_to_coords((x, y)))
        return space_coords

    def valid_move_coords(self, piece: ShittyPiece) -> List[str]:
        """
        get valid move space list from self.__valid_space_coords, and run more in
        depth tests on them to make sure they are really valid move coordinates
        """

        # check to see if a friendly piece is blocking
        valid_move_coords = self.__valid_space_coords(piece)
        piece_black = piece.black
        invalid_move_coords = []
        for coords in valid_move_coords:
            if piece_black:
                if self.layout.sprite_exists_black(coords):
                    invalid_move_coords.append(coords)
            else:
                if self.layout.sprite_exists_white(coords):
                    invalid_move_coords.append(coords)

        # pawn
        if piece.__class__.__name__ == 'ShittyPawn':
            for coords in valid_move_coords:
                if self.coords_to_indexes(coords)[0] != self.coords_to_indexes(piece.coords)[0]:
                    if piece_black:
                        if not self.layout.sprite_exists_white(coords):
                            invalid_move_coords.append(coords)
                    else:
                        if not self.layout.sprite_exists_black(coords):
                            invalid_move_coords.append(coords)

        # remove invalid coords from list
        for coords in reversed(invalid_move_coords):
            while coords in valid_move_coords:
                valid_move_coords.remove(coords)

        # return a list of chess coordinates strings
        return valid_move_coords

    def move_piece_xy(self, sprite: pygame.sprite.Sprite, x, y) -> bool:
        target_coords = self.xy_to_coords(x, y)
        if target_coords:
            if target_coords != sprite.coords:
                valid_move_coords = self.valid_move_coords(sprite)
                if target_coords in valid_move_coords:
                    sprite.move(self.coords_to_rect(target_coords))
                    sprite.coords = target_coords
                    return True
        return False
