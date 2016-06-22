from engine.controller.upgradeObjects.categoryHeader import CategoryHeader
import os


benschHeader = CategoryHeader (
    imagePath = os.path.join ('resources', 'ingame', 'upgrade', 'bensch', 'benschHeader.png'),
    hintText = 'Bensch Upgrades'
)

computerHeader = CategoryHeader (
    imagePath = os.path.join ('resources', 'ingame', 'upgrade', 'computer', 'computerHeader.png'),
    hintText = 'Computer Upgrades'
)