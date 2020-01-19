#!/usr/bin/env python
# coding=utf-8


import pygame


class ShittyPiece(pygame.sprite.Sprite):

    def __init__(self, screen: pygame.Surface, black: bool, rect: pygame.Rect, coords: str):
        pygame.sprite.Sprite.__init__(self)
        self.black = black
        self.screen = screen
        self.rect = rect
        self.coords = coords
        self.image = None


    def move(self, x: int, y: int):
        self.rect.left = x
        self.rect.top = y


    def set_size(self, width: int, height: int):
        self.rect.width = width
        self.rect.height = height


    def update(self):
        pass


    def draw(self):
        self.screen.blit(self.image, self.rect)


class ShittyPawn(ShittyPiece):

    def __init__(self, screen: pygame.Surface, black: bool, rect: pygame.Rect, coords: str):
        super().__init__(screen, black, rect, coords)
        img_path = ''
        if self.black:
            img_path = 'shitty_art/shittypawnblack.png'
        else:
            img_path = 'shitty_art/shittypawnwhite.png'
        self.image = pygame.image.load(img_path)
        self.initial_position = True


class ShittyRook(ShittyPiece):

    def __init__(self, screen: pygame.Surface, black: bool, rect: pygame.Rect, coords: str):
        super().__init__(screen, black, rect, coords)
        if self.black:
            img_path = 'shitty_art/shittyrookblack.png'
        else:
            img_path = 'shitty_art/shittyrookwhite.png'
        self.image = pygame.image.load(img_path)
        self.initial_position = True


class ShittyBishop(ShittyPiece):

    def __init__(self, screen: pygame.Surface, black: bool, rect: pygame.Rect, coords: str):
        super().__init__(screen, black, rect, coords)
        if self.black:
            img_path = 'shitty_art/shittybishopblack.png'
        else:
            img_path = 'shitty_art/shittybishopwhite.png'
        self.image = pygame.image.load(img_path)


class ShittyKnight(ShittyPiece):

    def __init__(self, screen: pygame.Surface, black: bool, rect: pygame.Rect, coords: str):
        super().__init__(screen, black, rect, coords)
        if self.black:
            img_path = 'shitty_art/shittyknightblack.png'
        else:
            img_path = 'shitty_art/shittyknightwhite.png'
        self.image = pygame.image.load(img_path)


class ShittyQueen(ShittyPiece):

    def __init__(self, screen: pygame.Surface, black: bool, rect: pygame.Rect, coords: str):
        super().__init__(screen, black, rect, coords)
        if self.black:
            img_path = 'shitty_art/shittyqueenblack.png'
        else:
            img_path = 'shitty_art/shittyqueenwhite.png'
        self.image = pygame.image.load(img_path)


class ShittyKing(ShittyPiece):

    def __init__(self, screen: pygame.Surface, black: bool, rect: pygame.Rect, coords: str):
        super().__init__(screen, black, rect, coords)
        if self.black:
            img_path = 'shitty_art/shittykingblack.png'
        else:
            img_path = 'shitty_art/shittykingwhite.png'
        self.image = pygame.image.load(img_path)
        self.initial_position = True
