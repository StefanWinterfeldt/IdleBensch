from engine.controller.upgradeObjects.upgradeCategory import UpgradeCategory
import globals.upgrade.categoryHeaders as CH
import globals.upgrade.benschUpgrades as BU


benschCategory = UpgradeCategory (CH.benschHeader, [BU.billigerEDrink])

categories = [benschCategory]
