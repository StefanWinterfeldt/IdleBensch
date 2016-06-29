from engine.controller.upgradeObjects.upgrade import Upgrade
import globals.upgrade.activationFunctions as AF
import globals.upgrade.unlockFunctions as UF
import os

angelPact = Upgrade (
    name = 'Engels-Pakt',
    cost = 0.01,
    hintText = ['Im Himmel kann es ziemlich langweilig werden, nicht mit dir.'],
    imagePath = os.path.join ('resources', 'ingame', 'upgrade', 'occult', 'angelPact.png'),
    unlockFunction = UF.getAlwaysUnlockedFunction (),
    activationFunction = AF.getPassiveFunction ('Missing Text')
)

bloodPact = Upgrade (
    name = 'Blut-Pakt',
    cost = 0.01,
    hintText = ['Solange du stets betonst wie wichtig Blutspenden sind werden dir auch die Vampire zuschauen.'],
    imagePath = os.path.join ('resources', 'ingame', 'upgrade', 'occult', 'bloodPact.png'),
    unlockFunction = UF.getAlwaysUnlockedFunction (),
    activationFunction = AF.getPassiveFunction ('Missing Text')
)

cookiePact = Upgrade (
    name = 'Cookie-Pakt',
    cost = 0.01,
    hintText = ['Die Wesen aus dem Cookieverse bieten dir Kekse gegen Views, ein fairer tausch.'],
    imagePath = os.path.join ('resources', 'ingame', 'upgrade', 'occult', 'cookiePact.png'),
    unlockFunction = UF.getAlwaysUnlockedFunction (),
    activationFunction = AF.getPassiveFunction ('Missing Text')
)

deathPact = Upgrade (
    name = 'Todes-Pakt',
    cost = 0.01,
    hintText = ['Der Schnitter und seine vielen Helfer schauen lieber deine Videos als Seelen zu ernten.'],
    imagePath = os.path.join ('resources', 'ingame', 'upgrade', 'occult', 'deathPact.png'),
    unlockFunction = UF.getAlwaysUnlockedFunction (),
    activationFunction = AF.getPassiveFunction ('Missing Text')
)

demonPact = Upgrade (
    name = 'Daemonen-Pakt',
    cost = 0.01,
    hintText = ['Die Hoelle muss warten - auf Hitbox laeuft Bensch!'],
    imagePath = os.path.join ('resources', 'ingame', 'upgrade', 'occult', 'demonPact.png'),
    unlockFunction = UF.getAlwaysUnlockedFunction (),
    activationFunction = AF.getPassiveFunction ('Missing Text')
)

dragonPact = Upgrade (
    name = 'Drachen-Pakt',
    cost = 0.01,
    hintText = ['Es gibt zwar nicht mehr viele Drachen, aber sie haben Geld. Viel Geld'],
    imagePath = os.path.join ('resources', 'ingame', 'upgrade', 'occult', 'dragonPact.png'),
    unlockFunction = UF.getAlwaysUnlockedFunction (),
    activationFunction = AF.getPassiveFunction ('Missing Text')
)

elderPact = Upgrade (
    name = 'Grosser Alter Pakt',
    cost = 0.01,
    hintText = ['Sie sehen und hoeren dich sowieso schon. Jetzt. In dieser Sekunde. Aber nun werden ihre Views gezaehlt.'],
    imagePath = os.path.join ('resources', 'ingame', 'upgrade', 'occult', 'elderPact.png'),
    unlockFunction = UF.getAlwaysUnlockedFunction (),
    activationFunction = AF.getPassiveFunction ('Missing Text')
)

forbiddenKnowledge = Upgrade (
    name = 'Verbotenes Wissen',
    cost = 0.01,
    hintText = ['Du weisst wohin das fuehrt. Und du wirst es trotzdem tun.'],
    imagePath = os.path.join ('resources', 'ingame', 'upgrade', 'occult', 'forbiddenKnowledge.png'),
    unlockFunction = UF.getAlwaysUnlockedFunction (),
    activationFunction = AF.getPassiveFunction ('Missing Text')
)

ghostPact = Upgrade (
    name = 'Geister-Pakt',
    cost = 0.01,
    hintText = ['Geister! Geister! Geister! Weissbrot!'],
    imagePath = os.path.join ('resources', 'ingame', 'upgrade', 'occult', 'ghostPact.png'),
    unlockFunction = UF.getAlwaysUnlockedFunction (),
    activationFunction = AF.getPassiveFunction ('Missing Text')
)

golemPact = Upgrade (
    name = 'Golem-Pakt',
    cost = 0.01,
    hintText = ['Diese Jungs koennen Monatelang am Stueck deine Videos gucken.'],
    imagePath = os.path.join ('resources', 'ingame', 'upgrade', 'occult', 'golemPact.png'),
    unlockFunction = UF.getAlwaysUnlockedFunction (),
    activationFunction = AF.getPassiveFunction ('Missing Text')
)

krakenPact = Upgrade (
    name = 'Kraken-Pakt',
    cost = 0.01,
    hintText = ['Auch in den lichtlosen Tiefen hoert man nun deine Stimme.'],
    imagePath = os.path.join ('resources', 'ingame', 'upgrade', 'occult', 'krakenPact.png'),
    unlockFunction = UF.getAlwaysUnlockedFunction (),
    activationFunction = AF.getPassiveFunction ('Missing Text')
)

moonPact = Upgrade (
    name = 'Mond-Pakt',
    cost = 0.01,
    hintText = ['Werwoelfe sehen dir zwar nur bei Vollmond zu, aber mit dem Haarwuchs steiger sich auch ihr Konsumverhalten.'],
    imagePath = os.path.join ('resources', 'ingame', 'upgrade', 'occult', 'moonPact.png'),
    unlockFunction = UF.getAlwaysUnlockedFunction (),
    activationFunction = AF.getPassiveFunction ('Missing Text')
)

sandWormPact = Upgrade (
    name = 'Sandwurm-Pakt',
    cost = 0.01,
    hintText = ['Der Stream muss fliessen.'],
    imagePath = os.path.join ('resources', 'ingame', 'upgrade', 'occult', 'sandWormPact.png'),
    unlockFunction = UF.getAlwaysUnlockedFunction (),
    activationFunction = AF.getPassiveFunction ('Missing Text')
)

slimePact = Upgrade (
    name = 'Schleim-Pakt',
    cost = 0.01,
    hintText = ['Hast du dich jemals gefragt was unter deiner Spuele lebt? Es ist ein Fan von dir.'],
    imagePath = os.path.join ('resources', 'ingame', 'upgrade', 'occult', 'slimePact.png'),
    unlockFunction = UF.getAlwaysUnlockedFunction (),
    activationFunction = AF.getPassiveFunction ('Missing Text')
)

tentaclePact = Upgrade (
    name = 'Tentakel-Pakt',
    cost = 0.01,
    hintText = ['Die Tentakel wollten einst die Erde erobern, nun heisst ihr Anfueher Taddaeus und schaut deinen Videos.'],
    imagePath = os.path.join ('resources', 'ingame', 'upgrade', 'occult', 'tentaclePact.png'),
    unlockFunction = UF.getAlwaysUnlockedFunction (),
    activationFunction = AF.getPassiveFunction ('Missing Text')
)

zombiePact = Upgrade (
    name = 'Zombie-Pakt',
    cost = 0.01,
    hintText = ['Zombies sind pflegeleicht und schauen regelmaessig deine Videos. Ausserdem unterscheiden sie sich kaum von deinen restlichen Fans.'],
    imagePath = os.path.join ('resources', 'ingame', 'upgrade', 'occult', 'zombiePact.png'),
    unlockFunction = UF.getAlwaysUnlockedFunction (),
    activationFunction = AF.getPassiveFunction ('Missing Text')
)