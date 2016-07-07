from engine.controller.saveObjects.saveGame import SaveGame
import engine.controller.clickViewController as clickViewController
import engine.controller.gameStateTriggerController as gameStateTriggerController
import engine.controller.passiveIncome as passiveIncomeController
import engine.controller.timeSlotController as timeSlotController
import engine.util.upgrade as upgradeUtil
import globals.gameLogic as GL
import globals.gameState as GS
import os
import pickle

ticksSinceLastSave = 0

def writeGameState(saveGame):
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
    saveGame.activeUpgradeIds = [upgrade.id for upgrade in upgradeUtil.getAllUpgrades() if upgrade.active]

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
    saveGame = createSaveGame()
    saveFile = open ('saveGames/game.sav', 'wb')
    pickle.dump (saveGame, saveFile, pickle.HIGHEST_PROTOCOL)
    saveFile.close ()

