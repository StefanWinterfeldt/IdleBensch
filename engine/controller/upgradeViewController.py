import constants.color as CC
import constants.display as CD
import globals.view as GV
import pygame

def initialize ():
    GV.upgradeViewAbsoluteRect = pygame.Rect ((0 + CD.CLICK_VIEW_SIZE [0], CD.MESSAGE_VIEW_SIZE [1], CD.UPGRADE_VIEW_SIZE [0], CD.UPGRADE_VIEW_SIZE [1]))
    GV.upgradeView = GV.mainView.subsurface (GV.upgradeViewAbsoluteRect)
    pygame.draw.rect (GV.upgradeView, CC.DARK_GREEN, (0, 0, CD.UPGRADE_VIEW_SIZE [0] - 1, CD.UPGRADE_VIEW_SIZE [1] - 1), 2)

def update ():
    pass
