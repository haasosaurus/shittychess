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
        self.coords_to_chess_coords = {}
        self.chess_coords_to_coords = {}

    def configure(self) -> NoReturn:
        """
        configure class's properties after they have been assigned externally
        """

        for y, number in enumerate(self.settings.row_headers):
            for x, letter in enumerate(self.settings.col_headers):
                chess_coords = f'{letter}{number}'
                coords = x, y
                self.coords_to_chess_coords.update({coords: chess_coords})
                self.chess_coords_to_coords.update({chess_coords: coords})

    def mouse_to_coords(self, x: int, y: int) -> Union[Tuple[int, int], None]:
        """
        takes mouse position (x and y) and returns zero-indexed x, y
        coordinates
        """

        collisions = pygame.sprite.spritecollide(
            ShittyMousePointer(x, y),
            self.board.spaces_group,
            False
        )
        if len(collisions) == 1:
            return collisions[0].coords
        return None

    def mouse_to_sprite(
            self,
            x: int,
            y: int,
            black: bool
    ) -> Union[ShittyPiece, None]:
        """returns piece sprite if clicked, or None"""

        if black:
            target_group = self.layout.sprite_group_black
        else:
            target_group = self.layout.sprite_group_white
        collisions = pygame.sprite.spritecollide(
            ShittyMousePointer(x, y),
            target_group,
            False
        )
        if len(collisions) == 1:
            return collisions[0]
        return None

    def coords_to_rect(self, coords: Tuple[int, int]) -> Union[pygame.Rect, None]:
        """
        takes zero-indexed x, y board space coordinates to board space and
        returns a pygame.Rect
        """

        return pygame.Rect.copy(self.board.spaces[coords].rect)

    def coords_to_sprite(self, coords: Tuple[int, int]) -> Union[ShittyPiece, None]:
        """
        takes zero-indexed x, y board space coordinates and returns sprite if
        sprite exists at coords else returns None
        """

        for sprite in self.layout.sprite_group_all.sprites():
            if sprite.coords == coords:
                return sprite
        return None

    def __valid_space_coords(self, piece: ShittyPiece) -> List[Tuple[int, int]]:
        """
        make a list of valid moves for a piece that are on the game board,
        no other error checking performed. return them as a list of
        zero-indexed x, y board space coordinates
        """

        space_coords = []
        if piece.move_patterns().horizontal > 0:
            pass
        if piece.move_patterns().vertical > 0:
            pass
        if piece.move_patterns().diagonal > 0:
            pass
        for pattern in piece.move_patterns().pattern_list:
            x = piece.coords[0] + pattern[0]
            if x >= self.settings.cols or x < 0:
                continue
            y = piece.coords[1] + pattern[1]
            if self.settings.rows > y >= 0:
                space_coords.append((x, y))
        return space_coords

    def valid_move_coords(self, piece: ShittyPiece) -> List[Tuple[int, int]]:
        """
        get valid move space list from self.__valid_space_coords, and run more in
        depth tests on them to make sure they are really valid move coordinates
        """

        # check to see if a friendly piece is blocking
        valid_move_coords = self.__valid_space_coords(piece)
        invalid_move_coords = []
        for coords in valid_move_coords:
            sprite = self.coords_to_sprite(coords)

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
                if coords[0] != piece.coords[0]:
                    sprite = self.coords_to_sprite(coords)

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

        target_coords = self.mouse_to_coords(x, y)
        if target_coords:
            if target_coords != sprite.coords:
                valid_move_coords = self.valid_move_coords(sprite)
                if target_coords in valid_move_coords:
                    sprite.move(self.coords_to_rect(target_coords))
                    sprite.coords = target_coords
                    return True
        return False
