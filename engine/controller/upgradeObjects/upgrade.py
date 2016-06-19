import pygame

class Upgrade:

    absoluteRect = None
    active = False
    areaCode = None
    relativeRect = None
    unlockFunction = None
    visible = False

    def __init__(self, imagePath, hintText, unlockFunction):
        self.image = pygame.image.load (imagePath)
        self.hintText = hintText
        self.unlockFunction = unlockFunction

    def isUnlocked (self):
        return self.unlockFunction ()
