import constants.display as DC
import engine.view.mainView as mainView
import globals.gameState as gameState
import globals.view as view
import pygame
import random

def initializeFont ():
    gameState.fontName = pygame.font.get_default_font ()
    gameState.font = pygame.font.Font (gameState.fontName, DC.FONTSIZE)

def initializeViews ():
    view.screen = pygame.display.set_mode (DC.RESOLUTION, pygame.FULLSCREEN | pygame.HWSURFACE)
    mainView.initialize ()

def initialize ():
    random.seed ()
    pygame.init ()
    gameState.clock = pygame.time.Clock ()
    initializeFont ()
    initializeViews ()
