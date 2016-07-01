import constants.display as CD
import engine.controller.clickViewController as clickViewController
import engine.controller.gameStateTriggerController as gameStateTriggerController
import engine.controller.passiveIncome as passiveIncomeController
import engine.controller.timeSlotController as timeSlotController
import engine.controller.upgradeViewController as upgradeViewController
import engine.util.text as textUtil
import globals.gameState as GS
import globals.upgrade.categories as categories
import random


USER_CLICKS_PER_SECOND = 3

accumulatedUserClicks = 0
tickCount = 0

def mockUnneededFunctionality ():
    upgradeViewController.drawCategories = lambda : None

def refreshCategoryVisibility ():
    for category in categories.categories:
        upgradeViewController.refreshUpgradeVisibility (category)

def moreUpgradesAvailable ():
    return len (getAvailableUpgrades ()) != 0

def getAvailableUpgrades ():
    allUpgrades = []
    for category in categories.categories:
        allUpgrades += category.upgrades
    availableUpgrades = [upgrade for upgrade in allUpgrades if upgrade.active == False and upgrade.visible and upgrade.isUnlocked ()]
    return availableUpgrades

def printStatus ():
    seconds = tickCount / CD.FRAME_RATE
    minutes = seconds / 60
    hours = minutes / 60
    print 'Time: ' + str (tickCount) + ' Ticks - ' + str (hours) + ' Hours ' + str (minutes) + ' Minutes ' + str (seconds) + ' Seconds'
    print 'Money: ' + textUtil.convertToHumanReadableString(GS.money) + ' Euro'

def getUserClicksPerTick ():
    return USER_CLICKS_PER_SECOND / float (CD.FRAME_RATE)

def prepareSimulation ():
    random.seed ()
    mockUnneededFunctionality()
    refreshCategoryVisibility ()

def buyUpgradeIfPossible ():
    affordableUpgrades = [upgrade for upgrade in getAvailableUpgrades () if upgrade.cost <= GS.money]
    if len (affordableUpgrades) > 0:
        upgradeToBeBought = random.choice (affordableUpgrades)
        upgradeViewController.handleClickOnUpgrade (upgradeToBeBought)
        refreshCategoryVisibility ()
        print 'Bought Upgrade: ' + upgradeToBeBought.name
        printStatus ()

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

prepareSimulation ()
simulate ()
