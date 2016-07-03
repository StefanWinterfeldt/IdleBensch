from engine.controller.upgradeObjects.upgrade import Upgrade
import globals.upgrade.activationFunctions as AF
import globals.upgrade.unlockFunctions as UF
import os


catTV = Upgrade (
    id = 49,
    name = 'Katzenfernsehen',
    cost = 0.01,
    hintText = ['Auch Katzen werden dir zusehen mit dem patentierten Katzenfernseher.'],
    imagePath = os.path.join ('resources', 'ingame', 'upgrade', 'tech', 'catTV.png'),
    unlockFunction = UF.getUnlockFunctionRequiringActiveUpgrades([24]),
    activationFunction = AF.getPassiveFunction ('Missing Text')
)

dnaMutation = Upgrade (
    id = 50,
    name = 'DNA-Mutation',
    cost = 0.01,
    hintText = ['Oeffnet die Tuer fuer eine Reihe von ebenso wunderbaren wie fragwuerdigen Koerpermodifikationen'],
    imagePath = os.path.join ('resources', 'ingame', 'upgrade', 'tech', 'dnaMutation.png'),
    unlockFunction = UF.getAlwaysUnlockedFunction (),
    activationFunction = AF.getPassiveFunction ('Missing Text')
)

dysonSphere = Upgrade (
    id = 51,
    name = 'Dyson Sphaere',
    cost = 0.01,
    hintText = ['Loest alle Energieprobleme fuer die naechsten 2000 Jahre - so hat jeder mehr Zeit dir zuzusehen'],
    imagePath = os.path.join ('resources', 'ingame', 'upgrade', 'tech', 'dysonSphere.png'),
    unlockFunction = UF.getAlwaysUnlockedFunction (),
    activationFunction = AF.getPassiveFunction ('Missing Text')
)

ftlTransmission = Upgrade (
    id = 52,
    name = 'Ueberlicht Uebertragung',
    cost = 0.01,
    hintText = ['Aliens koennen dich in Echtzeit bewundern und an deinen Streams teilnehmen.'],
    imagePath = os.path.join ('resources', 'ingame', 'upgrade', 'tech', 'ftlTransmission.png'),
    unlockFunction = UF.getUnlockFunctionRequiringActiveUpgrades([23]),
    activationFunction = AF.getPassiveFunction ('Missing Text')
)

idleBensch = Upgrade (
    id = 53,
    name = 'Idle Bensch - Das Spiel',
    cost = 0.01,
    hintText = ['Tu das nicht. Du wirst das Multiversum durch 0 teilen.'],
    imagePath = os.path.join ('resources', 'ingame', 'upgrade', 'tech', 'idleBensch.png'),
    unlockFunction = UF.getAlwaysUnlockedFunction (),
    activationFunction = AF.getPassiveFunction ('Missing Text')
)

kaffeeMaschine = Upgrade (
    id = 54,
    name = 'Kaffeemaschine',
    cost = 0.01,
    hintText = ['Auch ein Koffeintremor kann beim Klicken helfen.'],
    imagePath = os.path.join ('resources', 'ingame', 'upgrade', 'tech', 'kaffeeMaschine.png'),
    unlockFunction = UF.getAlwaysUnlockedFunction (),
    activationFunction = AF.getPassiveFunction ('Missing Text')
)

kiPsychologie = Upgrade (
    id = 55,
    name = 'KI-Psychologie',
    cost = 0.01,
    hintText = ['Wenn du denken kannst wie eine KI kannst du sie besser ausnutzen.'],
    imagePath = os.path.join ('resources', 'ingame', 'upgrade', 'tech', 'kiPsychologie.png'),
    unlockFunction = UF.getAlwaysUnlockedFunction (),
    activationFunction = AF.getPassiveFunction ('Missing Text')
)

metaTheory = Upgrade (
    id = 56,
    name = 'Meta-Theorie',
    cost = 0.01,
    hintText = ['Die Meta-Theorie besagt dass alles ineinander enthalten ist. Wenn du lange genug auf ein Quantenteilchen zoomst siehst du das ganze Universum.'],
    imagePath = os.path.join ('resources', 'ingame', 'upgrade', 'tech', 'metaTheory.png'),
    unlockFunction = UF.getUnlockFunctionRequiringActiveUpgrades([72]),
    activationFunction = AF.getPassiveFunction ('Missing Text')
)

omnipresentBroadcast = Upgrade (
    id = 57,
    name = 'Allgegenwaertige Uebertragung',
    cost = 0.01,
    hintText = ['Du bist im ganzen Universum zu empfangen, gleichzeitig. Selbst die Wesen in der Schwaerze zwischen den Galaxien koennen dich jetzt sehen.'],
    imagePath = os.path.join ('resources', 'ingame', 'upgrade', 'tech', 'omnipresentBroadcast.png'),
    unlockFunction = UF.getAlwaysUnlockedFunction (),
    activationFunction = AF.getPassiveFunction ('Missing Text')
)

parallelRealities = Upgrade (
    id = 58,
    name = 'Alternative Dimensionen',
    cost = 0.01,
    hintText = ['Wirr lieferrn auch in parrrallele Rrealitaeten. Menschen aus Parallelwelten, selbst andere Versionen von dir, schauen dir nun zu.'],
    imagePath = os.path.join ('resources', 'ingame', 'upgrade', 'tech', 'parallelRealities.png'),
    unlockFunction = UF.getUnlockFunctionRequiringActiveUpgrades([28]),
    activationFunction = AF.getPassiveFunction ('Missing Text')
)

riesenLaser = Upgrade (
    id = 59,
    name = 'Riesiger Laser',
    cost = 0.01,
    hintText = ['Du kannst ih dazu verwenden um dein Gesicht in den Mond zu brennen - kostenlose Werbung!'],
    imagePath = os.path.join ('resources', 'ingame', 'upgrade', 'tech', 'riesenLaser.png'),
    unlockFunction = UF.getAlwaysUnlockedFunction (),
    activationFunction = AF.getPassiveFunction ('Missing Text')
)

roboBensch = Upgrade (
    id = 60,
    name = 'Robo-Bensch',
    cost = 0.01,
    hintText = ['Sieht dir verblueffend aehlich. Deine Zuschauer bemerken sicher keinen Unterschied.'],
    imagePath = os.path.join ('resources', 'ingame', 'upgrade', 'tech', 'roboBensch.png'),
    unlockFunction = UF.getAlwaysUnlockedFunction (),
    activationFunction = AF.getPassiveFunction ('Missing Text')
)

seti = Upgrade (
    id = 61,
    name = 'SETI',
    cost = 0.01,
    hintText = ['Wer Ausserirdische sucht, der findet sie auch. Und sie sind Fans von dir.'],
    imagePath = os.path.join ('resources', 'ingame', 'upgrade', 'tech', 'seti.png'),
    unlockFunction = UF.getUnlockFunctionRequiringActiveUpgrades([29]),
    activationFunction = AF.getPassiveFunction ('Missing Text')
)

tesseract = Upgrade (
    id = 62,
    name = 'Tesserakt',
    cost = 0.01,
    hintText = ['Ich bin mir nicht sicher wie es funktioniert, aber wenn du von der richtigen Seite hineinsiehst hast du mehr Zuschauer.'],
    imagePath = os.path.join ('resources', 'ingame', 'upgrade', 'tech', 'tesseract.png'),
    unlockFunction = UF.getAlwaysUnlockedFunction (),
    activationFunction = AF.getPassiveFunction ('Missing Text')
)

timeTravel = Upgrade (
    id = 63,
    name = 'Zeitreisen',
    cost = 0.01,
    hintText = ['Jetzt kann man deine Folgen sehen bevor du sie aufzeichnest. Und du kannst beim Aufnehmen schon auf Kommentare reagieren.'],
    imagePath = os.path.join ('resources', 'ingame', 'upgrade', 'tech', 'timeTravel.png'),
    unlockFunction = UF.getAlwaysUnlockedFunction (),
    activationFunction = AF.getPassiveFunction ('Missing Text')
)

unterbewussteBotschaften = Upgrade (
    id = 64,
    name = 'Unterbewusste Botschaften',
    cost = 0.01,
    hintText = ['Mach deine Zuschauer Geistig von dir abhaengig. Damit bist du auch nicht schlimmer als das Fernsehen.'],
    imagePath = os.path.join ('resources', 'ingame', 'upgrade', 'tech', 'unterbewussteBotschaften.png'),
    unlockFunction = UF.getUnlockFunctionRequiringActiveUpgrades([21]),
    activationFunction = AF.getPassiveFunction ('Missing Text')
)