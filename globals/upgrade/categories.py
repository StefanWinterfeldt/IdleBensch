from engine.controller.upgradeObjects.upgradeCategory import UpgradeCategory
import globals.upgrade.benschUpgrades as BU
import globals.upgrade.categoryHeaders as CH
import globals.upgrade.computerUpgrades as CU
import globals.upgrade.merchUpgrades as MU
import globals.upgrade.occultUpgrades as OU
import globals.upgrade.techUpgrades as TU


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
        # BU.hamsterProgrammer,
        # BU.extraHaende,
        # BU.streamMod,
        # BU.klon,
        # BU.senorPopo,
        # BU.drittesAuge
    ]
)

computerCategory = UpgradeCategory (
    header = CH.computerHeader,
    upgrades = [
        CU.schulPC,
        CU.modem56K,
        CU.anrufbeantworter,
        CU.schlechteKamera,
        CU.ergoMaus,
        CU.normalPC,
        # CU.modemDSL,
        # CU.hdKamera,
        # CU.ultraTastatur,
        # CU.highEndPC,
        # CU.satellitModem,
        # CU.brainInAJar,
        # CU.holoKamera,
        # CU.glasfaser,
        # CU.brainInterface,
        # CU.quantumComputer
    ]
)

merchCategory = UpgradeCategory (
    header = CH.merchHeader,
    upgrades = [
        # MU.shirt,
        # MU.tasse,
        # MU.arschPad,
        # MU.bier,
        # MU.film1,
        # MU.eauDeBensch,
        # MU.bart,
        # MU.musicAlbum,
        # MU.schnapps,
        # MU.actionFigur,
        # MU.hoerspiel,
        # MU.roman,
        # MU.film2,
        # MU.modeLabel,
        # MU.oper,
        # MU.realDoll
    ]
)

techCategory = UpgradeCategory (
    header = CH.techHeader,
    upgrades = [
        # TU.kaffeeMaschine,
        # TU.catTV,
        # TU.unterbewussteBotschaften,
        # TU.riesenLaser,
        # TU.roboBensch,
        # TU.seti,
        # TU.kiPsychologie,
        # TU.dnaMutation,
        # TU.dysonSphere,
        # TU.ftlTransmission,
        # TU.timeTravel,
        # TU.tesseract,
        # TU.parallelRealities,
        # TU.omnipresentBroadcast,
        # TU.metaTheory,
        # TU.idleBensch
    ]
)

occultCategory = UpgradeCategory (
    header = CH.occultHeader,
    upgrades = [
        # OU.zombiePact,
        # OU.ghostPact,
        # OU.golemPact,
        # OU.bloodPact,
        # OU.slimePact,
        # OU.moonPact,
        # OU.demonPact,
        # OU.krakenPact,
        # OU.angelPact,
        # OU.dragonPact,
        # OU.sandWormPact,
        # OU.deathPact,
        # OU.cookiePact,
        # OU.tentaclePact,
        # OU.elderPact,
        # OU.forbiddenKnowledge
    ]
)

categories = [
    benschCategory,
    computerCategory,
    # merchCategory,
    # techCategory,
    # occultCategory
]
