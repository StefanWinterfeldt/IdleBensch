import constants.color as color
import constants.display as DC
import globals.gameState as gameState
import globals.view as view
import pygame


def initialize ():
    pygame.init ()
    gameState.clock = pygame.time.Clock ()
    view.screen = pygame.display.set_mode (DC.RESOLUTION, pygame.FULLSCREEN | pygame.HWSURFACE)
    view.screen.fill (color.BLACK)
