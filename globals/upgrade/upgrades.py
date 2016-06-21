from engine.controller.upgradeObjects.upgrade import Upgrade
import globals.upgrade.activationFunctions as AF
import globals.upgrade.unlockFunctions as UF
import os


billigerEDrink = Upgrade (
    name = 'Billiger E-Drink',
    cost = 0.29,
    hintText = ['Guenstiger kommst du nicht an Koffein.'],
    imagePath = os.path.join ('resources', 'ingame', 'upgrade', 'billigerEDrink.png'),
    visibilityFunction = lambda: True,
    unlockFunction = UF.getAlwaysUnlockedFunction (),
    activationFunction = AF.getIncreaseEpisodesPerClickByPercentageFunction (100)
)
