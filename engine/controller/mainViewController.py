import constants.display as DC
import engine.controller.chatViewController as chatViewController
import engine.controller.clickViewController as clickViewController
import engine.controller.faceViewController as faceViewController
import engine.controller.hintViewController as hintViewController
import engine.controller.messageViewController as messageViewController
import engine.controller.moneyViewController as moneyViewController
import globals.view as view
import pygame

def initialize ():
    view.mainView = pygame.Surface (DC.RESOLUTION, pygame.HWSURFACE)
    clickViewController.initialize ()
    moneyViewController.initialize ()
    hintViewController.initialize ()
    faceViewController.initialize ()
    chatViewController.initialize ()
    messageViewController.initialize ()

def update ():
    clickViewController.update ()
    moneyViewController.update ()
    hintViewController.update ()
    faceViewController.update ()
    chatViewController.update ()
    messageViewController.update ()
    view.screen.blit (view.mainView, (0, 0))
