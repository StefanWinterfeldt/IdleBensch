import constants.display as DC
import globals.gameState as gameState
import pygame


def initialize ():
    pygame.init ()
    gameState.clock = pygame.time.Clock ()
    screen = pygame.display.set_mode (DC.RESOLUTION, pygame.FULLSCREEN | pygame.HWSURFACE)
    screen.fill ((0, 0, 0))
    return screen
