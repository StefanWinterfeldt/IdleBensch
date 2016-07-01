from globals.upgrade.annotatedFunction import AnnotatedFunction
import engine.util.upgrade as upgradeUtil

def allTheseUpgradesAreActive (upgradeIds):
    requiredUpgrades = [upgradeUtil.getUpgradeById (upgradeId) for upgradeId in upgradeIds]
    state = True
    for upgrade in requiredUpgrades:
        state = state and upgrade.active
    return state

def getAlwaysUnlockedFunction ():
    return AnnotatedFunction (
        text = None,
        function = lambda x: True,
        parameter = None
    )

def getUnlockFunctionRequiringActiveUpgrades (upgradeIds):
    return AnnotatedFunction (
        text = 'Dieses Upgrade benoetigt noch andere Upgrades.',
        function = allTheseUpgradesAreActive,
        parameter = upgradeIds
    )
