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
import engine.util.text as textUtil
import engine.util.upgrade as upgradeUtil
import globals.chatData as chatData
import globals.gameState as GS
import globals.view as GV
import pygame
import random

areaCode = 'CHV',
hintText = 'Sobald du deinen ersten Stream freigeschaltet hast werden deine Zuschauer hier mit dir chatten.'
tempSurface = None
ticksSinceLastMessage = 0

def handleMotion (event):
    if GS.currentMouseArea != areaCode:
        GS.currentMouseArea = areaCode
        hintViewController.showText (hintText)

def getRenderedChatMessage ():
    nick = chatData.getRandomNick ()
    message = chatData.getRandomMessage ()
    textRender = textUtil.renderTextWithWordWrap (nick + ': ' + message, GV.chatView.get_width () - 10)
    color = random.choice (CC.CHAT_COLORS)
    nickRender = textUtil.renderLines ([nick + ':'], False, CD.FONT_SIZE, color)
    textRender.blit (nickRender, (0, 0))
    return textRender

def scrollBy (height):
    tempSurface.blit (GV.chatView, (0, 0))
    GV.chatView.fill (CC.BLACK)
    GV.chatView.blit (tempSurface, (0, -height), (0, 0, tempSurface.get_width (), tempSurface.get_height () - 2))

def getRenderedModAction ():
    message = chatData.getRandomModAction ()
    textRender = textUtil.renderTextWithWordWrap (message, GV.chatView.get_width () - 10, CC.GRAY)
    return textRender

def getRenderedModMessage ():
    message = chatData.getRandomModMessage ()
    textRender = textUtil.renderTextWithWordWrap ('Ori: ' + message, GV.chatView.get_width () - 10)
    nickRender = textUtil.renderLines (['Ori:'], False, CD.FONT_SIZE, CC.PURPLE)
    textRender.blit (nickRender, (0, 0))
    return textRender

def getRenderedModInteraction ():
    if random.randint (0, 1) == 1:
        return getRenderedModAction ()
    else:
        return getRenderedModMessage ()

def addMessage ():
    if upgradeUtil.getUpgradeById (12).active and random.random () < CO.CHANCE_OF_MOD_INTERACTION:
        renderedMessage = getRenderedModInteraction ()
    else:
        renderedMessage = getRenderedChatMessage ()
    scrollBy (renderedMessage.get_height ())
    GV.chatView.blit (renderedMessage, (5, GV.chatView.get_height () - renderedMessage.get_height ()))

def initialize ():
    global tempSurface
    GV.chatViewAbsoluteRect = pygame.Rect ((CD.RESOLUTION [0] - CD.CHAT_VIEW_SIZE [0], CD.FACE_VIEW_SIZE [1], CD.CHAT_VIEW_SIZE [0], CD.CHAT_VIEW_SIZE [1]))
    GV.chatView = GV.gameView.subsurface (GV.chatViewAbsoluteRect)
    tempSurface = pygame.Surface ((GV.chatView.get_width (), GV.chatView.get_height ()))
    pygame.draw.rect (GV.chatView, CC.DARK_GREEN, (0, 0, CD.CHAT_VIEW_SIZE [0] - 1, CD.CHAT_VIEW_SIZE [1] - 1), 2)

def update ():
    global ticksSinceLastMessage
    if GS.streams > 0:
        if ticksSinceLastMessage >= (CO.BASE_SECONDS_BETWEEN_CHAT_MESSAGES * CD.FRAME_RATE) / GS.streams:
            addMessage ()
            pygame.draw.rect (GV.chatView, CC.DARK_GREEN, (0, 0, CD.CHAT_VIEW_SIZE [0] - 1, CD.CHAT_VIEW_SIZE [1] - 1), 2)
            ticksSinceLastMessage = 0
        ticksSinceLastMessage += 1
