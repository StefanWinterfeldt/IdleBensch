from engine.controller.upgradeObjects.categoryHeader import CategoryHeader
import os


benschHeader = CategoryHeader (
    imagePath = os.path.join ('resources', 'ingame', 'upgrade', 'bensch', 'benschHeader.png'),
    hintText = 'Selbstverbesserung durch Konsum! Das sind die Bensch Upgrades.',
    visible = True
)

computerHeader = CategoryHeader (
    imagePath = os.path.join ('resources', 'ingame', 'upgrade', 'computer', 'computerHeader.png'),
    hintText = 'Stecke Geld in deinen Computer - es wird ihn schneller machen!'
)

merchHeader = CategoryHeader (
    imagePath = os.path.join ('resources', 'ingame', 'upgrade', 'merch', 'merchHeader.png'),
    hintText = 'Merchandise! Kauf meinen Scheiss!'
)

occultHeader = CategoryHeader (
    imagePath = os.path.join ('resources', 'ingame', 'upgrade', 'occult', 'occultHeader.png'),
    hintText = 'Das Okkulte - schliesse Vertraege mit den Wesen der Unterwelt und erweitere deine Fanbase.'
)

techHeader = CategoryHeader (
    imagePath = os.path.join ('resources', 'ingame', 'upgrade', 'tech', 'techHeader.png'),
    hintText = 'Der grosse Spass fuer Langweiler! Bauen Sie sich ihr eigenes Vogelhaeuschen!'
)
