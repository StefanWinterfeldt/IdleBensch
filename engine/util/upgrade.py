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
