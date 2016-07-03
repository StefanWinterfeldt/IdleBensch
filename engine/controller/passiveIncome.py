import constants.display as CD
import engine.controller.clickViewController as clickViewController
import engine.service.modifiedGameLogic as MGL
import globals.gameState as GS
import math
import random

ticksSinceLastProcess = 0
currentAutoClicks = 0
currentSubscribers = 0

def processMerchPurchases ():
    purchases = 0
    purchaseAmount = 0
    purchaseChance = MGL.getPurchaseChancePerSubscriberPerSecond ()
    for i in range (int (GS.subscriber)):
        if random.random () < purchaseChance:
            purchases += 1
    for i in range (purchases):
        purchaseCents = random.randint (math.floor (MGL.getMinPurchase () * 100), math.floor (MGL.getMaxPurchase () * 100))
        purchaseAmount += (purchaseCents * 0.01)
    GS.money += purchaseAmount

def processDonations ():
    donations = 0
    donationAmount = 0
    donationChance = MGL.getDonationChancePerStreamPerSecond ()
    for i in range (GS.streams):
        if random.random () < donationChance:
            donations += 1
    for i in range (donations):
        donatedCents = random.randint (math.floor (MGL.getMinDonation () * 100), math.floor (MGL.getMaxDonation () * 100))
        donationAmount += (donatedCents * 0.01)
    GS.money += donationAmount

def processSubscriberIncrease ():
    global currentSubscribers
    currentSubscribers += MGL.getSubscribersPerSecond ()
    if currentSubscribers >= 1:
        newSubscribers = math.floor (currentSubscribers)
        GS.subscriber += newSubscribers
        currentSubscribers -= newSubscribers

def processAutoClicks ():
    global currentAutoClicks
    currentAutoClicks += MGL.getClicksPerSecond ()
    if currentAutoClicks >= 1:
        newClicks = int (currentAutoClicks)
        for i in range (newClicks):
            clickViewController.handleClick (None)
        currentAutoClicks -= newClicks

def initialize ():
    pass

def update ():
    global ticksSinceLastProcess
    ticksSinceLastProcess += 1
    ticksSinceLastProcess %= CD.FRAME_RATE
    if ticksSinceLastProcess == 0:
        processAutoClicks ()
        processSubscriberIncrease ()
        processDonations ()
        processMerchPurchases ()
