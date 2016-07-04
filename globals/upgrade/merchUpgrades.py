from engine.controller.upgradeObjects.upgrade import Upgrade
import globals.upgrade.activationFunctions as AF
import globals.upgrade.unlockFunctions as UF
import os


actionFigur = Upgrade (
    id = 33,
    name = 'Bensch Action-Figur',
    cost = 26000.0,
    hintText = ['Jetzt kann jeder den historischen Kampf gegen Dr. Octokraken nachspielen.'],
    imagePath = os.path.join ('resources', 'ingame', 'upgrade', 'merch', 'actionFigur.png'),
    unlockFunction = UF.getAlwaysUnlockedFunction (),
    activationFunction = AF.getActivateDonationsFunction ()
)

arschPad = Upgrade (
    id = 34,
    name = 'Ergo-Mousepad mit Arsch-Kissen',
    cost = 900.0,
    hintText = ['Eine naturgetreue Abformung deines Hinterns, mit echtem Rosshaar.'],
    imagePath = os.path.join ('resources', 'ingame', 'upgrade', 'merch', 'arschPad.png'),
    unlockFunction = UF.getAlwaysUnlockedFunction (),
    activationFunction = AF.getIncreaseMaxPurchaseAmountByPercentage (30)
)

bart = Upgrade (
    id = 35,
    name = 'Der Bart fuer ihn und sie',
    cost = 3200.0,
    hintText = ['Besonders beliebt bei Zuschauern mit altersbedingt ausgebliebenem Bartwuchs.'],
    imagePath = os.path.join ('resources', 'ingame', 'upgrade', 'merch', 'bart.png'),
    unlockFunction = UF.getAlwaysUnlockedFunction (),
    activationFunction = AF.getIncreasePurchaseChanceByPercentage (30)
)

bier = Upgrade (
    id = 36,
    name = 'Das Bensch-Bier',
    cost = 1200.0,
    hintText = ['Beliebtester Brauweizen bei baertigen Bauarbeitern.'],
    imagePath = os.path.join ('resources', 'ingame', 'upgrade', 'merch', 'bier.png'),
    unlockFunction = UF.getAlwaysUnlockedFunction (),
    activationFunction = AF.getIncreasePurchaseChanceByPercentage (20)
)

eauDeBensch = Upgrade (
    id = 37,
    name = 'Eau De Bensch',
    cost = 2500.0,
    hintText = ['Der Name ist Programm'],
    imagePath = os.path.join ('resources', 'ingame', 'upgrade', 'merch', 'eauDeBensch.png'),
    unlockFunction = UF.getAlwaysUnlockedFunction (),
    activationFunction = AF.getIncreaseMaxPurchaseAmountByPercentage (40)
)

film1 = Upgrade (
    id = 38,
    name = 'Das Opossum und die Drogen',
    cost = 1750.0,
    hintText = ['Der Kult Film, jetzt im Directors-Cut (3 Sek. laenger).'],
    imagePath = os.path.join ('resources', 'ingame', 'upgrade', 'merch', 'film1.png'),
    unlockFunction = UF.getUnlockFunctionRequiringActiveUpgrades ([24]),
    activationFunction = AF.getIncreaseMaxPurchaseAmountByPercentage (30)
)

film2 = Upgrade (
    id = 39,
    name = 'Church Dreams on Acid',
    cost = 0.0,
    hintText = ['Der umstrittene Nachfolger von DOUDD.'],
    imagePath = os.path.join ('resources', 'ingame', 'upgrade', 'merch', 'film2.png'),
    unlockFunction = UF.getAlwaysUnlockedFunction (),
    activationFunction = AF.getPassiveFunction ('Missing Text')
)

hoerspiel = Upgrade (
    id = 40,
    name = 'Die drei XXX',
    cost = 40000.0,
    hintText = ['Die beliebte Hoerspielserie.'],
    imagePath = os.path.join ('resources', 'ingame', 'upgrade', 'merch', 'hoerspiel.png'),
    unlockFunction = UF.getAlwaysUnlockedFunction (),
    activationFunction = AF.getIncreaseMaxPurchaseAmountByPercentage (100)
)

modeLabel = Upgrade (
    id = 41,
    name = 'Ein eigenes Modelabel',
    cost = 0.0,
    hintText = ['Mal ehrlich, jeder Idiot kann heutzutage Mode Designen.'],
    imagePath = os.path.join ('resources', 'ingame', 'upgrade', 'merch', 'modeLabel.png'),
    unlockFunction = UF.getAlwaysUnlockedFunction (),
    activationFunction = AF.getPassiveFunction ('Missing Text')
)

musicAlbum = Upgrade (
    id = 42,
    name = 'Schrapnellgemaecht - Das Album',
    cost = 8500.0,
    hintText = ['Im Keller gefunden und rasch 2 Millionen Mal aufgelegt.'],
    imagePath = os.path.join ('resources', 'ingame', 'upgrade', 'merch', 'musicAlbum.png'),
    unlockFunction = UF.getAlwaysUnlockedFunction (),
    activationFunction = AF.getIncreaseMaxPurchaseAmountByPercentage (40)
)

oper = Upgrade (
    id = 43,
    name = 'Das Phantom von Opa',
    cost = 0.0,
    hintText = ['Endlich wieder ein Grund ins Staatstheater zu gehen.'],
    imagePath = os.path.join ('resources', 'ingame', 'upgrade', 'merch', 'oper.png'),
    unlockFunction = UF.getAlwaysUnlockedFunction (),
    activationFunction = AF.getPassiveFunction ('Missing Text')
)

realDoll = Upgrade (
    id = 44,
    name = 'Bensch RealDoll',
    cost = 0.0,
    hintText = ['Auf Wusch auch mit ueberraschtem Gesichtsausdruck. Platz zwei neben der Antonio Banderas Blow up Doll.'],
    imagePath = os.path.join ('resources', 'ingame', 'upgrade', 'merch', 'realDoll.png'),
    unlockFunction = UF.getAlwaysUnlockedFunction (),
    activationFunction = AF.getPassiveFunction ('Missing Text')
)

roman = Upgrade (
    id = 45,
    name = 'Autobiographie',
    cost = 65000.0,
    hintText = ['Sollte erst unter dem Titel "50 Shades of Bensch" erscheinen, aber "Bart und Spiele" passte besser.'],
    imagePath = os.path.join ('resources', 'ingame', 'upgrade', 'merch', 'roman.png'),
    unlockFunction = UF.getAlwaysUnlockedFunction (),
    activationFunction = AF.getIncreaseMaxPurchaseAmountByPercentage (50)
)

schnapps = Upgrade (
    id = 46,
    name = 'Bensch - Der Schnapps',
    cost = 11500.0,
    hintText = ['Aus der Kurzkieseler Pils Brauerei.'],
    imagePath = os.path.join ('resources', 'ingame', 'upgrade', 'merch', 'schnaps.png'),
    unlockFunction = UF.getAlwaysUnlockedFunction (),
    activationFunction = AF.getIncreasePurchaseChanceByPercentage (50)
)

shirt = Upgrade (
    id = 47,
    name = 'Der Klassiker',
    cost = 300.0,
    hintText = ['Ein Shirt mit deinem Gesicht drauf, herzlich Glueckwunsch.'],
    imagePath = os.path.join ('resources', 'ingame', 'upgrade', 'merch', 'shirt.png'),
    unlockFunction = UF.getAlwaysUnlockedFunction (),
    activationFunction = AF.getActivatePurchasesFunction ()
)

tasse = Upgrade (
    id = 48,
    name = 'Bensch-Tasse',
    cost = 500.0,
    hintText = ['Und ploetzlich stehen ueberall Leute die dir aus dem Kopf trinken...'],
    imagePath = os.path.join ('resources', 'ingame', 'upgrade', 'merch', 'tasse.png'),
    unlockFunction = UF.getAlwaysUnlockedFunction (),
    activationFunction = AF.getIncreaseMaxPurchaseAmountByPercentage (20)
)
