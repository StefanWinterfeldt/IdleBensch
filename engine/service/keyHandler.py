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

import engine.controller.upgradeViewController as upgradeViewController
import engine.util.upgrade as upgradeUtil
import globals.gameLogic as GL
import globals.gameState as GS
import pygame
import sys

def handleGameKeyEvent (event):
    if event.key == pygame.K_ESCAPE:
        GS.context = 'menu'
    elif event.key == pygame.K_v and GL.DEV_MODE:
        upgradeUtil.makeAllUpgradesVisible ()
        upgradeViewController.drawCategories ()
    elif event.key == pygame.K_c and GL.DEV_MODE:
        upgradeUtil.setAllCostsToZero ()

def handleMenuKeyEvent (event):
    if event.key == pygame.K_ESCAPE:
        GS.context = 'game'

def handleCreditsEvent (event):
    if event.key == pygame.K_ESCAPE:
        sys.exit ()

def handleKeyEvent (event):
    if GS.context == 'game':
        handleGameKeyEvent (event)
    elif GS.context == 'menu':
        handleMenuKeyEvent (event)
    elif GS.context == 'credits':
        handleCreditsEvent (event)
