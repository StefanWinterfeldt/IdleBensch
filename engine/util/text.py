import constants.color as CC
import globals.gameUtils as GGU
import pygame

def checkIfWordsWouldFit (words, maxWidth):
    line = ' '.join (words)
    return GGU.font.size (line) [0] < maxWidth

def renderLines (lines):
    renderedLines = [GGU.font.render (line, True, CC.WHITE) for line in lines]
    yPos = 0
    neededX = max ([l.get_width () for l in renderedLines])
    neededY = sum ([l.get_height () for l in renderedLines])
    combinedLines = pygame.Surface ((neededX, neededY))
    for line in renderedLines:
        combinedLines.blit (line, (0, yPos))
        yPos += line.get_height ()
    return combinedLines

def renderTextWithWordWrap (text, maxWidth):
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
    return renderLines (assembledLines)
