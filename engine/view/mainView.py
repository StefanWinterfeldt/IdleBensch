import constants.display as DC
import engine.view.clickView as clickView
import globals.view as view
import pygame

def initialize ():
    view.mainView = pygame.Surface (DC.RESOLUTION, pygame.HWSURFACE)
    clickView.initialize ()

def update ():
    view.screen.blit (view.mainView, (0, 0))
    clickView.update ()
