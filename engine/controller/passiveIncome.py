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
    purchaseChance = MGL.getPurchaseChancePerSubscriberPerSecond ()
    if purchaseChance != 0:
        purchases = GS.subscriber * purchaseChance
        purchaseCents = random.randint (math.floor (MGL.getMinPurchase () * 100), math.floor (MGL.getMaxPurchase () * 100))
        purchaseAmount = (purchaseCents * 0.01) * purchases
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
