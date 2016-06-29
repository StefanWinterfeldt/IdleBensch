import engine.service.modifiedGameLogic as MGL
import globals.gameState as GS
import math


currentSubscribers = 0

def processSubscriberIncrease ():
    global currentSubscribers
    currentSubscribers += MGL.getSubscribersPerTick ()
    if currentSubscribers >= 1:
        newSubscribers = math.floor (currentSubscribers)
        GS.subscriber += newSubscribers
        currentSubscribers -= newSubscribers

def initialize ():
    pass

def update ():
    processSubscriberIncrease ()
