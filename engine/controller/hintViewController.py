import constants.color as CC
import constants.display as CD
import engine.util.text as textUtil
import globals.view as GV
import pygame

def clearText ():
    GV.hintView.fill (CC.BLACK)
    pygame.draw.rect (GV.hintView, CC.DARK_GREEN, (0, 0, CD.HINT_VIEW_SIZE [0] - 1, CD.HINT_VIEW_SIZE [1] - 1), 2)

def initialize ():
    GV.hintView = GV.mainView.subsurface ((0, CD.CLICK_VIEW_SIZE [1] + CD.MONEY_VIEW_SIZE [1] - 1, CD.HINT_VIEW_SIZE [0], CD.HINT_VIEW_SIZE [1]))
    pygame.draw.rect (GV.hintView, CC.DARK_GREEN, (0, 0, CD.HINT_VIEW_SIZE [0] - 1, CD.HINT_VIEW_SIZE [1] - 1), 2)

def showText (text):
    GV.hintView.fill (CC.BLACK)
    GV.hintView.blit (textUtil.renderTextWithWordWrap (text, CD.HINT_VIEW_SIZE [0] - 10), (5, 5))
    pygame.draw.rect (GV.hintView, CC.DARK_GREEN, (0, 0, CD.HINT_VIEW_SIZE [0] - 1, CD.HINT_VIEW_SIZE [1] - 1), 2)

def update ():
    pass
