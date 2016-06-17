import constants.color as CC
import constants.display as CD
import engine.util.draw as drawUtil
import engine.util.text as textUtil
import globals.gameState as GGS
import globals.gameUtils as GGU
import globals.view as GV
import pygame


activeSections = []
episodeSection = None
episodeSectionAbsoluteRect = None
sectionSize = (360, 72)

def drawEpisodeSection ():
    drawUtil.drawCentered (textUtil.renderLines (['Folgen:', str (GGS.episodes)], True), episodeSection)
    pygame.draw.rect (episodeSection, CC.DARK_GREEN, episodeSection.get_rect (), 1)

def drawSections ():
    if episodeSection in activeSections:
        drawEpisodeSection ()

def initialize ():
    GV.moneyViewAbsoluteRect = pygame.Rect ((0, CD.CLICK_VIEW_SIZE [1] - 1, CD.MONEY_VIEW_SIZE [0], CD.MONEY_VIEW_SIZE [1]))
    GV.moneyView = GV.mainView.subsurface (GV.moneyViewAbsoluteRect)
    initializeEpisodeSection ()
    pygame.draw.rect (GV.moneyView, CC.DARK_GREEN, (0, 0, CD.MONEY_VIEW_SIZE [0] - 1, CD.MONEY_VIEW_SIZE [1] - 1), 2)

def initializeEpisodeSection ():
    global activeSections
    global episodeSectionAbsoluteRect
    global episodeSection
    episodeSectionAbsoluteRect = pygame.Rect (GV.moneyViewAbsoluteRect [0], GV.moneyViewAbsoluteRect [1], sectionSize [0], sectionSize [1])
    episodeSection = GV.moneyView.subsurface ((0, 0, sectionSize [0], sectionSize [1]))
    activeSections.append (episodeSection)

def update ():
    GV.moneyView.fill (CC.BLACK)
    drawSections ()
    pygame.draw.rect (GV.moneyView, CC.DARK_GREEN, (0, 0, CD.MONEY_VIEW_SIZE [0] - 1, CD.MONEY_VIEW_SIZE [1] - 1), 2)
