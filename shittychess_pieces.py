#!/usr/bin/env python
# coding=utf-8


import pygame


class ShittyPiece(pygame.sprite.Sprite):

    def __init__(self, screen):
        self.image = None
        self.screen = screen
        self.rect = pygame.Rect(0, 0, 0, 0)


    def move(self, rect):
        self.rect = rect


    def draw(self):
        self.screen.blit(self.image, self.rect)


class ShittyPawn(ShittyPiece):

    def __init__(self, screen):
        super().__init__(screen)
        self.img_path_black = 'shitty_art/shittypawnblack.png'
        self.img_path_white = 'shitty_art/shittypawnwhite.png'
        self.image = pygame.image.load(self.img_path_black)
        self.rect = pygame.Rect(0, 0, 0, 0)


class ShittyRook(ShittyPiece):

    def __init__(self, screen):
        super().__init__(screen)
        self.img_path_black = 'shitty_art/shittyrookblack.png'
        self.img_path_white = 'shitty_art/shittyrookwhite.png'
        self.image = pygame.image.load(self.img_path_black)
        self.rect = pygame.Rect(0, 0, 0, 0)


class ShittyBishop(ShittyPiece):

    def __init__(self, screen):
        super().__init__(screen)
        self.img_path_black = 'shitty_art/shittybishopblack.png'
        self.img_path_white = 'shitty_art/shittybishopwhite.png'
        self.image = pygame.image.load(self.img_path_black)
        self.rect = pygame.Rect(0, 0, 0, 0)


class ShittyKnight(ShittyPiece):

    def __init__(self, screen):
        super().__init__(screen)
        self.img_path_black = 'shitty_art/shittyknightblack.png'
        self.img_path_white = 'shitty_art/shittyknightwhite.png'
        self.image = pygame.image.load(self.img_path_black)
        self.rect = pygame.Rect(0, 0, 0, 0)


class ShittyQueen(ShittyPiece):

    def __init__(self, screen):
        super().__init__(screen)
        self.img_path_black = 'shitty_art/shittyqueenblack.png'
        self.img_path_white = 'shitty_art/shittyqueenwhite.png'
        self.image = pygame.image.load(self.img_path_black)
        self.rect = pygame.Rect(0, 0, 0, 0)


class ShittyKing(ShittyPiece):

    def __init__(self, screen):
        super().__init__(screen)
        self.img_path_black = 'shitty_art/shittykingblack.png'
        self.img_path_white = 'shitty_art/shittykingwhite.png'
        self.image = pygame.image.load(self.img_path_black)
        self.rect = pygame.Rect(0, 0, 0, 0)
