import constants.color as color
import constants.display as DC
import engine.util.draw as draw
import globals.gameState as GS
import globals.view as view
import pygame

def drawHeadings ():
    episodeHeading = GS.font.render ('Folgen:', True, color.WHITE)
    draw.drawXCentered (episodeHeading, view.moneyView, 2)

def initialize ():
    view.moneyView = view.mainView.subsurface ((0, DC.CLICKVIEWSIZE [1] - 1, DC.MONEYVIEWSIZE [0], DC.MONEYVIEWSIZE [1]))
    pygame.draw.rect (view.moneyView, color.DARKGREEN, (0, 0, DC.MONEYVIEWSIZE [0] - 1, DC.MONEYVIEWSIZE [1] - 1), 2)
    drawHeadings ()

def update ():
    pass
