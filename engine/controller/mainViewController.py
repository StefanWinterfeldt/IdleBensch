import constants.display as DC
import engine.controller.clickViewController as clickViewController
import globals.view as view
import pygame

def initialize ():
    view.mainView = pygame.Surface (DC.RESOLUTION, pygame.HWSURFACE)
    clickViewController.initialize ()

def update ():
    view.screen.blit (view.mainView, (0, 0))
    clickViewController.update ()
