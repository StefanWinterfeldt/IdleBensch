import constants.color as CC
import constants.display as CD
import engine.util.draw as draw
import globals.gameState as GGS
import globals.gameUtils as GGU
import globals.view as GV
import pygame

def drawValues ():
    yPos = 5
    episodeHeading = GGU.font.render ('Folgen:', True, CC.WHITE)
    draw.drawXCentered (episodeHeading, GV.moneyView, yPos)
    yPos += episodeHeading.get_height () + 5
    episodeValue = GGU.font.render (str(GGS.episodes), True, CC.WHITE)
    draw.drawXCentered (episodeValue, GV.moneyView, yPos)

def initialize ():
    GV.moneyView = GV.mainView.subsurface ((0, CD.CLICK_VIEW_SIZE [1] - 1, CD.MONEY_VIEW_SIZE [0], CD.MONEY_VIEW_SIZE [1]))
    pygame.draw.rect (GV.moneyView, CC.DARK_GREEN, (0, 0, CD.MONEY_VIEW_SIZE [0] - 1, CD.MONEY_VIEW_SIZE [1] - 1), 2)

def update ():
    GV.moneyView.fill (CC.BLACK)
    drawValues ()
    pygame.draw.rect (GV.moneyView, CC.DARK_GREEN, (0, 0, CD.MONEY_VIEW_SIZE [0] - 1, CD.MONEY_VIEW_SIZE [1] - 1), 2)
