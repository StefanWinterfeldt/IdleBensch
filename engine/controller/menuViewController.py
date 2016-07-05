import constants.display as CD
import globals.view as GV
import pygame

def initialize ():
    GV.menuView = pygame.Surface (CD.RESOLUTION, pygame.HWSURFACE)

def update ():
    GV.screen.blit (GV.menuView, (0, 0))