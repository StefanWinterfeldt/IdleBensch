import constants.display as DC
import pygame


def initialize ():
    pygame.init ()
    screen = pygame.display.set_mode (DC.RESOLUTION, pygame.FULLSCREEN | pygame.HWSURFACE)
    screen.fill ((0, 0, 0))
    return screen
