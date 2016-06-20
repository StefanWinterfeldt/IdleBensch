import constants.gameLogic as CGL
import engine.controller.timeSlotController as timeSlotController
import engine.service.modifiedGameLogic as modifiedGameLogic
import globals.gameState as GGS
import math


lastFullEpisodes = 0
lastFullSeasons = 0
lastFullViews = 0

def checkEpisodes ():
    global lastFullEpisodes
    if lastFullEpisodes != GGS.episodes:
        timeSlotController.handleNewEpisodes (GGS.episodes - lastFullEpisodes)
        lastFullEpisodes = GGS.episodes

def checkSeasons ():
    global lastFullSeasons
    if lastFullSeasons != GGS.seasons:
        timeSlotController.handleNewSeasons (GGS.seasons - lastFullSeasons)
        lastFullSeasons = GGS.seasons

def checkViews ():
    global lastFullViews
    currentFullViews = int (math.floor (GGS.views))
    if currentFullViews != lastFullViews:
        GGS.money += modifiedGameLogic.getMoneyPerView () * (currentFullViews - lastFullViews)
        lastFullViews = currentFullViews

# ToDo: Remember to set last values when loading a save game
def initialize ():
    pass

def update ():
    checkEpisodes ()
    checkSeasons ()
    checkViews ()
