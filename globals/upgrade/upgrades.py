from engine.controller.upgradeObjects.upgrade import Upgrade
import os

def upgrade1Activation ():
    print 'test1'

def upgrade2Activation ():
    print 'test2'

def upgrade3Activation ():
    print 'test3'

testUpgrade1 = Upgrade (
    os.path.join ('resources', 'ingame', 'upgrade', 'defaultUpgrade.png'),
    'Upgrade1',
    lambda : True,
    lambda : True,
    upgrade1Activation
)

testUpgrade2 = Upgrade (
    os.path.join ('resources', 'ingame', 'upgrade', 'defaultUpgrade.png'),
    'Upgrade2',
    lambda : True,
    lambda : testUpgrade1.active,
    upgrade2Activation
)

testUpgrade3 = Upgrade (
    os.path.join ('resources', 'ingame', 'upgrade', 'defaultUpgrade.png'),
    'Upgrade3',
    lambda : True,
    lambda : testUpgrade2.active,
    upgrade3Activation
)
