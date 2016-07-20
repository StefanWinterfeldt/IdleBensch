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
import engine.controller.saveController as saveController
import engine.util.draw as drawUtil
import engine.util.event as eventUtil
import engine.util.text as textUtil
import globals.gameState as GS
import globals.gameUtils as GU
import globals.view as GV
import pygame
import sys


gameButton = None
quitButton = None
gameButtonRect = None
quitButtonRect = None

def calculateButtonRects ():
    global gameButtonRect
    global quitButtonRect
    width = GV.menuView.get_width () / 2
    height = ((GV.menuView.get_height () / 2) - 30) / 2
    gameButtonRect = pygame.Rect ((GV.menuView.get_width () / 2) - (width / 2), (GV.menuView.get_height () / 2) + 10, width, height)
    quitButtonRect = pygame.Rect ((GV.menuView.get_width () / 2) - (width / 2), (GV.menuView.get_height () / 2) + 20 + height, width, height)

def initialize ():
    global gameButton
    global quitButton
    GV.menuView = pygame.Surface (CD.RESOLUTION, pygame.HWSURFACE)
    calculateButtonRects ()
    gameButton = GV.menuView.subsurface (gameButtonRect)
    quitButton = GV.menuView.subsurface (quitButtonRect)
    drawTitle ()

def drawTitle ():
    GV.menuView.blit (GU.titleImage, ((GV.menuView.get_width () / 2) - (GU.titleImage.get_width () / 2), (GV.menuView.get_height () / 4) - (GU.titleImage.get_height () / 2)))

def drawButtons ():
    pygame.draw.rect (gameButton, CC.DARK_GREEN, (1, 1, gameButton.get_width () - 2, gameButton.get_height () - 2), 2)
    pygame.draw.rect (quitButton, CC.DARK_GREEN, (1, 1, quitButton.get_width () - 2, quitButton.get_height () - 2), 2)
    gameButtonText = 'Neues Spiel' if not GS.stateWasAltered else 'Weiterspielen'
    quitButtonText = 'Beenden' if not GS.stateWasAltered else 'Speichern und Beenden'
    drawUtil.drawCentered (textUtil.renderLines ([gameButtonText], True, 72), gameButton)
    drawUtil.drawCentered (textUtil.renderLines ([quitButtonText], True, 72), quitButton)

def update ():
    drawButtons ()
    GV.screen.blit (GV.menuView, (0, 0))

def quitGame ():
    if GS.stateWasAltered:
        saveController.save ()
    sys.exit ()

def handleClick (event):
    if eventUtil.eventHappenedInRect (event, gameButtonRect):
        GS.context = 'game'
    elif eventUtil.eventHappenedInRect (event, quitButtonRect):
        quitGame ()
