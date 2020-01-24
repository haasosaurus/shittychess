# coding=utf-8


from typing import NoReturn

import pygame


class ShittyEventHandler:
    """manages all the pygame events for the game"""

    def __init__(self) -> NoReturn:
        self.screen = None  # pygame.Surface
        self.settings = None  # ShittySettings
        self.layout = None  # ShittyLayout
        self.logic = None  # ShittyLogic
        self.board = None  # ShittyBoard

        # initialize mouse press bools
        self.left_mouse_pressed = False
        self.middle_mouse_pressed = False
        self.right_mouse_pressed = False

        # save last frame's mouse position
        self.left_mouse_last_frame = False
        self.middle_mouse_last_frame = False
        self.right_mouse_last_frame = False

        # initialize mouse click bools
        self.left_mouse_click = False
        self.middle_mouse_click = False
        self.right_mouse_click = False

        # piece moving bools
        self.holding_piece = False
        self.holding_piece_sprite = None
        self.holding_piece_original_rect = None

    def process_events(self) -> bool:
        """process pygame events"""

        redraw_required = False

        # complete mouse clicks with no looping
        self.left_mouse_click = False
        self.middle_mouse_click = False
        self.right_mouse_click = False

        for event in pygame.event.get():

            if (
                    event.type == pygame.KEYDOWN
                    or event.type == pygame.KEYUP
                    or event.type == pygame.QUIT
                    or event.type == pygame.MOUSEBUTTONDOWN
                    or event.type == pygame.MOUSEBUTTONUP
            ):
                # set flag to update the screen
                redraw_required = True

            if event.type == pygame.KEYDOWN:

                # exit game
                if event.key == pygame.K_q:
                    self.settings.exiting = True

                # toggle headers enabled
                if event.key == pygame.K_h:
                    self.settings.headers_enabled = not self.settings.headers_enabled
                    self.screen = pygame.display.set_mode((self.settings.screen_width(), self.settings.screen_height()))
                    self.board.resize()
                    self.layout.resize()

                # toggle player turn
                if event.key == pygame.K_t:
                    self.settings.turn_black = not self.settings.turn_black

            # exit game
            elif event.type == pygame.QUIT:
                self.settings.exiting = True

            # press mouse buttons
            elif event.type == pygame.MOUSEBUTTONDOWN:

                # left mouse button
                if event.button == 1:
                    self.left_mouse_pressed = True
                    if not self.left_mouse_last_frame:
                        self.left_mouse_click = True

                    # piece movement - picking up
                    if not self.holding_piece:
                        self.board.sprite_to_highlight = None
                        x, y = pygame.mouse.get_pos()
                        sprite = self.logic.mouse_to_sprite(x, y, black=self.settings.turn_black)
                        if sprite:
                            pygame.mouse.get_rel()
                            self.board.sprite_to_highlight = sprite
                            self.holding_piece_original_rect = pygame.Rect.copy(sprite.rect)
                            self.holding_piece_sprite = sprite
                            sprite.move_to_front()
                            self.holding_piece = True


                # middle mouse button
                elif event.button == 2:
                    self.middle_mouse_pressed = True
                    if not self.middle_mouse_last_frame:
                        self.middle_mouse_click = True

                    # highlight available moves
                    if not self.holding_piece:
                        x, y = pygame.mouse.get_pos()
                        sprite = self.logic.mouse_to_sprite(x, y, black=self.settings.turn_black)

                        # clicked the sprite you're already highlighting
                        if sprite == self.board.sprite_to_highlight:

                            # disable highlighting
                            self.board.sprite_to_highlight = None

                        # clicked somewhere else
                        else:

                            # highlight clicked sprite, or none if you didn't click on any
                            self.board.sprite_to_highlight = sprite

                # right mouse button
                elif event.button == 3:
                    self.right_mouse_pressed = True
                    if not self.right_mouse_last_frame:
                        self.right_mouse_click = True

            # release mouse buttons
            elif event.type == pygame.MOUSEBUTTONUP:

                # left mouse button
                if event.button == 1:
                    self.left_mouse_pressed = False

                    # piece movement - dropping
                    if self.holding_piece:
                        x, y = pygame.mouse.get_pos()
                        if not self.logic.move_piece_with_mouse(self.holding_piece_sprite, x, y):
                            self.holding_piece_sprite.rect = self.holding_piece_original_rect
                        self.board.sprite_to_highlight = None
                        self.holding_piece = False
                        self.holding_piece_sprite = None
                        self.holding_piece_original_rect = None

                # middle mouse button
                elif event.button == 2:
                    self.middle_mouse_pressed = False

                # right mouse button
                elif event.button == 3:
                    self.right_mouse_pressed = False

            # mouse motion
            elif event.type == pygame.MOUSEMOTION:

                # piece movement - motion
                if self.holding_piece:
                    x, y = pygame.mouse.get_rel()
                    tmp_rect = pygame.Rect.copy(self.holding_piece_sprite.rect)
                    tmp_rect.left += x
                    tmp_rect.top += y
                    if tmp_rect != self.holding_piece_sprite.rect:
                        self.holding_piece_sprite.set_rect(tmp_rect)
                        redraw_required = True

        # set mouse button last frame to current one
        self.left_mouse_last_frame = self.left_mouse_pressed
        self.middle_mouse_last_frame = self.middle_mouse_pressed
        self.right_mouse_last_frame = self.right_mouse_pressed

        return redraw_required
