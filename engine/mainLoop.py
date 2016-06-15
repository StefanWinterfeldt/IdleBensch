import engine.keyHandler as keyHandler
import pygame
import sys


def loop ():
    while True:
        for event in pygame.event.get ():
            if event.type == pygame.QUIT: sys.exit ()
            if event.type == pygame.KEYDOWN: keyHandler.handleKeyEvent (event)

        pygame.display.flip ()
