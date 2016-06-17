import constants.display as DC
import engine.controller.mainViewController as mainViewController
import globals.gameUtils as GGU
import globals.view as GV
import pygame
import random

def initializeFont ():
    GGU.fontName = pygame.font.get_default_font ()
    GGU.font = pygame.font.Font (GGU.fontName, DC.FONT_SIZE)

def initializeViews ():
    GV.screen = pygame.display.set_mode (DC.RESOLUTION, pygame.FULLSCREEN | pygame.HWSURFACE)
    mainViewController.initialize ()

def initialize ():
    random.seed ()
    pygame.init ()
    GGU.clock = pygame.time.Clock ()
    initializeFont ()
    initializeViews ()
