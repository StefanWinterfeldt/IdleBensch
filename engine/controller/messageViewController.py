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
import constants.control as CO
import constants.display as CD
import engine.controller.hintViewController as hintViewController
import engine.util.draw as drawUtil
import engine.util.text as textUtil
import globals.gameState as GS
import globals.messages as messages
import globals.view as GV
import pygame
import random

areaCode = 'MEV'
hintText = 'Hier erfaehrst du die neuesten Nachrichten.'
ticksSinceLastMessage = 0

def handleMotion (event):
    if GS.currentMouseArea != areaCode:
        GS.currentMouseArea = areaCode
        hintViewController.showText (hintText)

def getAvailableMessages ():
    return [message for message in messages.messages if message.isAvailable ()]

def showRandomMessage ():
    GV.messageView.fill (CC.BLACK)
    pygame.draw.rect (GV.messageView, CC.DARK_GREEN, (0, 0, CD.MESSAGE_VIEW_SIZE [0] - 1, CD.MESSAGE_VIEW_SIZE [1] - 1), 2)
    availableMessages = getAvailableMessages ()
    if len (availableMessages) >= 1:
        chosenMessage = random.choice (availableMessages)
        drawUtil.drawCentered (textUtil.renderTextWithWordWrap (chosenMessage.text, CD.MESSAGE_VIEW_SIZE [0] - 10), GV.messageView)

def initialize ():
    GV.messageViewAbsoluteRect = pygame.Rect ((0 + CD.CLICK_VIEW_SIZE [0], 0, CD.MESSAGE_VIEW_SIZE [0], CD.MESSAGE_VIEW_SIZE [1]))
    GV.messageView = GV.gameView.subsurface (GV.messageViewAbsoluteRect)
    showRandomMessage ()

def update ():
    global ticksSinceLastMessage
    if ticksSinceLastMessage >= (CO.SECONDS_BETWEEN_MESSAGES * CD.FRAME_RATE):
        showRandomMessage ()
        ticksSinceLastMessage = 0
    ticksSinceLastMessage += 1
