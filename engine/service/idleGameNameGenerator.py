import constants.color as color
import constants.idleGameNames as IGN
import engine.util.draw as draw
import globals.gameState as gameState
import pygame
import random

def buildSingleTextLine (text):
    return gameState.font.render (text, True, color.WHITE)

def combineRenderedLines (lines):
    combinedHeight = sum ([l.get_height () for l in lines])
    combinedWidth = max ([l.get_width () for l in lines])
    combinedLines = pygame.Surface ((combinedWidth, combinedHeight), pygame.HWSURFACE)
    yOffset = 0
    for l in lines:
        draw.drawXCentered (l, combinedLines, yOffset)
        yOffset += l.get_height ()
    return combinedLines

def generateIdleGameName ():
    renderedPrefix = buildSingleTextLine (random.choice (IGN.PREFIXES))
    renderedName = buildSingleTextLine (random.choice (IGN.NAMES))
    renderedSuffix = buildSingleTextLine (random.choice (IGN.SUFFIXES))
    return combineRenderedLines ([renderedPrefix, renderedName, renderedSuffix])
