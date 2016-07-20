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

import engine.controller.messageViewController as messageViewController
import engine.controller.achievementViewController as achievementViewController
import engine.controller.chatViewController as chatViewController
import engine.controller.clickViewController as clickViewController
import engine.controller.faceViewController as faceViewController
import engine.controller.hintViewController as hintViewController
import engine.controller.menuViewController as menuViewController
import engine.controller.moneyViewController as moneyViewController
import engine.controller.upgradeViewController as upgradeViewController
import engine.util.event as eventUtil
import globals.gameState as GGS
import globals.view as GV
import pygame

def dispatchClickToView (event):
    if eventUtil.eventHappenedInRect (event, GV.clickViewAbsoluteRect):
        clickViewController.handleClick (event)
    elif eventUtil.eventHappenedInRect (event, GV.upgradeViewAbsoluteRect):
        upgradeViewController.handleClick (event)

def dispatchMotionToView (event):
    if eventUtil.eventHappenedInRect (event, GV.clickViewAbsoluteRect):
        clickViewController.handleMotion (event)
    elif eventUtil.eventHappenedInRect (event, GV.moneyViewAbsoluteRect):
        moneyViewController.handleMotion (event)
    elif eventUtil.eventHappenedInRect (event, GV.hintViewAbsoluteRect):
        hintViewController.handleMotion (event)
    elif eventUtil.eventHappenedInRect (event, GV.faceViewAbsoluteRect):
        faceViewController.handleMotion (event)
    elif eventUtil.eventHappenedInRect (event, GV.upgradeViewAbsoluteRect):
        upgradeViewController.handleMotion (event)
    elif eventUtil.eventHappenedInRect (event, GV.chatViewAbsoluteRect):
        chatViewController.handleMotion (event)
    elif eventUtil.eventHappenedInRect (event, GV.achievementViewAbsoluteRect):
        achievementViewController.handleMotion (event)
    elif eventUtil.eventHappenedInRect (event, GV.messageViewAbsoluteRect):
        messageViewController.handleMotion (event)
    else:
        if GGS.currentMouseArea is not None:
            GGS.currentMouseArea = None
            hintViewController.clearText ()

def handleGameMouseEvent (event):
    if event.type == pygame.MOUSEBUTTONDOWN:
        dispatchClickToView (event)
    elif event.type == pygame.MOUSEMOTION:
        dispatchMotionToView (event)

def handleMenuMouseEvent (event):
    if event.type == pygame.MOUSEBUTTONDOWN:
        menuViewController.handleClick (event)

def handleMouseEvent (event):
    if GGS.context == 'game':
        handleGameMouseEvent (event)
    elif GGS.context == 'menu':
        handleMenuMouseEvent (event)
