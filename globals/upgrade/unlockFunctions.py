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

from globals.upgrade.annotatedFunction import AnnotatedFunction
import engine.util.upgrade

def allTheseUpgradesAreActive (upgradeIds):
    requiredUpgrades = [engine.util.upgrade.getUpgradeById (upgradeId) for upgradeId in upgradeIds]
    state = True
    for upgrade in requiredUpgrades:
        state = state and upgrade.active
    return state

def getTextRequiringUpgrades (upgradeIds):
    upgradeNames = [engine.util.upgrade.getUpgradeById(upgradeId).name for upgradeId in upgradeIds]
    return 'Dieses Upgrade benoetigt die folgenden anderen Upgrades: ' + ', '.join (upgradeNames) + '.'

def getAlwaysUnlockedFunction ():
    return AnnotatedFunction (
        text = None,
        function = lambda x: True,
        parameter = None
    )

def getUnlockFunctionRequiringActiveUpgrades (upgradeIds):
    return AnnotatedFunction (
        textFunction = getTextRequiringUpgrades,
        function = allTheseUpgradesAreActive,
        parameter = upgradeIds
    )
