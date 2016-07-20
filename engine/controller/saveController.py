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

from engine.controller.saveObjects.saveGame import SaveGame
import constants.control as CO
import constants.display as CD
import engine.controller.achievementViewController as achievementViewController
import engine.controller.clickViewController as clickViewController
import engine.controller.gameStateTriggerController as gameStateTriggerController
import engine.controller.passiveIncome as passiveIncomeController
import engine.controller.timeSlotController as timeSlotController
import engine.controller.upgradeViewController as upgradeController
import engine.util.upgrade as upgradeUtil
import globals.gameLogic as GL
import globals.gameState as GS
import globals.upgrade.categories as categories
import os
import pickle


ticksSinceLastSave = 0

def writeGameState (saveGame):
    saveGame.episodes = GS.episodes
    saveGame.money = GS.money
    saveGame.seasons = GS.seasons
    saveGame.streams = GS.streams
    saveGame.subscriber = GS.subscriber
    saveGame.views = GS.views

def writeGameLogic (saveGame):
    saveGame.BASE_CLICKS_PER_SECOND = GL.BASE_CLICKS_PER_SECOND
    saveGame.BASE_DONATION_CHANCE_PER_STREAM_PER_SECOND = GL.BASE_DONATION_CHANCE_PER_STREAM_PER_SECOND
    saveGame.BASE_PURCHASE_CHANCE_PER_SUBSCRIBER_PER_SECOND = GL.BASE_PURCHASE_CHANCE_PER_SUBSCRIBER_PER_SECOND
    saveGame.BASE_EPISODES_PER_CLICK = GL.BASE_EPISODES_PER_CLICK
    saveGame.BASE_EPISODES_PER_SEASON = GL.BASE_EPISODES_PER_SEASON
    saveGame.BASE_MAX_DONATION = GL.BASE_MAX_DONATION
    saveGame.BASE_MAX_PURCHASE = GL.BASE_MAX_PURCHASE
    saveGame.BASE_MAX_SUBSCRIBERS_PER_EPISODE = GL.BASE_MAX_SUBSCRIBERS_PER_EPISODE
    saveGame.BASE_MAX_SUBSCRIBERS_PER_SEASON = GL.BASE_MAX_SUBSCRIBERS_PER_SEASON
    saveGame.BASE_MIN_DONATION = GL.BASE_MIN_DONATION
    saveGame.BASE_MIN_PURCHASE = GL.BASE_MIN_PURCHASE
    saveGame.BASE_MIN_SUBSCRIBERS_PER_EPISODE = GL.BASE_MIN_SUBSCRIBERS_PER_EPISODE
    saveGame.BASE_MIN_SUBSCRIBERS_PER_SEASON = GL.BASE_MIN_SUBSCRIBERS_PER_SEASON
    saveGame.BASE_MONEY_PER_VIEW = GL.BASE_MONEY_PER_VIEW
    saveGame.BASE_SUBSCRIBER_VIEWS_PER_EPISODE = GL.BASE_SUBSCRIBER_VIEWS_PER_EPISODE
    saveGame.BASE_SUBSCRIBERS_PER_STREAM_PER_SECOND = GL.BASE_SUBSCRIBERS_PER_STREAM_PER_SECOND
    saveGame.BASE_SECONDS_TO_PROCESS_EPISODE = GL.BASE_SECONDS_TO_PROCESS_EPISODE
    saveGame.BASE_SECONDS_TO_PROCESS_SEASON = GL.BASE_SECONDS_TO_PROCESS_SEASON
    saveGame.BASE_VIEWS_PER_EPISODE = GL.BASE_VIEWS_PER_EPISODE

def writeUpgradeStates (saveGame):
    saveGame.activeUpgradeIds = [upgrade.id for upgrade in upgradeUtil.getAllUpgrades () if upgrade.active]
    saveGame.visibleUpgradeIds = [upgrade.id for upgrade in upgradeUtil.getAllUpgrades () if upgrade.visible]

def writeControllerStates (saveGame):
    saveGame.lastFullEpisodes = gameStateTriggerController.lastFullEpisodes
    saveGame.lastFullSeasons = gameStateTriggerController.lastFullSeasons
    saveGame.lastFullViews = gameStateTriggerController.lastFullViews
    saveGame.timeSlots = timeSlotController.timeSlots
    saveGame.ticksSinceLastProcess = passiveIncomeController.ticksSinceLastProcess
    saveGame.currentAutoClicks = passiveIncomeController.currentAutoClicks
    saveGame.currentSubscribers = passiveIncomeController.currentSubscribers
    saveGame.episodeCompletion = clickViewController.episodeCompletion
    saveGame.seasonCompletion = clickViewController.seasonCompletion
    saveGame.currentMilestone = achievementViewController.currentMilestone
    saveGame.lastMilestone = achievementViewController.lastMilestone

def createSaveGameFolderIfNecessary ():
    if not os.path.exists ('saveGames'):
        os.mkdir ('saveGames')

def initialize ():
    createSaveGameFolderIfNecessary ()

def createSaveGame ():
    saveGame = SaveGame ()
    writeGameState (saveGame)
    writeGameLogic (saveGame)
    writeUpgradeStates (saveGame)
    writeControllerStates (saveGame)
    return saveGame

def save ():
    if not GS.endingInProgress:
        saveGame = createSaveGame ()
        saveFile = open ('saveGames/game.sav', 'wb')
        pickle.dump (saveGame, saveFile, pickle.HIGHEST_PROTOCOL)
        saveFile.close ()

def readGameState (saveGame):
    GS.episodes = saveGame.episodes
    GS.money = saveGame.money
    GS.seasons = saveGame.seasons
    GS.streams = saveGame.streams
    GS.subscriber = saveGame.subscriber
    GS.views = saveGame.views

def readGameLogic (saveGame):
    GL.BASE_CLICKS_PER_SECOND = saveGame.BASE_CLICKS_PER_SECOND
    GL.BASE_DONATION_CHANCE_PER_STREAM_PER_SECOND = saveGame.BASE_DONATION_CHANCE_PER_STREAM_PER_SECOND
    GL.BASE_PURCHASE_CHANCE_PER_SUBSCRIBER_PER_SECOND = saveGame.BASE_PURCHASE_CHANCE_PER_SUBSCRIBER_PER_SECOND
    GL.BASE_EPISODES_PER_CLICK = saveGame.BASE_EPISODES_PER_CLICK
    GL.BASE_EPISODES_PER_SEASON = saveGame.BASE_EPISODES_PER_SEASON
    GL.BASE_MAX_DONATION = saveGame.BASE_MAX_DONATION
    GL.BASE_MAX_PURCHASE = saveGame.BASE_MAX_PURCHASE
    GL.BASE_MAX_SUBSCRIBERS_PER_EPISODE = saveGame.BASE_MAX_SUBSCRIBERS_PER_EPISODE
    GL.BASE_MAX_SUBSCRIBERS_PER_SEASON = saveGame.BASE_MAX_SUBSCRIBERS_PER_SEASON
    GL.BASE_MIN_DONATION = saveGame.BASE_MIN_DONATION
    GL.BASE_MIN_PURCHASE = saveGame.BASE_MIN_PURCHASE
    GL.BASE_MIN_SUBSCRIBERS_PER_EPISODE = saveGame.BASE_MIN_SUBSCRIBERS_PER_EPISODE
    GL.BASE_MIN_SUBSCRIBERS_PER_SEASON = saveGame.BASE_MIN_SUBSCRIBERS_PER_SEASON
    GL.BASE_MONEY_PER_VIEW = saveGame.BASE_MONEY_PER_VIEW
    GL.BASE_SUBSCRIBER_VIEWS_PER_EPISODE = saveGame.BASE_SUBSCRIBER_VIEWS_PER_EPISODE
    GL.BASE_SUBSCRIBERS_PER_STREAM_PER_SECOND = saveGame.BASE_SUBSCRIBERS_PER_STREAM_PER_SECOND
    GL.BASE_SECONDS_TO_PROCESS_EPISODE = saveGame.BASE_SECONDS_TO_PROCESS_EPISODE
    GL.BASE_SECONDS_TO_PROCESS_SEASON = saveGame.BASE_SECONDS_TO_PROCESS_SEASON
    GL.BASE_VIEWS_PER_EPISODE = saveGame.BASE_VIEWS_PER_EPISODE

def anyUpgradeIsVisible (category):
    for upgrade in category.upgrades:
        if upgrade.visible:
            return True
    return False

def readUpgradeStates (saveGame):
    for id in saveGame.activeUpgradeIds:
        upgradeUtil.getUpgradeById (id).active = True
    for id in saveGame.visibleUpgradeIds:
        upgradeUtil.getUpgradeById (id).visible = True
    for category in categories.categories:
        if anyUpgradeIsVisible (category):
            category.header.visible = True
    upgradeController.drawCategories ()

def readControllerStates (saveGame):
    gameStateTriggerController.lastFullEpisodes = saveGame.lastFullEpisodes
    gameStateTriggerController.lastFullSeasons = saveGame.lastFullSeasons
    gameStateTriggerController.lastFullViews = saveGame.lastFullViews
    timeSlotController.timeSlots = saveGame.timeSlots
    passiveIncomeController.ticksSinceLastProcess = saveGame.ticksSinceLastProcess
    passiveIncomeController.currentAutoClicks = saveGame.currentAutoClicks
    passiveIncomeController.currentSubscribers = saveGame.currentSubscribers
    clickViewController.episodeCompletion = saveGame.episodeCompletion
    clickViewController.seasonCompletion = saveGame.seasonCompletion
    achievementViewController.currentMilestone = saveGame.currentMilestone
    achievementViewController.lastMilestone = saveGame.lastMilestone

def readSaveGame (saveGame):
    readGameState (saveGame)
    readGameLogic (saveGame)
    readUpgradeStates (saveGame)
    readControllerStates (saveGame)

def loadSaveGame ():
    saveFile = open ('saveGames/game.sav', 'rb')
    saveGame = pickle.load (saveFile)
    saveFile.close ()
    readSaveGame (saveGame)
    GS.stateWasAltered = True

def saveGameExists ():
    return os.path.exists ('saveGames/game.sav')

def update ():
    global ticksSinceLastSave
    if ticksSinceLastSave >= (CO.SECONDS_BETWEEN_AUTO_SAVES * CD.FRAME_RATE):
        save ()
        ticksSinceLastSave = 0
    ticksSinceLastSave += 1
