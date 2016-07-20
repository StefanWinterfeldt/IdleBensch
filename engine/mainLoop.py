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

import constants.display as DC
import engine.service.keyHandler as keyHandler
import engine.service.mouseHandler as mouseHandler
import engine.controller.endingController as endingController
import engine.controller.endSequenceController as endSequenceController
import engine.controller.introController as introController
import engine.controller.menuViewController as menuViewController
import engine.controller.gameStateTriggerController as gameStateTriggerController
import engine.controller.gameViewController as gameViewController
import engine.controller.passiveIncome as passiveIncomeController
import engine.controller.saveController as saveController
import engine.controller.timeSlotController as timeSlotController
import globals.gameState as GS
import globals.gameUtils as GGU
import pygame
import sys

def updateDisplay ():
    if GS.context == 'game':
        gameViewController.update ()
    elif GS.context == 'menu':
        menuViewController.update ()
    elif GS.context == 'endSequence':
        endSequenceController.update ()
    elif GS.context == 'intro':
        introController.update ()
    pygame.display.flip ()

def updateNonDisplayControllers ():
    passiveIncomeController.update ()
    saveController.update ()
    endingController.update ()

def updateTimeSlots ():
    timeSlotController.update ()

def triggerActionsBasedOnGameStateChanges ():
    gameStateTriggerController.update ()

def handleEvents ():
    for event in pygame.event.get ():
        if event.type == pygame.QUIT: sys.exit ()
        if event.type == pygame.KEYDOWN: keyHandler.handleKeyEvent (event)
        if event.type in [pygame.MOUSEBUTTONDOWN, pygame.MOUSEMOTION]: mouseHandler.handleMouseEvent (event)

def loop ():
    while True:
        GGU.clock.tick (DC.FRAME_RATE)
        handleEvents ()
        if GS.context == 'game':
            GS.stateWasAltered = True
            triggerActionsBasedOnGameStateChanges ()
            updateNonDisplayControllers ()
            updateTimeSlots ()
        updateDisplay ()
