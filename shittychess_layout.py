#!/usr/bin/env python
# coding=utf-8


import itertools

import pygame

from shittychess_logic import ShittyLogic

from shittychess_pieces import ShittyPawn
from shittychess_pieces import ShittyKnight
from shittychess_pieces import ShittyBishop
from shittychess_pieces import ShittyRook
from shittychess_pieces import ShittyQueen
from shittychess_pieces import ShittyKing


# this class clearly needs to be unfucked
class ShittyLayout:

    def __init__(self, screen: pygame.Surface, logic: ShittyLogic):
        self.screen = screen
        self.logic = logic

        self.sprite_group_black = pygame.sprite.Group()
        self.sprite_group_white = pygame.sprite.Group()
        self.sprite_group_all = pygame.sprite.Group()

        self.default_black_pawn_coords = ['a7', 'b7', 'c7', 'd7', 'e7', 'f7', 'g7', 'h7']
        self.default_black_rook_coords = ['a8', 'h8']
        self.default_black_knight_coords = ['b8', 'g8']
        self.default_black_bishop_coords = ['c8', 'f8']
        self.default_black_queen_coords = 'd8'
        self.default_black_king_coords = 'e8'
        self.default_white_pawn_coords = ['a2', 'b2', 'c2', 'd2', 'e2', 'f2', 'g2', 'h2']
        self.default_white_rook_coords = ['a1', 'h1']
        self.default_white_knight_coords = ['b1', 'g1']
        self.default_white_bishop_coords = ['c1', 'f1']
        self.default_white_queen_coords = 'd1'
        self.default_white_king_coords = 'e1'
        self.reset()


    def draw(self):
        self.sprite_group_all.draw(self.screen)


    def clear(self):
        self.sprite_group_black.empty()
        self.sprite_group_white.empty()
        self.sprite_group_all.empty()


    def reset(self):
        self.clear()
        for crds in self.default_black_pawn_coords:
            self.sprite_group_black.add(ShittyPawn(self.screen, black=True, rect=self.logic.coords(crds), coords=crds))
        for crds in self.default_black_rook_coords:
            self.sprite_group_black.add(ShittyRook(self.screen, black=True, rect=self.logic.coords(crds), coords=crds))
        for crds in self.default_black_knight_coords:
            self.sprite_group_black.add(ShittyKnight(self.screen, black=True, rect=self.logic.coords(crds), coords=crds))
        for crds in self.default_black_bishop_coords:
            self.sprite_group_black.add(ShittyBishop(self.screen, black=True, rect=self.logic.coords(crds), coords=crds))
        self.sprite_group_black.add(ShittyQueen(self.screen, black=True, rect=self.logic.coords(self.default_black_queen_coords), coords=self.default_black_queen_coords))
        self.sprite_group_black.add(ShittyKing(self.screen, black=True, rect=self.logic.coords(self.default_black_king_coords), coords=self.default_black_king_coords))

        for crds in self.default_white_pawn_coords:
            self.sprite_group_white.add(ShittyPawn(self.screen, black=False, rect=self.logic.coords(crds), coords=crds))
        for crds in self.default_white_rook_coords:
            self.sprite_group_white.add(ShittyRook(self.screen, black=False, rect=self.logic.coords(crds), coords=crds))
        for crds in self.default_white_knight_coords:
            self.sprite_group_white.add(ShittyKnight(self.screen, black=False, rect=self.logic.coords(crds), coords=crds))
        for crds in self.default_white_bishop_coords:
            self.sprite_group_white.add(ShittyBishop(self.screen, black=False, rect=self.logic.coords(crds), coords=crds))
        self.sprite_group_white.add(ShittyQueen(self.screen, black=False, rect=self.logic.coords(self.default_white_queen_coords), coords=self.default_white_queen_coords))
        self.sprite_group_white.add(ShittyKing(self.screen, black=False, rect=self.logic.coords(self.default_white_king_coords), coords=self.default_white_king_coords))

        for sprite in itertools.chain(self.sprite_group_black, self.sprite_group_white):
            self.sprite_group_all.add(sprite)


    def resize(self):
        for sprite in self.sprite_group_all:
            tmp_rect = self.logic.coords(sprite.coords)
            sprite.move(tmp_rect.left, tmp_rect.top)
