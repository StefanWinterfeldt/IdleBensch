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
import engine.controller.gameStateTriggerController as gameStateTriggerController
import engine.controller.passiveIncome as passiveIncomeController
import engine.controller.timeSlotController as timeSlotController
import engine.controller.upgradeViewController as upgradeViewController
import engine.controller.endingController as endingController
import engine.util.text as textUtil
import globals.gameState as GS
import globals.upgrade.categories as categories
import numpy
import random


USER_CLICKS_PER_SECOND = 4

accumulatedUserClicks = 0
buyLogs = []
tickCount = 0

def analyze ():
    print '---'
    distancesBetweenUpgrades = []
    lastTicks = 0
    for log in buyLogs:
        print 'Upgrade:             ' + log ['name']
        print 'Bought at:           ' + getTimeString (log ['ticks'])
        ticksSinceLastBuy = log ['ticks'] - lastTicks
        print 'Time since last buy: ' + getTimeString (ticksSinceLastBuy)
        print ''
        distancesBetweenUpgrades.append (ticksSinceLastBuy)
        lastTicks = log ['ticks']
    minimum = int (min (distancesBetweenUpgrades))
    maximum = int (max (distancesBetweenUpgrades))
    mean = int (numpy.mean (distancesBetweenUpgrades))
    median = int (numpy.median (distancesBetweenUpgrades))
    std = numpy.std (distancesBetweenUpgrades)
    print '---'
    print 'Overall time taken:           ' + getTimeString (buyLogs [-1] ['ticks'])
    print 'Min time between upgrades:    ' + getTimeString (minimum)
    print 'Max time between upgrades:    ' + getTimeString (maximum)
    print 'Mean time between upgrades:   ' + getTimeString (mean)
    print 'Median time between upgrades: ' + getTimeString (median)
    print 'Standard deviation:           ' + str (std)
    print 'Views:                        ' + str (GS.views)
    print 'Subscribers:                  ' + str (GS.subscriber)

def addBuyLog (upgradeName):
    global buyLogs
    buyLogs.append ({'name': upgradeName, 'ticks': tickCount})

def getNumberOfActiveUpgrades ():
    return len ([upgrade for upgrade in getAllUpgrades () if upgrade.active])

def getNumberOfUpgrades ():
    return len (getAllUpgrades ())

def getAllUpgrades ():
    allUpgrades = []
    for category in categories.categories:
        allUpgrades += category.upgrades
    return allUpgrades

def getCompletionPercentage ():
    percentage = 100.0 / getNumberOfUpgrades () * getNumberOfActiveUpgrades ()
    return 'Completion: ' + textUtil.convertToHumanReadableString (percentage, True) + '% ' + getCurrentTimeString ()

def mockUnneededFunctionality ():
    clickViewController.randomize = lambda: None
    upgradeViewController.drawCategories = lambda: None
    endingController.activateEnding = lambda: None

def refreshCategoryVisibility ():
    for category in categories.categories:
        upgradeViewController.refreshUpgradeVisibility (category)

def moreUpgradesAvailable ():
    return len (getAvailableUpgrades ()) != 0

def getAvailableUpgrades ():
    availableUpgrades = [upgrade for upgrade in getAllUpgrades () if upgrade.active == False and upgrade.visible and upgrade.isUnlocked ()]
    return availableUpgrades

def getTimeString (ticks):
    countedTicks = ticks
    hours = countedTicks / (60 * 60 * CD.FRAME_RATE)
    countedTicks -= (60 * 60 * CD.FRAME_RATE) * hours
    minutes = (countedTicks / (60 * CD.FRAME_RATE))
    countedTicks -= (60 * CD.FRAME_RATE) * minutes
    seconds = countedTicks / CD.FRAME_RATE
    return str (ticks) + ' Ticks - ' + str (hours) + ' Hours | ' + str (minutes) + ' Minutes | ' + str (seconds) + ' Seconds'

def getCurrentTimeString ():
    return getTimeString (tickCount)

def getUserClicksPerTick ():
    return USER_CLICKS_PER_SECOND / float (CD.FRAME_RATE)

def prepareSimulation ():
    random.seed ()
    mockUnneededFunctionality ()
    refreshCategoryVisibility ()

def buyUpgradeIfPossible ():
    affordableUpgrades = [upgrade for upgrade in getAvailableUpgrades () if upgrade.cost <= GS.money]
    if len (affordableUpgrades) > 0:
        minCost = min ([upgrade.cost for upgrade in affordableUpgrades])
        upgradeToBeBought = None
        for upgrade in affordableUpgrades:
            if upgrade.cost == minCost:
                upgradeToBeBought = upgrade
        upgradeViewController.handleClickOnUpgrade (upgradeToBeBought)
        refreshCategoryVisibility ()
        addBuyLog (upgradeToBeBought.name)
        print getCompletionPercentage ()

def handleSimulatedClicks ():
    global accumulatedUserClicks
    accumulatedUserClicks += getUserClicksPerTick ()
    if accumulatedUserClicks > 1:
        newClicks = int (accumulatedUserClicks)
        for i in range (newClicks): clickViewController.handleClick (None)
        accumulatedUserClicks -= newClicks

def printCurrentMoney ():
    print 'Money: ' + textUtil.convertToHumanReadableString (GS.money, True) + ' at ' + getCurrentTimeString ()

def tick ():
    global tickCount
    buyUpgradeIfPossible ()
    handleSimulatedClicks ()
    gameStateTriggerController.update ()
    passiveIncomeController.update ()
    timeSlotController.update ()
    tickCount += 1

def simulate ():
    while moreUpgradesAvailable ():
        tick ()
        # if tickCount % 1000 == 0:
        #     printCurrentMoney ()
    analyze ()

prepareSimulation ()
simulate ()
