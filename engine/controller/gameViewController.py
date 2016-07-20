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
import engine.controller.achievementViewController as achievementViewController
import engine.controller.chatViewController as chatViewController
import engine.controller.clickViewController as clickViewController
import engine.controller.faceViewController as faceViewController
import engine.controller.hintViewController as hintViewController
import engine.controller.messageViewController as messageViewController
import engine.controller.menuViewController as menuViewController
import engine.controller.moneyViewController as moneyViewController
import engine.controller.upgradeViewController as upgradeViewController
import globals.view as view
import pygame

def initialize ():
    view.gameView = pygame.Surface (DC.RESOLUTION, pygame.HWSURFACE)
    achievementViewController.initialize ()
    clickViewController.initialize ()
    moneyViewController.initialize ()
    hintViewController.initialize ()
    faceViewController.initialize ()
    chatViewController.initialize ()
    upgradeViewController.initialize ()
    messageViewController.initialize ()
    menuViewController.initialize ()

def update ():
    clickViewController.update ()
    moneyViewController.update ()
    hintViewController.update ()
    faceViewController.update ()
    chatViewController.update ()
    messageViewController.update ()
    upgradeViewController.update ()
    achievementViewController.update ()
    view.screen.blit (view.gameView, (0, 0))
