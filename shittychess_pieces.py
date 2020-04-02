# coding=utf-8


import itertools

import pygame

from shittychess_sprites import ShittyPawn
from shittychess_sprites import ShittyKnight
from shittychess_sprites import ShittyBishop
from shittychess_sprites import ShittyRook
from shittychess_sprites import ShittyQueen
from shittychess_sprites import ShittyKing


class ShittyPieces:
    """
    this class manages where all the pieces are on the board
    might want to use this as a property of ShittyBoard
    """

    def __init__(self) -> None:
        self.screen = None  # pygame.Surface
        self.settings = None  # ShittySettings
        self.logic = None  # ShittyLogic

        self.sprite_group_black = pygame.sprite.LayeredUpdates()
        self.sprite_group_white = pygame.sprite.LayeredUpdates()

        self.initial_piece_layout = []

    def configure(self) -> None:
        """
        configure properties after some of them have been
        assigned externally
        """

        self.reset()

    def reset(self) -> None:
        """reset the board to a new game state"""

        initial_piece_layout = [
            # black
            {'pos': 'a8', 'type': ShittyRook, 'color': 'black'},
            {'pos': 'b8', 'type': ShittyKnight, 'color': 'black'},
            {'pos': 'c8', 'type': ShittyBishop, 'color': 'black'},
            {'pos': 'd8', 'type': ShittyQueen, 'color': 'black'},
            {'pos': 'e8', 'type': ShittyKing, 'color': 'black'},
            {'pos': 'f8', 'type': ShittyBishop, 'color': 'black'},
            {'pos': 'g8', 'type': ShittyKnight, 'color': 'black'},
            {'pos': 'h8', 'type': ShittyRook, 'color': 'black'},
            {'pos': 'a7', 'type': ShittyPawn, 'color': 'black'},
            {'pos': 'b7', 'type': ShittyPawn, 'color': 'black'},
            {'pos': 'c7', 'type': ShittyPawn, 'color': 'black'},
            {'pos': 'd7', 'type': ShittyPawn, 'color': 'black'},
            {'pos': 'e7', 'type': ShittyPawn, 'color': 'black'},
            {'pos': 'f7', 'type': ShittyPawn, 'color': 'black'},
            {'pos': 'g7', 'type': ShittyPawn, 'color': 'black'},
            {'pos': 'h7', 'type': ShittyPawn, 'color': 'black'},

            # white,
            {'pos': 'a2', 'type': ShittyPawn, 'color': 'white'},
            {'pos': 'b2', 'type': ShittyPawn, 'color': 'white'},
            {'pos': 'c2', 'type': ShittyPawn, 'color': 'white'},
            {'pos': 'd2', 'type': ShittyPawn, 'color': 'white'},
            {'pos': 'e2', 'type': ShittyPawn, 'color': 'white'},
            {'pos': 'f2', 'type': ShittyPawn, 'color': 'white'},
            {'pos': 'g2', 'type': ShittyPawn, 'color': 'white'},
            {'pos': 'h2', 'type': ShittyPawn, 'color': 'white'},
            {'pos': 'a1', 'type': ShittyRook, 'color': 'white'},
            {'pos': 'b1', 'type': ShittyKnight, 'color': 'white'},
            {'pos': 'c1', 'type': ShittyBishop, 'color': 'white'},
            {'pos': 'd1', 'type': ShittyQueen, 'color': 'white'},
            {'pos': 'e1', 'type': ShittyKing, 'color': 'white'},
            {'pos': 'f1', 'type': ShittyBishop, 'color': 'white'},
            {'pos': 'g1', 'type': ShittyKnight, 'color': 'white'},
            {'pos': 'h1', 'type': ShittyRook, 'color': 'white'},
        ]

        self.clear()
        for piece in initial_piece_layout:
            coords = self.logic.chess_coords_to_coords[piece['pos']]
            if piece['color'] == 'black':
                self.sprite_group_black.add(
                    piece['type'](
                        piece['color'],
                        self.logic.coords_to_rect(coords),
                        coords,
                        self.settings.piece_path(
                            piece['type'].name,
                            piece['color']
                        )
                    )
                )
            else:
                self.sprite_group_white.add(
                    piece['type'](
                        piece['color'],
                        self.logic.coords_to_rect(coords),
                        coords,
                        self.settings.piece_path(
                            piece['type'].name,
                            piece['color']
                        )
                    )
                )

    def draw(self) -> None:
        """draw all the pieces"""

        # temporary, fix this soon
        if self.settings.turn_black:
            self.sprite_group_white.draw(self.screen)
            self.sprite_group_black.draw(self.screen)
        else:
            self.sprite_group_black.draw(self.screen)
            self.sprite_group_white.draw(self.screen)

    def clear(self) -> None:
        """
        remove all the pieces from the sprite group containers
        this will clear the board of all pieces
        """

        self.sprite_group_black.empty()
        self.sprite_group_white.empty()

    def resize(self) -> None:
        """
        reposition all the pieces to their current correct position
        this should be used if the board size is changed, or headers
        are disabled or enabled, as that will change the board size
        """

        for sprite in itertools.chain(
                self.sprite_group_black,
                self.sprite_group_white
        ):
            tmp_rect = self.logic.coords_to_rect(sprite.coords)
            sprite.set_rect(pygame.Rect(
                tmp_rect.left,
                tmp_rect.top,
                sprite.rect.width,
                sprite.rect.height
            ))
