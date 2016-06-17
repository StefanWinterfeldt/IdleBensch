import constants.display as DC
import engine.controller.clickViewController as clickViewController
import engine.controller.hintViewController as hintViewController
import engine.controller.moneyViewController as moneyViewController
import globals.view as view
import pygame

def initialize ():
    view.mainView = pygame.Surface (DC.RESOLUTION, pygame.HWSURFACE)
    clickViewController.initialize ()
    moneyViewController.initialize ()
    hintViewController.initialize ()

def update ():
    clickViewController.update ()
    moneyViewController.update ()
    hintViewController.update ()
    view.screen.blit (view.mainView, (0, 0))
