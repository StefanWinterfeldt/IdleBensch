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
import globals.gameState as GS
import globals.gameUtils as GU
import globals.view as GV
import pygame


INTRO_TICKS = 200

ticks = 0

def fadeInCredits ():
    percentage = 1 - (ticks / float (INTRO_TICKS))
    overlay = pygame.Surface (GV.screen.get_size (), pygame.HWSURFACE)
    overlay.fill (CC.BLACK)
    overlay.set_alpha (int (255 * percentage))
    GV.screen.blit (GU.introImage, (0, 0))
    GV.screen.blit (overlay, (0, 0))

def update ():
    global ticks
    fadeInCredits ()
    ticks += 1
    if ticks > INTRO_TICKS:
        GS.context = 'menu'
