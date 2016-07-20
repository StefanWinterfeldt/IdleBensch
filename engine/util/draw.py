#Copyright 2016 Stefan Winterfeldt
#This file is part of Idle Bensch.
#
#Idle Bensch is free software: you can redistribute it and/or modify
#it under the terms of the GNU General Public License as published by
#the Free Software Foundation, either version 3 of the License, or
#(at your option) any later version.
#
#Idle Bensch is distributed in the hope that it will be useful,
#but WITHOUT ANY WARRANTY; without even the implied warranty of
#MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#GNU General Public License for more details.
#
#You should have received a copy of the GNU General Public License
#along with Idle Bensch.  If not, see <http://www.gnu.org/licenses/>.

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
