import constants.color as CC
import constants.display as CD
import constants.gameLogic as GL
import engine.controller.hintViewController as hintViewController
import engine.service.idleGameNameGenerator as idleGameNameGenerator
import engine.util.color as colorUtil
import engine.util.draw as draw
import globals.gameState as GGS
import globals.view as GV
import math
import pygame
import random


areaCode = 'CV'
circleFullRadius = None
episodeCirclePos = None
episodeCompletion = 0
hintText = 'Klicke hier um Folgen zu produzieren.'

def drawCompletionCircle ():
    pygame.draw.circle (GV.clickView, CC.BLACK, episodeCirclePos, circleFullRadius)
    currentRadius = int (circleFullRadius * episodeCompletion)
    pygame.draw.circle (GV.clickView, CC.DARK_GREEN, episodeCirclePos, currentRadius)

def getVariableHintText ():
    return "Momentan produzierst du " + str (GL.BASE_EPISODES_PER_CLICK) + " Folgen pro Klick."

def handleClick (event):
    global episodeCompletion
    randomize ()
    episodeCompletion += GL.BASE_EPISODES_PER_CLICK
    if episodeCompletion >= 1:
        episodesCompleted = int (math.floor (episodeCompletion))
        GGS.episodes += episodesCompleted
        episodeCompletion -= episodesCompleted

def handleMotion (event):
    if GGS.currentMouseArea != areaCode:
        GGS.currentMouseArea = areaCode
        hintViewController.showText (' '.join([hintText, getVariableHintText()]))

def initialize ():
    global episodeCirclePos
    global circleFullRadius
    GV.clickViewAbsoluteRect = pygame.Rect ((0, 0, CD.CLICK_VIEW_SIZE [0], CD.CLICK_VIEW_SIZE [1]))
    GV.clickView = GV.mainView.subsurface (GV.clickViewAbsoluteRect)
    episodeCirclePos = (CD.CLICK_VIEW_SIZE [0] / 4, CD.CLICK_VIEW_SIZE [1] / 5)
    circleFullRadius = CD.CLICK_VIEW_SIZE [0] / 8
    randomize ()

def randomize ():
    backgroundColor = random.choice (CC.CLICK_VIEW_COLORS)
    GV.clickView.fill (backgroundColor)
    draw.drawCentered (idleGameNameGenerator.generateIdleGameName (colorUtil.invertColor (backgroundColor), backgroundColor), GV.clickView)
    pygame.draw.rect (GV.clickView, CC.DARK_GREEN, (0, 0, CD.CLICK_VIEW_SIZE [0] - 1, CD.CLICK_VIEW_SIZE [1] - 1), 2)

def update ():
    drawCompletionCircle ()
