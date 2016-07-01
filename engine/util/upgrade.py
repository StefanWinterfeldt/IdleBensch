import globals.upgrade.categories

def getAllUpgrades ():
    allUpgrades = []
    for category in globals.upgrade.categories.categories:
        allUpgrades += category.upgrades
    return allUpgrades

def getUpgradeById (upgradeId):
    matchingUpgrades = [upgrade for upgrade in getAllUpgrades() if upgrade.id == upgradeId]
    if len(matchingUpgrades) == 1:
        return matchingUpgrades[0]
    else:
        return None