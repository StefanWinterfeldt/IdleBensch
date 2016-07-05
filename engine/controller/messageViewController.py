import constants.color as CC
import constants.display as CD
import globals.view as GV
import pygame

def initialize ():
    GV.messageViewAbsoluteRect = pygame.Rect ((0 + CD.CLICK_VIEW_SIZE [0], 0, CD.MESSAGE_VIEW_SIZE [0], CD.MESSAGE_VIEW_SIZE [1]))
    GV.messageView = GV.gameView.subsurface (GV.messageViewAbsoluteRect)
    pygame.draw.rect (GV.messageView, CC.DARK_GREEN, (0, 0, CD.MESSAGE_VIEW_SIZE [0] - 1, CD.MESSAGE_VIEW_SIZE [1] - 1), 2)

def update ():
    pass