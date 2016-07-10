import pygame

def calculateXOffset (source, dest):
    return (dest.get_width () / 2) - (source.get_width () / 2)

def calculateYOffset (source, dest):
    return (dest.get_height () / 2) - (source.get_height () / 2)

def drawCentered (source, dest):
    xOffset = calculateXOffset (source, dest)
    yOffset = calculateYOffset (source, dest)
    dest.blit (source, (xOffset, yOffset))

def drawPartialLine (surface, color, start, end, width, percentage):
    xWay = (end [0] - start [0]) * percentage
    yWay = (end [1] - start [1]) * percentage
    adjustedEnd = (start [0] + xWay, start [1] + yWay)
    pygame.draw.line (surface, color, start, adjustedEnd, width)

def drawXCentered (source, dest, y):
    xOffset = calculateXOffset (source, dest)
    dest.blit (source, (xOffset, y))
