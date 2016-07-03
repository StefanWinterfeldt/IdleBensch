import globals.upgrade.categories

def makeAllUpgradesVisible ():
    for header in getAllUpgradeHeaders ():
        header.visible = True
    for upgrade in getAllUpgrades ():
        upgrade.visible = True

def setAllCostsToZero ():
    for upgrade in getAllUpgrades():
        upgrade.cost = 0.0

def getAllUpgradeHeaders ():
    return [category.header for category in globals.upgrade.categories.categories]

def getAllUpgrades ():
    allUpgrades = []
    for category in globals.upgrade.categories.categories:
        allUpgrades += category.upgrades
    return allUpgrades

def getUpgradeById (upgradeId):
    matchingUpgrades = [upgrade for upgrade in getAllUpgrades () if upgrade.id == upgradeId]
    if len (matchingUpgrades) == 1:
        return matchingUpgrades [0]
    else:
        return None
