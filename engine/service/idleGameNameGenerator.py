import constants.idleGameNames as CIGN
import constants.display as CD
import engine.util.draw as draw
import globals.gameUtils as GGU
import pygame
import random

def buildSingleTextLine (text, textColor, backgroundColor):
    fontSize = CD.CLICK_VIEW_FONT_SIZE
    font = pygame.font.Font (GGU.fontName, fontSize)
    while (font.size (text)[0] > CD.CLICK_VIEW_SIZE[0]) & (fontSize > 0):
        fontSize -= 1
        font = pygame.font.Font (GGU.fontName, fontSize)
    return font.render (text, True, textColor, backgroundColor)

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
    renderedPrefix = buildSingleTextLine (random.choice (CIGN.PREFIXES), textColor, backgroundColor)
    renderedName = buildSingleTextLine (random.choice (CIGN.NAMES), textColor, backgroundColor)
    renderedSuffix = buildSingleTextLine (random.choice (CIGN.SUFFIXES), textColor, backgroundColor)
    mode = random.randint (0, 1)
    if mode == 0:
        return combineRenderedLines ([renderedPrefix, renderedName], backgroundColor)
    else:
        return combineRenderedLines ([renderedPrefix, renderedName, renderedSuffix], backgroundColor)
