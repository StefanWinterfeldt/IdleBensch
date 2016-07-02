import engine.util.text as textUtil
import globals.gameState as GGS
import pygame

class Upgrade:
    absoluteRect = None
    active = False
    areaCode = None
    relativeRect = None
    visible = False

    def __init__ (self, id, name, cost, hintText, imagePath, unlockFunction, activationFunction):
        self.activationFunction = activationFunction
        self.cost = cost
        self.hintText = hintText
        self.id = id
        self.image = pygame.image.load (imagePath)
        self.name = name
        self.unlockFunction = unlockFunction

    def activate (self):
        GGS.money -= self.cost
        self.active = True
        self.activationFunction.execute ()

    def getHintText (self):
        lines = [self.name, 'Kosten: ' + textUtil.convertToHumanReadableString (self.cost, True)]
        unlockText = self.unlockFunction.getText ()
        if unlockText is not None: lines.append (unlockText)
        lines.append (self.activationFunction.getText ())
        return lines + self.hintText

    def isUnlocked (self):
        return self.unlockFunction.execute ()
