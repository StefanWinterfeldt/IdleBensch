import constants.display as DC
import engine.controller.gameViewController as gameViewController
import engine.controller.menuViewController as menuViewController
import globals.gameUtils as GGU
import globals.view as GV
import os
import pygame
import random

def initializeFont ():
    GGU.fontName = pygame.font.get_default_font ()
    GGU.font = pygame.font.Font (GGU.fontName, DC.FONT_SIZE)

def initializeUtilImages ():
    GGU.titleImage = pygame.image.load (os.path.join ('resources', 'ingame', 'title.png'))
    GGU.lockedSymbol = pygame.image.load (os.path.join ('resources', 'ingame', 'upgrade', 'lockedMask.png'))
    GGU.upgradeInactiveMask = pygame.image.load (os.path.join ('resources', 'ingame', 'upgrade', 'inactiveMask.png'))

def initializeViews ():
    GV.screen = pygame.display.set_mode (DC.RESOLUTION, pygame.FULLSCREEN | pygame.HWSURFACE)
    menuViewController.initialize ()
    gameViewController.initialize ()

def initialize ():
    random.seed ()
    pygame.init ()
    GGU.clock = pygame.time.Clock ()
    initializeUtilImages ()
    initializeFont ()
    initializeViews ()
