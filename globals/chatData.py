import random


food = [
    'Stockfisch',
    'Schellfisch',
    'Raeucheraal',
    'Seehecht',
    'Mammut',
    'Froschlaich',
    'Labskaus',
    'Schnecken',
    'Dorschrogen',
    'einen Hut',
    'Zauberpilze',
    'Stockbrot',
    '3 Liter zarten Saitling',
    'ein Dutzend Eier'
]

games = [
    'Minecraft',
    'Half-Life 3',
    'Stockenten Rodeo',
    'Hello Kitty Adventure',
    'Shark Revenge 2',
    'Rochenpogo',
    'den Waescherei-Simulator'
]

topics = [
    'der CSU',
    'Chemtrails',
    'Dr. Hodenschrot',
    'Elektrobier',
    'Winkelschleifern',
    'Wegwerfkanus'
]

websites = [
    'www.XXLpuempel24.de',
    'www.kack-in-den-traktor.de',
    'www.pasteten-KTGW.de',
    'www.billig-nach-nord-korea.at',
    'www.fettBurger-Aktion.de',
    'www.z0r.de'
]

verdicts = [
    'Suckt derbe!',
    'Geht so.',
    'Is voll langweilig.',
    'Kann man spielen.',
    'Is total ueberteuert.',
    'Ueberbewertet.',
    'Bestes Game ever!!!111'
]

stuff = [
    'Wann kommt eigentlich dieses elektronische Zeitalter?',
    'lol',
    'hi',
    '17! 17!',
    'Schnell! Die Damentoilette entflieht!',
    'HYPE HYPE HYPE HYPE HYPE HYPE HYPE HYPE HYPE',
    'deine Mudda schluckt gleich!',
    'Wusstet ihr: wenn ihr euer Passwort im Chat schreibt wird es automatisch durch Sternchen ersetzt, hier: *******',
    'Bensch, hab dir ne Mail geschickt!',
    'Das ist doch alles brotlose Kunst!',
    'Hinter dir! Ein Dreikoepfiger Affe!'
]

insults = [
    'Hodenkobold',
    'Kackbratze',
    'Homofuerst',
    'Arschpirat',
    'Schaumloeffel',
    'Klumpen',
    'haesslicher Klappspaten',
    'vollgeschissener Strumpf'
]

endingMessages = [
    '?reih theihcseg saW',
    'Und ich sah, und siehe, ein fahles Pferd. Und der darauf sass, des Name hiess Tod, und die Hoelle folgte ihm nach.',
    'Das hoert sich nicht gut an...',
    'ShE hAs DyEd HeR hAiR rEd',
    'RedRuM',
    'Liberate tuteme ex Infernis',
    'Azatoth Azatoth Azatoth Azatoth Azatoth Azatoth Azatoth Azatoth Azatoth Azatoth'
]

nickNames = [
    'KahlerKumpel88',
    'Draahkieh',
    'BadButter',
    'MrLessGame',
    'Mopsrolle',
    'KannyDing',
    'R4ap4x',
    'ManutiFaulenzt',
    'Kuurkrie',
    'CPOrly',
    'herbievorie',
    'Suirals',
    'niceKitty',
    'helljoe',
    'xanthilon',
    'gammaToxic',
    'f00sician',
    'Plonkh',
    'lobinator',
    'Robert Paulsen',
    'TheRealDrHodenschrot',
    'K.T.G.W.',
    'dasErsteX',
    'PrengelschneckLP'
]

messageFunctions = [
    lambda: 'Hey Bensch! Hast du schon mal ' + random.choice (food) + ' gegessen?',
    lambda: 'So, ich bin raus. Muss mir noch ' + random.choice (food) + ' braten.',
    lambda: 'Spielst du heute noch ' + random.choice (games) + '?',
    lambda: 'Bensch, was haelst du eigentlich von ' + random.choice (topics) + '?',
    lambda: 'Geht mal alle auf ' + random.choice (websites),
    lambda: 'Ich hab mir ' + random.choice (games) + ' gekauft. ' + random.choice (verdicts),
    lambda: random.choice (stuff),
    lambda: '@' + random.choice (nickNames) + ' was geht eigentlich mit dir du ' + random.choice (insults) + '?',
    lambda: 'Klick schneller du ' + random.choice (insults) + '!'
]

modActionFunctions = [
    lambda: random.choice (nickNames) + ' was timeouted',
    lambda: random.choice (nickNames) + ' was hit by a rather large trout'
]

modMessageFunctions = [
    lambda: 'gleich hagelt es Forellen!',
    lambda: '@' + random.choice (nickNames) + ' nicht spammen!'
]

def getRandomNick ():
    return random.choice (nickNames)

def getRandomMessage ():
    return random.choice (messageFunctions) ()

def getRandomModAction ():
    return random.choice (modActionFunctions) ()

def getRandomModMessage ():
    return random.choice (modMessageFunctions) ()