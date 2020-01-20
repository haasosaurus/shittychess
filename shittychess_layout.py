# coding=utf-8


import itertools

import pygame

from shittychess_logic import ShittyLogic
from shittychess_settings import ShittySettings

from shittychess_pieces import ShittyPawn
from shittychess_pieces import ShittyKnight
from shittychess_pieces import ShittyBishop
from shittychess_pieces import ShittyRook
from shittychess_pieces import ShittyQueen
from shittychess_pieces import ShittyKing


# this class clearly needs to be unfucked
class ShittyLayout:

    def __init__(self, screen: pygame.Surface, settings: ShittySettings, logic: ShittyLogic) -> None:
        self.screen = screen
        self.settings = settings
        self.logic = logic

        self.sprite_group_black = pygame.sprite.Group()
        self.sprite_group_white = pygame.sprite.Group()
        self.sprite_group_all = pygame.sprite.Group()

        self.initial_piece_layout = [
            ['a8', ShittyRook, True], ['b8', ShittyKnight, True], ['c8', ShittyBishop, True], ['d8', ShittyQueen, True],
            ['e8', ShittyKing, True], ['f8', ShittyBishop, True], ['g8', ShittyKnight, True], ['h8', ShittyRook, True],
            ['a7', ShittyPawn, True], ['b7', ShittyPawn, True], ['c7', ShittyPawn, True], ['d7', ShittyPawn, True],
            ['e7', ShittyPawn, True], ['f7', ShittyPawn, True], ['g7', ShittyPawn, True], ['h7', ShittyPawn, True],
            ['a2', ShittyRook, False], ['b2', ShittyKnight, False], ['c2', ShittyBishop, False], ['d2', ShittyQueen, False],
            ['e2', ShittyKing, False], ['f2', ShittyBishop, False], ['g2', ShittyKnight, False], ['h2', ShittyRook, False],
            ['a1', ShittyPawn, False], ['b1', ShittyPawn, False], ['c1', ShittyPawn, False], ['d1', ShittyPawn, False],
            ['e1', ShittyPawn, False], ['f1', ShittyPawn, False], ['g1', ShittyPawn, False], ['h1', ShittyPawn, False],
        ]

        self.reset()


    def reset(self) -> None:
        self.clear()
        for piece in self.initial_piece_layout:
            if piece[2]:
                self.sprite_group_black.add(piece[1](self.screen, piece[2], self.logic.coords(piece[0]), piece[0]))
            else:
                self.sprite_group_white.add(piece[1](self.screen, piece[2], self.logic.coords(piece[0]), piece[0]))
        for sprite in itertools.chain(self.sprite_group_black, self.sprite_group_white):
            self.sprite_group_all.add(sprite)

        if self.settings.debug:
            self.print_sprite_locations()


    def print_sprite_locations(self) -> None:
        print('black sprites:')
        for sprite in self.sprite_group_black.sprites():
            print(sprite.coords, end=' ')
        print('\nwhite sprites:')
        for sprite in self.sprite_group_white.sprites():
            print(sprite.coords, end=' ')
        print('\nall sprites:')
        for sprite in self.sprite_group_all.sprites():
            print(sprite.coords, end=' ')
        print()


    def draw(self) -> None:
        self.sprite_group_all.draw(self.screen)


    def clear(self) -> None:
        self.sprite_group_black.empty()
        self.sprite_group_white.empty()
        self.sprite_group_all.empty()


    def resize(self) -> None:
        for sprite in self.sprite_group_all:
            tmp_rect = self.logic.coords(sprite.coords)
            sprite.move(tmp_rect.left, tmp_rect.top)
