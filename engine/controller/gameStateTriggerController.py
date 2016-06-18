import engine.controller.timeSlotController as timeSlotController
import globals.gameState as GGS
import math


lastFullEpisodes = 0

def checkEpisodes ():
    global lastFullEpisodes
    currentFullEpisodes = int (math.floor (GGS.episodes))
    if lastFullEpisodes != currentFullEpisodes:
        timeSlotController.handleNewEpisodes (currentFullEpisodes - lastFullEpisodes)
        lastFullEpisodes = currentFullEpisodes

def update ():
    checkEpisodes ()
