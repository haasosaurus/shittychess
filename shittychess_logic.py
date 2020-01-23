# coding=utf-8


from typing import List
from typing import Tuple
from typing import Union
from typing import NoReturn

import pygame

from shittychess_sprites import ShittyMousePointer
from shittychess_pieces import ShittyPiece


class ShittyLogic:
    """
    game 'logic' class
    the shittiest logic, getting less shitty by the hour
    """

    def __init__(self) -> NoReturn:
        self.settings = None  # ShittySettings
        self.board = None  # ShittyBoard
        self.layout = None  # ShittyLayout
        self.__coords_to_space = {}
        self.__coords_to_indexes = {}
        self.__indexes_to_coords = {}

    def configure(self) -> NoReturn:
        """
        configure class's properties after they have been assigned externally
        this sets up all the dicts and their matching dicts that i thought we
        needed to make this 'logic' work
        """

        for space in self.board.board_space_group.sprites():
            self.__coords_to_space.update({space.coords: space})
            self.__coords_to_indexes.update({space.coords: space.indexes})
            self.__indexes_to_coords.update({space.indexes: space.coords})

    def xy_to_coords(self, x: int, y: int) -> Union[str, None]:
        """takes mouse position (x and y) and returns chess coordinates"""

        # this should throw an exception if len(collisions) > 1
        collisions = pygame.sprite.spritecollide(
            ShittyMousePointer(x, y),
            self.board.board_space_group,
            False
        )
        if len(collisions) == 1:
            return collisions[0].coords
        return None

    def coords_to_indexes(self, coords: str) -> Union[Tuple[int, int], None]:
        """
        takes chess coordinates, returns the corresponding zero-indexed tuple
        with 2D list indexes for the board space, or None if not found
        0, 5 = ShittyLogic.coords_to_indexes('f4')
        """

        if coords in self.__coords_to_indexes:
            return self.__coords_to_indexes[coords]
        return None

    def coords_to_rect(self, coords: str) -> Union[pygame.Rect, None]:
        """
        takes chess coordinates, returns a pygame.Rect object of the
        corresponding board space or None if not found
        pygame.Rect(0, 120, 60, 60) = ShittyLogic.coords_to_rect('f4')
        """

        if coords in self.__coords_to_space:
            return pygame.Rect.copy(self.__coords_to_space[coords].rect)
        return None

    def indexes_to_coords(self, indexes: Tuple[int, int]) -> Union[str, None]:
        """
        takes a zero-indexed tuple with 2D list indexes, returns the
        corresponding chess notation for a board space or None if not found
        'f4' = ShittyLogic.indexes_to_coords(0, 5)
        """

        if indexes in self.__indexes_to_coords:
            return self.__indexes_to_coords[indexes]
        return None

    def indexes_to_rect(self, indexes: Tuple[int, int]) -> Union[pygame.Rect, None]:
        """
        takes a zero-indexed tuple with 2D list indexes, returns a pygame.Rect
        object of the corresponding board space or None if not found
        pygame.Rect(0, 120, 60, 60) = ShittyLogic.indexes_to_rect(0, 5)
        """

        return self.coords_to_rect(self.indexes_to_coords(indexes))

    def rect_to_coords(self, rect: pygame.Rect) -> Union[str, None]:
        """
        takes a pygame.Rect object, returns the corresponding chess notation
        for a board space or None if not found
        'f4' = ShittyLogic.rect_to_coords(pygame.Rect(0, 120, 60, 60))
        """

        for space in self.board.board_space_group.sprites():
            if space.rect == rect:
                return space.coords
        return None

    def rect_to_indexes(self, rect: pygame.Rect) -> Union[Tuple[int, int], None]:
        """
        takes a pygame.Rect object, returns the corresponding zero-indexed
        tuple with 2D list indexes for the board space, or None if not found
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
        invalid_move_coords = []
        for coords in valid_move_coords:
            sprite = self.layout.coords_to_sprite(coords)

            # if there is a sprite at coords
            if sprite:

                # and it is friendly
                if sprite.black == piece.black:

                    # move not allowed, can't kill your friend
                    invalid_move_coords.append(coords)

        # pawn
        if piece.__class__.__name__ == 'ShittyPawn':
            for coords in valid_move_coords:

                # if moving diagonally
                if self.coords_to_indexes(coords)[0] != self.coords_to_indexes(piece.coords)[0]:
                    sprite = self.layout.coords_to_sprite(coords)

                    # if a sprite is not there
                    if not sprite:

                        # move not allowed, pawns can only go diagonally while attacking
                        invalid_move_coords.append(coords)

                # if moving vertically


        # remove invalid coords from list
        for coords in reversed(invalid_move_coords):
            while coords in valid_move_coords:
                valid_move_coords.remove(coords)

        # return a list of chess coordinates strings
        return valid_move_coords

    def move_piece_with_mouse(self, sprite: ShittyPiece, x, y) -> bool:
        """
        attempts to move argument sprite to mouse coordinate arguments
        returns True if it succeeds, False if it fails
        """

        target_coords = self.xy_to_coords(x, y)
        if target_coords:
            if target_coords != sprite.coords:
                valid_move_coords = self.valid_move_coords(sprite)
                if target_coords in valid_move_coords:
                    sprite.move(self.coords_to_rect(target_coords))
                    sprite.coords = target_coords
                    return True
        return False
