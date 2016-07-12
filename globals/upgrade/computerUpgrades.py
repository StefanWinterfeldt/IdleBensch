from engine.controller.upgradeObjects.upgrade import Upgrade
import globals.upgrade.activationFunctions as AF
import globals.upgrade.unlockFunctions as UF
import os


modem56K = Upgrade (
    id = 17,
    name = '56k Modem',
    cost = 12.0,
    hintText = ['Endlich kannst du deinen Akustik-Koppler loswerden! Und Dubstep spielt es auch!'],
    imagePath = os.path.join ('resources', 'ingame', 'upgrade', 'computer', '56kModem.png'),
    unlockFunction = UF.getAlwaysUnlockedFunction (),
    activationFunction = AF.getIncreaseSubscriberViewsPerEpisodeByPercentage (50)
)

anrufbeantworter = Upgrade (
    id = 18,
    name = 'Anrufbeantworter',
    cost = 25.0,
    hintText = ['Niemand wird dich mehr beim Aufnehmen stoeren.'],
    imagePath = os.path.join ('resources', 'ingame', 'upgrade', 'computer', 'anrufbeantworter.png'),
    unlockFunction = UF.getAlwaysUnlockedFunction (),
    activationFunction = AF.getIncreaseMaxSubscribersPerEpisode (8)
)

brainInAJar = Upgrade (
    id = 19,
    name = 'Bio-Computer',
    cost = 95000.0,
    hintText = ['Ja, ich weiss dass es wie ne Suesskartoffel aussieht. Versuch du mal in Paint ein Gehirn zu malen.'],
    imagePath = os.path.join ('resources', 'ingame', 'upgrade', 'computer', 'brainInAJar.png'),
    unlockFunction = UF.getUnlockFunctionRequiringActiveUpgrades ([50]),
    activationFunction = AF.getIncreaseSubscriberViewsPerEpisodeByPercentage (100)
)

brainInterface = Upgrade (
    id = 20,
    name = 'Neurales Interface',
    cost = 1500000.0,
    hintText = ['Jetzt brauchst du deine laestigen Haende nicht mehr.'],
    imagePath = os.path.join ('resources', 'ingame', 'upgrade', 'computer', 'brainInterface.png'),
    unlockFunction = UF.getAlwaysUnlockedFunction (),
    activationFunction = AF.getIncreaseClicksPerSecondByPercentageFunction (100)
)

modemDSL = Upgrade (
    id = 21,
    name = 'DSL Modem',
    cost = 800.0,
    hintText = ['Garantiert bis zu 100K... zumindest zwischen 3:13 und 3:14 Uhr.'],
    imagePath = os.path.join ('resources', 'ingame', 'upgrade', 'computer', 'dslModem.png'),
    unlockFunction = UF.getAlwaysUnlockedFunction (),
    activationFunction = AF.getIncreaseSubscribersPerStreamPerSecondByPercentage (50)
)

ergoMaus = Upgrade (
    id = 22,
    name = 'Ergonomische Maus',
    cost = 70.0,
    hintText = ['Aus echtem Stierhodenleder. Keine Macht dem Karpaltunnel!'],
    imagePath = os.path.join ('resources', 'ingame', 'upgrade', 'computer', 'ergoMaus.png'),
    unlockFunction = UF.getAlwaysUnlockedFunction (),
    activationFunction = AF.getIncreaseEpisodesPerClickByPercentageFunction (50)
)

glasfaser = Upgrade (
    id = 23,
    name = 'Glasfaserverbindung',
    cost = 700000.0,
    hintText = ['Internet mit Lichtgeschwindigkeit, damit koenntest du Pornos so schnell gucken wie neue produziert werden...'],
    imagePath = os.path.join ('resources', 'ingame', 'upgrade', 'computer', 'glasfaser.png'),
    unlockFunction = UF.getAlwaysUnlockedFunction (),
    activationFunction = AF.getIncreaseMaxSubscribersPerEpisode (300)
)

hdKamera = Upgrade (
    id = 24,
    name = 'HD Kamera',
    cost = 1500.0,
    hintText = ['Jetzt kann man auch dein Gesicht erkennen, ob das so ne gute Idee war...'],
    imagePath = os.path.join ('resources', 'ingame', 'upgrade', 'computer', 'HDKamera.png'),
    unlockFunction = UF.getAlwaysUnlockedFunction (),
    activationFunction = AF.getIncreaseMaxSubscribersPerEpisode (50)
)

highEndPC = Upgrade (
    id = 25,
    name = 'High End PC',
    cost = 5000.0,
    hintText = ['Darauf lauft sogar deine Mutter fluessig.'],
    imagePath = os.path.join ('resources', 'ingame', 'upgrade', 'computer', 'highEndPC.png'),
    unlockFunction = UF.getAlwaysUnlockedFunction (),
    activationFunction = AF.getActivateTechCategory ()
)

holoKamera = Upgrade (
    id = 26,
    name = 'Holographische Kamera',
    cost = 150000.0,
    hintText = ['Mit dem richtigen Equipment koennen sich deine Zuschauer einen Lebensgrossen Holo-Bensch in ihr Wohnzimmer projizieren.'],
    imagePath = os.path.join ('resources', 'ingame', 'upgrade', 'computer', 'holoKamera.png'),
    unlockFunction = UF.getAlwaysUnlockedFunction (),
    activationFunction = AF.getIncreaseSubscriberViewsPerEpisodeByPercentage (100)
)

normalPC = Upgrade (
    id = 27,
    name = 'Normaler PC',
    cost = 250.0,
    hintText = ['Gebraucht und nix besonderes, aber auch nicht aus Presspappe.'],
    imagePath = os.path.join ('resources', 'ingame', 'upgrade', 'computer', 'normalPC.png'),
    unlockFunction = UF.getAlwaysUnlockedFunction (),
    activationFunction = AF.getActivateMerchCategory ()
)

quantumComputer = Upgrade (
    id = 28,
    name = 'Quantencomputer',
    cost = 300000000.0,
    hintText = ['2000 Jahre Forschung fuer... Quanten-IdleGames.'],
    imagePath = os.path.join ('resources', 'ingame', 'upgrade', 'computer', 'quantumComputer.png'),
    unlockFunction = UF.getAlwaysUnlockedFunction (),
    activationFunction = AF.getIncreaseClicksPerSecondByPercentageFunction (100)
)

satellitModem = Upgrade (
    id = 29,
    name = 'Satelliten-Uplink',
    cost = 30000.0,
    hintText = ['Selbst das Hubble-Teleskop kann dir jetzt zuschauen.'],
    imagePath = os.path.join ('resources', 'ingame', 'upgrade', 'computer', 'satellitModem.png'),
    unlockFunction = UF.getAlwaysUnlockedFunction (),
    activationFunction = AF.getIncreaseSubscribersPerStreamPerSecondByPercentage (70)
)

schlechteKamera = Upgrade (
    id = 30,
    name = 'Billige Kamera',
    cost = 50.0,
    hintText = ['Gabs gebraucht auf Ebay. Ein Blick auf die SD-Karte verraet warum sie so billig war...'],
    imagePath = os.path.join ('resources', 'ingame', 'upgrade', 'computer', 'schlechteKamera.png'),
    unlockFunction = UF.getAlwaysUnlockedFunction (),
    activationFunction = AF.getActivateStreamFunction ()
)

schulPC = Upgrade (
    id = 31,
    name = 'Alter Schul-PC',
    cost = 5.0,
    hintText = ['Der Stil der fruehen 90er in Nikotin-Gelb, niemand wird ihn vermissen und du musst nicht mehr so tun als wuerde dein lieblings Pappkarton ein Rechner sein.'],
    imagePath = os.path.join ('resources', 'ingame', 'upgrade', 'computer', 'schulPC.png'),
    unlockFunction = UF.getAlwaysUnlockedFunction (),
    activationFunction = AF.getIncreaseEpisodesPerClickByPercentageFunction (50)
)

ultraTastatur = Upgrade (
    id = 32,
    name = 'Gaming Tastatur',
    cost = 2000.0,
    hintText = ['Hat leichtgaengige Tasten und leuchtet im dunkeln.'],
    imagePath = os.path.join ('resources', 'ingame', 'upgrade', 'computer', 'ultraTastatur.png'),
    unlockFunction = UF.getAlwaysUnlockedFunction (),
    activationFunction = AF.getIncreaseEpisodesPerClickByPercentageFunction (70)
)
