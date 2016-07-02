from globals.upgrade.annotatedFunction import AnnotatedFunction
import engine.util.upgrade as upgradeUtil

def allTheseUpgradesAreActive (upgradeIds):
    requiredUpgrades = [upgradeUtil.getUpgradeById (upgradeId) for upgradeId in upgradeIds]
    state = True
    for upgrade in requiredUpgrades:
        state = state and upgrade.active
    return state

def getTextRequiringUpgrades (upgradeIds):
    upgradeNames = [upgradeUtil.getUpgradeById(upgradeId).name for upgradeId in upgradeIds]
    return 'Dieses Upgrade benoetigt noch die folgenden anderen Upgrades: ' + ', '.join (upgradeNames) + '.'

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
