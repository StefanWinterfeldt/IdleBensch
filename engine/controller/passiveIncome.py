import engine.controller.clickViewController as clickViewController
import engine.service.modifiedGameLogic as MGL
import globals.gameState as GS
import math
import random


currentAutoClicks = 0
currentSubscribers = 0

def processMerchPurchases ():
    purchasesThisTick = 0
    purchaseAmount = 0
    for i in range (int (GS.subscriber)):
        if random.random () < MGL.getPurchaseChancePerSubscriberPerTick ():
            purchasesThisTick += 1
    for i in range (purchasesThisTick):
        purchaseCents = random.randint (math.floor (MGL.getMinPurchase () * 100), math.floor (MGL.getMaxPurchase () * 100))
        purchaseAmount += (purchaseCents * 0.01)
    GS.money += purchaseAmount

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

def processAutoClicks ():
    global currentAutoClicks
    currentAutoClicks += MGL.getClicksPerTick ()
    if currentAutoClicks >= 1:
        newClicks = int (currentAutoClicks)
        for i in range (newClicks):
            clickViewController.handleClick (None)
        currentAutoClicks -= newClicks

def initialize ():
    pass

def update ():
    processAutoClicks ()
    processSubscriberIncrease ()
    processDonations ()
    processMerchPurchases ()
