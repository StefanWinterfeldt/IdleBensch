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
        self.activationFunction.execute ()

    def getHintText (self):
        lines = [self.name, 'Kosten: ' + textUtil.convertToHumanReadableString (self.cost, True)]
        if self.unlockFunction.text is not None: lines.append (self.unlockFunction.text)
        lines.append (self.activationFunction.text)
        return lines + self.hintText

    def isUnlocked (self):
        return self.unlockFunction.execute ()

    def isVisible (self):
        return self.visibilityFunction ()
