import constants.display as DC
import engine.view.mainView as mainView
import globals.gameState as gameState
import globals.view as view
import pygame

def initializeViews ():
    view.screen = pygame.display.set_mode (DC.RESOLUTION, pygame.FULLSCREEN | pygame.HWSURFACE)
    mainView.initialize ()

def initialize ():
    pygame.init ()
    gameState.clock = pygame.time.Clock ()
    initializeViews ()
