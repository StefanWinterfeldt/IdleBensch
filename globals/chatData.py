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
    'www.billig-nach-nord-korea.at'
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
    'deine Mudda schluckt gleich!'
]

insults = [
    'ein Hodenkobold',
    'ne Kackbratze',
    'ein Homofuerst',
    'ein Arschpirat',
    'ein Schaumloeffel',
    'ein Klumpen',
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
    lambda: '@' + random.choice (nickNames) + ' was bist du eigentlich fuer ' + random.choice (insults) + '?'
]

def getRandomNick ():
    return random.choice (nickNames)

def getRandomMessage ():
    return random.choice (messageFunctions) ()
