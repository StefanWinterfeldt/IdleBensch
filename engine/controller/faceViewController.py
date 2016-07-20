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
import engine.util.draw as drawUtil
import engine.util.text as textUtil
import globals.gameState as GGS
import globals.view as GV
import pygame

areaCode = 'FV'
hintText = 'Hier ist Platz fuer deine Face-Cam.'

def handleMotion (event):
    if GGS.currentMouseArea != areaCode:
        GGS.currentMouseArea = areaCode
        hintViewController.showText (hintText)

def initialize ():
    GV.faceViewAbsoluteRect = pygame.Rect ((CD.RESOLUTION [0] - CD.FACE_VIEW_SIZE [0], 0, CD.FACE_VIEW_SIZE [0], CD.FACE_VIEW_SIZE [1]))
    GV.faceView = GV.gameView.subsurface (GV.faceViewAbsoluteRect)
    drawUtil.drawCentered (textUtil.renderLines(['A Place', 'For Your Face'], True, CD.FACE_VIEW_FONT_SIZE), GV.faceView)
    pygame.draw.rect (GV.faceView, CC.DARK_GREEN, (0, 0, CD.FACE_VIEW_SIZE [0] - 1, CD.FACE_VIEW_SIZE [1] - 1), 2)

def update ():
    pass
