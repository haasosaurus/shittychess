#!/usr/bin/env python
# coding=utf-8


import sys
import pygame


class ShittyEventMonitor:

    def __init__(self):
        pass


    def process_events(self):
        # Look for mouse input
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    sys.exit()
