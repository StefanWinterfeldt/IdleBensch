import constants.color as CC
import globals.gameState as GS
import globals.gameUtils as GU
import globals.view as GV
import pygame


INTRO_TICKS = 200

ticks = 0

def fadeInCredits ():
    percentage = 1 - (ticks / float (INTRO_TICKS))
    overlay = pygame.Surface (GV.screen.get_size (), pygame.HWSURFACE)
    overlay.fill (CC.BLACK)
    overlay.set_alpha (int (255 * percentage))
    GV.screen.blit (GU.introImage, (0, 0))
    GV.screen.blit (overlay, (0, 0))

def update ():
    global ticks
    fadeInCredits ()
    ticks += 1
    if ticks > INTRO_TICKS:
        GS.context = 'menu'
