from engine.controller.upgradeObjects.upgrade import Upgrade
import globals.upgrade.activationFunctions as AF
import globals.upgrade.unlockFunctions as UF
import os


billigerEDrink = Upgrade (
    name = 'Billiger E-Drink',
    cost = 0.01,
    hintText = ['Schmeckt nach Klebstoff. Weil welcher drin ist'],
    imagePath = os.path.join ('resources', 'ingame', 'upgrade', 'bensch', 'billigerEDrink.png'),
    unlockFunction = UF.getAlwaysUnlockedFunction (),
    activationFunction = AF.getIncreaseEpisodesPerClickByPercentageFunction (20)
)

normalerEDrink = Upgrade (
    name = 'Standard E-Drink',
    cost = 0.01,
    hintText = ['Bekannt aus jeder Tankstelle.'],
    imagePath = os.path.join ('resources', 'ingame', 'upgrade', 'bensch', 'normalerEDrink.png'),
    unlockFunction = UF.getAlwaysUnlockedFunction (),
    activationFunction = AF.getIncreaseEpisodesPerClickByPercentageFunction (30)
)

teurerEDrink = Upgrade (
    name = 'Premium E-Drink',
    cost = 0.01,
    hintText = ['Er hat ein Bild von nem C-Promi auf der Rueckseite'],
    imagePath = os.path.join ('resources', 'ingame', 'upgrade', 'bensch', 'teurerEDrink.png'),
    unlockFunction = UF.getAlwaysUnlockedFunction (),
    activationFunction = AF.getIncreaseEpisodesPerClickByPercentageFunction (40)
)

fuenfKomma0 = Upgrade (
    name = '5,0',
    cost = 0.01,
    hintText = ['Das Universalbier, macht gluecklich und loest die Zunge.'],
    imagePath = os.path.join ('resources', 'ingame', 'upgrade', 'bensch', '5komma0.png'),
    unlockFunction = UF.getAlwaysUnlockedFunction (),
    activationFunction = AF.getIncreaseMaxSubscribersPerEpisode (1)
)

drittesAuge = Upgrade (
    name = 'Drittes Auge',
    cost = 0.01,
    hintText = ['Oeffne deinen Geist fuer ein anderes Publikum'],
    imagePath = os.path.join ('resources', 'ingame', 'upgrade', 'bensch', 'drittesAuge.png'),
    unlockFunction = UF.getAlwaysUnlockedFunction (),
    activationFunction = AF.getPassiveFunction ('Missing Text')
)

extraHaende = Upgrade (
    name = 'Extra Haende',
    cost = 0.01,
    hintText = ['Unglaublich! Der Mann hat wirklich vier linke Haende!'],
    imagePath = os.path.join ('resources', 'ingame', 'upgrade', 'bensch', 'extraHaende.png'),
    unlockFunction = UF.getAlwaysUnlockedFunction (),
    activationFunction = AF.getPassiveFunction ('Missing Text')
)

hamsterProgrammer = Upgrade (
    name = 'Hamsterartiger Programmierer',
    cost = 0.01,
    hintText = ['Entwickelt mehr Idle Games, damit du mehr zu spielen hast.'],
    imagePath = os.path.join ('resources', 'ingame', 'upgrade', 'bensch', 'hamsterProgrammer.png'),
    unlockFunction = UF.getAlwaysUnlockedFunction (),
    activationFunction = AF.getPassiveFunction ('Missing Text')
)

klon = Upgrade (
    name = 'Klon Bensch',
    cost = 0.01,
    hintText = ['Jetzt gibt es zwei von dir, gib das mal bei der Steuererklaerung an.'],
    imagePath = os.path.join ('resources', 'ingame', 'upgrade', 'bensch', 'klon.png'),
    unlockFunction = UF.getAlwaysUnlockedFunction (),
    activationFunction = AF.getPassiveFunction ('Missing Text')
)

logikKurs = Upgrade (
    name = "Logik fuer Let's Player",
    cost = 0.01,
    hintText = ['Du erkennst schneller Loopholes in Idle Games und wirst so noch effektiver.'],
    imagePath = os.path.join ('resources', 'ingame', 'upgrade', 'bensch', 'logikKurs.png'),
    unlockFunction = UF.getAlwaysUnlockedFunction (),
    activationFunction = AF.getPassiveFunction ('Missing Text')
)

matheKurs = Upgrade (
    name = 'Mathe fuer Finanzbeamte',
    cost = 0.01,
    hintText = ['Wenn du das verstehst wirst du ach jedes Idle Game durchschauen.'],
    imagePath = os.path.join ('resources', 'ingame', 'upgrade', 'bensch', 'matheKurs.png'),
    unlockFunction = UF.getAlwaysUnlockedFunction (),
    activationFunction = AF.getPassiveFunction ('Missing Text')
)

mrScotch = Upgrade (
    name = 'Mr. Scotch',
    cost = 0.01,
    hintText = ['Das ist mein Kumpel Mr. Scotch, mit ihm haben alle mehr Spass!'],
    imagePath = os.path.join ('resources', 'ingame', 'upgrade', 'bensch', 'mrScotch.png'),
    unlockFunction = UF.getAlwaysUnlockedFunction (),
    activationFunction = AF.getPassiveFunction ('Missing Text')
)

streamMod = Upgrade (
    name = 'Stream Moderator',
    cost = 0.01,
    hintText = ['"Nein, BrotFotzeHitler ist KEIN guter Nickname!"'],
    imagePath = os.path.join ('resources', 'ingame', 'upgrade', 'bensch', 'oriMod.png'),
    unlockFunction = UF.getAlwaysUnlockedFunction (),
    activationFunction = AF.getPassiveFunction ('Missing Text')
)

leibwaechter = Upgrade (
    name = 'Der gute Leibwaechter',
    cost = 0.01,
    hintText = ['Wenn man dringend Schnapps braucht... trinkt man das auch nicht.'],
    imagePath = os.path.join ('resources', 'ingame', 'upgrade', 'bensch', 'pott.png'),
    unlockFunction = UF.getAlwaysUnlockedFunction (),
    activationFunction = AF.getPassiveFunction ('Missing Text')
)

schwarzerKaffee = Upgrade (
    name = 'Richtig schwarzer Kaffee Junge!',
    cost = 0.01,
    hintText = ['"Willst du mich zu deinem Kaffee?"'],
    imagePath = os.path.join ('resources', 'ingame', 'upgrade', 'bensch', 'schwarzerKaffee.png'),
    unlockFunction = UF.getAlwaysUnlockedFunction (),
    activationFunction = AF.getPassiveFunction ('Missing Text')
)

senorPopo = Upgrade (
    name = 'Senor Popo',
    cost = 0.01,
    hintText = ['Das ist... schwer zu erklaeren'],
    imagePath = os.path.join ('resources', 'ingame', 'upgrade', 'bensch', 'senorPopo.png'),
    unlockFunction = UF.getAlwaysUnlockedFunction (),
    activationFunction = AF.getPassiveFunction ('Missing Text')
)

unterbewusstesKlicken = Upgrade (
    name = '"Wie Sie unterbewusst klicken"',
    cost = 0.01,
    hintText = ['Egal was du tust, nach diesem Buch wird dein Finger immer weiter klicken.'],
    imagePath = os.path.join ('resources', 'ingame', 'upgrade', 'bensch', 'unterbewusstesKlicken.png'),
    unlockFunction = UF.getAlwaysUnlockedFunction (),
    activationFunction = AF.getActivateAutoClickFunction()
)