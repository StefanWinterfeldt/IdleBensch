import engine.service.modifiedGameLogic as MGL
import globals.gameState as GS
import math
import random


currentSubscribers = 0

def processDonations ():
    donationsThisTick = 0
    donationAmount = 0
    for i in range (GS.streams):
        if random.random () < MGL.getDonationChancePerStreamPerTick ():
            donationsThisTick += 1
    for i in range (donationsThisTick):
        donatedCents = random.randint (math.floor (MGL.getMinDonation () * 100), math.floor (MGL.getMaxDonation () * 100))
        donationAmount += (donatedCents * 0.01)
    GS.money += donationAmount

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
    processDonations ()
