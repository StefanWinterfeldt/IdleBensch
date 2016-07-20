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

import math

import engine.controller.timeSlotController as timeSlotController
import engine.service.modifiedGameLogic as modifiedGameLogic
import globals.gameState as GGS


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

def initialize ():
    pass

def update ():
    checkEpisodes ()
    checkSeasons ()
    checkViews ()
