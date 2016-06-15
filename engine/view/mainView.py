import constants.color as color
import constants.display as DC
import globals.view as view
import pygame

def initialize ():
    view.mainView = pygame.Surface (DC.RESOLUTION, pygame.HWSURFACE)
    view.mainView.fill (color.RED)

def update ():
    view.screen.blit (view.mainView, (0, 0))
