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
import engine.controller.gameViewController as gameViewController
import engine.controller.menuViewController as menuViewController
import engine.controller.saveController as saveController
import globals.gameUtils as GGU
import globals.view as GV
import os
import pygame
import random

def initializeFont ():
    GGU.fontName = pygame.font.get_default_font ()
    GGU.font = pygame.font.Font (GGU.fontName, DC.FONT_SIZE)

def initializeUtilImages ():
    GGU.creditsImage = pygame.image.load (os.path.join ('resources', 'ingame', 'credits.png'))
    GGU.introImage = pygame.image.load (os.path.join ('resources', 'ingame', 'intro.png'))
    GGU.lockedSymbol = pygame.image.load (os.path.join ('resources', 'ingame', 'upgrade', 'lockedMask.png'))
    GGU.titleImage = pygame.image.load (os.path.join ('resources', 'ingame', 'title.png'))
    GGU.upgradeInactiveMask = pygame.image.load (os.path.join ('resources', 'ingame', 'upgrade', 'inactiveMask.png'))

def initializeViews ():
    GV.screen = pygame.display.set_mode (DC.RESOLUTION, pygame.FULLSCREEN | pygame.HWSURFACE)
    menuViewController.initialize ()
    gameViewController.initialize ()

def initializeAndLoadSaveGameIfPossible ():
    saveController.initialize ()
    if saveController.saveGameExists ():
        saveController.loadSaveGame ()

def initialize ():
    random.seed ()
    pygame.init ()
    GGU.clock = pygame.time.Clock ()
    initializeUtilImages ()
    initializeFont ()
    initializeViews ()
    initializeAndLoadSaveGameIfPossible ()
