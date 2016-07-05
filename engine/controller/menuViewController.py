import constants.color as CC
import constants.display as CD
import engine.util.draw as drawUtil
import engine.util.text as textUtil
import globals.view as GV
import pygame


gameButton = None
quitButton = None
gameButtonRect = None
quitButtonRect = None

def calculateButtonRects ():
    global gameButtonRect
    global quitButtonRect
    width = GV.menuView.get_width () / 2
    height = ((GV.menuView.get_height () / 2) - 30) / 2
    gameButtonRect = pygame.Rect ((GV.menuView.get_width () / 2) - (width / 2), (GV.menuView.get_height () / 2) + 10, width, height)
    quitButtonRect = pygame.Rect ((GV.menuView.get_width () / 2) - (width / 2), (GV.menuView.get_height () / 2) + 20 + height, width, height)

def initialize ():
    global gameButton
    global quitButton
    GV.menuView = pygame.Surface (CD.RESOLUTION, pygame.HWSURFACE)
    calculateButtonRects ()
    gameButton = GV.menuView.subsurface (gameButtonRect)
    quitButton = GV.menuView.subsurface (quitButtonRect)

def drawButtons ():
    pygame.draw.rect (gameButton, CC.DARK_GREEN, (1, 1, gameButton.get_width () - 2, gameButton.get_height () - 2), 2)
    pygame.draw.rect (quitButton, CC.DARK_GREEN, (1, 1, quitButton.get_width () - 2, quitButton.get_height () - 2), 2)
    drawUtil.drawCentered (textUtil.renderLines (['Neues Spiel'], True, 72), gameButton)
    drawUtil.drawCentered (textUtil.renderLines (['Beenden'], True, 72), quitButton)

def update ():
    drawButtons ()
    GV.screen.blit (GV.menuView, (0, 0))
