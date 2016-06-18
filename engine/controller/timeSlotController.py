import constants.gameLogic as CGL
from engine.controller.timeObjects.timedAction import TimedAction
from engine.controller.timeObjects.timeSlot import TimeSlot
import engine.service.modifiedGameLogic as modifiedGameLogic
import globals.gameState as GGS
import random


timeSlots = []

def handleNewEpisodes (numberOfEpisodes):
    global timeSlots
    totalViewsToAllocate = modifiedGameLogic.getViewsPerEpisode ()
    totalSubscribersToAllocate = 0
    for i in range (numberOfEpisodes):
        totalSubscribersToAllocate += random.randint (CGL.BASE_MIN_SUBSCRIBERS_PER_EPISODE, CGL.BASE_MAX_SUBSCRIBERS_PER_EPISODE)
    viewsPerSlot = totalViewsToAllocate / float (CGL.BASE_TICKS_TO_PROCESS_EPISODE)
    subscribersPerSlot = totalSubscribersToAllocate / float (CGL.BASE_TICKS_TO_PROCESS_EPISODE)
    prepareTimeSlotsForFutureTicks (CGL.BASE_TICKS_TO_PROCESS_EPISODE)
    for i in range (CGL.BASE_TICKS_TO_PROCESS_EPISODE):
        timeSlots [i].addAction (TimedAction (increaseViews, viewsPerSlot))
        timeSlots [i].addAction (TimedAction (increaseSubscribers, subscribersPerSlot))

def handleNewSeasons (numberOfSeasons):
    global timeSlots
    totalSubscribersToAllocate = 0
    for i in range (numberOfSeasons):
        totalSubscribersToAllocate += random.randint (CGL.BASE_MIN_SUBSCRIBERS_PER_SEASON, CGL.BASE_MAX_SUBSCRIBERS_PER_SEASON)
    subscribersPerSlot = totalSubscribersToAllocate / float (CGL.BASE_TICKS_TO_PROCESS_SEASON)
    prepareTimeSlotsForFutureTicks (CGL.BASE_TICKS_TO_PROCESS_SEASON)
    for i in range (CGL.BASE_TICKS_TO_PROCESS_SEASON):
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
