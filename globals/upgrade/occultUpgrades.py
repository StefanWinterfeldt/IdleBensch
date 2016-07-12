from engine.controller.upgradeObjects.upgrade import Upgrade
import globals.upgrade.activationFunctions as AF
import globals.upgrade.unlockFunctions as UF
import os


angelPact = Upgrade (
    id = 65,
    name = 'Engels-Pakt',
    cost = 60000000.0,
    hintText = ['Im Himmel kann es ziemlich langweilig werden, nicht mit dir.'],
    imagePath = os.path.join ('resources', 'ingame', 'upgrade', 'occult', 'angelPact.png'),
    unlockFunction = UF.getAlwaysUnlockedFunction (),
    activationFunction = AF.getIncreaseMaxSubscribersPerEpisode (500)
)

bloodPact = Upgrade (
    id = 66,
    name = 'Blut-Pakt',
    cost = 13000000.0,
    hintText = ['Solange du stets betonst wie wichtig Blutspenden sind werden dir auch die Vampire zuschauen.'],
    imagePath = os.path.join ('resources', 'ingame', 'upgrade', 'occult', 'bloodPact.png'),
    unlockFunction = UF.getAlwaysUnlockedFunction (),
    activationFunction = AF.getIncreaseMaxDonationAmount (1200)
)

cookiePact = Upgrade (
    id = 67,
    name = 'Cookie-Pakt',
    cost = 700000000.0,
    hintText = ['Die Wesen aus dem Cookieverse bieten dir Kekse gegen Views, ein fairer tausch.'],
    imagePath = os.path.join ('resources', 'ingame', 'upgrade', 'occult', 'cookiePact.png'),
    unlockFunction = UF.getAlwaysUnlockedFunction (),
    activationFunction = AF.getIncreaseViewsPerEpisodeByPercentage (1000)
)

deathPact = Upgrade (
    id = 68,
    name = 'Todes-Pakt',
    cost = 500000000.0,
    hintText = ['Der Schnitter und seine vielen Helfer schauen lieber deine Videos als Seelen zu ernten.'],
    imagePath = os.path.join ('resources', 'ingame', 'upgrade', 'occult', 'deathPact.png'),
    unlockFunction = UF.getAlwaysUnlockedFunction (),
    activationFunction = AF.getIncreaseMaxSubscribersPerEpisode (5000)
)

demonPact = Upgrade (
    id = 69,
    name = 'Daemonen-Pakt',
    cost = 35000000.0,
    hintText = ['Die Hoelle muss warten - auf Hitbox laeuft Bensch!'],
    imagePath = os.path.join ('resources', 'ingame', 'upgrade', 'occult', 'demonPact.png'),
    unlockFunction = UF.getAlwaysUnlockedFunction (),
    activationFunction = AF.getIncreaseDonationChanceByPercentage (100)
)

dragonPact = Upgrade (
    id = 70,
    name = 'Drachen-Pakt',
    cost = 200000000.0,
    hintText = ['Es gibt zwar nicht mehr viele Drachen, aber sie haben Geld. Viel Geld.'],
    imagePath = os.path.join ('resources', 'ingame', 'upgrade', 'occult', 'dragonPact.png'),
    unlockFunction = UF.getAlwaysUnlockedFunction (),
    activationFunction = AF.getIncreaseMaxDonationAmount (50000)
)

elderPact = Upgrade (
    id = 71,
    name = 'Grosser Alter Pakt',
    cost = 5000000000.0,
    hintText = ['Sie sehen und hoeren dich sowieso schon. Jetzt. In dieser Sekunde. Aber nun werden ihre Views gezaehlt.'],
    imagePath = os.path.join ('resources', 'ingame', 'upgrade', 'occult', 'elderPact.png'),
    unlockFunction = UF.getUnlockFunctionRequiringActiveUpgrades ([57]),
    activationFunction = AF.getIncreaseViewsPerEpisodeByPercentage (1000)
)

forbiddenKnowledge = Upgrade (
    id = 72,
    name = 'Verbotenes Wissen',
    cost = 6670000000.0,
    hintText = ['Du weisst wohin das fuehrt. Und du wirst es trotzdem tun.'],
    imagePath = os.path.join ('resources', 'ingame', 'upgrade', 'occult', 'forbiddenKnowledge.png'),
    unlockFunction = UF.getAlwaysUnlockedFunction (),
    activationFunction = AF.getIncreaseSubscribersPerStreamPerSecondByPercentage (666)
)

ghostPact = Upgrade (
    id = 73,
    name = 'Geister-Pakt',
    cost = 9000000.0,
    hintText = ['Geister! Geister! Geister! Weissbrot!'],
    imagePath = os.path.join ('resources', 'ingame', 'upgrade', 'occult', 'ghostPact.png'),
    unlockFunction = UF.getAlwaysUnlockedFunction (),
    activationFunction = AF.getIncreaseMaxSubscribersPerEpisode (120)
)

golemPact = Upgrade (
    id = 74,
    name = 'Golem-Pakt',
    cost = 12000000.0,
    hintText = ['Diese Jungs koennen Monatelang am Stueck deine Videos gucken.'],
    imagePath = os.path.join ('resources', 'ingame', 'upgrade', 'occult', 'golemPact.png'),
    unlockFunction = UF.getAlwaysUnlockedFunction (),
    activationFunction = AF.getIncreaseSubscriberViewsPerEpisodeByPercentage (100)
)

krakenPact = Upgrade (
    id = 75,
    name = 'Kraken-Pakt',
    cost = 45000000.0,
    hintText = ['Auch in den lichtlosen Tiefen hoert man nun deine Stimme.'],
    imagePath = os.path.join ('resources', 'ingame', 'upgrade', 'occult', 'krakenPact.png'),
    unlockFunction = UF.getAlwaysUnlockedFunction (),
    activationFunction = AF.getIncreaseMaxSubscribersPerEpisode (600)
)

moonPact = Upgrade (
    id = 76,
    name = 'Mond-Pakt',
    cost = 20000000.0,
    hintText = ['Werwoelfe sehen dir zwar nur bei Vollmond zu, aber mit dem Haarwuchs steigert sich auch ihr Konsumverhalten.'],
    imagePath = os.path.join ('resources', 'ingame', 'upgrade', 'occult', 'moonPact.png'),
    unlockFunction = UF.getAlwaysUnlockedFunction (),
    activationFunction = AF.getIncreasePurchaseChanceByPercentage (200)
)

sandWormPact = Upgrade (
    id = 77,
    name = 'Sandwurm-Pakt',
    cost = 400000000.0,
    hintText = ['Der Stream muss fliessen.'],
    imagePath = os.path.join ('resources', 'ingame', 'upgrade', 'occult', 'sandWormPact.png'),
    unlockFunction = UF.getAlwaysUnlockedFunction (),
    activationFunction = AF.getIncreaseSubscribersPerStreamPerSecondByPercentage (100)
)

slimePact = Upgrade (
    id = 78,
    name = 'Schleim-Pakt',
    cost = 16000000.0,
    hintText = ['Hast du dich jemals gefragt was unter deiner Spuele lebt? Es ist ein Fan von dir.'],
    imagePath = os.path.join ('resources', 'ingame', 'upgrade', 'occult', 'slimePact.png'),
    unlockFunction = UF.getAlwaysUnlockedFunction (),
    activationFunction = AF.getIncreaseMaxSubscribersPerEpisode (2500)
)

tentaclePact = Upgrade (
    id = 79,
    name = 'Tentakel-Pakt',
    cost = 110000000.0,
    hintText = ['Die Tentakel wollten einst die Erde erobern, nun heisst ihr Anfueher Taddaeus und schaut deine Videos.'],
    imagePath = os.path.join ('resources', 'ingame', 'upgrade', 'occult', 'tentaclePact.png'),
    unlockFunction = UF.getUnlockFunctionRequiringActiveUpgrades ([44]),
    activationFunction = AF.getIncreaseClicksPerSecondByPercentageFunction (100)
)

zombiePact = Upgrade (
    id = 80,
    name = 'Zombie-Pakt',
    cost = 8000000.0,
    hintText = ['Zombies sind pflegeleicht und schauen regelmaessig deine Videos. Ausserdem unterscheiden sie sich kaum von deinen restlichen Fans.'],
    imagePath = os.path.join ('resources', 'ingame', 'upgrade', 'occult', 'zombiePact.png'),
    unlockFunction = UF.getAlwaysUnlockedFunction (),
    activationFunction = AF.getIncreaseSubscriberViewsPerEpisodeByPercentage (25)
)
