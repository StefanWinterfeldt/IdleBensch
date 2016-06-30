import constants.color as CC
import constants.display as CD
import engine.controller.hintViewController as hintViewController
import engine.service.idleGameNameGenerator as idleGameNameGenerator
import engine.service.modifiedGameLogic as modifiedGameLogic
import engine.util.color as colorUtil
import engine.util.draw as draw
import engine.util.text as textUtil
import globals.gameLogic as GL
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
seasonCirclePos = None
seasonCompletion = 0

def checkAndHandleEpisodeCompletion ():
    global episodeCompletion
    global seasonCompletion
    if episodeCompletion >= 1:
        episodesCompleted = int (math.floor (episodeCompletion))
        GGS.episodes += episodesCompleted
        episodeCompletion -= episodesCompleted
        seasonCompletion += (episodesCompleted / float (modifiedGameLogic.getEpisodesPerSeason ()))

def checkAndHandleSeasonCompletion ():
    global seasonCompletion
    if seasonCompletion >= 1:
        seasonsCompleted = int (math.floor (seasonCompletion))
        GGS.seasons += seasonsCompleted
        seasonCompletion -= seasonsCompleted
        randomize ()

def drawCompletionCircles ():
    pygame.draw.circle (GV.clickView, CC.BLACK, episodeCirclePos, circleFullRadius)
    currentRadius = int (circleFullRadius * episodeCompletion)
    pygame.draw.circle (GV.clickView, CC.DARK_GREEN, episodeCirclePos, currentRadius)
    pygame.draw.circle (GV.clickView, CC.BLACK, seasonCirclePos, circleFullRadius)
    currentRadius = int (circleFullRadius * seasonCompletion)
    pygame.draw.circle (GV.clickView, CC.DARK_GREEN, seasonCirclePos, currentRadius)

def getVariableHintText ():
    text = "Momentan produzierst du " + textUtil.convertToHumanReadableString (modifiedGameLogic.getEpisodesPerClick (), True) + " Folgen pro Klick."
    if modifiedGameLogic.getClicksPerSecond () >= 0.00001: text += "Und du klickst " + textUtil.convertToHumanReadableString (modifiedGameLogic.getClicksPerSecond (), True) + " mal pro Sekunde automatisch."
    return text

def handleClick (event):
    global episodeCompletion
    episodeCompletion += modifiedGameLogic.getEpisodesPerClick ()
    checkAndHandleEpisodeCompletion ()
    checkAndHandleSeasonCompletion ()

def handleMotion (event):
    if GGS.currentMouseArea != areaCode:
        GGS.currentMouseArea = areaCode
        hintViewController.showText (' '.join ([hintText, getVariableHintText ()]))

def initialize ():
    global circleFullRadius
    global episodeCirclePos
    global seasonCirclePos
    GV.clickViewAbsoluteRect = pygame.Rect ((0, 0, CD.CLICK_VIEW_SIZE [0], CD.CLICK_VIEW_SIZE [1]))
    GV.clickView = GV.mainView.subsurface (GV.clickViewAbsoluteRect)
    episodeCirclePos = (CD.CLICK_VIEW_SIZE [0] / 4, CD.CLICK_VIEW_SIZE [1] / 5)
    seasonCirclePos = ((CD.CLICK_VIEW_SIZE [0] / 4) * 3, CD.CLICK_VIEW_SIZE [1] / 5)
    circleFullRadius = CD.CLICK_VIEW_SIZE [0] / 8
    randomize ()

def randomize ():
    backgroundColor = random.choice (CC.CLICK_VIEW_COLORS)
    GV.clickView.fill (backgroundColor)
    draw.drawCentered (idleGameNameGenerator.generateIdleGameName (colorUtil.invertColor (backgroundColor), backgroundColor), GV.clickView)
    pygame.draw.rect (GV.clickView, CC.DARK_GREEN, (0, 0, CD.CLICK_VIEW_SIZE [0] - 1, CD.CLICK_VIEW_SIZE [1] - 1), 2)

def update ():
    drawCompletionCircles ()
