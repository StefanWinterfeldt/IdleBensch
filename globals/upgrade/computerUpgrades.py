from engine.controller.upgradeObjects.upgrade import Upgrade
import globals.upgrade.activationFunctions as AF
import globals.upgrade.unlockFunctions as UF
import os


modem56K = Upgrade (
    name = '56k Modem',
    cost = 0.01,
    hintText = ['Endlich kannst du deinen Akustik-Koppler loswerden! Und Dubstep spielt es auch!'],
    imagePath = os.path.join ('resources', 'ingame', 'upgrade', 'computer', '56kModem.png'),
    unlockFunction = UF.getAlwaysUnlockedFunction (),
    activationFunction = AF.getPassiveFunction ('Missing Text')
)

anrufbeantworter = Upgrade (
    name = 'Anrufbeantworter',
    cost = 0.01,
    hintText = ['Niemand wird dich mehr beim Aufnehmen stoeren.'],
    imagePath = os.path.join ('resources', 'ingame', 'upgrade', 'computer', 'anrufbeantworter.png'),
    unlockFunction = UF.getAlwaysUnlockedFunction (),
    activationFunction = AF.getPassiveFunction ('Missing Text')
)

brainInAJar = Upgrade (
    name = 'Bio-Computer',
    cost = 0.01,
    hintText = ['Ja, ich weiss dass es wie ne Suesskartoffel aussieht. Versuch du mal in Paint ein Gehirn zu malen.'],
    imagePath = os.path.join ('resources', 'ingame', 'upgrade', 'computer', 'brainInAJar.png'),
    unlockFunction = UF.getAlwaysUnlockedFunction (),
    activationFunction = AF.getPassiveFunction ('Missing Text')
)

brainInterface = Upgrade (
    name = 'Neurales Interface',
    cost = 0.01,
    hintText = ['Jetzt brauchst du deine laestigen Haende nicht mehr.'],
    imagePath = os.path.join ('resources', 'ingame', 'upgrade', 'computer', 'brainInterface.png'),
    unlockFunction = UF.getAlwaysUnlockedFunction (),
    activationFunction = AF.getPassiveFunction ('Missing Text')
)

modemDSL = Upgrade (
    name = 'DSL Modem',
    cost = 0.01,
    hintText = ['Garantiert bis zu 100K... zumindest zwischen 3:13 und 3:14 Uhr.'],
    imagePath = os.path.join ('resources', 'ingame', 'upgrade', 'computer', 'dslModem.png'),
    unlockFunction = UF.getAlwaysUnlockedFunction (),
    activationFunction = AF.getPassiveFunction ('Missing Text')
)

ergoMaus = Upgrade (
    name = 'Ergonomische Maus',
    cost = 0.01,
    hintText = ['Aus echtem Stierhodenleder. Keine Macht dem Karpaltunnel!'],
    imagePath = os.path.join ('resources', 'ingame', 'upgrade', 'computer', 'ergoMaus.png'),
    unlockFunction = UF.getAlwaysUnlockedFunction (),
    activationFunction = AF.getPassiveFunction ('Missing Text')
)

glasfaser = Upgrade (
    name = 'Glasfaserverbindung',
    cost = 0.01,
    hintText = ['Internet mit Lichtgeschwindigkeit, damit koenntest du Pornos so schnell gucken wie neue produziert werden...'],
    imagePath = os.path.join ('resources', 'ingame', 'upgrade', 'computer', 'glasfaser.png'),
    unlockFunction = UF.getAlwaysUnlockedFunction (),
    activationFunction = AF.getPassiveFunction ('Missing Text')
)

hdKamera = Upgrade (
    name = 'HD Kamera',
    cost = 0.01,
    hintText = ['Jetzt kann man auch dein Gesicht erkennen, ob das so ne gute Idee war...'],
    imagePath = os.path.join ('resources', 'ingame', 'upgrade', 'computer', 'HDKamera.png'),
    unlockFunction = UF.getAlwaysUnlockedFunction (),
    activationFunction = AF.getPassiveFunction ('Missing Text')
)

highEndPC = Upgrade (
    name = 'High End PC',
    cost = 0.01,
    hintText = ['Darauf lauft sogar deine Mutter fluessig.'],
    imagePath = os.path.join ('resources', 'ingame', 'upgrade', 'computer', 'highEndPC.png'),
    unlockFunction = UF.getAlwaysUnlockedFunction (),
    activationFunction = AF.getPassiveFunction ('Missing Text')
)

holoKamera = Upgrade (
    name = 'Holographische Kamera',
    cost = 0.01,
    hintText = ['Mit dem richtigen Equipment koennen sich deine Zuschauer einen Lebensgrossen Holo-Bensch in ihr Wohnzimmer projizieren.'],
    imagePath = os.path.join ('resources', 'ingame', 'upgrade', 'computer', 'holoKamera.png'),
    unlockFunction = UF.getAlwaysUnlockedFunction (),
    activationFunction = AF.getPassiveFunction ('Missing Text')
)

normalPC = Upgrade (
    name = 'Normaler PC',
    cost = 0.01,
    hintText = ['Nix besonderes, aber auch nicht aus Presspappe.'],
    imagePath = os.path.join ('resources', 'ingame', 'upgrade', 'computer', 'normalPC.png'),
    unlockFunction = UF.getAlwaysUnlockedFunction (),
    activationFunction = AF.getPassiveFunction ('Missing Text')
)

quantumComputer = Upgrade (
    name = 'Quantencomputer',
    cost = 0.01,
    hintText = ['2000 Jahre Forschung fuer... Quanten-IdleGames'],
    imagePath = os.path.join ('resources', 'ingame', 'upgrade', 'computer', 'quantumComputer.png'),
    unlockFunction = UF.getAlwaysUnlockedFunction (),
    activationFunction = AF.getPassiveFunction ('Missing Text')
)

satellitModem = Upgrade (
    name = 'Satelliten-Uplink',
    cost = 0.01,
    hintText = ['Selbst das Hubble-Teleskop kann dir jetzt zuschauen.'],
    imagePath = os.path.join ('resources', 'ingame', 'upgrade', 'computer', 'satellitModem.png'),
    unlockFunction = UF.getAlwaysUnlockedFunction (),
    activationFunction = AF.getPassiveFunction ('Missing Text')
)

schlechteKamera = Upgrade (
    name = 'Billige Kamera',
    cost = 0.01,
    hintText = ['Gabs gebraucht auf Ebay. Ein Blick auf die SD-Karte verraet warum sie so billig war...'],
    imagePath = os.path.join ('resources', 'ingame', 'upgrade', 'computer', 'schlechteKamera.png'),
    unlockFunction = UF.getAlwaysUnlockedFunction (),
    activationFunction = AF.getActivateStreamFunction ()
)

schulPC = Upgrade (
    name = 'Alter Schul-PC',
    cost = 0.01,
    hintText = ['Der Stil der fruehen 90er in Nikotin-Gelb, niemand wird ihn vermissen.'],
    imagePath = os.path.join ('resources', 'ingame', 'upgrade', 'computer', 'schulPC.png'),
    unlockFunction = UF.getAlwaysUnlockedFunction (),
    activationFunction = AF.getPassiveFunction ('Missing Text')
)

ultraTastatur = Upgrade (
    name = 'Gaming Tastatur',
    cost = 0.01,
    hintText = ['Hat leichtgaengige Tasten und leuchtet im dunkeln'],
    imagePath = os.path.join ('resources', 'ingame', 'upgrade', 'computer', 'ultraTastatur.png'),
    unlockFunction = UF.getAlwaysUnlockedFunction (),
    activationFunction = AF.getPassiveFunction ('Missing Text')
)
