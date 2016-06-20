import constants.gameLogic as CGL
from engine.controller.timeObjects.timedAction import TimedAction
from engine.controller.timeObjects.timeSlot import TimeSlot
import engine.service.modifiedGameLogic as modifiedGameLogic
import globals.gameState as GGS
import random


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
