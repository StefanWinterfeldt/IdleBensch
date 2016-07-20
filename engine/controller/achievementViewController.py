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
import constants.display as CD
import engine.controller.hintViewController as hintViewController
import engine.util.color as colorUtil
import engine.util.draw as drawUtil
import engine.util.text as textUtil
import globals.gameState as GS
import globals.subscriberMilestones as milestones
import globals.view as GV
import pygame

areaCode = 'AV'
hintText = 'Hier siehst du wie du im Vergleich mit anderen YouTubern stehst.'
currentMilestone = None
lastMilestone = None
progressSurface = None
textSurface = None

def handleMotion (event):
    if GS.currentMouseArea != areaCode:
        GS.currentMouseArea = areaCode
        hintViewController.showText (hintText)

def switchMilestonesIfPossible ():
    global currentMilestone
    global lastMilestone
    if currentMilestone is not None:
        if GS.subscriber > currentMilestone.subscribersNeeded:
            lastMilestone = currentMilestone
            currentMilestone = milestones.getNextMilestone (currentMilestone)

def getProgressPercentage ():
    start = 0 if lastMilestone is None else lastMilestone.subscribersNeeded
    end = currentMilestone.subscribersNeeded
    return (GS.subscriber - start) / (end - start)

def drawText ():
    if lastMilestone is not None:
        textSurface.fill (CC.BLACK)
        drawUtil.drawCentered(textUtil.renderLines (['Du hast mehr Subscriber als: ' + lastMilestone.name], False, 32), textSurface)

def drawProgress ():
    progressSurface.fill (CC.BLACK)
    if currentMilestone is not None:
        progressPercentage = getProgressPercentage ()
        progressMeterWidth = progressSurface.get_width () * progressPercentage
        pygame.draw.rect (progressSurface, colorUtil.getColorFromGradient (CC.RED, CC.GREEN, progressPercentage), (0, (progressSurface.get_height () / 2) - 30, progressMeterWidth, 60))

def initializeMilestones ():
    global currentMilestone
    currentMilestone = milestones.sortedMilestones [0]

def initialize ():
    global progressSurface
    global textSurface
    GV.achievementViewAbsoluteRect = pygame.Rect ((0 + CD.CLICK_VIEW_SIZE [0], CD.MESSAGE_VIEW_SIZE [1] + CD.UPGRADE_VIEW_SIZE [1], CD.ACHIEVEMENT_VIEW_SIZE [0], CD.ACHIEVEMENT_VIEW_SIZE [1]))
    GV.achievementView = GV.gameView.subsurface (GV.achievementViewAbsoluteRect)
    textSurface = GV.achievementView.subsurface ((0, 0, GV.achievementView.get_width (), GV.achievementView.get_height () / 2))
    progressSurface = GV.achievementView.subsurface ((0, GV.achievementView.get_height () / 2, GV.achievementView.get_width (), GV.achievementView.get_height () / 2))
    initializeMilestones ()
    pygame.draw.rect (GV.achievementView, CC.DARK_GREEN, (0, 0, CD.ACHIEVEMENT_VIEW_SIZE [0] - 1, CD.ACHIEVEMENT_VIEW_SIZE [1] - 1), 2)

def update ():
    switchMilestonesIfPossible()
    drawText ()
    drawProgress()
    pygame.draw.rect (GV.achievementView, CC.DARK_GREEN, (0, 0, CD.ACHIEVEMENT_VIEW_SIZE [0] - 1, CD.ACHIEVEMENT_VIEW_SIZE [1] - 1), 2)
