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

import constants.color as CC
import engine.util.color as colorUtil
import engine.util.draw as drawUtil
import globals.gameState as GS
import globals.gameUtils as GU
import globals.view as GV
import math
import pygame


LEVEL1_TICKS = 300
LEVEL2_TICKS = 200
LEVEL3_TICKS = 600
LEVEL4_TICKS = 100
LEVEL5_TICKS = 200
LEVEL6_TICKS = 600

level = 1
ticks = 0

circleRect = None
pentagramPoints = []

def fadeInCredits ():
    percentage = 1 - (ticks / float (LEVEL6_TICKS))
    overlay = pygame.Surface (GV.screen.get_size (), pygame.HWSURFACE)
    overlay.fill (CC.BLACK)
    overlay.set_alpha (int (255 * percentage))
    GV.screen.blit (GU.creditsImage, (0, 0))
    GV.screen.blit (overlay, (0, 0))

def fadeout ():
    percentage = (ticks / float (LEVEL5_TICKS))
    color = colorUtil.getColorFromGradient (CC.DARK_RED, CC.BLACK, percentage)
    GV.screen.fill (color)

def drawMiddleCircle ():
    percentage = (ticks / float (LEVEL4_TICKS))
    origin = (GV.screen.get_width () / 2, GV.screen.get_height () / 2)
    radius = GV.screen.get_width ()
    pygame.draw.circle (GV.screen, CC.DARK_RED, origin, int (radius * percentage))

def drawSubCircles ():
    percentage = (ticks / float (LEVEL2_TICKS))
    radius = 50
    pygame.draw.circle (GV.screen, CC.RED, pentagramPoints [0], int (radius * percentage))
    pygame.draw.circle (GV.screen, CC.RED, pentagramPoints [1], int (radius * percentage))
    pygame.draw.circle (GV.screen, CC.RED, pentagramPoints [2], int (radius * percentage))
    pygame.draw.circle (GV.screen, CC.RED, pentagramPoints [3], int (radius * percentage))
    pygame.draw.circle (GV.screen, CC.RED, pentagramPoints [4], int (radius * percentage))

def calculatePentagramPoints ():
    origin = (GV.screen.get_width () / 2, GV.screen.get_height () / 2)
    radius = (GV.screen.get_height () / 2) - 50
    c1 = math.cos ((2 * math.pi) / 5)
    c2 = math.cos ((math.pi) / 5)
    s1 = math.sin ((2 * math.pi / 5))
    s2 = math.sin ((4 * math.pi / 5))
    pentagramPoints.append ((origin [0], origin [1] + radius))
    pentagramPoints.append ((int (origin [0] - s1 * radius), int (origin [1] + c1 * radius)))
    pentagramPoints.append ((int (origin [0] - s2 * radius), int (origin [1] - c2 * radius)))
    pentagramPoints.append ((int (origin [0] + s2 * radius), int (origin [1] - c2 * radius)))
    pentagramPoints.append ((int (origin [0] + s1 * radius), int (origin [1] + c1 * radius)))

def drawPentagramPart ():
    percentage = (ticks / float (LEVEL3_TICKS))
    drawUtil.drawPartialLine (GV.screen, CC.RED, pentagramPoints [0], pentagramPoints [2], 40, percentage)
    drawUtil.drawPartialLine (GV.screen, CC.RED, pentagramPoints [2], pentagramPoints [4], 40, percentage)
    drawUtil.drawPartialLine (GV.screen, CC.RED, pentagramPoints [4], pentagramPoints [1], 40, percentage)
    drawUtil.drawPartialLine (GV.screen, CC.RED, pentagramPoints [1], pentagramPoints [3], 40, percentage)
    drawUtil.drawPartialLine (GV.screen, CC.RED, pentagramPoints [3], pentagramPoints [0], 40, percentage)

def drawCirclePart ():
    global circleRect
    if circleRect is None:
        width = GV.screen.get_height () - 100
        circleRect = ((GV.screen.get_width () / 2) - (width / 2), (GV.screen.get_height () / 2) - (width / 2), width, width)
    stopAngle = (ticks / float (LEVEL1_TICKS)) * 2 * math.pi
    pygame.draw.arc (GV.screen, CC.RED, circleRect, 0, stopAngle, 40)

def carryOutLevelActions ():
    if level == 1:
        drawCirclePart ()
    elif level == 2:
        drawSubCircles ()
    elif level == 3:
        drawPentagramPart ()
    elif level == 4:
        drawMiddleCircle ()
    elif level == 5:
        fadeout ()
    elif level == 6:
        fadeInCredits ()
    elif level == 7:
        GS.context = 'credits'

def increaseLevelAndResetTicks ():
    global level
    global ticks
    level += 1
    ticks = 0

def switchLevelIfPossible ():
    global level
    global ticks
    if level == 1 and ticks > LEVEL1_TICKS + 1:
        increaseLevelAndResetTicks ()
        calculatePentagramPoints ()
    elif level == 2 and ticks > LEVEL2_TICKS + 1:
        increaseLevelAndResetTicks ()
    elif level == 3 and ticks > LEVEL3_TICKS + 1:
        increaseLevelAndResetTicks ()
    elif level == 4 and ticks > LEVEL4_TICKS + 1:
        increaseLevelAndResetTicks ()
    elif level == 5 and ticks > LEVEL5_TICKS + 1:
        increaseLevelAndResetTicks ()
    elif level == 6 and ticks > LEVEL6_TICKS + 1:
        increaseLevelAndResetTicks ()

def update ():
    global ticks
    carryOutLevelActions ()
    switchLevelIfPossible ()
    ticks += 1
