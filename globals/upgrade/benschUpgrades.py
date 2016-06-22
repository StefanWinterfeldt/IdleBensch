from engine.controller.upgradeObjects.upgrade import Upgrade
import globals.upgrade.activationFunctions as AF
import globals.upgrade.unlockFunctions as UF
import os


billigerEDrink = Upgrade (
    name = 'Billiger E-Drink',
    cost = 0.09,
    hintText = ['Schmeckt nach Klebstoff. Weil welcher drin ist'],
    imagePath = os.path.join ('resources', 'ingame', 'upgrade', 'bensch', 'billigerEDrink.png'),
    unlockFunction = UF.getAlwaysUnlockedFunction (),
    activationFunction = AF.getIncreaseEpisodesPerClickByPercentageFunction (20)
)

normalerEDrink = Upgrade (
    name = 'Standard E-Drink',
    cost = 0.99,
    hintText = ['Bekannt aus jeder Tankstelle.'],
    imagePath = os.path.join ('resources', 'ingame', 'upgrade', 'bensch', 'normalerEDrink.png'),
    unlockFunction = UF.getAlwaysUnlockedFunction (),
    activationFunction = AF.getIncreaseEpisodesPerClickByPercentageFunction (30)
)

teurerEDrink = Upgrade (
    name = 'Premium E-Drink',
    cost = 3.99,
    hintText = ['Er hat ein Bild von nem C-Promi auf der Rueckseite'],
    imagePath = os.path.join ('resources', 'ingame', 'upgrade', 'bensch', 'teurerEDrink.png'),
    unlockFunction = UF.getAlwaysUnlockedFunction (),
    activationFunction = AF.getIncreaseEpisodesPerClickByPercentageFunction (40)
)

fuenfKomma0 = Upgrade (
    name = '5,0',
    cost = 0.49,
    hintText = ['Das Universalbier, macht gluecklich und loest die Zunge.'],
    imagePath = os.path.join ('resources', 'ingame', 'upgrade', 'bensch', '5komma0.png'),
    unlockFunction = UF.getAlwaysUnlockedFunction (),
    activationFunction = AF.getIncreaseMaxSubscribersPerEpisode(1)
)