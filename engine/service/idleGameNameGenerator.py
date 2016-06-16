import constants.idleGameNames as IGN
import engine.util.draw as draw
import globals.gameState as gameState
import pygame
import random

def buildSingleTextLine (text, textColor, backgroundColor):
    return gameState.font.render (text, True, textColor, backgroundColor)

def combineRenderedLines (lines, backgroundColor):
    combinedHeight = sum ([l.get_height () for l in lines])
    combinedWidth = max ([l.get_width () for l in lines])
    combinedLines = pygame.Surface ((combinedWidth, combinedHeight), pygame.HWSURFACE)
    combinedLines.fill (backgroundColor)
    yOffset = 0
    for l in lines:
        draw.drawXCentered (l, combinedLines, yOffset)
        yOffset += l.get_height ()
    return combinedLines

def generateIdleGameName (textColor, backgroundColor):
    renderedPrefix = buildSingleTextLine (random.choice (IGN.PREFIXES), textColor, backgroundColor)
    renderedName = buildSingleTextLine (random.choice (IGN.NAMES), textColor, backgroundColor)
    renderedSuffix = buildSingleTextLine (random.choice (IGN.SUFFIXES), textColor, backgroundColor)
    return combineRenderedLines ([renderedPrefix, renderedName, renderedSuffix], backgroundColor)
