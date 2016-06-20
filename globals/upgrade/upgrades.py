from engine.controller.upgradeObjects.upgrade import Upgrade
import os

def upgrade1Activation ():
    print 'test1'

testUpgrade1 = Upgrade (
    os.path.join ('resources', 'ingame', 'upgrade', 'defaultUpgrade.png'),
    'Upgrade1',
    lambda: True,
    lambda: True,
    upgrade1Activation
)
