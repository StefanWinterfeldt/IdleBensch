from engine.controller.upgradeObjects.upgrade import Upgrade
import globals.upgrade.activationFunctions as AF
import globals.upgrade.unlockFunctions as UF
import os


modem56K = Upgrade (
    id = 17,
    name = '56k Modem',
    cost = 20.0,
    hintText = ['Endlich kannst du deinen Akustik-Koppler loswerden! Und Dubstep spielt es auch!'],
    imagePath = os.path.join ('resources', 'ingame', 'upgrade', 'computer', '56kModem.png'),
    unlockFunction = UF.getAlwaysUnlockedFunction (),
    activationFunction = AF.getIncreaseMinSubscribersPerEpisode (1)
)

anrufbeantworter = Upgrade (
    id = 18,
    name = 'Anrufbeantworter',
    cost = 40.0,
    hintText = ['Niemand wird dich mehr beim Aufnehmen stoeren.'],
    imagePath = os.path.join ('resources', 'ingame', 'upgrade', 'computer', 'anrufbeantworter.png'),
    unlockFunction = UF.getAlwaysUnlockedFunction (),
    activationFunction = AF.getIncreaseEpisodesPerClickByPercentageFunction (100)
)

brainInAJar = Upgrade (
    id = 19,
    name = 'Bio-Computer',
    cost = 25000.0,
    hintText = ['Ja, ich weiss dass es wie ne Suesskartoffel aussieht. Versuch du mal in Paint ein Gehirn zu malen.'],
    imagePath = os.path.join ('resources', 'ingame', 'upgrade', 'computer', 'brainInAJar.png'),
    unlockFunction = UF.getUnlockFunctionRequiringActiveUpgrades ([50]),
    activationFunction = AF.getPassiveFunction ('Missing Text')
)

brainInterface = Upgrade (
    id = 20,
    name = 'Neurales Interface',
    cost = 0.01,
    hintText = ['Jetzt brauchst du deine laestigen Haende nicht mehr.'],
    imagePath = os.path.join ('resources', 'ingame', 'upgrade', 'computer', 'brainInterface.png'),
    unlockFunction = UF.getAlwaysUnlockedFunction (),
    activationFunction = AF.getPassiveFunction ('Missing Text')
)

modemDSL = Upgrade (
    id = 21,
    name = 'DSL Modem',
    cost = 700.0,
    hintText = ['Garantiert bis zu 100K... zumindest zwischen 3:13 und 3:14 Uhr.'],
    imagePath = os.path.join ('resources', 'ingame', 'upgrade', 'computer', 'dslModem.png'),
    unlockFunction = UF.getAlwaysUnlockedFunction (),
    activationFunction = AF.getIncreaseSubscribersPerStreamPerSecondByPercentage (50)
)

ergoMaus = Upgrade (
    id = 22,
    name = 'Ergonomische Maus',
    cost = 100.0,
    hintText = ['Aus echtem Stierhodenleder. Keine Macht dem Karpaltunnel!'],
    imagePath = os.path.join ('resources', 'ingame', 'upgrade', 'computer', 'ergoMaus.png'),
    unlockFunction = UF.getAlwaysUnlockedFunction (),
    activationFunction = AF.getIncreaseEpisodesPerClickByPercentageFunction (120)
)

glasfaser = Upgrade (
    id = 23,
    name = 'Glasfaserverbindung',
    cost = 0.01,
    hintText = ['Internet mit Lichtgeschwindigkeit, damit koenntest du Pornos so schnell gucken wie neue produziert werden...'],
    imagePath = os.path.join ('resources', 'ingame', 'upgrade', 'computer', 'glasfaser.png'),
    unlockFunction = UF.getAlwaysUnlockedFunction (),
    activationFunction = AF.getPassiveFunction ('Missing Text')
)

hdKamera = Upgrade (
    id = 24,
    name = 'HD Kamera',
    cost = 1000.0,
    hintText = ['Jetzt kann man auch dein Gesicht erkennen, ob das so ne gute Idee war...'],
    imagePath = os.path.join ('resources', 'ingame', 'upgrade', 'computer', 'HDKamera.png'),
    unlockFunction = UF.getAlwaysUnlockedFunction (),
    activationFunction = AF.getIncreaseViewsPerEpisodeByPercentage (100)
)

highEndPC = Upgrade (
    id = 25,
    name = 'High End PC',
    cost = 3000.0,
    hintText = ['Darauf lauft sogar deine Mutter fluessig.'],
    imagePath = os.path.join ('resources', 'ingame', 'upgrade', 'computer', 'highEndPC.png'),
    unlockFunction = UF.getAlwaysUnlockedFunction (),
    activationFunction = AF.getActivateTechCategory ()
)

holoKamera = Upgrade (
    id = 26,
    name = 'Holographische Kamera',
    cost = 0.01,
    hintText = ['Mit dem richtigen Equipment koennen sich deine Zuschauer einen Lebensgrossen Holo-Bensch in ihr Wohnzimmer projizieren.'],
    imagePath = os.path.join ('resources', 'ingame', 'upgrade', 'computer', 'holoKamera.png'),
    unlockFunction = UF.getAlwaysUnlockedFunction (),
    activationFunction = AF.getPassiveFunction ('Missing Text')
)

normalPC = Upgrade (
    id = 27,
    name = 'Normaler PC',
    cost = 500.0,
    hintText = ['Nix besonderes, aber auch nicht aus Presspappe.'],
    imagePath = os.path.join ('resources', 'ingame', 'upgrade', 'computer', 'normalPC.png'),
    unlockFunction = UF.getAlwaysUnlockedFunction (),
    activationFunction = AF.getActivateMerchCategory ()
)

quantumComputer = Upgrade (
    id = 28,
    name = 'Quantencomputer',
    cost = 0.01,
    hintText = ['2000 Jahre Forschung fuer... Quanten-IdleGames'],
    imagePath = os.path.join ('resources', 'ingame', 'upgrade', 'computer', 'quantumComputer.png'),
    unlockFunction = UF.getAlwaysUnlockedFunction (),
    activationFunction = AF.getPassiveFunction ('Missing Text')
)

satellitModem = Upgrade (
    id = 29,
    name = 'Satelliten-Uplink',
    cost = 5000.0,
    hintText = ['Selbst das Hubble-Teleskop kann dir jetzt zuschauen.'],
    imagePath = os.path.join ('resources', 'ingame', 'upgrade', 'computer', 'satellitModem.png'),
    unlockFunction = UF.getAlwaysUnlockedFunction (),
    activationFunction = AF.getIncreaseMinSubscribersPerEpisode (5)
)

schlechteKamera = Upgrade (
    id = 30,
    name = 'Billige Kamera',
    cost = 0.01,
    hintText = ['Gabs gebraucht auf Ebay. Ein Blick auf die SD-Karte verraet warum sie so billig war...'],
    imagePath = os.path.join ('resources', 'ingame', 'upgrade', 'computer', 'schlechteKamera.png'),
    unlockFunction = UF.getAlwaysUnlockedFunction (),
    activationFunction = AF.getActivateStreamFunction ()
)

schulPC = Upgrade (
    id = 31,
    name = 'Alter Schul-PC',
    cost = 10.0,
    hintText = ['Der Stil der fruehen 90er in Nikotin-Gelb, niemand wird ihn vermissen und du musst nicht mehr so tun als dei lieblings Pappkarton ein Rechner sein.'],
    imagePath = os.path.join ('resources', 'ingame', 'upgrade', 'computer', 'schulPC.png'),
    unlockFunction = UF.getAlwaysUnlockedFunction (),
    activationFunction = AF.getIncreaseEpisodesPerClickByPercentageFunction (100),
    visible = True
)

ultraTastatur = Upgrade (
    id = 32,
    name = 'Gaming Tastatur',
    cost = 2000.0,
    hintText = ['Hat leichtgaengige Tasten und leuchtet im dunkeln'],
    imagePath = os.path.join ('resources', 'ingame', 'upgrade', 'computer', 'ultraTastatur.png'),
    unlockFunction = UF.getAlwaysUnlockedFunction (),
    activationFunction = AF.getIncreaseClicksPerSecondByPercentageFunction (100)
)
