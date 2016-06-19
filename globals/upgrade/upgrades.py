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
    upgrade1Activation,
    lambda : True
)

testUpgrade2 = Upgrade (
    os.path.join ('resources', 'ingame', 'upgrade', 'defaultUpgrade.png'),
    'Upgrade2',
    lambda : testUpgrade1.active,
    upgrade2Activation,
    lambda : True
)

testUpgrade3 = Upgrade (
    os.path.join ('resources', 'ingame', 'upgrade', 'defaultUpgrade.png'),
    'Upgrade3',
    lambda : testUpgrade2.active,
    upgrade3Activation,
    lambda : True
)
