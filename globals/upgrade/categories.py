from engine.controller.upgradeObjects.upgradeCategory import UpgradeCategory
import globals.upgrade.categoryHeaders as CH
import globals.upgrade.upgrades as U


benschCategory = UpgradeCategory (CH.benschHeader, [U.testUpgrade1])

categories = [benschCategory]
