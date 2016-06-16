import constants.display as DC
import engine.controller.clickViewController as clickViewController
import engine.controller.moneyViewController as moneyViewController
import globals.view as view
import pygame

def initialize ():
    view.mainView = pygame.Surface (DC.RESOLUTION, pygame.HWSURFACE)
    clickViewController.initialize ()
    moneyViewController.initialize ()

def update ():
    clickViewController.update ()
    moneyViewController.update ()
    view.screen.blit (view.mainView, (0, 0))
