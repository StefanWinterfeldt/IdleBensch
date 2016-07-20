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

from engine.controller.messageObjects.message import Message
import constants.color as CC
import constants.display as CD
import constants.control as CO
import engine.controller.clickViewController as clickViewController
import engine.controller.messageViewController as messageViewController
import engine.util.draw as drawUtil
import engine.util.text as textUtil
import engine.util.upgrade
import globals.chatData as chatData
import globals.gameLogic as GL
import globals.gameState as GS
import globals.messages as messages
import globals.view as GV
import importlib
import os
import pygame
import random


endingTicks = 0
endingLevel = 0
lastModifiedUpgrade = 0

def drawIdleBensch ():
    clickViewController.episodeCompletion = 0
    clickViewController.seasonCompletion = 0
    GV.clickView.fill (CC.BLACK)
    drawUtil.drawCentered (textUtil.renderLines (['Idle', 'Bensch'], True, 48, CC.PURPLE), GV.clickView)
    pygame.draw.rect (GV.clickView, CC.DARK_GREEN, (0, 0, CD.CLICK_VIEW_SIZE [0] - 1, CD.CLICK_VIEW_SIZE [1] - 1), 2)

def deactivateGameLogic ():
    GL.BASE_CLICKS_PER_SECOND = 0.0
    GL.BASE_DONATION_CHANCE_PER_STREAM_PER_SECOND = 0.0
    GL.BASE_PURCHASE_CHANCE_PER_SUBSCRIBER_PER_SECOND = 0.0
    GL.BASE_EPISODES_PER_CLICK = 0.0
    GL.BASE_EPISODES_PER_SEASON = 100.0
    GL.BASE_MAX_DONATION = 0.0
    GL.BASE_MAX_PURCHASE = 0.0
    GL.BASE_MAX_SUBSCRIBERS_PER_EPISODE = 0.0
    GL.BASE_MAX_SUBSCRIBERS_PER_SEASON = 0.0
    GL.BASE_MIN_DONATION = 0.0
    GL.BASE_MIN_PURCHASE = 0.0
    GL.BASE_MIN_SUBSCRIBERS_PER_EPISODE = 0.0
    GL.BASE_MIN_SUBSCRIBERS_PER_SEASON = 0.0
    GL.BASE_MONEY_PER_VIEW = 0.0
    GL.BASE_SUBSCRIBER_VIEWS_PER_EPISODE = 0.0
    GL.BASE_SUBSCRIBERS_PER_STREAM_PER_SECOND = 0.0
    GL.BASE_SECONDS_TO_PROCESS_EPISODE = 10
    GL.BASE_SECONDS_TO_PROCESS_SEASON = 100
    GL.BASE_VIEWS_PER_EPISODE = 0.0
    CO.CHANCE_OF_MOD_INTERACTION = 0.0

def activateEnding ():
    GS.endingInProgress = True
    deactivateGameLogic ()
    drawIdleBensch ()

def modifyMessage ():
    messages.messages = [Message (None, None, "Letzte Meldung: Beruehmter Let's Player bringt Universum zu Einsturz. So long as thanks for all the clicks...")]
    messageViewController.showRandomMessage ()

def modifyChat ():
    chatData.messageFunctions = [lambda: random.choice (chatData.endingMessages)]

def initialize ():
    pass

def switchEndingLevel ():
    global endingLevel
    endingLevel += 1
    if endingLevel == 1:
        modifyMessage ()
    elif endingLevel == 2:
        modifyChat ()
    elif endingLevel == 4:
        GS.context = 'endSequence'

def modifyUpgradeIfPossible ():
    global lastModifiedUpgrade
    if lastModifiedUpgrade < 80:
        upgrade = engine.util.upgrade.getUpgradeById (lastModifiedUpgrade + 1)
        upgrade.image = pygame.image.load (os.path.join ('resources', 'ingame', 'upgrade', 'tech', 'idleBensch.png'))
        UVC = importlib.import_module ('engine.controller.upgradeViewController')
        UVC.drawCategories ()
        lastModifiedUpgrade += 1

def update ():
    global endingTicks
    if GS.endingInProgress:
        if endingTicks >= CO.SECONDS_BETWEEN_ENDING_LEVELS * CD.FRAME_RATE:
            switchEndingLevel ()
            endingTicks = 0
        endingTicks += 1
        if endingLevel > 2 and endingTicks % 5 == 0:
            modifyUpgradeIfPossible ()
