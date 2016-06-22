from engine.controller.upgradeObjects.upgradeCategory import UpgradeCategory
import globals.upgrade.categoryHeaders as CH
import globals.upgrade.benschUpgrades as BU


benschCategory = UpgradeCategory (
    header = CH.benschHeader,
    upgrades = [
        BU.billigerEDrink,
        BU.fuenfKomma0,
        BU.normalerEDrink,
        BU.schwarzerKaffee,
        BU.unterbewusstesKlicken,
        BU.leibwaechter,
        BU.teurerEDrink,
        BU.logikKurs,
        BU.mrScotch,
        BU.matheKurs,
        BU.hamsterProgrammer,
        BU.extraHaende,
        BU.streamMod,
        BU.klon,
        BU.senorPopo,
        BU.drittesAuge
    ]
)

computerCategory = UpgradeCategory (
    header = CH.computerHeader,
    upgrades = []
)

categories = [benschCategory, computerCategory]
