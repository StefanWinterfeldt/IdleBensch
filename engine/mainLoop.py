import constants.display as DC
import engine.keyHandler as keyHandler
import globals.gameState as gameState
import pygame
import sys


def loop ():
    while True:
        gameState.clock.tick (DC.FRAMERATE)

        for event in pygame.event.get ():
            if event.type == pygame.QUIT: sys.exit ()
            if event.type == pygame.KEYDOWN: keyHandler.handleKeyEvent (event)

        pygame.display.flip ()
