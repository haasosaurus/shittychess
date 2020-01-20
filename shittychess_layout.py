# coding=utf-8


import itertools

import pygame

from shittychess_pieces import ShittyPiece
from shittychess_pieces import ShittyPawn
from shittychess_pieces import ShittyKnight
from shittychess_pieces import ShittyBishop
from shittychess_pieces import ShittyRook
from shittychess_pieces import ShittyQueen
from shittychess_pieces import ShittyKing


class ShittyGroup(pygame.sprite.Group):
    """
    subclassing sprite Group to add more functionality
    """

    def __init__(self):
        pygame.sprite.Group.__init__(self)

    def sprite_exists(self, coords: str) -> bool:
        for sprite in self.sprites():
            if sprite.coords == coords:
                return True
        return False

    def coords_to_sprite(self, coords: str) -> ShittyPiece:
        for sprite in self.sprites():
            if sprite.coords == coords:
                return sprite
        return ShittyPiece(None, True, pygame.Rect(0, 0, 0, 0), '')


class ShittyLayout:
    """
    this class manages where all the pieces are on the board
    might want to use this as a property of ShittyBoard
    """

    def __init__(self) -> None:
        self.screen = None  # pygame.Surface
        self.settings = None  # ShittySettings
        self.logic = None  # ShittyLogic

        self.sprite_group_black = ShittyGroup()
        self.sprite_group_white = ShittyGroup()
        self.sprite_group_all = ShittyGroup()

        self.initial_piece_layout = [
            ['a8', ShittyRook, True], ['b8', ShittyKnight, True], ['c8', ShittyBishop, True], ['d8', ShittyQueen, True],
            ['e8', ShittyKing, True], ['f8', ShittyBishop, True], ['g8', ShittyKnight, True], ['h8', ShittyRook, True],
            ['a7', ShittyPawn, True], ['b7', ShittyPawn, True], ['c7', ShittyPawn, True], ['d7', ShittyPawn, True],
            ['e7', ShittyPawn, True], ['f7', ShittyPawn, True], ['g7', ShittyPawn, True], ['h7', ShittyPawn, True],
            ['a2', ShittyPawn, False], ['b2', ShittyPawn, False], ['c2', ShittyPawn, False], ['d2', ShittyPawn, False],
            ['e2', ShittyPawn, False], ['f2', ShittyPawn, False], ['g2', ShittyPawn, False], ['h2', ShittyPawn, False],
            ['a1', ShittyRook, False], ['b1', ShittyKnight, False], ['c1', ShittyBishop, False], ['d1', ShittyQueen, False],
            ['e1', ShittyKing, False], ['f1', ShittyBishop, False], ['g1', ShittyKnight, False], ['h1', ShittyRook, False],
        ]

    def configure(self) -> None:
        """
        configure layout's properties after they have been assigned externally
        """

        self.reset()

    def coords_to_sprite(self, coords: str) -> ShittyPiece:
        # return self.sprite_group_all.coords_to_sprite(coords)
        tmp_sprite = self.sprite_group_all.coords_to_sprite(coords)
        if tmp_sprite:
            return tmp_sprite

    def sprite_exists_all(self, coords: str) -> bool:
        return self.sprite_group_all.sprite_exists(coords)

    def sprite_exists_black(self, coords: str) -> bool:
        return self.sprite_group_black.sprite_exists(coords)

    def sprite_exists_white(self, coords: str) -> bool:
        return self.sprite_group_white.sprite_exists(coords)

    def reset(self) -> None:
        """
        reset the board to a new game state
        """

        self.clear()
        for piece in self.initial_piece_layout:
            if piece[2]:
                self.sprite_group_black.add(piece[1](self.screen, piece[2], self.logic.coords_to_rect(piece[0]), piece[0]))
            else:
                self.sprite_group_white.add(piece[1](self.screen, piece[2], self.logic.coords_to_rect(piece[0]), piece[0]))
        for sprite in itertools.chain(self.sprite_group_black, self.sprite_group_white):
            self.sprite_group_all.add(sprite)

    def draw(self) -> None:
        """
        draw all the pieces
        """

        self.sprite_group_all.draw(self.screen)

    def clear(self) -> None:
        """
        remove all the pieces from the sprite group containers
        this will clear the board of all pieces
        """

        self.sprite_group_black.empty()
        self.sprite_group_white.empty()
        self.sprite_group_all.empty()

    def resize(self) -> None:
        """
        reposition all the pieces to their current correct position
        this should be used if the board size is changed, or headers
        are disabled or enabled, as that will change the board size
        """

        for sprite in self.sprite_group_all:
            tmp_rect = self.logic.coords_to_rect(sprite.coords)
            sprite.move(tmp_rect.left, tmp_rect.top)
