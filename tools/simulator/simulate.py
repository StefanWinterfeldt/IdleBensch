import constants.display as CD
import engine.controller.clickViewController as clickViewController
import engine.controller.gameStateTriggerController as gameStateTriggerController
import engine.controller.passiveIncome as passiveIncomeController
import engine.controller.timeSlotController as timeSlotController
import engine.controller.upgradeViewController as upgradeViewController
import engine.util.text as textUtil
import globals.gameState as GS
import globals.upgrade.categories as categories
import numpy
import random


USER_CLICKS_PER_SECOND = 3

accumulatedUserClicks = 0
buyLogs = []
tickCount = 0

def analyze ():
    print '---'
    distancesBetweenUpgrades = []
    lastTicks = 0
    for log in buyLogs:
        print 'Upgrade: ' + log ['name'] + ' bought at ' + getTimeString (log ['ticks'])
        distancesBetweenUpgrades.append (log ['ticks'] - lastTicks)
        lastTicks = log ['ticks']
    median = int (numpy.median (distancesBetweenUpgrades))
    std = numpy.std (distancesBetweenUpgrades)
    print '---'
    print 'Overall time taken: ' + getTimeString (buyLogs [-1] ['ticks'])
    print 'Median time between upgrades: ' + getTimeString (median)
    print 'Standard deviation: ' + str (std)

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
    return textUtil.convertToHumanReadableString (percentage, True) + '% ' + getCurrentTimeString ()

def mockUnneededFunctionality ():
    upgradeViewController.drawCategories = lambda: None

def refreshCategoryVisibility ():
    for category in categories.categories:
        upgradeViewController.refreshUpgradeVisibility (category)

def moreUpgradesAvailable ():
    return len (getAvailableUpgrades ()) != 0

def getAvailableUpgrades ():
    availableUpgrades = [upgrade for upgrade in getAllUpgrades () if upgrade.active == False and upgrade.visible and upgrade.isUnlocked ()]
    return availableUpgrades

def getTimeString (ticks):
    seconds = ticks / CD.FRAME_RATE
    minutes = seconds / 60
    hours = minutes / 60
    return str (ticks) + ' Ticks - ' + str (hours) + ' Hours ' + str (minutes) + ' Minutes ' + str (seconds) + ' Seconds'

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
        upgradeToBeBought = random.choice (affordableUpgrades)
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
    analyze ()

prepareSimulation ()
simulate ()
