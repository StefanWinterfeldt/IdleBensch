import engine.util.text as textUtil
import globals.gameState as GGS
import pygame

class Upgrade:
    absoluteRect = None
    active = False
    areaCode = None
    relativeRect = None

    def __init__ (self, name, cost, hintText, imagePath, visibilityFunction, unlockFunction, activationFunction):
        self.activationFunction = activationFunction
        self.cost = cost
        self.hintText = hintText
        self.image = pygame.image.load (imagePath)
        self.name = name
        self.unlockFunction = unlockFunction
        self.visibilityFunction = visibilityFunction

    def activate (self):
        GGS.money -= self.cost
        self.active = True
        self.activationFunction ()

    def getHintText (self):
        lines = [self.name, 'Kosten: ' + textUtil.convertToHumanReadableString (self.cost, True)]
        return lines + self.hintText

    def isUnlocked (self):
        return self.unlockFunction ()

    def isVisible (self):
        return self.visibilityFunction ()
