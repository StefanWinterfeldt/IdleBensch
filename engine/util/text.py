import constants.color as CC
import constants.display as CD
import engine.util.draw as drawUtil
import globals.gameUtils as GGU
import math
import pygame
import types

def checkIfWordsWouldFit (words, maxWidth):
    line = ' '.join (words)
    return GGU.font.size (line) [0] < maxWidth

def convertToHumanReadableString (number, withFractions = False):
    numberString = str (int (math.floor (number)))
    if withFractions:
        fraction = str (number).split ('.') [1]
        numberString += '.' + fraction [:4]
    return numberString

def renderLines (lines, centered = False, fontSize = CD.FONT_SIZE, color = CC.WHITE):
    font = pygame.font.Font (GGU.fontName, fontSize)
    renderedLines = [font.render (line, True, color) for line in lines]
    yPos = 0
    neededX = max ([l.get_width () for l in renderedLines])
    neededY = sum ([l.get_height () for l in renderedLines])
    combinedLines = pygame.Surface ((neededX, neededY))
    for line in renderedLines:
        if centered:
            drawUtil.drawXCentered (line, combinedLines, yPos)
        else:
            combinedLines.blit (line, (0, yPos))
        yPos += line.get_height ()
    return combinedLines

def renderTextWithWordWrap (text, maxWidth, color=CC.WHITE):
    if isinstance (text, types.StringType):
        return renderLines (getWrappedLines (text, maxWidth), color=color)
    elif isinstance (text, types.ListType):
        lines = []
        for line in text:
            lines += getWrappedLines (line, maxWidth)
        return renderLines (lines)

def getWrappedLines (text, maxWidth):
    words = text.split ()
    assembledLines = []
    nextLine = []
    while len (words) > 0:
        if checkIfWordsWouldFit (nextLine + [words [0]], maxWidth):
            nextLine.append (words.pop (0))
        else:
            assembledLines.append (' '.join (nextLine))
            nextLine = []
    assembledLines.append (' '.join (nextLine))
    return assembledLines
