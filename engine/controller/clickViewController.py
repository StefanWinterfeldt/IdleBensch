import constants.color as color
import constants.display as DC
import engine.service.idleGameNameGenerator as IGNG
import engine.util.color as colorUtil
import engine.util.draw as draw
import globals.gameState as GS
import globals.view as view
import math
import pygame
import random


completionCircleFullRadius = None
completionCirclePos = None

def drawCompletionCircle ():
    pygame.draw.circle (view.clickView, color.BLACK, completionCirclePos, completionCircleFullRadius)
    currentRadius = int ((completionCircleFullRadius / 100.0) * GS.episodeCompletionPercentage)
    pygame.draw.circle (view.clickView, color.DARKGREEN, completionCirclePos, currentRadius)

def handleClick (position):
    randomize ()
    GS.episodeCompletionPercentage += 5
    if GS.episodeCompletionPercentage > 100: GS.episodeCompletionPercentage = 0

def initialize ():
    global completionCirclePos
    global completionCircleFullRadius
    view.clickView = view.mainView.subsurface ((0, 0, DC.CLICKVIEWSIZE [0], DC.CLICKVIEWSIZE [1]))
    completionCirclePos = (DC.CLICKVIEWSIZE [0] / 2, DC.CLICKVIEWSIZE [1] / 5)
    completionCircleFullRadius = DC.CLICKVIEWSIZE [0] / 8
    randomize ()

def randomize ():
    backgroundColor = random.choice (color.CLICKVIEWCOLORS)
    view.clickView.fill (backgroundColor)
    draw.drawCentered (IGNG.generateIdleGameName (colorUtil.invertColor (backgroundColor), backgroundColor), view.clickView)
    pygame.draw.rect (view.clickView, color.DARKGREEN, (0, 0, DC.CLICKVIEWSIZE [0] - 1, DC.CLICKVIEWSIZE [1] - 1), 2)

def update ():
    drawCompletionCircle ()
