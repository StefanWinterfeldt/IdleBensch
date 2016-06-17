import constants.color as color
import constants.display as DC
import constants.gameLogic as GL
import engine.service.idleGameNameGenerator as IGNG
import engine.util.color as colorUtil
import engine.util.draw as draw
import globals.gameState as GS
import globals.view as view
import pygame
import random


completionCircleFullRadius = None
completionCirclePos = None

def drawCompletionCircle ():
    pygame.draw.circle (view.clickView, color.BLACK, completionCirclePos, completionCircleFullRadius)
    currentRadius = int ((completionCircleFullRadius / 100.0) * GS.episodeCompletionPercentage)
    pygame.draw.circle (view.clickView, color.DARK_GREEN, completionCirclePos, currentRadius)

def handleClick (position):
    randomize ()
    GS.episodeCompletionPercentage += GL.BASE_EPISODE_PERCENTAGE_PER_CLICK
    if GS.episodeCompletionPercentage > 100:
        GS.episodeCompletionPercentage = 0
        GS.episodes += 1

def initialize ():
    global completionCirclePos
    global completionCircleFullRadius
    view.clickView = view.mainView.subsurface ((0, 0, DC.CLICK_VIEW_SIZE [0], DC.CLICK_VIEW_SIZE [1]))
    completionCirclePos = (DC.CLICK_VIEW_SIZE [0] / 2, DC.CLICK_VIEW_SIZE [1] / 5)
    completionCircleFullRadius = DC.CLICK_VIEW_SIZE [0] / 8
    randomize ()

def randomize ():
    backgroundColor = random.choice (color.CLICK_VIEW_COLORS)
    view.clickView.fill (backgroundColor)
    draw.drawCentered (IGNG.generateIdleGameName (colorUtil.invertColor (backgroundColor), backgroundColor), view.clickView)
    pygame.draw.rect (view.clickView, color.DARK_GREEN, (0, 0, DC.CLICK_VIEW_SIZE [0] - 1, DC.CLICK_VIEW_SIZE [1] - 1), 2)

def update ():
    drawCompletionCircle ()
