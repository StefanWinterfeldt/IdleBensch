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

import random

import engine.service.modifiedGameLogic as modifiedGameLogic
import globals.gameState as GGS
from engine.controller.timeObjects.timeSlot import TimeSlot
from engine.controller.timeObjects.timedAction import TimedAction


timeSlots = []

def handleNewEpisodes (numberOfEpisodes):
    global timeSlots
    totalViewsToAllocate = modifiedGameLogic.getViewsPerEpisode () * numberOfEpisodes
    totalSubscribersToAllocate = 0
    for i in range (numberOfEpisodes):
        totalSubscribersToAllocate += random.randint (modifiedGameLogic.getMinSubscribersPerEpisode (), modifiedGameLogic.getMaxSubscribersPerEpisode ())
    viewsPerSlot = totalViewsToAllocate / float (modifiedGameLogic.getTicksToProcessEpisode ())
    subscribersPerSlot = totalSubscribersToAllocate / float (modifiedGameLogic.getTicksToProcessEpisode ())
    prepareTimeSlotsForFutureTicks (modifiedGameLogic.getTicksToProcessEpisode ())
    for i in range (modifiedGameLogic.getTicksToProcessEpisode ()):
        timeSlots [i].addAction (TimedAction (increaseViews, viewsPerSlot))
        timeSlots [i].addAction (TimedAction (increaseSubscribers, subscribersPerSlot))

def handleNewSeasons (numberOfSeasons):
    global timeSlots
    totalSubscribersToAllocate = 0
    for i in range (numberOfSeasons):
        totalSubscribersToAllocate += random.randint (modifiedGameLogic.getMinSubscribersPerSeason (), modifiedGameLogic.getMaxSubscribersPerSeason ())
    subscribersPerSlot = totalSubscribersToAllocate / float (modifiedGameLogic.getTicksToProcessSeason ())
    prepareTimeSlotsForFutureTicks (modifiedGameLogic.getTicksToProcessSeason ())
    for i in range (modifiedGameLogic.getTicksToProcessSeason ()):
        timeSlots [i].addAction (TimedAction (increaseSubscribers, subscribersPerSlot))

def initialize ():
    pass

def increaseSubscribers (number):
    GGS.subscriber += number

def increaseViews (number):
    GGS.views += number

def prepareTimeSlotsForFutureTicks (ticks):
    global timeSlots
    slotsToBeCreated = ticks - len (timeSlots)
    if slotsToBeCreated > 0:
        for i in range (slotsToBeCreated):
            timeSlots.append (TimeSlot ())

def update ():
    global timeSlots
    if len (timeSlots) > 0: timeSlots.pop (0).executeActions ()
