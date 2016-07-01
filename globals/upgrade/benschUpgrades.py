from engine.controller.upgradeObjects.upgrade import Upgrade
import globals.upgrade.activationFunctions as AF
import globals.upgrade.unlockFunctions as UF
import os


billigerEDrink = Upgrade (
    name = 'Billiger E-Drink',
    cost = 0.19,
    hintText = ['Schmeckt nach Klebstoff. Weil welcher drin ist'],
    imagePath = os.path.join ('resources', 'ingame', 'upgrade', 'bensch', 'billigerEDrink.png'),
    unlockFunction = UF.getAlwaysUnlockedFunction (),
    activationFunction = AF.getIncreaseEpisodesPerClickByPercentageFunction (10)
)

normalerEDrink = Upgrade (
    name = 'Standard E-Drink',
    cost = 0.99,
    hintText = ['Bekannt aus jeder Tankstelle.'],
    imagePath = os.path.join ('resources', 'ingame', 'upgrade', 'bensch', 'normalerEDrink.png'),
    unlockFunction = UF.getAlwaysUnlockedFunction (),
    activationFunction = AF.getIncreaseEpisodesPerClickByPercentageFunction (20)
)

teurerEDrink = Upgrade (
    name = 'Premium E-Drink',
    cost = 11.0,
    hintText = ['Er hat ein Bild von nem C-Promi auf der Rueckseite'],
    imagePath = os.path.join ('resources', 'ingame', 'upgrade', 'bensch', 'teurerEDrink.png'),
    unlockFunction = UF.getAlwaysUnlockedFunction (),
    activationFunction = AF.getIncreaseEpisodesPerClickByPercentageFunction (40)
)

fuenfKomma0 = Upgrade (
    name = '5,0',
    cost = 0.45,
    hintText = ['Das Universalbier, macht gluecklich und loest die Zunge.'],
    imagePath = os.path.join ('resources', 'ingame', 'upgrade', 'bensch', '5komma0.png'),
    unlockFunction = UF.getAlwaysUnlockedFunction (),
    activationFunction = AF.getIncreaseMaxSubscribersPerEpisode (1)
)

drittesAuge = Upgrade (
    name = 'Drittes Auge',
    cost = 6660000.0,
    hintText = ['Oeffne deinen Geist fuer ein anderes Publikum'],
    imagePath = os.path.join ('resources', 'ingame', 'upgrade', 'bensch', 'drittesAuge.png'),
    unlockFunction = UF.getAlwaysUnlockedFunction (),
    activationFunction = AF.getPassiveFunction ('Missing Text')
)

extraHaende = Upgrade (
    name = 'Extra Haende',
    cost = 5000.0,
    hintText = ['Unglaublich! Der Mann hat wirklich vier linke Haende!'],
    imagePath = os.path.join ('resources', 'ingame', 'upgrade', 'bensch', 'extraHaende.png'),
    unlockFunction = UF.getAlwaysUnlockedFunction (),
    activationFunction = AF.getIncreaseClicksPerSecondByPercentageFunction (100)
)

hamsterProgrammer = Upgrade (
    name = 'Hamsterartiger Programmierer',
    cost = 1337.0,
    hintText = ['Entwickelt mehr Idle Games, damit du mehr zu spielen hast.'],
    imagePath = os.path.join ('resources', 'ingame', 'upgrade', 'bensch', 'hamsterProgrammer.png'),
    unlockFunction = UF.getAlwaysUnlockedFunction (),
    activationFunction = AF.getIncreaseSubscriberViewsPerEpisodeByPercentage (30)
)

klon = Upgrade (
    name = 'Klon Bensch',
    cost = 250000.0,
    hintText = ['Jetzt gibt es zwei von dir, gib das mal bei der Steuererklaerung an.'],
    imagePath = os.path.join ('resources', 'ingame', 'upgrade', 'bensch', 'klon.png'),
    unlockFunction = UF.getAlwaysUnlockedFunction (),
    activationFunction = AF.getIncreaseNumberOfStreamsByOne ()
)

logikKurs = Upgrade (
    name = "Logik fuer Let's Player",
    cost = 50.0,
    hintText = ['Du erkennst schneller Loopholes in Idle Games und wirst so noch effektiver.'],
    imagePath = os.path.join ('resources', 'ingame', 'upgrade', 'bensch', 'logikKurs.png'),
    unlockFunction = UF.getAlwaysUnlockedFunction (),
    activationFunction = AF.getIncreaseViewsPerEpisodeByPercentage (20)
)

matheKurs = Upgrade (
    name = 'Mathe fuer Finanzbeamte',
    cost = 350.0,
    hintText = ['Wenn du das verstehst wirst du ach jedes Idle Game durchschauen.'],
    imagePath = os.path.join ('resources', 'ingame', 'upgrade', 'bensch', 'matheKurs.png'),
    unlockFunction = UF.getAlwaysUnlockedFunction (),
    activationFunction = AF.getIncreaseViewsPerEpisodeByPercentage (30)
)

mrScotch = Upgrade (
    name = 'Mr. Scotch',
    cost = 120.0,
    hintText = ['Das ist mein Kumpel Mr. Scotch, mit ihm haben alle mehr Spass!'],
    imagePath = os.path.join ('resources', 'ingame', 'upgrade', 'bensch', 'mrScotch.png'),
    unlockFunction = UF.getAlwaysUnlockedFunction (),
    activationFunction = AF.getIncreaseMaxSubscribersPerEpisode (5)
)

streamMod = Upgrade (
    name = 'Stream Moderator',
    cost = 30000.0,
    hintText = ['"Nein, BrotFotzeHitler ist KEIN guter Nickname!"'],
    imagePath = os.path.join ('resources', 'ingame', 'upgrade', 'bensch', 'oriMod.png'),
    unlockFunction = UF.getAlwaysUnlockedFunction (),
    activationFunction = AF.getIncreaseSubscribersPerStreamPerSecondByPercentage (100)
)

leibwaechter = Upgrade (
    name = 'Der gute Leibwaechter',
    cost = 7.95,
    hintText = ['Wenn man dringend Schnapps braucht... trinkt man das auch nicht.'],
    imagePath = os.path.join ('resources', 'ingame', 'upgrade', 'bensch', 'pott.png'),
    unlockFunction = UF.getAlwaysUnlockedFunction (),
    activationFunction = AF.getIncreaseMinSubscribersPerEpisode (1)
)

schwarzerKaffee = Upgrade (
    name = 'Richtig schwarzer Kaffee Junge!',
    cost = 2.49,
    hintText = ['"Willst du mich zu deinem Kaffee?"'],
    imagePath = os.path.join ('resources', 'ingame', 'upgrade', 'bensch', 'schwarzerKaffee.png'),
    unlockFunction = UF.getAlwaysUnlockedFunction (),
    activationFunction = AF.getIncreaseEpisodesPerClickByPercentageFunction (30)
)

senorPopo = Upgrade (
    name = 'Senor Popo',
    cost = 500000.0,
    hintText = ['Das ist... schwer zu erklaeren'],
    imagePath = os.path.join ('resources', 'ingame', 'upgrade', 'bensch', 'senorPopo.png'),
    unlockFunction = UF.getAlwaysUnlockedFunction (),
    activationFunction = AF.getIncreaseViewsPerEpisodeByPercentage(200)
)

unterbewusstesKlicken = Upgrade (
    name = '"Wie Sie unterbewusst klicken"',
    cost = 6.99,
    hintText = ['Egal was du tust, nach diesem Buch wird dein Finger immer weiter klicken.'],
    imagePath = os.path.join ('resources', 'ingame', 'upgrade', 'bensch', 'unterbewusstesKlicken.png'),
    unlockFunction = UF.getAlwaysUnlockedFunction (),
    activationFunction = AF.getActivateAutoClickFunction ()
)
