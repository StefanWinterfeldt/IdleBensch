from engine.controller.upgradeObjects.upgrade import Upgrade
import os


testUpgrade1 = Upgrade (
    os.path.join ('resources', 'ingame', 'upgrade', 'defaultUpgrade.png'),
    'Upgrade1',
    lambda : False
)

testUpgrade2 = Upgrade (
    os.path.join ('resources', 'ingame', 'upgrade', 'defaultUpgrade.png'),
    'Upgrade2',
    lambda : False
)

testUpgrade3 = Upgrade (
    os.path.join ('resources', 'ingame', 'upgrade', 'defaultUpgrade.png'),
    'Upgrade3',
    lambda : False
)
