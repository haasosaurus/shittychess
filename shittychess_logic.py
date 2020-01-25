# coding=utf-8

import itertools
from typing import List
from typing import Tuple
from typing import Union
from typing import NoReturn

import pygame

from shittychess_sprites import ShittyMousePointer
from shittychess_sprites import ShittyPiece


class ShittyLogic:
    """
    game 'logic' class
    the shittiest logic, getting less shitty by the hour
    """

    def __init__(self) -> NoReturn:
        self.settings = None  # ShittySettings
        self.board = None  # ShittyBoard
        self.layout = None  # ShittyLayout
        self.coords_to_chess_coords = {}  # Dict[Tuple[int, int], str]
        self.chess_coords_to_coords = {}  # Dict[str, Tuple[int, int]]

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

        for sprite in itertools.chain(
                self.layout.sprite_group_black.sprites(),
                self.layout.sprite_group_white.sprites()
        ):
            if sprite.coords == coords:
                return sprite
        return None

    def valid_move_coords(self, piece: ShittyPiece) -> List[Tuple[int, int]]:
        """
        make a list of valid moves for a piece that are on the game board,
        no other error checking performed. return them as a list of
        zero-indexed x, y board space coordinates
        """

        if piece.__class__.__name__ == 'ShittyKnight':
            return self.__knight_valid_move_coords(piece)

        valid_spaces = []

        for movement in piece.movements:
            if movement.horizontal > 0:
                max_right = min(piece.coords[0] + movement.horizontal + 1, self.settings.cols)
                max_left = max((piece.coords[0] - movement.horizontal - 1), -1)

                # check to the right
                for x in range(piece.coords[0] + 1, max_right):
                    sprite = self.coords_to_sprite((x, piece.coords[1]))
                    if sprite:

                        # blocked by a friendly
                        if piece.black == sprite.black:
                            break

                        # enemy there, can kill them but go no further
                        valid_spaces.append((x, piece.coords[1]))
                        break

                    # nobody's there, free to move there
                    valid_spaces.append((x, piece.coords[1]))

                # check to the left
                for x in range(piece.coords[0] - 1, max_left, -1):
                    sprite = self.coords_to_sprite((x, piece.coords[1]))
                    if sprite:

                        # blocked by a friendly
                        if piece.black == sprite.black:
                            break

                        # enemy there, can kill them but go no further
                        valid_spaces.append((x, piece.coords[1]))
                        break

                    # nobody's there, free to move there
                    valid_spaces.append((x, piece.coords[1]))

            if movement.vertical > 0:
                max_down = min(piece.coords[1] + movement.vertical + 1, self.settings.rows)
                max_up = max((piece.coords[1] - movement.vertical - 1), -1)

                # some pawn stuff
                if piece.__class__.__name__ == 'ShittyPawn':
                    if piece.black:
                        if self.settings.black_top:
                            max_up = piece.coords[1]
                        else:
                            max_down = piece.coords[1]
                    else:
                        if self.settings.black_top:
                            max_down = piece.coords[1]
                        else:
                            max_up = piece.coords[1]

                # check down
                for y in range(piece.coords[1] + 1, max_down):
                    sprite = self.coords_to_sprite((piece.coords[0], y))
                    if sprite:

                        # blocked by a friendly
                        if piece.black == sprite.black or piece.__class__.__name__ == 'ShittyPawn':
                            break

                        # enemy there, can kill them but go no further
                        valid_spaces.append((piece.coords[0], y))
                        break

                    # nobody's there, free to move there
                    valid_spaces.append((piece.coords[0], y))

                # check up
                for y in range(piece.coords[1] - 1, max_up, -1):
                    sprite = self.coords_to_sprite((piece.coords[0], y))
                    if sprite:

                        # blocked by a friendly
                        if piece.black == sprite.black or piece.__class__.__name__ == 'ShittyPawn':
                            break

                        # enemy there, can kill them but go no further
                        valid_spaces.append((piece.coords[0], y))
                        break

                    # nobody's there, free to move there
                    valid_spaces.append((piece.coords[0], y))

            if movement.diagonal > 0:
                max_right = min(piece.coords[0] + movement.diagonal + 1, self.settings.cols)
                max_left = max((piece.coords[0] - movement.diagonal - 1), -1)
                max_down = min(piece.coords[1] + movement.diagonal + 1, self.settings.rows)
                max_up = max((piece.coords[1] - movement.diagonal - 1), -1)

                # pawn stuff
                if piece.__class__.__name__ == 'ShittyPawn':

                    if piece.black:
                        if self.settings.black_top:
                            max_up = piece.coords[1]
                        else:
                            max_down = piece.coords[1]
                    else:
                        if self.settings.black_top:
                            max_down = piece.coords[1]
                        else:
                            max_up = piece.coords[1]

                # check right/down
                for x, y in zip(
                        range(piece.coords[0] + 1, max_right),
                        range(piece.coords[1] + 1, max_down)
                ):

                    sprite = self.coords_to_sprite((x, y))

                    # pawn stuff
                    if piece.__class__.__name__ == 'ShittyPawn':
                        if not sprite or sprite.black == piece.black:
                            break

                    if sprite:

                        # blocked by a friendly
                        if piece.black == sprite.black:
                            break

                        # enemy there, can kill them but go no further
                        valid_spaces.append((x, y))
                        break

                    # nobody's there, free to move there
                    valid_spaces.append((x, y))

                # check right/up
                for x, y in zip(
                        range(piece.coords[0] + 1, max_right),
                        range(piece.coords[1] - 1, max_up, -1)
                ):
                    sprite = self.coords_to_sprite((x, y))

                    # pawn stuff
                    if piece.__class__.__name__ == 'ShittyPawn':
                        if not sprite or sprite.black == piece.black:
                            break

                    if sprite:

                        # blocked by a friendly
                        if piece.black == sprite.black:
                            break

                        # enemy there, can kill them but go no further
                        valid_spaces.append((x, y))
                        break

                    # nobody's there, free to move there
                    valid_spaces.append((x, y))

                # check left/down
                for x, y in zip(
                        range(piece.coords[0] - 1, max_left, -1),
                        range(piece.coords[1] + 1, max_down)
                ):
                    sprite = self.coords_to_sprite((x, y))

                    # pawn stuff
                    if piece.__class__.__name__ == 'ShittyPawn':
                        if not sprite or sprite.black == piece.black:
                            break

                    if sprite:

                        # blocked by a friendly
                        if piece.black == sprite.black:
                            break

                        # enemy there, can kill them but go no further
                        valid_spaces.append((x, y))
                        break

                    # nobody's there, free to move there
                    valid_spaces.append((x, y))

                # check left/up
                for x, y in zip(
                        range(piece.coords[0] - 1, max_left, -1),
                        range(piece.coords[1] - 1, max_up, -1)
                ):
                    sprite = self.coords_to_sprite((x, y))

                    # pawn stuff
                    if piece.__class__.__name__ == 'ShittyPawn':
                        if not sprite or sprite.black == piece.black:
                            break

                    if sprite:

                        # blocked by a friendly
                        if piece.black == sprite.black:
                            break

                        # enemy there, can kill them but go no further
                        valid_spaces.append((x, y))
                        break

                    # nobody's there, free to move there
                    valid_spaces.append((x, y))

        return valid_spaces

    def __knight_valid_move_coords(self, piece: ShittyPiece) -> List[Tuple[int, int]]:
        """get knight specif valid spaces"""

        valid_spaces = []
        for movement in piece.movements:
            coords_list = list(itertools.product(*((x, -x) for x in (movement.horizontal, movement.vertical))))
            for x_movement, y_movement in coords_list:
                x = piece.coords[0] + x_movement
                y = piece.coords[1] + y_movement
                if 0 <= x < self.settings.cols and 0 <= y < self.settings.rows:
                    sprite = self.coords_to_sprite((x, y))
                    if sprite:

                        # blocked by a friendly
                        if piece.black == sprite.black:
                            continue

                    # either an open space or an enemy to kill
                    valid_spaces.append((x, y))

        return valid_spaces

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
                    pygame.sprite.spritecollide(
                        sprite,
                        self.layout.sprite_group_white if sprite.black else self.layout.sprite_group_black,
                        True
                    )
                    return True
        return False
