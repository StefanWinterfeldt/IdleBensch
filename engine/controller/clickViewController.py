import constants.color as CC
import constants.display as CD
import constants.gameLogic as GL
import engine.controller.hintViewController as hintViewController
import engine.service.idleGameNameGenerator as idleGameNameGenerator
import engine.util.color as colorUtil
import engine.util.draw as draw
import globals.gameState as GGS
import globals.view as GV
import pygame
import random


areaCode = 'CV'
completionCircleFullRadius = None
completionCirclePos = None
hintText = 'Klicke hier um Folgen zu produzieren.'

def drawCompletionCircle ():
    pygame.draw.circle (GV.clickView, CC.BLACK, completionCirclePos, completionCircleFullRadius)
    currentRadius = int ((completionCircleFullRadius / 100.0) * GGS.episodeCompletionPercentage)
    pygame.draw.circle (GV.clickView, CC.DARK_GREEN, completionCirclePos, currentRadius)

def handleClick (position):
    randomize ()
    GGS.episodeCompletionPercentage += GL.BASE_EPISODE_PERCENTAGE_PER_CLICK
    if GGS.episodeCompletionPercentage > 100:
        GGS.episodeCompletionPercentage = 0
        GGS.episodes += 1

def handleMotion (position):
    if GGS.currentMouseArea != areaCode:
        GGS.currentMouseArea = areaCode
        hintViewController.showText (hintText)

def initialize ():
    global completionCirclePos
    global completionCircleFullRadius
    GV.clickViewAbsoluteRect = pygame.Rect ((0, 0, CD.CLICK_VIEW_SIZE [0], CD.CLICK_VIEW_SIZE [1]))
    GV.clickView = GV.mainView.subsurface (GV.clickViewAbsoluteRect)
    completionCirclePos = (CD.CLICK_VIEW_SIZE [0] / 2, CD.CLICK_VIEW_SIZE [1] / 5)
    completionCircleFullRadius = CD.CLICK_VIEW_SIZE [0] / 8
    randomize ()

def randomize ():
    backgroundColor = random.choice (CC.CLICK_VIEW_COLORS)
    GV.clickView.fill (backgroundColor)
    draw.drawCentered (idleGameNameGenerator.generateIdleGameName (colorUtil.invertColor (backgroundColor), backgroundColor), GV.clickView)
    pygame.draw.rect (GV.clickView, CC.DARK_GREEN, (0, 0, CD.CLICK_VIEW_SIZE [0] - 1, CD.CLICK_VIEW_SIZE [1] - 1), 2)

def update ():
    drawCompletionCircle ()
