import pygame

class Upgrade:

    absoluteRect = None
    activationFunction = None
    active = False
    areaCode = None
    cost = 0
    relativeRect = None
    unlockFunction = None
    visibilityFunction = None

    def __init__(self, imagePath, hintText, visibilityFunction, unlockFunction, activationFunction):
        self.activationFunction = activationFunction
        self.image = pygame.image.load (imagePath)
        self.hintText = hintText
        self.unlockFunction = unlockFunction
        self.visibilityFunction = visibilityFunction

    def activate (self):
        self.active = True
        self.activationFunction ()

    def isUnlocked (self):
        return self.unlockFunction ()

    def isVisible (self):
        return self.visibilityFunction ()
