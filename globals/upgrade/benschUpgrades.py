#Copyright 2016 Stefan Winterfeldt
#This file is part of Idle Bensch.
#
#Idle Bensch is free software: you can redistribute it and/or modify
#it under the terms of the GNU General Public License as published by
#the Free Software Foundation, either version 3 of the License, or
#(at your option) any later version.
#
#Idle Bensch is distributed in the hope that it will be useful,
#but WITHOUT ANY WARRANTY; without even the implied warranty of
#MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#GNU General Public License for more details.
#
#You should have received a copy of the GNU General Public License
#along with Idle Bensch.  If not, see <http://www.gnu.org/licenses/>.

from engine.controller.upgradeObjects.upgrade import Upgrade
import globals.upgrade.activationFunctions as AF
import globals.upgrade.unlockFunctions as UF
import os


billigerEDrink = Upgrade (
    id = 1,
    name = 'Billiger E-Drink',
    cost = 0.19,
    hintText = ['Schmeckt nach Klebstoff. Weil welcher drin ist.'],
    imagePath = os.path.join ('resources', 'ingame', 'upgrade', 'bensch', 'billigerEDrink.png'),
    unlockFunction = UF.getAlwaysUnlockedFunction (),
    activationFunction = AF.getIncreaseEpisodesPerClickByPercentageFunction (15),
    visible = True
)

normalerEDrink = Upgrade (
    id = 2,
    name = 'Standard E-Drink',
    cost = 0.99,
    hintText = ['Bekannt aus jeder Tankstelle.'],
    imagePath = os.path.join ('resources', 'ingame', 'upgrade', 'bensch', 'normalerEDrink.png'),
    unlockFunction = UF.getAlwaysUnlockedFunction (),
    activationFunction = AF.getIncreaseEpisodesPerClickByPercentageFunction (25)
)

teurerEDrink = Upgrade (
    id = 3,
    name = 'Premium E-Drink',
    cost = 17.0,
    hintText = ['Er hat ein Bild von nem C-Promi auf der Rueckseite.'],
    imagePath = os.path.join ('resources', 'ingame', 'upgrade', 'bensch', 'teurerEDrink.png'),
    unlockFunction = UF.getAlwaysUnlockedFunction (),
    activationFunction = AF.getIncreaseClicksPerSecondByPercentageFunction (50)
)

fuenfKomma0 = Upgrade (
    id = 4,
    name = '5,0',
    cost = 0.45,
    hintText = ['Das Universalbier, macht gluecklich und loest die Zunge.'],
    imagePath = os.path.join ('resources', 'ingame', 'upgrade', 'bensch', '5komma0.png'),
    unlockFunction = UF.getAlwaysUnlockedFunction (),
    activationFunction = AF.getIncreaseMaxSubscribersPerEpisode (3)
)

drittesAuge = Upgrade (
    id = 5,
    name = 'Drittes Auge',
    cost = 6660000.0,
    hintText = ['Oeffne deinen Geist fuer ein anderes Publikum.'],
    imagePath = os.path.join ('resources', 'ingame', 'upgrade', 'bensch', 'drittesAuge.png'),
    unlockFunction = UF.getUnlockFunctionRequiringActiveUpgrades ([20]),
    activationFunction = AF.getActivateOccultCategory ()
)

extraHaende = Upgrade (
    id = 6,
    name = 'Extra Haende',
    cost = 75000.0,
    hintText = ['Unglaublich! Der Mann hat wirklich vier linke Haende!'],
    imagePath = os.path.join ('resources', 'ingame', 'upgrade', 'bensch', 'extraHaende.png'),
    unlockFunction = UF.getUnlockFunctionRequiringActiveUpgrades ([50]),
    activationFunction = AF.getIncreaseEpisodesPerClickByPercentageFunction (100)
)

hamsterProgrammer = Upgrade (
    id = 7,
    name = 'Hamsterartiger Programmierer',
    cost = 21337.0,
    hintText = ['Entwickelt mehr Idle Games, damit du mehr zu spielen hast.'],
    imagePath = os.path.join ('resources', 'ingame', 'upgrade', 'bensch', 'hamsterProgrammer.png'),
    unlockFunction = UF.getUnlockFunctionRequiringActiveUpgrades ([25]),
    activationFunction = AF.getIncreaseViewsPerEpisodeByPercentage (50)
)

klon = Upgrade (
    id = 8,
    name = 'Klon Bensch',
    cost = 200000.0,
    hintText = ['Jetzt gibt es zwei von dir, gib das mal bei der Steuererklaerung an.'],
    imagePath = os.path.join ('resources', 'ingame', 'upgrade', 'bensch', 'klon.png'),
    unlockFunction = UF.getUnlockFunctionRequiringActiveUpgrades ([50]),
    activationFunction = AF.getIncreaseNumberOfStreamsByOne ()
)

logikKurs = Upgrade (
    id = 9,
    name = "Logik fuer Let's Player",
    cost = 35.0,
    hintText = ['Du erkennst schneller Loopholes in Idle Games und wirst so noch effektiver.'],
    imagePath = os.path.join ('resources', 'ingame', 'upgrade', 'bensch', 'logikKurs.png'),
    unlockFunction = UF.getAlwaysUnlockedFunction (),
    activationFunction = AF.getIncreaseViewsPerEpisodeByPercentage (20)
)

matheKurs = Upgrade (
    id = 10,
    name = 'Mathe fuer Finanzbeamte',
    cost = 140.0,
    hintText = ['Wenn du das verstehst wirst du auch jedes Idle Game durchschauen.'],
    imagePath = os.path.join ('resources', 'ingame', 'upgrade', 'bensch', 'matheKurs.png'),
    unlockFunction = UF.getAlwaysUnlockedFunction (),
    activationFunction = AF.getIncreaseViewsPerEpisodeByPercentage (50)
)

mrScotch = Upgrade (
    id = 11,
    name = 'Mr. Scotch',
    cost = 90.0,
    hintText = ['Das ist mein Kumpel Mr. Scotch, mit ihm haben alle mehr Spass!'],
    imagePath = os.path.join ('resources', 'ingame', 'upgrade', 'bensch', 'mrScotch.png'),
    unlockFunction = UF.getAlwaysUnlockedFunction (),
    activationFunction = AF.getIncreaseMaxSubscribersPerEpisode (20)
)

streamMod = Upgrade (
    id = 12,
    name = 'Stream Moderator',
    cost = 200000.0,
    hintText = ['"Nein, BrotFotzeHitler ist KEIN guter Nickname!"'],
    imagePath = os.path.join ('resources', 'ingame', 'upgrade', 'bensch', 'oriMod.png'),
    unlockFunction = UF.getUnlockFunctionRequiringActiveUpgrades ([26]),
    activationFunction = AF.getIncreaseSubscribersPerStreamPerSecondByPercentage (100)
)

leibwaechter = Upgrade (
    id = 13,
    name = 'Der gute Leibwaechter',
    cost = 7.99,
    hintText = ['Wenn man dringend Schnapps braucht... trinkt man das auch nicht.'],
    imagePath = os.path.join ('resources', 'ingame', 'upgrade', 'bensch', 'pott.png'),
    unlockFunction = UF.getAlwaysUnlockedFunction (),
    activationFunction = AF.getIncreaseMaxSubscribersPerEpisode (6)
)

schwarzerKaffee = Upgrade (
    id = 14,
    name = 'Richtig schwarzer Kaffee Junge!',
    cost = 2.19,
    hintText = ['"Willst du mich zu deinem Kaffee?"'],
    imagePath = os.path.join ('resources', 'ingame', 'upgrade', 'bensch', 'schwarzerKaffee.png'),
    unlockFunction = UF.getAlwaysUnlockedFunction (),
    activationFunction = AF.getActivateComputerCategory ()
)

senorPopo = Upgrade (
    id = 15,
    name = 'Senor Popo',
    cost = 1200000.0,
    hintText = ['Das ist... schwer zu erklaeren.'],
    imagePath = os.path.join ('resources', 'ingame', 'upgrade', 'bensch', 'senorPopo.png'),
    unlockFunction = UF.getUnlockFunctionRequiringActiveUpgrades ([40]),
    activationFunction = AF.getIncreaseSubscriberViewsPerEpisodeByPercentage (100)
)

unterbewusstesKlicken = Upgrade (
    id = 16,
    name = '"Wie Sie unterbewusst klicken"',
    cost = 6.99,
    hintText = ['Egal was du tust, nach diesem Buch wird dein Finger immer weiter klicken.'],
    imagePath = os.path.join ('resources', 'ingame', 'upgrade', 'bensch', 'unterbewusstesKlicken.png'),
    unlockFunction = UF.getAlwaysUnlockedFunction (),
    activationFunction = AF.getActivateAutoClickFunction ()
)
