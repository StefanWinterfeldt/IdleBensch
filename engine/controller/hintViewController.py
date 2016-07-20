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
import engine.util.text as textUtil
import globals.gameState as GGS
import globals.view as GV
import pygame


areaCode = 'HV'
hintText = 'In dieser Box erscheinen hilfreiche Hilfetexte, wie dieser hier.'

def clearText ():
    GV.hintView.fill (CC.BLACK)
    pygame.draw.rect (GV.hintView, CC.DARK_GREEN, (0, 0, CD.HINT_VIEW_SIZE [0] - 1, CD.HINT_VIEW_SIZE [1] - 1), 2)

def handleMotion (event):
    if GGS.currentMouseArea != areaCode:
        GGS.currentMouseArea = areaCode
        showText (hintText)

def initialize ():
    GV.hintViewAbsoluteRect = pygame.Rect ((0, CD.CLICK_VIEW_SIZE [1] + CD.MONEY_VIEW_SIZE [1] - 1, CD.HINT_VIEW_SIZE [0], CD.HINT_VIEW_SIZE [1]))
    GV.hintView = GV.gameView.subsurface (GV.hintViewAbsoluteRect)
    pygame.draw.rect (GV.hintView, CC.DARK_GREEN, (0, 0, CD.HINT_VIEW_SIZE [0] - 1, CD.HINT_VIEW_SIZE [1] - 1), 2)

def showText (text):
    GV.hintView.fill (CC.BLACK)
    GV.hintView.blit (textUtil.renderTextWithWordWrap (text, CD.HINT_VIEW_SIZE [0] - 10), (5, 5))
    pygame.draw.rect (GV.hintView, CC.DARK_GREEN, (0, 0, CD.HINT_VIEW_SIZE [0] - 1, CD.HINT_VIEW_SIZE [1] - 1), 2)

def update ():
    pass
