from engine.controller.saveObjects.saveGame import SaveGame

import os


def createSaveGameFolderIfNecessary ():
    if not os.path.exists ('saveGames'):
        os.mkdir ('saveGames')

def initialize ():
    createSaveGameFolderIfNecessary ()

def save ():
    saveGame = SaveGame ()

