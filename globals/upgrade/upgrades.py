from engine.controller.upgradeObjects.upgrade import Upgrade
import globals.upgrade.activationFunctions as AF
import os


billigerEDrink = Upgrade (
    'Billiger E-Drink',
    0.29,
    ['Du erzeugst doppelt so viele Folgen pro Klick.', 'Guenstiger kommst du nicht an Koffein.'],
    os.path.join ('resources', 'ingame', 'upgrade', 'defaultUpgrade.png'),
    lambda: True,
    lambda: True,
    activationFunction = AF.doubleEpisodesPerClick
)
