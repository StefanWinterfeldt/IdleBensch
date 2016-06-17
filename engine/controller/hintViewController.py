import constants.color as CC
import constants.display as CD
import globals.view as GV
import pygame

def initialize ():
    GV.hintView = GV.mainView.subsurface ((0, CD.CLICK_VIEW_SIZE [1] + CD.MONEY_VIEW_SIZE [1] - 1, CD.HINT_VIEW_SIZE [0], CD.HINT_VIEW_SIZE [1]))
    pygame.draw.rect (GV.hintView, CC.DARK_GREEN, (0, 0, CD.HINT_VIEW_SIZE [0] - 1, CD.HINT_VIEW_SIZE [1] - 1), 2)

def update ():
    pass