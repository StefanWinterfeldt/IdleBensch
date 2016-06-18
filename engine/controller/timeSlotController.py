import constants.gameLogic as CGL
from engine.controller.timeObjects.timedAction import TimedAction
from engine.controller.timeObjects.timeSlot import TimeSlot
import globals.gameState as GGS


timeSlots = []

def handleNewEpisodes (numberOfEpisodes):
    global timeSlots
    totalViewsToAllocate = numberOfEpisodes * CGL.BASE_VIEWS_PER_EPISODE
    viewsPerSlot = totalViewsToAllocate / float (CGL.BASE_TICKS_TO_PROCESS_EPISODE)
    prepareTimeSlotsForFutureTicks (CGL.BASE_TICKS_TO_PROCESS_EPISODE)
    for i in range (CGL.BASE_TICKS_TO_PROCESS_EPISODE):
        timeSlots [i].addAction (TimedAction (increaseViews, viewsPerSlot))

def initialize ():
    pass

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
