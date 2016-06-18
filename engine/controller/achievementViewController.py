import constants.color as CC
import constants.display as CD
import globals.view as GV
import pygame

def initialize ():
    GV.achievementViewAbsoluteRect = pygame.Rect ((0 + CD.CLICK_VIEW_SIZE [0], CD.MESSAGE_VIEW_SIZE [1] + CD.UPGRADE_VIEW_SIZE [1], CD.ACHIEVEMENT_VIEW_SIZE [0], CD.ACHIEVEMENT_VIEW_SIZE [1]))
    GV.achievementView = GV.mainView.subsurface (GV.achievementViewAbsoluteRect)
    pygame.draw.rect (GV.achievementView, CC.DARK_GREEN, (0, 0, CD.ACHIEVEMENT_VIEW_SIZE [0] - 1, CD.ACHIEVEMENT_VIEW_SIZE [1] - 1), 2)

def update ():
    pass
